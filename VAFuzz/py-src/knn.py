import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pickle
from collections import defaultdict


def cull_pc_queue():
    with open("/tmp/pqeue.pkl", "rb") as file:
        pqeue = pickle.load(file)
        # print("Currently we have {} traces".format(len(pqeue)))
        # print("Current Presence Conditions:")
        # for each in pqeue:
        #     print(each[1])
        
        selected, coverage, unique_bits = select_structured_traces_complete(pqeue)
        # print(f"Original traces: {len(pqeue)}")
        # print(f"Selected traces: {len(selected)}")
        # print(f"Total bit positions covered: {sorted(coverage)}")
        # print("\nTraces with unique bits:")
        for idx, bits in unique_bits.items():
            num, string, _ = pqeue[idx]
            # print(f"Trace {num} ({string}) uniquely covers bits: {sorted(bits)}")
        # print("\nSelected traces with metadata:")
        # for num, string, trace in selected:
            # print(f"Number: {num}, String: {string}")
            # print(f"Trace: {trace}")
            # print()
        
        
        # Save selected traces to pqeue.pkl
        with open("/tmp/pqeue.pkl", "wb") as file:
            pickle.dump(selected, file)
            

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
    traces = np.array([t[2] for t in trace_tuples])
    
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
        

if __name__ == "__main__":
    cull_pc_queue()