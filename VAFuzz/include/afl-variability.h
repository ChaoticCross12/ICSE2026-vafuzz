#ifndef AFL_VARIABILITY_H
#define AFL_VARIABILITY_H

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
#include <math.h>

// Utilities
void copy_option_entry(struct option_entry *dest, struct option_entry *src);
void set_temp_config_file_path(afl_state_t *afl);
void copy_option_setting(struct option_setting *dest, struct option_setting *src);
u8 compare_option_setting(struct option_setting *opt_set1, struct option_setting *opt_set2);
void config_calibration_helper(afl_state_t *afl);
char* randomString(int length, u128);

u32 count_lines_in_file(u8 *);

// Variability Awareness
void read_grammar_file(afl_state_t *);
void generate_settings_matrix(afl_state_t *);
void expand_config_scores_matrix(afl_state_t *);
void generate_config_scores_matrix(afl_state_t *);
void free_settings_matrix(afl_state_t *);
void read_config_file(afl_state_t *);
void print_option_setting_matrix(afl_state_t *);
void print_config_score(afl_state_t *);
void print_config_score_lengths(afl_state_t *);
double* calibrate_config_case(afl_state_t *);
struct config_queue_entry variability_driver(afl_state_t *afl, bool first_run, u32 max_iters, struct config_queue_entry selected_pres_cond);
u8 inject_config_to_fsrv(afl_state_t *afl, struct option_setting **opt_setting_row);
u8 inject_config_str_to_fsrv(afl_state_t *afl, u8 *config);
// void read_config_str_file(afl_state_t *afl);
void variable_analysis_all_combs(afl_state_t *afl);
u8* bitmap_to_config(afl_state_t *afl, u8* bitmap);
u8* config_to_bitmap(afl_state_t *afl, u8* config);
void argv_havoc(afl_state_t *afl, u8* cur_bitmap);

int random_int(int min, int max);

double random_double(double min, double max);

#endif