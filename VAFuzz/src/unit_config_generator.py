import os
import json
import random
import time
import string
import re

MAX_OPTIONS = 50
MAX_CHOICES = 1000

class OptionType:
    BOOL = 0
    CHOICE = 1
    INTNUM = 2
    REALNUM = 3
    STRING = 4


# class Option:
#     def __init__(self):
#         self.opt = ""
#         self.type = OptionType.BOOL
#         self.choices = ["" for _ in range(MAX_CHOICES)]
#         self.num_choices = 0
#         self.range = [0, 0]

class Grammar:
    def __init__(self):
        self.cmdline = ""
        self.connector = ""
        self.strmax = 0
        self.options = [Option() for _ in range(MAX_OPTIONS)]
        self.num_options = 0
        self.depend = ["" for _ in range(MAX_OPTIONS)]
        self.num_depend = 0
        self.conflict = [["", ""] for _ in range(MAX_OPTIONS)]
        self.num_conflict = 0
        self.maxcombs = 0

def parse_json(json_content, grammar):
    data = json.loads(json_content)

    grammar.cmdline = data.get("cmdline", "")
    grammar.connector = data.get("connector", "")
    grammar.strmax = data.get("strmax", 0)
    grammar.maxcombs = data.get("maxcombs", 0)

    options = data.get("options", [])
    grammar.num_options = min(len(options), MAX_OPTIONS)
    for i, opt_data in enumerate(options):
        if i >= MAX_OPTIONS:
            break

        option = grammar.options[i]
        option.opt = opt_data.get("opt", "")
        option.type = getattr(OptionType, opt_data.get("type", "BOOL").upper())
        option.num_choices = 0
        option.range = [0, 0]

        if option.type == OptionType.CHOICE:
            choices = opt_data.get("choices", [])
            option.num_choices = min(len(choices), MAX_CHOICES)
            for j, choice in enumerate(choices):
                if j >= MAX_CHOICES:
                    break
                option.choices[j] = choice

        if "range" in opt_data:
            option.range[0] = opt_data["range"][0]
            option.range[1] = opt_data["range"][1]
              
    dependents = data.get("depend", [])
    grammar.num_depend = min(len(dependents), MAX_OPTIONS)
    for i, dependent in enumerate(dependents):
        if i >= MAX_OPTIONS:
            break
        grammar.depend[i] = dependent

    conflicts = data.get("conflict", [])
    grammar.num_conflict = min(len(conflicts), MAX_OPTIONS)
    for i, conflict_data in enumerate(conflicts):
        if i >= MAX_OPTIONS:
            break
        grammar.conflict[i][0] = conflict_data[0]
        grammar.conflict[i][1] = conflict_data[1]


