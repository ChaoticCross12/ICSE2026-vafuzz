import ast
import random
import string
import re
from z3 import *

# KNN
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pickle
from collections import defaultdict


# This will serve as a mapping between the Z3 variable names
# and their corresponding Z3 variables.
class Option:
    def __init__(
        self, opt_name, opt_type,
        prefix, connector=' ',
        choices = [], 
        range_l = 0, range_h = 0):
        
        self.opt_name = opt_name
        self.opt_type = opt_type
        self.prefix = prefix
        self.connector = connector
        self.choices = choices
        self.range_h = range_h
        self.range_l = range_l
        
        self.z3_var = None
        self.z3_choices = None
        
        if self.opt_type == "bool":
            self.z3_var = Bool(opt_name)
        elif self.opt_type == "int":
            self.z3_var = Int(opt_name)
        elif self.opt_type == "real":
            self.z3_var = Real(opt_name)
        elif self.opt_type == "choice":
            self.z3_choices = Datatype(opt_name + "_choices")
            for choice in choices:
                self.z3_choices.declare(choice)
            self.z3_choices = self.z3_choices.create()
            self.z3_var = Const(opt_name, self.z3_choices)

def extract_variable_names(constraint_string):
    
    """
    Extract Z3 variable names from a complex constraint string like 'solver.add(And(Not(html), chkregister))'.
    It handles multiple logical operations and returns a set of variable names.
    """
    try:
        # Parse the string as an AST
        tree = ast.parse(constraint_string)
    except SyntaxError:
        print("Invalid constraint string.")
        return set()

    variable_names = set()

    # Walk through the tree and extract variable names
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            # Add variables (Name nodes like `html` and `chkregister`)
            variable_names.add(node.id)

    # Filter out known keywords like 'solver', 'add', 'Not', 'And', 'Or', 'Implies'
    keywords = {"solver", "add", "Not", "And", "Or", "Implies", "True", "False"}
    return variable_names - keywords


def extract_option_names(constraint_string):
    pattern = r"options\['(.*?)'\]"
    return set(re.findall(pattern, constraint_string))


# def extract_variable_names_and_values(constraint_string):
#     """
#     Extracts variable names and their values from a constraint string.
#     If a variable has no explicit value, it is assumed to be a boolean set to True.
#     Ignores specific keywords.
#     """
#     # Define the keywords to ignore
#     keywords = {"solver", "add", "Not", "And", "Or", "Implies", "True", "False"}
    
#     # Regular expression to capture assignments or comparisons of the form `var == value`
#     pattern = r'\b(\w+)\s*==\s*([\w"]+)|\b(\w+)\b'
#     matches = re.findall(pattern, constraint_string)
    
#     variable_values = {}

#     for match in matches:
#         if match[0] and match[0] not in keywords:  # If the first group is non-empty, it's an assignment
#             var_name, var_value = match[0], match[1]
#             # Try to convert var_value to int if it's numeric, otherwise keep as string
#             variable_values[var_name] = int(var_value) if var_value.isdigit() else var_value.strip('"')
#         elif match[2] and match[2] not in keywords:  # If the third group is non-empty, it's a standalone variable
#             var_name = match[2]
#             if var_name not in variable_values:  # Set to True if not explicitly assigned
#                 variable_values[var_name] = True

#     return variable_values

def extract_variable_names_and_values(constraint_string):
    """
    Extracts variable names and their values from a complex constraint string.
    Handles nested dictionary access, Z3 variable extraction, and numeric values.
    """
    keywords = {"solver", "add", "Not", "And", "Or", "Implies", "True", "False"}
    
    pattern = r'(options\[\'?\w+\'?\]\.z3_var)\s*==\s*(options\[\'?\w+\'?\]\.z3_choices\.\w+|\d+(?:\.\d+)?)\b|(options\[\'?\w+\'?\]\.z3_var)\b'
    matches = re.findall(pattern, constraint_string)
    
    variable_values = {}

    for match in matches:
        if match[0] and match[0] not in keywords:
            var_name, var_value = match[0], match[1]
            # Convert to numeric if it's a number
            if var_value.replace('.', '').isdigit():
                var_value = float(var_value) if '.' in var_value else int(var_value)
            variable_values[var_name] = var_value
        elif match[2] and match[2] not in keywords:
            var_name = match[2]
            if var_name not in variable_values:
                variable_values[var_name] = True

    return variable_values

