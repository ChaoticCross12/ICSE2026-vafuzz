#include <stdio.h>
#include "afl-fuzz.h"
void get_init_info(afl_state_t *afl, u8* z3_solver_path);
void split_and_remove_ext(const u8 *path, u8 *directory, u8 *filename);
void request_configs(afl_state_t *afl, u8* pres_cond_file_path, u8* z3_solver_path, u8 config_number);
void send_feedback(afl_state_t *afl, u8* z3_solver_path);
void send_data_feedback(afl_state_t *afl, u8* z3_solver_path);