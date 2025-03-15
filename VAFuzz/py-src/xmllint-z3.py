
import itertools
import random
import string
from z3 import *
import sys
from generator_helpers import *
import pickle
from heapq import heappush, heappop
import pprint
import os
import math

choice_dict = {} # <<<<<< Fill this manually
# Variable declarations
debug = Bool('debug')
debugent = Bool('debugent')
copy = Bool('copy')
recover = Bool('recover')
huge = Bool('huge')
noent = Bool('noent')
noenc = Bool('noenc')
noout = Bool('noout')
nonet = Bool('nonet')
encode = Bool('encode')
nocompact = Bool('nocompact')
htmlout = Bool('htmlout')
nowrap = Bool('nowrap')
valid = Bool('valid')
postvalid = Bool('postvalid')
quiet = Bool('quiet')
timing = Bool('timing')
repeat = Bool('repeat')
insert = Bool('insert')
html = Bool('html')
xmlout = Bool('xmlout')
nodefdtd = Bool('nodefdtd')
push = Bool('push')
pushsmall = Bool('pushsmall')
memory = Bool('memory')
nowarning = Bool('nowarning')
pedantic = Bool('pedantic')
noblanks = Bool('noblanks')
nocdata = Bool('nocdata')
format = Bool('format')
dropdtd = Bool('dropdtd')
nodict = Bool('nodict')
c14n = Bool('c14n')
c14n11 = Bool('c14n11')
nsclean = Bool('nsclean')
testIO = Bool('testIO')
compress = Bool('compress')
catalogs = Bool('catalogs')
nocatalogs = Bool('nocatalogs')
auto = Bool('auto')
xinclude = Bool('xinclude')
noxincludenode = Bool('noxincludenode')
loaddtd = Bool('loaddtd')
dtdattr = Bool('dtdattr')
stream = Bool('stream')
walker = Bool('walker')
chkregister = Bool('chkregister')
sax1 = Bool('sax1')
sax = Bool('sax')
oldxml10 = Bool('oldxml10')

variable_list = ['debug', 'debugent', 'copy', 'recover', 'huge', 'noent', 'noenc', 'noout', 'nonet', 'encode', 'nocompact', 'htmlout', 'nowrap', 'valid', 'postvalid', 'quiet', 'timing', 'repeat', 'insert', 'html', 'xmlout', 'nodefdtd', 'push', 'pushsmall', 'memory', 'nowarning', 'pedantic', 'noblanks', 'nocdata', 'format', 'dropdtd', 'nodict', 'c14n', 'c14n11', 'nsclean', 'testIO', 'compress', 'catalogs', 'nocatalogs', 'auto', 'xinclude', 'noxincludenode', 'loaddtd', 'dtdattr', 'stream', 'walker', 'chkregister', 'sax1', 'sax', 'oldxml10']
lows = {}
highs = {}

