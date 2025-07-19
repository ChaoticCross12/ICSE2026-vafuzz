# Introduction
This document is regarding our artifact for our paper titled “Variability-Aware Fuzzing” For ICSE 2026.

# File Structure
The submitted package is organized in the following structure.
* **VAFuzz** contains our source code. This is a fork of AFL++4.04c. In order to build it, please follow the build instructions in the directory.

* **Grammar** contains the grammar files we used throughout the evaluation of VAFuzz. These can be used to reproduce the results in our paper.

* **Evaluation Results** is a directory that contains all of our results from RQ1 and RQ2. Here we have:
  * `RQ1_Coverage.md`: This file contains the detailed coverage results for VAFuzz as well as every baseline used in our evaluation.
  * `RQ1_Unique_Bugs_Found.md`: Here we have a list and description of the unique bugs discovered during the RQ1 experiments.
  * `RQ1_Bug_IDs.md`: This file provides the specific bug IDs referenced in our RQ1 analysis, allowing for easy cross-referencing with our results and discussion.
  * `RQ2_Ablation_Study_1.md` and `RQ2_Ablation_Study_2.md`: These files contain the results of our ablation studies for RQ2, where we systematically removed or altered components to assess their impact on performance and bug-finding effectiveness. Specifically Study_1 modified different components of VAFuzz and Study_2 tested the impact of the initial configuration generation approach.
  * `Mutator_Analysis.md`: Here we have an analysis of the different mutators used in our fuzzing experiments, including their effectiveness and contribution to the results.
  * `Runtime Overhead.md`: This file presents measurements and analysis of the runtime overhead introduced by our approach, providing insight into its efficiency.
  * `bugs.png`: Here we have a visual summary (figure) of the common bugs found during our evaluation, as referenced in the paper.
  * `Presence Condition Analysis/`: This directory contains the results of our presence condition analysis, including:
    * `Summary.md`: A comprehensive summary of the presence condition analysis across all evaluated targets.
    * `djpeg.txt`, `jpegtran.txt`, `readelf.txt`, `xmllint.txt`: Here we have detailed, target-specific results for each of these programs, showing the outcomes of our presence condition analysis for each.

All the data pertaining to our Evaluation section is available in these files and subdirectories, providing a complete record of our experimental results and supporting data.

## Non AFL++ Dependencies
* python 3.11
* Z3 constraint solver (python3.11 -m pip install z3-solver)

# Building VAFuzz 
The build and run instructions in VAFuzz have been adopted from AFL++ 4.04c. Additionally, it is important to note that VAFuzz works on **LLVM-15**. For instrumentation, we added configuration changing support to the **afl-clang-fast**, and **afl-gcc** compilers. For all of our evaluations, we used **afl-clang-fast**.