# Generate random strings
def random_string(length=3):
    return ''.join(random.choices(string.ascii_letters, k=length))

# Generate all combinations based on variable types
def generate_combinations(variables):
    combinations = []
    
    def backtrack(current_assignment, idx):
        if idx == len(variables):
            combinations.append(current_assignment.copy())
            return
        
        var_name = variables[idx]
        var = eval(var_name)  # Obtain the Z3 variable using eval
        
        if is_bool(var):
            # Boolean variable - set to True or False
            for value in [True, False]:
                current_assignment[var_name] = value
                backtrack(current_assignment, idx + 1)
        
        elif is_int(var):
            # Integer variable - set to 3 random integers
            for value in random.sample(range(-100, 100), 3):
                current_assignment[var_name] = value
                backtrack(current_assignment, idx + 1)
        
        elif is_real(var):
            # Real variable - set to 3 random real numbers
            for value in [random.uniform(-100, 100) for _ in range(3)]:
                current_assignment[var_name] = value
                backtrack(current_assignment, idx + 1)
        
        elif is_choice(var):
            # Choice variable - set to each of its choices
            choices = var.sort().num_constructors()
            for choice_idx in range(choices):
                current_assignment[var_name] = choice_idx
                backtrack(current_assignment, idx + 1)
        
        elif is_string(var):
            # String variable - set to 3 random strings
            for value in [random_string() for _ in range(3)]:
                current_assignment[var_name] = value
                backtrack(current_assignment, idx + 1)

    backtrack({}, 0)
    return combinations


def clean_data_arrs(data_obj_list, id_cutoff):
    filtered_arrays = []
    for array in data_obj_list:
        # Find the index of the last occurrence of the cutoff ID
        last_index = max((i for i, item in enumerate(array) if item[0] == id_cutoff), default=-1)
        
        # Slice the array up to and including the last occurrence
        filtered_array = array[:last_index + 1] if last_index != -1 else []
        
        filtered_arrays.append(filtered_array)
    
    return filtered_arrays


def keep_last_entries_by_id(arrays):
    filtered_arrays = []
    
    for array in arrays:
        # Dictionary to store the last occurrence of each ID
        last_entries = {}
        
        # Iterate through the array to find last occurrences
        for item in array:
            last_entries[item[0]] = item
        
        # Convert the last entries dictionary back to a list, sorted by ID
        filtered_array = list(last_entries.values())
        
        # Optional: Sort the filtered array by the first element (ID)
        filtered_array.sort(key=lambda x: x[0])
        
        filtered_arrays.append(filtered_array)
    
    return filtered_arrays


def convert_to_bitmap(arrays):
    bitmaps = []

    # Find the maximum ID across all arrays to determine bitmap length
    max_id = max(max(item[0] for item in array) for array in arrays)
    
    for array in arrays:
        # Initialize bitmap with zeros
        bitmap = [0] * (max_id + 1)
        
        # Fill in values for existing IDs
        for item in array:
            bitmap[item[0]] = item[1]
        
        bitmaps.append(bitmap)
    
    return bitmaps


def cull_pc_queue():
    with open("/tmp/pqeue.pkl", "rb") as file:
        pqeue = pickle.load(file)
        
        selected, coverage, unique_bits = select_structured_traces_complete(pqeue)
        for idx, bits in unique_bits.items():
            num, string, _ = pqeue[idx]        
        
        # Save selected traces to pqeue.pkl
        with open("/tmp/pqeue.pkl", "wb") as file:
            pickle.dump(selected, file)