def request_config_generation(constraint_file, 
                              configs_to_generate, 
                              generator_number=1,
                              pc_rand_selection=0.0):
    solver = Solver()
    # Constraints
    solver.add(Or(Not(catalogs), Not(nocatalogs)))
    solver.add(Or(Not(xinclude), Not(noxincludenode)))
    solver.add(Implies(xmlout, And(Bool('html'))))


    # Generator helpers
    configs_to_generate = int(configs_to_generate)
    var_s = set()
    
    # Checked if we have pickled the pqeue
    pqeue = []
    try:
        with open(constraint_file, "rb") as file:
            pqeue = pickle.load(file)
    except OSError: # TODO: What do we do if we dont have the file and if empty
        # print("No file found")
        with open(constraint_file, "wb") as file:
            pickle.dump(pqeue, file)

    
    # GENERATOR 3
    if generator_number == 3:
        if len(pqeue) < 2:
            # print("Pqeue doesnt have enough elements")
            exit(1)
        # print("PC Queue: " + str(pqeue))
        pc_0 = None
        random_float_0 = random.uniform(0, 1)
        if random_float_0 < (pc_rand_selection / 2.0):
            random_idx = random.randint(0, len(pqeue) - 1)
            pc_0 = pqeue[random_idx]
        else:
            pc_0 = heappop(pqeue)
            
        # print("PC" + str(pc_0))
    
    if pqeue == []:
        print("Empty pqeue")
    else:
        # print("PC Queue: " + str(pqeue))

        random_float = random.uniform(0, 1)
        
        pc = None
        if random_float < pc_rand_selection:
            random_idx = random.randint(0, len(pqeue) - 1)
            pc = pqeue[random_idx]
        else:
            pc = heappop(pqeue)
            # energy = abs(pc[0])
        # print("PC" + str(pc))
        # Check if the pqeue is empty
        # if len(pqeue) == 0:
        if not pc[1] == "default_settings_for_all":        
            condition = "solver.add(" + pc[1] + ")"
            # print("Cond:", condition)
            var_s.update(extract_variable_names(condition))
            exec(condition)
        
        if pc[1] == "default_settings_for_all" and generator_number == 3:
            pc = pc_0


    # GENERATOR 1
    if generator_number == 1 or generator_number == 3:
        combinations = []
        variables = list(var_s)
        
        for idx, var in enumerate(variables):
            if (isinstance(globals()[var], DatatypeSortRef)):
                variables.pop(idx)
        
        def backtrack(current_assignment, idx):
            # Stop if we've generated enough configurations
            if len(combinations) >= configs_to_generate:
                return True  # Return True to indicate we should stop
            
            if idx == len(variables):
                combinations.append(current_assignment.copy())
                return False  # Return False to continue generating
            
            var_name = variables[idx]
            var = globals()[var_name]
            
            if is_bool(var):
                for value in [True, False]:
                    current_assignment[var_name] = value
                    if backtrack(current_assignment, idx + 1):
                        return True
            
            elif is_int(var):
                for value in [False] + random.sample(range(lows[var_name], highs[var_name]), 3):
                    current_assignment[var_name] = value
                    if backtrack(current_assignment, idx + 1):
                        return True
            
            elif is_real(var):
                for value in [False] + [random.uniform(lows[var_name], highs[var_name]) for _ in range(3)]:
                    current_assignment[var_name] = value
                    if backtrack(current_assignment, idx + 1):
                        return True
            
            elif isinstance(var, DatatypeRef):
                choices = var.sort().num_constructors()
                for choice_idx in range(choices):
                    current_assignment[var_name] = var.sort().constructor(choice_idx)
                    if backtrack(current_assignment, idx + 1):
                        return True
            else:
                for value in [random_string() for _ in range(3)]:
                    current_assignment[var_name] = value
                    if backtrack(current_assignment, idx + 1):
                        return True
            
            return False

        backtrack({}, 0)
        config_string_struct = generate_config_strings(combinations, pc)
        # print("Generated Config Str:" + str(config_string_struct[2]))
        
        # Check SAT
        # if solver.check() == sat:
        #     # print('SAT')
        
        # F = Not(And(a == True, b == True))
        # G = Or(Not(a), Not(b))
        # # print(is_equivalent(F == G))


    # GENERATOR 2
    elif generator_number == 2:
        combinations = []
        for var_name in variable_list:
            combinations_entry = {}
            
            var = globals()[var_name]  # Obtain the Z3 variable using eval
            
            if is_bool(var):
                combinations_entry[var_name] = True
            elif is_int(var):
                combinations_entry[var_name] = random.randint(lows[var_name], highs[var_name])
            elif is_real(var):
                combinations_entry[var_name] = random.uniform(lows[var_name], highs[var_name])
            elif isinstance(var, DatatypeRef):
                choices = var.sort().num_constructors()
                choice_idx = random.randint(0, choices - 1)
                combinations_entry[var_name] = var.sort().constructor(choice_idx)
            else:
                combinations_entry[var_name] = random_string()

            combinations.append(combinations_entry)

        config_string_struct = generate_config_strings(combinations)
    
    
    # GENERATOR 4
    elif (generator_number == 4):
        if not pc[1] == "default_settings_for_all":
            configs = []
            
            var_names = extract_variable_names_and_values(pc[1])
            print("Var names: " + str(var_names))
            for each in var_names:
                configs.append({each: var_names[each]})
            
            config_string_struct = generate_config_strings(configs, pc)
        else:
            config_string_struct = generate_config_strings([{}], pc)
        
        pprint.pp(config_string_struct)
    
    
    
    # Configs have been generated and stored in config_string_struct
    
    if generator_number == 3:
        if not pc_0[1] == "default_settings_for_all":        
            condition = "solver.add(" + pc_0[1] + ")"
            print("Cond Gen 3:", condition)
            # energy = abs(pc_0[0])
            
            gen_3_var_s = extract_variable_names(condition)
            
            no_similar = True
            for each in gen_3_var_s:
                if each in var_s:
                    no_similar = False
                    break
            
            if no_similar:    
                var_s.update(extract_variable_names(condition))
                
                
                exec(condition)
                
                config_ext_s = extract_variable_names(condition)
                config_ext_dict = {}
                
                for each in config_ext_s:
                    config_ext_dict[each] = True
                # todo
                config_ext_string_struct = generate_config_strings([config_ext_dict], pc_0)
                # print("Config ext string struct: " + str(config_ext_string_struct[0]))
                config_ext_str = config_ext_string_struct[0][0]
                # print("Config ext str: " + str(config_ext_str))
                
                # Add to original config string struct
                for idx in range(len(config_string_struct[0])):
                    config_string_struct[0][idx] = config_string_struct[0][idx].strip()
                    ext_ls = config_ext_str.strip().split("-")[1:]
                    # print("Ext ls: " + str(ext_ls))
                    for j in range(len(ext_ls)):
                        # found = False
                        option_setting = "-" + ext_ls[j]
                        option_setting = option_setting.strip()
                        # print("Checking if: " + option_setting + " is in " + config_string_struct[0][idx])
                        if  option_setting not in config_string_struct[0][idx]:
                            # print("Adding: " + option_setting)
                            config_string_struct[0][idx] += " " + option_setting
                        # else:
                            
                            
                    
                    # if not found:
                    #     config_string_struct[0][idx] += " " + config_ext_str + " "
            
                cur_pc = config_string_struct[2][1]
                
                # remove )
                # print("CUR pc: " + str(cur_pc))
                if cur_pc[0:3] == "Not":
                    pass
                elif ")" in cur_pc:
                    cur_pc = cur_pc[:-1]
                for new_var in config_ext_dict:
                    cur_pc += ", " + new_var
                cur_pc += ")"
                
                if "And" not in cur_pc:
                    if cur_pc[0:3] == "Not":
                        cur_pc = "(" + cur_pc
                    
                    if "(" == cur_pc[0]:
                        cur_pc = "And" + cur_pc
                    else:
                        cur_pc = "And(" + cur_pc
                
                # print("CUR pc: " + str(cur_pc))
                config_string_struct[2] = (0, cur_pc)
            
            else: # default base case
                pass
    
    
    
    favoured_list = []
    # data favoured list
    if generator_number != 2:
        try :
            with open("/tmp/data_info.pkl", "rb") as file:
                data_asso_info = pickle.load(file)

                for each in data_asso_info:
                    each_ls, var = each[0], each[1]
                    if "(" in var:
                        var = var[1:]
                    if ")" in var:
                        var = var[:-1]
                        
                    # print("Searching for: " + var + " in " + str(var_s))
                    if var in var_s:
                        favoured_list.extend(each_ls)
        
            # print("Favoured list: " + str(favoured_list))

        except OSError:
            # print("No data info file found")
            exit(1)
    
    
    config_string_struct.append(favoured_list)
    # config_string_struct.append(energy)
    # print("Config string struct: " + str(config_string_struct))
    # save pqeue
    with open("/tmp/pqeue.pkl", "wb") as file:
        pickle.dump(pqeue, file)
    return config_string_struct


