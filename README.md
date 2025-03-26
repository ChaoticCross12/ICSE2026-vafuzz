# Introduction
This document is regarding our artifact for our paper titled “Variability-Aware Fuzzing” For ICSE 2026.

# File Structure
The submitted package is organized in the following structure.
* **VAFuzz** contains our source code. This is a fork of AFL++4.04c. In order to build it, please follow the build instructions in the directory.

* **Grammar** contains the grammar files we used throughout the evaluation of VAFuzz. These can be used to reproduce the results in our paper.

* **Evaluation Results** is a directory that contains all of our results from RQ1 and RQ2. Here, one will find our coverage results along with any other statistic that we mention throughout the paper. Also, we have our bug finding results, as mentioned in the paper, listed here. Our ablation study is also available in this directory. Overall, all the data pretaining to our Evaluation section is available in this spreadsheet.

## Non AFL++ Dependencies
* python 3.11
* Z3 constraint solver (python3.11 -m pip install z3-solver)

# Building VAFuzz 
The build and run instructions in VAFuzz have been adopted from AFL++ 4.04c. Additionally, it is important to note that VAFuzz works on **LLVM-15**. For instrumentation, we added configuration changing support to the **afl-clang-fast**, and **afl-gcc** compilers. For all of our evaluations, we used **afl-clang-fast**.
