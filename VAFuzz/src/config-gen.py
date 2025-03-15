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


class Option:
    def __init__(self):
        self.opt = ""
        self.type = OptionType.BOOL
        self.choices = ["" for _ in range(MAX_CHOICES)]
        self.num_choices = 0
        self.range = [0, 0]

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

def generate_combinations(grammar, program_name, output_folder):
    print(f"Generating command lines for {program_name}")
    output_filename = os.path.join(output_folder, "Commands", f"{program_name}.txt")
    with open(output_filename, "w") as output_file:
        program_header = program_name.split("_")[0]
        
        configurations = []
        
        while len(configurations) < grammar.maxcombs:
            config_string = f"{program_header} "
            config = {}
            conflicting = False
            
            for i in range(grammar.num_options):
                option = grammar.options[i]
                
                # debug
                # if program_name == "cxxfilt_2":
                #     if option.opt == "--format":
                #         print(f"option: {option.opt}")
                #         print(f"choices {list(filter(lambda x: x != '', option.choices))}")
                        
                
                
                if option.opt in config:
                    continue  # Skip options that are already set
                
                if option.opt in grammar.depend:
                    if grammar.depend[option.opt] not in config:
                        continue  # Skip options dependent on other options that are not set
                
                if option.opt in [conflict[0] for conflict in grammar.conflict]:
                    for conflict in grammar.conflict:
                        if conflict[0] in config and conflict[1] in config and config[conflict[0]] == config[conflict[1]]:
                            conflicting = True
                            break
                    if conflicting:
                        break
                
                if option.type == OptionType.BOOL:
                    config[option.opt] = random.choice([True, False])
                    if config[option.opt] == True:
                        config_string += f"{option.opt} "
                elif option.type == OptionType.INTNUM:
                    config[option.opt] = random.randint(option.range[0], option.range[1])
                    config_string += f"{option.opt} {config[option.opt]} "
                elif option.type == OptionType.REALNUM:
                    config[option.opt] = round(random.uniform(option.range[0], option.range[1]), 2)
                    config_string += f"{option.opt} {config[option.opt]} "
                elif option.type == OptionType.CHOICE:
                    config[option.opt] = random.choice(list(filter(lambda x: x != '', option.choices)))
                    config_string += f"{option.opt} {config[option.opt]} "
                elif option.type == OptionType.STRING:
                    config[option.opt] = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, grammar.strmax)))
                    config_string += f"{option.opt} {config[option.opt]} "
                
            if not conflicting:
                configurations.append(config)
                output_file.write(config_string + "\n")
                    
                    
        output_file.write("\n")





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

            generate_combinations(grammar, program_name, output_folder)

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