def is_equivalent(claim, show=False, **keywords):
    s = Solver()
    s.set(**keywords)
    s.add(Not(claim))
    if show:
        print(s)
    r = s.check()
    if r == unsat:
        return True
    
    else:
        return False


#configs: [{'b': True}, {'b': False}]
def generate_config_strings(configs, presence_cond_used=(0, "")):
    config_strings = []
    option_indices = {}

    for idx, config in enumerate(configs):
        # Create a string representation of each configuration
        config_str = []
        for key, value in config.items():
            if isinstance(value, bool):
                if value:  # If the boolean is True, include the flag (-key)
                    config_str.append(f"-{key}")
                    if f"-{key}" not in option_indices:
                        option_indices[f"-{key}"] = []
                    option_indices[f"-{key}"].append(idx)
            else:
                if value is False:
                    continue
                
                if isinstance(value, FuncDeclRef):
                    value = str(value)
                    value = value.replace("opt", "")
                    value = value.replace("_", "-")
                    value = value.replace("colonoperator", ":")

                
                option_str = f"-{key} {value}"
                # print(option_str)
                config_str.append(option_str)
                if option_str not in option_indices:
                    option_indices[option_str] = []
                option_indices[option_str].append(idx)

        # Join all key=value pairs into a single string for this configuration
        final_str = " ".join(config_str)
        if final_str == "":
            final_str = " "
        config_strings.append(final_str)

    # print(option_indices)
    return [config_strings, option_indices, presence_cond_used]


def save_pq():
    pqeue = []
    heappush(pqeue, (0, "And(Not(a), b)"))
    
    with open("/tmp/pqeue.pkl", "wb") as file:
        pickle.dump(pqeue, file)

def save_pq_2():
    pqeue = []
    heappush(pqeue, (-1, "And(a, b)"))
    heappush(pqeue, (-2, "And(b, d)"))
    heappush(pqeue, (0, "And(Not(a), b)"))

    with open("/tmp/pqeue.pkl", "wb") as file:
        pickle.dump(pqeue, file)

def save_data_info():
    data = []
    
    with open("/tmp/data_info.pkl", "wb") as file:
        pickle.dump(data, file)
    

def send_feedback(config_ls, trace_ls, presence_cond, virgin_bits):
    feedback = list(zip(config_ls, trace_ls))
    analyze_feedback(feedback, presence_cond, virgin_bits)
    
    # open pqeue and see if length is too big
    with open("/tmp/pqeue.pkl", "rb") as file:
        pqeue = pickle.load(file)
        if len(pqeue) > 50: cull_pc_queue()

    # for each in feedback:
    #     save_presence_condition(each)
    return 0


