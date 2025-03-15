import itertools
import random
import string
from z3 import *
import sys
from generator_helpers import * 

debug = Bool('debug')
debugent = Bool('debugent')
copy = Bool('copy')
recover = Bool('recover')
huge = Bool('huge')
noent = Bool('noent')
noenc = Bool('noenc')
noout = Bool('noout')
load_trace = Bool('load_trace')
nonet = Bool('nonet')
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
maxmem = Int('maxmem')
nowarning = Bool('nowarning')
noblanks = Bool('noblanks')
nocdata = Bool('nocdata')
format = Bool('format')
dropdtd = Bool('dropdtd')
PrettyChoices = Datatype('PrettyChoices')
PrettyChoices.declare('opt0')
PrettyChoices.declare('opt1')
PrettyChoices.declare('opt2')
PrettyChoices = PrettyChoices.create()
pretty = Const('pretty', PrettyChoices)
c14n = Bool('c14n')
c14n11 = Bool('c14n11')
exc_c14n = Bool('exc_c14n')
nsclean = Bool('nsclean')
testIO = Bool('testIO')
catalogs = Bool('catalogs')
nocatalogs = Bool('nocatalogs')
auto = Bool('auto')
xinclude = Bool('xinclude')
noxincludenode = Bool('noxincludenode')
nofixup_base_uris = Bool('nofixup_base_uris')
loaddtd = Bool('loaddtd')
dtdattr = Bool('dtdattr')
stream = Bool('stream')
walker = Bool('walker')
chkregister = Bool('chkregister')
sax1 = Bool('sax1')
sax = Bool('sax')
oldxml10 = Bool('oldxml10')


def generate_config_strings(configs):
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
                option_str = f"-{key} {value}"
                config_str.append(option_str)
                if option_str not in option_indices:
                    option_indices[option_str] = []
                option_indices[option_str].append(idx)

        # Join all key=value pairs into a single string for this configuration
        config_strings.append(" ".join(config_str))

    print(option_indices)
    return [config_strings, option_indices]




def run_solver(constraint_file, configs_to_generate, generator_number=1):
    solver = Solver()

    # Variable declarations

    # Constraints
    solver.add(And(maxmem >= 0, maxmem <= 2147483647))
    solver.add(Or(Not(catalogs), Not(nocatalogs)))
    solver.add(Or(Not(xinclude), Not(noxincludenode)))
    solver.add(Implies(xmlout, And(Bool('html'))))

    # Generator helpers
    var_s = set()

    # Additional Constraints
    # Case: gen 1
    with open(constraint_file, 'r') as file:
        conditions = file.read()
        
        if generator_number == 1:
            print(conditions)
            var_s.update(extract_variable_names(conditions))           
            # var_s.add('pretty')
        else:
            exec(conditions)


    # GENERATOR 1
    if generator_number == 1:
        print("printing var_s")
        print(var_s)
        combinations = []
        variables = list(var_s)
        
        for i, var in enumerate(variables):
            if (isinstance(globals()[var], DatatypeSortRef)):
                variables.pop(i)
        
        print(variables)
        
        def backtrack(current_assignment, idx):
            if idx == len(variables):
                combinations.append(current_assignment.copy())
                return
            
            var_name = variables[idx]
            var = globals()[var_name]  # Obtain the Z3 variable using eval
            # print(var.sort)
            if is_bool(var):
                print("1")
                # Boolean variable - set to True or False
                for value in [True, False]:
                    current_assignment[var_name] = value
                    backtrack(current_assignment, idx + 1)
            
            elif is_int(var):
                print("2")
                # Integer variable - set to 3 random integers
                for value in random.sample(range(-100, 100), 3):
                    current_assignment[var_name] = value
                    backtrack(current_assignment, idx + 1)
            
            elif is_real(var):
                print("3")
                # Real variable - set to 3 random real numbers
                for value in [random.uniform(-100, 100) for _ in range(3)]:
                    current_assignment[var_name] = value
                    backtrack(current_assignment, idx + 1)
            
            elif isinstance(var, DatatypeRef):
                print("4")
                # Choice variable - set to each of its choices
                choices = var.sort().num_constructors()
                for choice_idx in range(choices):
                    current_assignment[var_name] = var.sort().constructor(choice_idx)
                    backtrack(current_assignment, idx + 1)
            else:
                print("5")
                # String variable - set to 3 random strings
                for value in [random_string() for _ in range(3)]:
                    current_assignment[var_name] = value
                    backtrack(current_assignment, idx + 1)

        backtrack({}, 0)

        config_strings = generate_config_strings(combinations)
        return config_strings


    # Generator 2?
    solutions = []
    sols_str = set()
    counter = 0
    while solver.check() == sat:
        config = ""
        model = solver.model()
        solutions.append(model)
        # print('SAT')
        print(model)

        # Create a blocking clause to exclude the current model
        block = []
        for var in model:
            print(var)
            config += "-"
            # Check if the variable is a boolean
            if is_true(model[var]) or is_false(model[var]):  # Boolean
                block.append(var != model[var])
                if is_true(model[var]):
                    config += str(var) + " "
                else:
                    config = config[:-1]
            elif model[var].sort().kind() == Z3_INT_SORT:  # Integer
                block.append(var != model[var])
                config += str(var) + " " + str(model[var]) + " "
            elif model[var].sort().kind() == Z3_REAL_SORT:  # Real
                block.append(var != model[var])
                config += str(var) + " " + str(model[var]) + " "
            elif model[var].sort().kind() == Z3_UNINTERPRETED_SORT:  # Enumeration (Uninterpreted sort)
                block.append(var != model[var])
                config += str(var) + " " + str(model[var]) + " "
            else:
                # If it's an unexpected type, just block the current value
                block.append(var != model[var])
                config += str(var) + " " + str(model[var]) + " "
                

        # Add the blocking clause to exclude the current model in the next iteration
        solver.add(Or(block))
        sols_str.add(config)
        counter+= 1
        if counter >= int(configs_to_generate):
            break


    if not solutions:
        print('UNSAT')
    return list(sols_str)

def main():
    if len(sys.argv) != 3:
        print('Usage: python [solver name].py <additional constraint file> <number of configs>')
        return

    constraint_file = sys.argv[1]
    configs_to_generate = int(sys.argv[2])
    solutions = run_solver(constraint_file, configs_to_generate)
    print(solutions)

if __name__ == '__main__':
    main()
