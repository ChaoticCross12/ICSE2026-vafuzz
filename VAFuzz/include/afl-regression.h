#ifndef AFL_REGRESSION_H
#define AFL_REGRESSION_H

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <errno.h>
#include <signal.h>
#include <dirent.h>
#include <ctype.h>
#include <fcntl.h>
#include <termios.h>
#include <dlfcn.h>
#include <sched.h>
#include "afl-fuzz.h"
#include "afl-presence-condition.h"

// void generate_encoded_matrix(afl_state_t *afl, u32 rows, u32 cols, u8 sample_code);
u32 generate_encoded_matrix(afl_state_t *afl, u8 sample_code);
void run_regression_analysis(afl_state_t *afl, struct config_queue_entry *selected_pres_cond, u8 sample_code);
// void check_and_expand_matrix(afl_state_t *afl);
void print_encoded_matrix(afl_state_t *afl, u32 rows);
void print_encoded_matrix_to_file(afl_state_t *afl, u32 rows, FILE *f);

#endif