def analyze_feedback(feedback, presence_cond, virgin_bits):
    # G = pretty == PrettyChoices.0
    # # print(PrettyChoices.opt1)
    # # print(PrettyChoices.name)
    # G1 = pretty == PrettyChoices.constructor(0)
    
    # print("Analyzing feedback!")
    # pprint.pp(feedback)
    # print("Presence cond: " + presence_cond + "<")
    
    if presence_cond == "default_settings_for_all":
        presence_cond = " "
    
    if presence_cond != " ":
        vars_to_analyze = extract_variable_names_and_values(presence_cond);
        # # print("VARS TO ANALYZE")
        # # print(vars_to_analyze)
        
    # Normalize virgin bits
    normalzied_virgin_bits = [0] * len(virgin_bits)
    for idx in range(len(virgin_bits)):
        normalzied_virgin_bits[idx] = virgin_bits[idx] / 255
    
    # Each config
    for each in feedback:
        config = each[0]
        trace = each[1]
    
    # Energy allocation

        energy = 0
        for idx, bit in enumerate(trace):
            if bit != 0:
                energy += (1 * normalzied_virgin_bits[idx])
        if (len(trace) == 0):
            energy = 0
        else:
            energy = math.ceil((energy / len(trace)) * 100)

        if presence_cond == " ":
            save_presence_condition((config, trace, energy))
        else:            
            save_presence_condition((config, trace, energy), use_pc_vars=True, pc_vars=vars_to_analyze)
        
    # each variable
    if presence_cond != " ":
        for each_var in vars_to_analyze:
            pos_idx = set()
            
            # Find positives
            if is_bool(globals()[each_var]):
                for idx in range(len(feedback)):
                    config, trace = feedback[idx]
                    
                    if "-" + each_var in config:
                        pos_idx.add(idx)
            
                
                final_pos_trace = [min(col) for col in zip(*[feedback[idx][1] for idx in pos_idx])]
                
                for idx, bit in enumerate(final_pos_trace):
                    if bit != 0:
                        energy += (1 * normalzied_virgin_bits[idx])
                
                if (len(final_pos_trace) == 0):
                    energy = 0
                else:
                    energy = math.ceil((energy / len(final_pos_trace)) * 100)
                # print("new energy: " + str(energy))
                # print("------")
                # print(each_var)
                # print(energy)
                # print("Final pos trace:")
                # print(final_pos_trace)
                save_presence_condition(("-" + each_var, final_pos_trace, energy))
                        
                        
            else: # Not a bool
                for idx in range(len(feedback)):
                    config, trace = feedback[idx]
                    if "-" + each_var + " " + str(vars_to_analyze[each_var]) in config:
                        pos_idx.add(idx)
            
                
                final_pos_trace = [min(col) for col in zip(*[feedback[idx][1] for idx in pos_idx])]
                
                energy = sum(1 for x in final_pos_trace if x != 0)
                save_presence_condition(("-" + each_var + " " + str(vars_to_analyze[each_var]), energy))

            
            # Find negatives
            neg_idx = set(range(len(feedback))) - pos_idx
            
            if is_bool(globals()[each_var]):
                for idx in range(len(feedback)):
                    config, trace = feedback[idx]
                    if "-" + each_var not in config:
                        neg_idx.add(idx)
                
                
                final_neg_trace = [min(col) for col in zip(*[feedback[idx][1] for idx in neg_idx])]            

                for idx, bit in enumerate(final_neg_trace):
                    if bit != 0:
                        energy += (1 * normalzied_virgin_bits[idx])
                
                if (len(final_neg_trace) == 0):
                    energy = 0
                else:
                    energy = math.ceil((energy / len(final_neg_trace)) * 100)
                
                # print("Final neg trace:")
                # print(final_neg_trace)
                save_presence_condition(("-" + each_var, final_neg_trace, energy), is_negated=True)
                            
            else: # Not a bool
                for idx in range(len(feedback)):
                    config, trace = feedback[idx]
                    if "-" + each_var + " " + str(vars_to_analyze[each_var]) not in config:
                        neg_idx.add(idx)
                
                
                final_neg_trace = [min(col) for col in zip(*[feedback[idx][1] for idx in neg_idx])]
                
                energy = sum(1 for x in final_neg_trace if x != 0)
                save_presence_condition(("-" + each_var + " " + str(vars_to_analyze[each_var]), energy), is_negated=True)
    # read_pq()