def generate_option_combinations(grammar, program_name, output_folder):
    print(f"Generating command lines for {program_name}")
    output_filename = os.path.join(output_folder, "Commands", f"{program_name}_options.txt")
    
    with open(output_filename, "w") as output_file:
        program_header = program_name.split("_")[0]
        
        included_options = set()  # To keep track of options already included in the configuration
        
        for i in range(grammar.num_options):
            option = grammar.options[i]
            
            if option.opt in included_options:
                continue  # Skip options that are already included
            
            # Check if this option depends on another
            dependent_on = None
            
            grammar.depend = list(filter(lambda x: x != '', grammar.depend))
            
            for dep in grammar.depend:
                if dep["opt"] == option.opt:
                    dependent_on = dep["on"]
                    break
            
            if dependent_on:
                # Include both the dependent option and the one it depends on
                included_options.add(option.opt)
                output_options = [option]
                # for each_dep in dependent_on:
                #     included_options.add(each_dep)
                print("Waw", option.opt)
                
                for each_dep in dependent_on:
                    for i, opt in enumerate(grammar.options):
                        if opt.opt == each_dep:
                            output_options.append(opt)
            else:
                output_options = [option]
                
            if program_name == "xmllint_1" and option.opt == "--xmlout":
                print(len(output_options))
                for output_option in output_options:
                    print(f"Option: {output_option.opt} Type: {output_option.type} Range: {output_option.range}")
                # exit(0)
            
            for i, output_option in enumerate(output_options):
                if output_option.type == OptionType.BOOL:
                    if len(output_options) == 1:
                        config_string = f"{program_header} {output_option.opt} "
                        output_file.write(config_string + "\n")
                        
                    else:
                        if i == 0:
                            config_string = f"{program_header} {output_option.opt} "
                            output_file.write(config_string)
                        else:
                            config_string = f"{output_option.opt} "
                            if i == len(output_options) - 1:
                                output_file.write(config_string + "\n")
                            else:
                                output_file.write(config_string)
                    
                    
                elif output_option.type == OptionType.INTNUM:
                    randint = random.randint(option.range[0], option.range[1])
                    if len(output_options) == 1:
                        config_string = f"{program_header} {output_option.opt} {randint} "
                        output_file.write(config_string + "\n")
                        
                    else:
                        if i == 0:
                            config_string = f"{program_header} {output_option.opt} {randint} "
                            output_file.write(config_string)
                        else:
                            config_string = f"{output_option.opt} {randint} "
                            if i == len(output_options) - 1:
                                output_file.write(config_string + "\n")
                            else:
                                output_file.write(config_string)
                            
                        
                elif output_option.type == OptionType.REALNUM:
                    randreal = round(random.uniform(option.range[0], option.range[1]), 2)
                    if len(output_options) == 1:
                        config_string = f"{program_header} {output_option.opt} {randreal} "
                        output_file.write(config_string + "\n")
                        
                    else:
                        if i == 0:
                            config_string = f"{program_header} {output_option.opt} {randreal} "
                            output_file.write(config_string)
                            
                        else:
                            config_string = f"{output_option.opt} {randreal} "
                            if i == len(output_options) - 1:
                                output_file.write(config_string + "\n")
                            else:
                                output_file.write(config_string)
                        
                elif output_option.type == OptionType.CHOICE:
                    for choice in output_option.choices[:output_option.num_choices]:
                        if len(output_options) == 1:
                            config_string = f"{program_header} {output_option.opt} {choice} "
                            output_file.write(config_string + "\n")
                            
                        else:
                            if i == 0:
                                config_string = f"{program_header} {output_option.opt} {choice} "
                                output_file.write(config_string)
                                
                            else:
                                config_string = f"{output_option.opt} {choice} "
                                if i == len(output_options) - 1:
                                    output_file.write(config_string + "\n")
                                else:
                                    output_file.write(config_string)
                # todo
                elif output_option.type == OptionType.STRING:
                    config_string = f"{program_header} {output_option.opt} "
                    for _ in range(5):  # Generate 5 random strings for each option
                        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, grammar.strmax)))
                        
                        if len(output_options) == 1:
                            output_file.write(config_string + random_string + "\n")
                        else:
                            if i == 0:
                                output_file.write(config_string + random_string + " ")
                            else:
                                if i == len(output_options) - 1:
                                    output_file.write(random_string + "\n")
                                else:
                                    output_file.write(random_string + " ")



def process_grammar_files(grammar_folder, output_folder):
    os.makedirs(os.path.join(output_folder, "Commands"), exist_ok=True)

    for filename in os.listdir(grammar_folder):
        if filename.endswith(".json"):
            grammar = Grammar()
            program_name = os.path.splitext(filename)[0]

            file_path = os.path.join(grammar_folder, filename)
            print(f"Processing grammar file: {file_path}")

            with open(file_path, "r") as file:
                json_content = file.read()

            parse_json(json_content, grammar)

            generate_option_combinations(grammar, program_name, output_folder)

def main():
    import sys
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <GrammarFolderPath> <OutputFolderPath>")
        return 1

    grammar_folder = sys.argv[1]
    output_folder = sys.argv[2]

    process_grammar_files(grammar_folder, output_folder)

    print("Command files generated successfully!")

if __name__ == "__main__":
    main()