def pad_traces(trace_lists):
    """Pad all traces to the length of the longest trace."""
    max_length = max(len(trace) for trace in trace_lists)
    padded_traces = []
    for trace in trace_lists:
        # Pad with zeros if necessary
        padded = list(trace) + [0] * (max_length - len(trace))
        padded_traces.append(padded)
    return np.array(padded_traces)

def select_structured_traces_complete(trace_tuples, k=None, min_coverage=1):
    """
    Select diverse traces ensuring no unique bits are lost.
    
    Args:
        trace_tuples: List of tuples, each containing (number, string, trace_list)
        k: Number of clusters (if None, will be estimated)
        min_coverage: Minimum number of times a bit should be reached to be considered covered
    
    Returns:
        selected_traces: List of selected (number, string, trace_list) tuples
        coverage: Set of bit positions covered
        unique_bits_info: Dict mapping selected traces to their unique bits
    """
    # Extract just the trace lists for analysis
    traces = pad_traces([t[2] for t in trace_tuples])
    
    # First, identify traces with unique bits
    bit_execution_count = defaultdict(set)  # Maps bit position to traces that execute it
    for idx, trace in enumerate(traces):
        for bit_pos, freq in enumerate(trace):
            if freq >= min_coverage:
                bit_execution_count[bit_pos].add(idx)
    
    # Find traces that are the only ones executing certain bits
    unique_executors = set()
    unique_bits_info = defaultdict(set)
    
    for bit_pos, executing_traces in bit_execution_count.items():
        if len(executing_traces) == 1:
            trace_idx = executing_traces.pop()
            unique_executors.add(trace_idx)
            unique_bits_info[trace_idx].add(bit_pos)
    
    # Start with traces that have unique bits
    selected_indices = list(unique_executors)
    selected_tuples = [trace_tuples[idx] for idx in selected_indices]
    
    # Calculate current coverage
    coverage = set()
    for idx in selected_indices:
        coverage.update(j for j, freq in enumerate(traces[idx]) 
                       if freq >= min_coverage)
    
    # Remove already selected traces from consideration
    remaining_traces = [(idx, trace) for idx, trace in enumerate(traces) 
                       if idx not in selected_indices]
    
    if remaining_traces:
        # Prepare remaining traces for clustering
        remaining_indices = [idx for idx, _ in remaining_traces]
        remaining_trace_arrays = np.array([trace for _, trace in remaining_traces])
        
        # Scale the remaining traces
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(remaining_trace_arrays)
        
        # Determine k for remaining traces
        if k is None:
            unique_patterns = len(set(tuple(x > 0) for x in remaining_trace_arrays))
            k = max(2, min(unique_patterns, len(remaining_trace_arrays) // 2))
        
        # Cluster remaining traces
        kmeans = KMeans(n_clusters=k, random_state=42)
        clusters = kmeans.fit_predict(X_scaled)
        
        # Select representatives from each cluster
        for i in range(k):
            cluster_indices = [idx for idx, cluster in enumerate(clusters) if cluster == i]
            if not cluster_indices:
                continue
            
            # Find trace in cluster that adds most new coverage
            best_new_coverage = 0
            best_trace_idx = None
            
            for cluster_idx in cluster_indices:
                original_idx = remaining_indices[cluster_idx]
                trace = traces[original_idx]
                trace_positions = {j for j, freq in enumerate(trace) 
                                 if freq >= min_coverage}
                new_coverage = len(trace_positions - coverage)
                
                if new_coverage > best_new_coverage:
                    best_new_coverage = new_coverage
                    best_trace_idx = original_idx
            
            if best_trace_idx is not None and best_new_coverage > 0:
                selected_indices.append(best_trace_idx)
                selected_tuples.append(trace_tuples[best_trace_idx])
                coverage.update(j for j, freq in enumerate(traces[best_trace_idx]) 
                              if freq >= min_coverage)
    
    return selected_tuples, coverage, dict(unique_bits_info)