def analyze_feedback_data(config_list, 
                          data_obj_list, 
                          presence_cond, 
                          id_cutoff, 
                          pc_level_data_asso,
                          output_dir="/output/default"):
    # print("Presence cond: " + presence_cond + "<")
    # print("Analyzing feedback!")
    # print("Config list:")
    # pprint.pp(config_list)
    # print("Data obj list:")
    # pprint.pp(data_obj_list)
    # print("Output dir: " + output_dir)
    
    # print(id_cutoff)
    
    # Clean data for analysis
    cleaned_data_matrix = clean_data_arrs(data_obj_list, id_cutoff)
    important_data = keep_last_entries_by_id(cleaned_data_matrix)
    # pprint.pp(cleaned_data_matrix)
    # print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    # pprint.pp(important_data)
    # print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    is_interesting = False

    for each_imp in important_data:
        # print("each imp")
        # print(each_imp)
        if each_imp != []:
            # print("TRIGGER?????")
            is_interesting = True
    
    # print("Is interesting?")
    # print(is_interesting)
    
    if not is_interesting:
        # print("No interesting data")
        return 0
    
    # save execution config
    suffix_ls = [0] * (id_cutoff + 1)
    
    os.makedirs(output_dir + "/queue_argvs/", exist_ok=True)
    # os.makedirs(output_dir + "/crashed_argv/", exist_ok=True)

    for idx in range(len(important_data)):
        each_imp_data = important_data[idx]
        for each_triple in each_imp_data:
            data_id = each_triple[0]
            data_has_bits = each_triple[1]
            data_crashed = each_triple[2]
            
            file_id = "id:" + str(data_id).zfill(6) + "_"
            suffix = suffix_ls[data_id]
            suffix_ls[data_id] += 1
            
            file_name = file_id + str(suffix)
            
            if data_has_bits == 2:
                file_name += "+cov"
            
            with open(output_dir + "/queue_argvs/" + file_name, "w") as file:
                file.write(config_list[idx])
                
            # if data_crashed:
            #     with open(output_dir + "/crashed_argv/" + file_name, "w") as file:
            #         file.write(config_list[idx])
        
    
    data_traces = convert_to_bitmap(important_data)
    # pprint.pp(data_traces)
    
    
    # G = pretty == PrettyChoices.0
    # # print(PrettyChoices.opt1)
    # # print(PrettyChoices.name)
    # G1 = pretty == PrettyChoices.constructor(0)
    
    # # print("Analyzing feedback!")
    if presence_cond != " ":
        vars_to_analyze = extract_variable_names_and_values(presence_cond);
        # # print("VARS TO ANALYZE")
        # # print(vars_to_analyze)
    
    if not pc_level_data_asso:
        # Each config
        # for i in range(len(config_list)):
        #     config = config_list[i]
        #     trace = data_traces[i]
            
        #     favoured_ls = []
        #     for i, bit in enumerate(trace):
        #         if bit != 0:
        #             favoured_ls.append(i)
            
        #     # print("Config: " + config)
        #     # print("Favoured: " + str(favoured_ls))
        #     if presence_cond == " ":
        #         save_presence_condition_data_info((config, favoured_ls))
                
        #     save_presence_condition_data_info((config, favoured_ls), use_pc_vars=True, pc_vars=vars_to_analyze)

        # each variable
        if presence_cond != " ":
            for each_var in vars_to_analyze:
                # print("Analyzing variable: " + each_var + " with value: " + str(vars_to_analyze[each_var]))
                pos_idx = set()
                
                # Find positives
                if is_bool(globals()[each_var]):
                    for idx in range(len(config_list)):
                        config, trace = config_list[idx], data_traces[idx]
                        
                        if "-" + each_var in config:
                            pos_idx.add(idx)
                
                    # # print("Positives: " + str(pos_idx))
                    
                    # final_pos_trace = [min(col) for col in zip(*[feedback[idx][1] for idx in pos_idx])]
                    # final_pos_trace = [min(col) for col in zip(*[data_traces[idx] for idx in pos_idx])]
                    final_pos_trace = [max(col) for col in zip(*[data_traces[idx] for idx in pos_idx])]

                    # Build favoured list
                    favoured_ls = []
                    for idx, x in enumerate(final_pos_trace):
                        if x != 0:
                            favoured_ls.append(idx)
                    # print(favoured_ls)
                    save_presence_condition_data_info(("-" + each_var, favoured_ls))                   
                            
                else: # Not a bool
                    for idx in range(len(config_list)):
                        config, trace = config_list[idx], data_traces[idx]
                        
                        if "-" + each_var + " " + str(vars_to_analyze[each_var]) in config:
                            pos_idx.add(idx)
                
                    # print("Positives: " + str(pos_idx))
                    
                    final_pos_trace = [max(col) for col in zip(*[data_traces[idx] for idx in pos_idx])]
                    
                    # Build favoured list
                    favoured_ls = []
                    for idx, x in enumerate(final_pos_trace):
                        if x != 0:
                            favoured_ls.append(idx)
                    # print(favoured_ls)
                    save_presence_condition_data_info(("-" + each_var, favoured_ls))                   

                
                # Find negatives
                # neg_idx = set(range(len(config_list))) - pos_idx
                
                # if is_bool(globals()[each_var]):
                #     for idx in range(len(config_list)):
                #         config, trace = config_list[idx], data_traces[idx]
                #         if "-" + each_var not in config:
                #             neg_idx.add(idx)
                    
                #     # print("Negatives: " + str(neg_idx))
                    
                #     final_neg_trace = [max(col) for col in zip(*[data_traces[idx] for idx in neg_idx])]

                #     # print("Final neg trace: " + str(final_neg_trace))
                    
                #     favoured_ls = []
                #     for idx, x in enumerate(final_neg_trace):
                #         if x != 0:
                #             favoured_ls.append(idx)
                #     # print(favoured_ls)
                #     save_presence_condition_data_info(("-" + each_var, favoured_ls))                   
                                
                # else: # Not a bool
                #     for idx in range(len(config_list)):
                #         config, trace = config_list[idx], data_traces[idx]
                #         if "-" + each_var + " " + str(vars_to_analyze[each_var]) not in config:
                #             neg_idx.add(idx)
                    
                #     # print("Negatives: " + str(neg_idx))
                    
                #     final_neg_trace = [max(col) for col in zip(*[data_traces[idx] for idx in neg_idx])]
                    
                #     favoured_ls = []
                #     for idx, x in enumerate(final_neg_trace):
                #         if x != 0:
                #             favoured_ls.append(idx)
                #     # print(favoured_ls)
                #     save_presence_condition_data_info(("-" + each_var, favoured_ls))  
    else:
        # Each config
        for idx in range(len(config_list)):
            config = config_list[idx]
            trace = data_traces[idx]
            
            favoured_ls = []
            for idx, bit in enumerate(trace):
                if bit != 0:
                    favoured_ls.append(idx)
            
            # print("Config: " + config)
            # print("Favoured: " + str(favoured_ls))
            if presence_cond == " ":
                save_presence_condition_data_info((config, favoured_ls))
            else:
                save_presence_condition_data_info((config, favoured_ls), use_pc_vars=True, pc_vars=vars_to_analyze)

        # each variable
        if presence_cond != " ":
            for each_var in vars_to_analyze:
                # print("Analyzing variable: " + each_var + " with value: " + str(vars_to_analyze[each_var]))
                pos_idx = set()
                
                # Find positives
                if is_bool(globals()[each_var]):
                    for idx in range(len(config_list)):
                        config, trace = config_list[idx], data_traces[idx]
                        
                        if "-" + each_var in config:
                            pos_idx.add(idx)
                
                    # # print("Positives: " + str(pos_idx))
                    
                    # final_pos_trace = [min(col) for col in zip(*[feedback[idx][1] for idx in pos_idx])]
                    # final_pos_trace = [min(col) for col in zip(*[data_traces[idx] for idx in pos_idx])]
                    final_pos_trace = [min(col) for col in zip(*[data_traces[idx] for idx in pos_idx])]

                    # Build favoured list
                    favoured_ls = []
                    for idx, x in enumerate(final_pos_trace):
                        if x != 0:
                            favoured_ls.append(idx)
                    # print(favoured_ls)
                    save_presence_condition_data_info(("-" + each_var, favoured_ls))                   
                            
                else: # Not a bool
                    for idx in range(len(config_list)):
                        config, trace = config_list[idx], data_traces[idx]
                        
                        if "-" + each_var + " " + str(vars_to_analyze[each_var]) in config:
                            pos_idx.add(idx)
                
                    # print("Positives: " + str(pos_idx))
                    
                    final_pos_trace = [min(col) for col in zip(*[data_traces[idx] for idx in pos_idx])]
                    
                    # Build favoured list
                    favoured_ls = []
                    for idx, x in enumerate(final_pos_trace):
                        if x != 0:
                            favoured_ls.append(idx)
                    # print(favoured_ls)
                    save_presence_condition_data_info(("-" + each_var, favoured_ls))                   

                
                # Find negatives
                neg_idx = set(range(len(config_list))) - pos_idx
                
                if is_bool(globals()[each_var]):
                    for idx in range(len(config_list)):
                        config, trace = config_list[idx], data_traces[idx]
                        if "-" + each_var not in config:
                            neg_idx.add(idx)
                    
                    # print("Negatives: " + str(neg_idx))
                    
                    final_neg_trace = [min(col) for col in zip(*[data_traces[idx] for idx in neg_idx])]

                    # print("Final neg trace: " + str(final_neg_trace))
                    
                    favoured_ls = []
                    for idx, x in enumerate(final_neg_trace):
                        if x != 0:
                            favoured_ls.append(idx)
                    # print(favoured_ls)
                    save_presence_condition_data_info(("-" + each_var, favoured_ls))                   
                                
                else: # Not a bool
                    for idx in range(len(config_list)):
                        config, trace = config_list[idx], data_traces[idx]
                        if "-" + each_var + " " + str(vars_to_analyze[each_var]) not in config:
                            neg_idx.add(idx)
                    
                    # print("Negatives: " + str(neg_idx))
                    
                    final_neg_trace = [min(col) for col in zip(*[data_traces[idx] for idx in neg_idx])]
                    
                    favoured_ls = []
                    for idx, x in enumerate(final_neg_trace):
                        if x != 0:
                            favoured_ls.append(idx)
                    # print(favoured_ls)
                    save_presence_condition_data_info(("-" + each_var, favoured_ls)) 
    read_data_info()
    return 0


def save_presence_condition(analyzed_feedback, is_negated=False, pc_vars={}, use_pc_vars=False):
    config, trace, energy = analyzed_feedback[0], analyzed_feedback[1], int(analyzed_feedback[2])

    # Generate presence condition from config
    # print("Config>>>>: " + config)
    # print("Trace: " + str(trace))
    # print("Energy: " + str(energy))
    config = config.strip()
    pres_cond_str = generate_presence_condition(config, 
                                                is_negated=is_negated,
                                                pc_vars=pc_vars,
                                                use_pc_vars=use_pc_vars)
    # pres_cond = Preseonce_Condition(energy, "somefilepath", pres_cond_str)
    # print("Retrieved PC: " + pres_cond_str + " with energy: " + str(energy))
    pres_cond = None
    
    if (pres_cond_str == "default_settings_for_all"):
        pres_cond = "default_settings_for_all"
    else:
        # print("Pres cond str: " + pres_cond_str)
        pres_cond = eval(pres_cond_str)
    
    # Check if the presence condition is already in the pqeue
    with open("/tmp/pqeue.pkl", "rb") as file:
        pqeue = pickle.load(file)
        found = False
        for idx, each_pc in enumerate(pqeue):
            if pres_cond_str == "default_settings_for_all":
                if each_pc[1] == "default_settings_for_all":
                    if each_pc[0] > -energy:
                        each_pc = list(each_pc)
                        each_pc[0] = -energy
                        each_pc[2] = trace
                        pqeue[idx] = tuple(each_pc)
                    found = True
                    break
                # print("Default settings for all already in pqeue")
            else:
                if each_pc[1] == "default_settings_for_all":
                    continue
                # print("Cur str: " + each_pc[1])
                # print("Each pc: " + str(each_pc))
                cur = eval(each_pc[1])
                # print("Cur: " + str(cur))
                # print("Pres: " + str(pres_cond))
                if (is_equivalent(cur == pres_cond)):
                    if each_pc[0] > -energy:
                        each_pc = list(each_pc)
                        each_pc[0] = -energy
                        each_pc[2] = trace
                        pqeue[idx] = tuple(each_pc)
                    found = True
                    break
        if not found:
            heappush(pqeue, (-energy, pres_cond_str, trace))
    
    # print(pqeue)
    with open("/tmp/pqeue.pkl", "wb") as file:
        pickle.dump(pqeue, file)
    
        

# A config would like like: "-a -b -c 3"
# So we have to parse the config and find out what the presence condition is
def generate_presence_condition(config, is_negated=False, pc_vars={}, use_pc_vars=False):
    config_ls_raw = re.split(r'\s(?=-\w)', config)
    config_ls = [config.strip()[1:] for config in config_ls_raw if config != ""]
    multi = False
        
    pres_conds_str = ""
    
    if (is_negated):
        pres_conds_str = "Not("
    if len(config_ls) > 1:
        pres_conds_str = "And("
        multi = True
    # print(config_ls)
    if len(config_ls) == 0 or config_ls[0] == '':
        return "default_settings_for_all"
    
    for each in config_ls:
        opt_set = each.split(" ")
        if len(opt_set) <= 0:
            # print("Invalid config string")
            return
        
        opt_name = opt_set[0]
        opt = globals()[opt_name]
        
        if len(opt_set) == 1:
            if is_bool(opt):
                pres_conds_str += f"{opt}, "
            else:
                # print("Invalid config string")
                return
        else:
            set_value_str = opt_set[1]
            # Do something else
            if is_int(opt):
                pres_conds_str += f"{opt} == {set_value_str}, "
            elif is_real(opt):
                pres_conds_str += f"{opt} == {set_value_str}, "
            elif isinstance(opt, DatatypeRef):
                pres_conds_str += f"{opt} == {choice_dict[opt_name]}.opt{set_value_str}, "
            else:
                pres_conds_str += f"{opt} == StringVal({set_value_str}), "
    
    if multi:
        if use_pc_vars:
            for each in pc_vars:
                if each not in config_ls:
                    if is_bool(globals()[each]):
                        pres_conds_str += f"Not({each}), "
                    else:
                        pres_conds_str += f"(Not{each} == {pc_vars[each]}), "
        pres_conds_str = pres_conds_str[:-2] + ")"
    else:
        if use_pc_vars:
            pres_conds_str = "And(" + pres_conds_str
            for each in pc_vars:
                if each not in config_ls:
                    if is_bool(globals()[each]):
                        pres_conds_str += f"Not({each}), "
                    else:
                        pres_conds_str += f"(Not{each} == {pc_vars[each]}), "
                        
            pres_conds_str = pres_conds_str[:-2] + ")"
        else:
            pres_conds_str = pres_conds_str[:-2]
    if (is_negated):
        pres_conds_str += ")"
    
    # # print("BEFORE RET: " + pres_conds_str)
    # Check for commas in the whole str, if not, remove the And
    if pres_conds_str.count(",") == 0 and "And" in pres_conds_str:
        pres_conds_str = pres_conds_str[3:]
    pres_conds_str = pres_conds_str.replace("-", "_")
    pres_conds_str = pres_conds_str.replace(":", "colonoperator")
    # # print("BEFORE RET: " + pres_conds_str)
    return pres_conds_str


def save_presence_condition_data_info(analyzed_feedback, 
                                      is_negated=False, 
                                      pc_vars={}, 
                                      use_pc_vars=False):
    config, favoured_ls = analyzed_feedback[0], analyzed_feedback[1]
    
    # Generate presence condition from config
    # print("Config: " + config)
    pres_cond_str = generate_presence_condition(config, 
                                                is_negated=is_negated,
                                                pc_vars=pc_vars,
                                                use_pc_vars=use_pc_vars)
    # pres_cond = Preseonce_Condition(energy, "somefilepath", pres_cond_str)
    # print("Retrieved PC: " + pres_cond_str + " with list: " + str(favoured_ls))
    pres_cond = None
    
    if (pres_cond_str == "default_settings_for_all"):
        pres_cond = "default_settings_for_all"
    else:
        # print("Pres cond str: " + pres_cond_str)
        pres_cond = eval(pres_cond_str)

    # Check if the presence condition is already in the pqeue

    data_info_ls = []
    try:
        with open("/tmp/data_info.pkl", "rb") as file:
            data_info_ls = pickle.load(file)
    except OSError: # TODO: What do we do if we dont have the file and if empty
        # print("No file found")
        with open("/tmp/data_info.pkl", "wb") as file:
            pickle.dump(data_info_ls, file)




    with open("/tmp/data_info.pkl", "rb") as file:
        data_info_ls = pickle.load(file)
        found = False
        
        for idx, each_pc in enumerate(data_info_ls):
            if pres_cond_str == "default_settings_for_all":
                if each_pc[1] == "default_settings_for_all":
                    # if each_pc[0] > energy:
                    if favoured_ls != []:
                        each_pc = list(each_pc)
                        each_pc[0] = list(set(each_pc[0] + favoured_ls))
                        data_info_ls[idx] = tuple(each_pc)
                    found = True
                    break
                # print("Default settings for all already in ls")
            else:
                if each_pc[1] == "default_settings_for_all":
                    continue
                cur = eval(each_pc[1])
                if (is_equivalent(cur == pres_cond)):
                    if favoured_ls != []:
                        each_pc = list(each_pc)
                        each_pc[0] = list(set(each_pc[0] + favoured_ls))
                        data_info_ls[idx] = tuple(each_pc)
                    found = True
                    break
        if not found:
            data_info_ls.append((favoured_ls, pres_cond_str))
    # # print(data_info_ls)
    with open("/tmp/data_info.pkl", "wb") as file:
        pickle.dump(data_info_ls, file)


def read_data_info():
    with open("/tmp/data_info.pkl", "rb") as file:
        data = pickle.load(file)
        # print(data)


def read_pq():
    with open("/tmp/pqeue.pkl", "rb") as file:
        pqeue = pickle.load(file)
        
        for each in pqeue:
            print("--------------------------------------------")
            print("Energy: " + str(each[0]) + " PC: " + each[1])
            trace = each[2]
            for idx, bit in enumerate(trace):
                if bit != 0:
                    print("Bit: " + str(idx), end=" ")
            print("")


def clear_pq():
    with open("/tmp/pqeue.pkl", "wb") as file:
        pickle.dump([], file)


def clear_data_info():
    with open("/tmp/data_info.pkl", "wb") as file:
        pickle.dump([], file)


def init_info():
    return ([len(variable_list)])

def main():

    # constraint_file = sys.argv[1]
    # configs_to_generate = int(sys.argv[2])
    # save_presence_condition(("-a -b", 10))
    clear_pq()
    # save_pq()
    # save_pq_2()
    # read_pq()
    # solutions = request_config_generation('/tmp/pqeue.pkl', 10, 3)
    # # print(solutions)
    # analyze_feedback([
    #     ("-a -b", [0, 0, 0]), 
    #     ("-b", [0, 0, 0]), 
    #     ("-a", [1, 0, 0]),
    #     ("", [1, 1, 0])
    #     ], "And(Not(a), b)")

    # analyze_feedback([
    #     ("-a", [1, 0, 0]), 
    #     ("-b", [1, 1, 0]), 
    #     ("", [0, 0, 0])
    #     ], " ")

    # read_pq()
    # save_data_info()
    
    # analyze_feedback_data(["-a", "-b", "-a -b", " "], 
    #                       [[(1, 0, 0), (1, 1, 0), (2, 1, 0), (3, 0, 0), (3, 0, 0), (4, 1, 0), (5, 1, 0), (6, 1, 0)], 
    #                        [(1, 0, 0), (1, 0, 0), (2, 1, 0), (3, 0, 0), (3, 0, 0), (4, 0, 0), (5, 0, 0), (6, 1, 0)],
    #                        [(1, 0, 0), (1, 0, 0), (2, 0, 0), (3, 0, 0), (3, 1, 0), (4, 0, 0), (5, 0, 0), (6, 0, 0)],
    #                        [(1, 0, 0), (1, 0, 0), (2, 0, 0), (3, 0, 0), (3, 0, 0), (4, 0, 0), (5, 0, 0), (6, 0, 0)]], 
    #                       "And(a, b)", 6, 1)
    
    # analyze_feedback_data(["-a", "-b", "-c", "-d"], 
    #                   [[(10, 0, 0), (11, 1, 0), (12, 0, 0)], 
    #                    [(10, 0, 0), (11, 0, 0), (12, 1, 0)],
    #                    [(10, 1, 0), (11, 0, 0), (12, 0, 0)],
    #                    [(10, 1, 0), (11, 0, 0), (12, 1, 0)]], 
    #                   "And(a, b, c, d)", 12, 0)
    
    # analyze_feedback_data(["-a", "-b", "-a -b", " "], 
    #                   [[(10, 0, 0), (11, 1, 0), (12, 0, 0)], 
    #                    [(10, 0, 0), (11, 0, 0), (12, 1, 0)],
    #                    [(10, 1, 0), (11, 0, 0), (12, 0, 0)],
    #                    [(10, 1, 0), (11, 0, 0), (12, 1, 0)]], 
    #                   "And(a, b)", 12, 0)
    
    # analyze_feedback_data(["-a", "-b"], 
    #                   [[(10, 0, 0), (11, 0, 0), (12, 0, 0)], 
    #                    [(10, 1, 0), (11, 0, 0), (12, 1, 0)]], 
    #                   "And(a, b)", 10, 0)


    
    # read_data_info()
    # # print(extract_variable_names_and_values("(And(Not(a), b, c==3))"))
    
    # F = Not(And(a == True, b == True))
        # G = Or(Not(a), Not(b))
        # # print(is_equivalent(F == G))

if __name__ == '__main__':
    main()
