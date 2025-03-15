#include "afl-regression.h"
#include "afl-presence-condition.h"
#include "afl-variability.h"
#include <gsl/gsl_multifit.h>
#include <math.h>

#define REG_COL_SIZE 50
#define MAX_KEY_SIZE 50

u8* generate_encoded_key(struct option_setting opt_set) {
  u8 *encoded_key = ck_alloc(sizeof(u8) * MAX_KEY_SIZE);
  if (opt_set.is_negated && strcmp(opt_set.type, "bool")) {
    strcat(encoded_key, "!");
  }

  strcat(encoded_key, opt_set.opt);

  if(strcmp(opt_set.type, "bool") == 0) {
    if(opt_set.bool_val == 1) {
      strcat(encoded_key, "_T");
    } else {
      strcat(encoded_key, "_F");
    }
  } else if (strcmp(opt_set.type, "intnum") == 0) {
    strcat(encoded_key, "_");
    u8* temp = ck_alloc(sizeof(u8) * 10);
    sprintf(temp, "%d", opt_set.int_val);
    strcat(encoded_key, temp);
  } else if (strcmp(opt_set.type, "realnum") == 0) {
    strcat(encoded_key, "_");
    u8* temp = ck_alloc(sizeof(u8) * 10);
    sprintf(temp, "%f", opt_set.real_val);
    strcat(encoded_key, temp);
  } else {
    strcat(encoded_key, "_");
    strcat(encoded_key, opt_set.str_val);
  }
  return encoded_key;
}


// sample Code: 0 = Pos, 1 = Neg, 2 = Whole (ignore statics)
u32 generate_encoded_matrix(afl_state_t *afl, u8 sample_code) {
  u128 configs_to_process = 0;
  if (sample_code == 0 || sample_code == 1) {
    configs_to_process = afl->config_count / 2;
  } else {
    configs_to_process = afl->config_count;
  }

  // Calculating number of rows
  u32 rows = 0;
  for (u32 i = 0; i < configs_to_process; i++) {
    if (sample_code == 1) {
    rows += afl->config_scores_lengths[i + configs_to_process];
    } else {
    rows += afl->config_scores_lengths[i];
    }
  }

  afl->encoded_opt_set_counter = 0;
  // mta todo: this needs to be smarter
  afl->regression_helper_ls = ck_alloc(sizeof(struct option_setting *) * 100);

  ACTF("Generating one-hot encoded matrix for options");
  afl->encoded_options = ck_alloc(sizeof(double **) * rows);
  afl->encoded_scores = ck_alloc(sizeof(double) * rows);

  

  // Initialize the matrix
  for (u32 i = 0; i < rows; i++) {
    afl->encoded_options[i] = ck_alloc(REG_COL_SIZE * sizeof(double *));
    for (u32 j = 0; j < REG_COL_SIZE; j++) {
      afl->encoded_options[i][j] = ck_alloc(sizeof(double));
      *afl->encoded_options[i][j] = 0.0;
    }
  }

  u32 encoded_rows_populated = 0;
  u32 cumulative_score_count;
  // For each configuration
  for (u32 i = 0; i < configs_to_process; i++) {
    u32 score_iter = 0;
    // For each option
    for (u32 j = 0; j < afl->options_count; j++) {
      struct option_setting *opt_set;
      if(sample_code == 1) {
        opt_set = afl->option_setting_matrix[i + configs_to_process][j];
      } else {
        opt_set = afl->option_setting_matrix[i][j];
      }
      // struct option_setting *opt_set = afl->option_setting_matrix[i][j];
      // Check if the option is set
      if (opt_set->opt == NULL || (opt_set->is_static && sample_code != 2)) { // NEW: And option is not static
        continue;
      } else {
        // If the option is set
        // Check if value in hashmap
        u8* encoded_key;
        if (sample_code == 1) {
          encoded_key = generate_encoded_key(*afl->option_setting_matrix[i + configs_to_process][j]);
        } else {
          encoded_key = generate_encoded_key(*afl->option_setting_matrix[i][j]);
        }
        // u8* encoded_key = generate_encoded_key(*afl->option_setting_matrix[i][j]);
        int opt_set_idx = hashIntGet(afl->encoded_opt_set_hashmap, encoded_key);

        if(opt_set_idx == -1) {
          // if not in hashmap, add to map and populate next untouched col
          hashIntInsert(afl->encoded_opt_set_hashmap, encoded_key, afl->encoded_opt_set_counter);
          
          // Regression Stuff
          u32 idx = hashIntGet(afl->encoded_opt_set_hashmap, encoded_key);
          if (afl->regression_helper_ls[idx] == NULL) {
            afl->regression_helper_ls[idx] = ck_alloc(sizeof(struct option_setting));
            afl->regression_helper_ls[idx] = afl->option_setting_matrix[i][j];
          } else {
             PFATAL("Error: Regression helper array is full");
          }

          opt_set_idx = hashIntGet(afl->encoded_opt_set_hashmap, encoded_key);
          afl->encoded_opt_set_counter++;
        }

        u32 temp = encoded_rows_populated;
        if (sample_code == 1) {
          cumulative_score_count = encoded_rows_populated + afl->config_scores_lengths[i + configs_to_process];
        } else {
          cumulative_score_count = encoded_rows_populated + afl->config_scores_lengths[i];
        }

        while (temp < cumulative_score_count) {
          *afl->encoded_options[temp][opt_set_idx] = 1.0;
          temp++;
        }        

        // for (u32 temp = i * afl->queued_items; temp < i * afl->queued_items + afl->queued_items; temp++) {
        //   *afl->encoded_options[temp][opt_set_idx] = 1.0;
        // }
      }
    }

    // Encode the scores for the configurations
    for (u32 k = encoded_rows_populated; k < cumulative_score_count; k++) {
      if (sample_code == 1) {
        afl->encoded_scores[k] = afl->config_scores[i + configs_to_process][score_iter];
        // afl->encoded_scores[ * afl->config_scores_lengths[i] + j] = afl->config_scores[i + configs_to_process][j];
      } else {
        afl->encoded_scores[k] = afl->config_scores[i][score_iter];
      }
      score_iter++;
    }
    
    if (sample_code == 1) {
      encoded_rows_populated += afl->config_scores_lengths[i + configs_to_process];
    } else {
      encoded_rows_populated += afl->config_scores_lengths[i];
    }
  }

  // Encode the scores for the configurations
  // afl->encoded_scores = ck_alloc(sizeof(double) * rows);
  // for (u32 i = 0; i < configs_to_process; i++) {
    // for (u32 j = 0; j < afl->config_scores_lengths[i]; j++) {
    //   if (sample_code == 0) {
    //     afl->encoded_scores[i * afl->config_scores_lengths[i] + j] = afl->config_scores[i][j];
    //   } else if (sample_code == 1) {
    //     afl->encoded_scores[i * afl->config_scores_lengths[i] + j] = afl->config_scores[i + configs_to_process][j];
    //   } else {
    //     afl->encoded_scores[i * afl->config_scores_lengths[i] + j] = afl->config_scores[i][j];
    //   }
    // }

    // for (u32 j = 0; j < afl->queued_items; j++) {
    //   if (sample_code == 0) {
    //     afl->encoded_scores[i * afl->queued_items + j] = afl->config_scores[i][j];
    //   } else if (sample_code == 1) {
    //     afl->encoded_scores[i * afl->queued_items + j] = afl->config_scores[i + configs_to_process][j];
    //   } else {
    //     afl->encoded_scores[i * afl->queued_items + j] = afl->config_scores[i][j];
    //   }
    // }
  // }
  OKF("One-hot encoded matrix generated");
  return encoded_rows_populated;
}


// sample Code: 0 = Pos, 1 = Neg, 2 = Whole (ignore statics)
// void generate_encoded_matrix(afl_state_t *afl, u32 rows, u32 cols, u8 sample_code) {
//   afl->encoded_opt_set_counter = 0;
//   // mta todo: this needs to be smarter
//   afl->regression_helper_ls = ck_alloc(sizeof(struct option_setting *) * 100);

//   ACTF("Generating one-hot encoded matrix for options");
//   afl->encoded_options = ck_alloc(sizeof(double **) * rows);
  

//   // Initialize the matrix
//   for (u32 i = 0; i < rows; i++) {
//     afl->encoded_options[i] = ck_alloc(REG_COL_SIZE * sizeof(double *));
//     for (u32 j = 0; j < REG_COL_SIZE; j++) {
//       afl->encoded_options[i][j] = ck_alloc(sizeof(double));
//       *afl->encoded_options[i][j] = 0.0;
//     }
//   }

//   u128 configs_to_process = 0;
//   if (sample_code == 0 || sample_code == 1) {
//     configs_to_process = afl->config_count / 2;
//   } else {
//     configs_to_process = afl->config_count;
//   }

//   // For each configuration
//   for (u32 i = 0; i < configs_to_process; i++) {
//     // For each option
//     for (u32 j = 0; j < cols; j++) {
//       struct option_setting *opt_set;
//       if(sample_code == 1) {
//         opt_set = afl->option_setting_matrix[i + configs_to_process][j];
//       } else {
//         opt_set = afl->option_setting_matrix[i][j];
//       }
//       // struct option_setting *opt_set = afl->option_setting_matrix[i][j];
//       // Check if the option is set
//       if (opt_set->opt == NULL || (opt_set->is_static && sample_code != 2)) { // NEW: And option is not static
//         continue;
//       } else {
//         // If the option is set
//         // Check if value in hashmap
//         u8* encoded_key;
//         if (sample_code == 1) {
//           encoded_key = generate_encoded_key(*afl->option_setting_matrix[i + configs_to_process][j]);
//         } else {
//           encoded_key = generate_encoded_key(*afl->option_setting_matrix[i][j]);
//         }
//         // u8* encoded_key = generate_encoded_key(*afl->option_setting_matrix[i][j]);
//         int opt_set_idx = hashIntGet(afl->encoded_opt_set_hashmap, encoded_key);

//         if(opt_set_idx == -1) {
//           // if not in hashmap, add to map and populate next untouched col
//           hashIntInsert(afl->encoded_opt_set_hashmap, encoded_key, afl->encoded_opt_set_counter);
          
//           // Regression Stuff
//           u32 idx = hashIntGet(afl->encoded_opt_set_hashmap, encoded_key);
//           if (afl->regression_helper_ls[idx] == NULL) {
//             afl->regression_helper_ls[idx] = ck_alloc(sizeof(struct option_setting));
//             afl->regression_helper_ls[idx] = afl->option_setting_matrix[i][j];
//           } else {
//              PFATAL("Error: Regression helper array is full");
//           }

//           opt_set_idx = hashIntGet(afl->encoded_opt_set_hashmap, encoded_key);
//           afl->encoded_opt_set_counter++;
//         }

//         for (u32 temp = i * afl->queued_items; temp < i * afl->queued_items + afl->queued_items; temp++) {
//           *afl->encoded_options[temp][opt_set_idx] = 1.0;

//         }
//       }
//     }
//   }

//   // Encode the scores for the configurations
//   afl->encoded_scores = ck_alloc(sizeof(double) * rows);
//   for (u32 i = 0; i < configs_to_process; i++) {
//     for (u32 j = 0; j < afl->queued_items; j++) {
//       if (sample_code == 0) {
//         afl->encoded_scores[i * afl->queued_items + j] = afl->config_scores[i][j];
//       } else if (sample_code == 1) {
//         afl->encoded_scores[i * afl->queued_items + j] = afl->config_scores[i + configs_to_process][j];
//       } else {
//         afl->encoded_scores[i * afl->queued_items + j] = afl->config_scores[i][j];
//       }
//     }
//   }

//   OKF("One-hot encoded matrix generated");
// }


// sample Code: 0 = Pos, 1 = Neg, 2 = Whole (ignore statics)
void run_regression_analysis(afl_state_t *afl, struct config_queue_entry *selected_pres_cond, u8 sample_code) {
  u128 configs_to_process = 0;
  u128 total_scored_executions = 0;

  if (sample_code == 0 || sample_code == 1) {
    configs_to_process = afl->config_count / 2;
    for (u32 i = 0; i < configs_to_process; i++) {
      if (sample_code == 0) {
        total_scored_executions += afl->config_scores_lengths[i];
      } else {
        total_scored_executions += afl->config_scores_lengths[i + configs_to_process];      
      }
    }
  } else {
    configs_to_process = afl->config_count;
    for (u32 i = 0; i < configs_to_process; i++) {
        total_scored_executions += afl->config_scores_lengths[i];
    }
  }

  // GSL Variables
  gsl_matrix *X = gsl_matrix_alloc(total_scored_executions, afl->encoded_opt_set_counter);
  gsl_vector *y = gsl_vector_alloc(total_scored_executions);
  gsl_vector *c = gsl_vector_alloc(afl->encoded_opt_set_counter);
  gsl_matrix *cov = gsl_matrix_alloc(afl->encoded_opt_set_counter, afl->encoded_opt_set_counter);
  gsl_multifit_linear_workspace *work = gsl_multifit_linear_alloc(total_scored_executions, afl->encoded_opt_set_counter);
  double *res = ck_alloc(sizeof(double) * total_scored_executions);

  u128 significant_count = 0;
  u128 sig_arr[afl->encoded_opt_set_counter];
  for (u32 i = 0; i < afl->encoded_opt_set_counter; i++) {
    sig_arr[i] = 0;
  }

  // Populate the target vector and design matrix
  for (u32 i = 0; i < total_scored_executions; i++) {
    for (u32 j = 0; j < afl->encoded_opt_set_counter; j++) {
      gsl_matrix_set(X, i, j, *afl->encoded_options[i][j]); 
    }    

    gsl_vector_set(y, i, afl->encoded_scores[i]);
  } 

  // print matrix and vector sizes
  printf("X: %ld x %ld\n", X->size1, X->size2);
  printf("y: %ld\n", y->size);

  gsl_multifit_linear(X, y, c, cov, res, work);

gsl_vector *std_err = gsl_vector_alloc(afl->encoded_opt_set_counter);
for (u32 i = 0; i < afl->encoded_opt_set_counter; i++) {
    gsl_vector_set(std_err, i, sqrt(gsl_matrix_get(cov, i, i)));
}

// Compute the t-statistics and determine significance
double alpha = afl->t_stat_crit_val; // Significance level
for (u32 i = 0; i < afl->encoded_opt_set_counter; i++) {
    double coef = gsl_vector_get(c, i);
    double se = gsl_vector_get(std_err, i);
    double t_stat = coef / se;

    // Calculate degrees of freedom (n - p)
    int df = total_scored_executions - afl->encoded_opt_set_counter - 1;

    // Calculate critical value from t-distribution
    double crit_value = gsl_cdf_tdist_Qinv(alpha / 2.0, df);

    printf("c_%d = %g, t-statistic = %g ", i, coef, t_stat);

    if (fabs(t_stat) > crit_value) {
        significant_count++;
        sig_arr[i] = 1;
        printf("significant at %.2f%% level\n", i, (1.0 - alpha) * 100);
    } else {
        printf("NOT statistically significant at %.2f%% level\n", i, (1.0 - alpha) * 100);
    }
}

  /***********************/
  /*    Presence Cond    */
  /***********************/
  // Add to config queue using helper array
  // MTA: creating new one every round. Need to fix this
  

  for (u32 i = 0; i < afl->encoded_opt_set_counter; i++) {
    if (sig_arr[i] == 0) {
      continue;
    }

    if(selected_pres_cond == NULL || sample_code == 2) {
      struct presence_condition_single *pres_cond = ck_alloc(sizeof(struct presence_condition_single));
      afl->regression_helper_ls[i]->is_static = true;
      copy_option_setting(&pres_cond->single_opt_set, afl->regression_helper_ls[i]);
      pres_cond->is_negated = false;
      pres_cond->end_of_condition = true;
      pres_cond->next_operator = 0;

      enqueue(afl->presence_condition_queue, pres_cond, gsl_vector_get(c, i), 1); // Last parameter needs to be updated

    } else {
      struct presence_condition_single *pres_cond = ck_alloc(sizeof(struct presence_condition_single) * (selected_pres_cond->conds_count + 1));
      for (u32 j = 0; j < selected_pres_cond->conds_count; j++) {
        // Here we are adding the opt sets in the presence cond to the new presence cond. We should negate here.
        copy_option_setting(&pres_cond[j].single_opt_set, &selected_pres_cond->pres_conds[j].single_opt_set);

        if (sample_code == 1) {
          pres_cond[j].single_opt_set.is_negated = true;
          if (strcmp(pres_cond[j].single_opt_set.type, "bool") == 0) {
            if (pres_cond[j].single_opt_set.bool_val == 1) {
              pres_cond[j].single_opt_set.bool_val = 0;
            } else {
              pres_cond[j].single_opt_set.bool_val = 1;
            }
          }
          pres_cond[j].is_negated = true;
        } else {
          pres_cond[j].is_negated = selected_pres_cond->pres_conds[j].is_negated;
        }

        pres_cond[j].next_operator = selected_pres_cond->pres_conds[j].next_operator;
        pres_cond[j].end_of_condition = false;
      }

      copy_option_setting(&pres_cond[selected_pres_cond->conds_count].single_opt_set, afl->regression_helper_ls[i]);
      pres_cond[selected_pres_cond->conds_count].is_negated = false;
      pres_cond[selected_pres_cond->conds_count].end_of_condition = true;
      pres_cond[selected_pres_cond->conds_count].next_operator = 0;

      enqueue(afl->presence_condition_queue, pres_cond, gsl_vector_get(c, i), selected_pres_cond->conds_count + 1); // Last parameter needs to be updated
    }
  } 

  // If no significant presence conditions found, add all if queue is empty
  if (!significant_count && is_empty(afl->presence_condition_queue)) {
    printf("No significant presence conditions found\n");
    printf("Adding all if queue is empty\n");
    
      for (u32 i = 0; i < afl->encoded_opt_set_counter; i++) {
        if (afl->presence_condition_queue->size == afl->presence_condition_queue->capacity) {
          break;
        }
        
        if(selected_pres_cond == NULL) {
          struct presence_condition_single *pres_cond = ck_alloc(sizeof(struct presence_condition_single));
          copy_option_setting(&pres_cond->single_opt_set, afl->regression_helper_ls[i]);
          pres_cond->is_negated = false;
          pres_cond->end_of_condition = true;
          pres_cond->next_operator = 0;

        } else {
          struct presence_condition_single *pres_cond = ck_alloc(sizeof(struct presence_condition_single) * (selected_pres_cond->conds_count + 1));
          for (u32 j = 0; j < selected_pres_cond->conds_count; j++) {
          copy_option_setting(&pres_cond[j].single_opt_set, &selected_pres_cond->pres_conds[j].single_opt_set);
          pres_cond[j].is_negated = selected_pres_cond->pres_conds[j].is_negated;
          pres_cond[j].next_operator = selected_pres_cond->pres_conds[j].next_operator;
          pres_cond[j].end_of_condition = false;
        }

        copy_option_setting(&pres_cond[selected_pres_cond->conds_count].single_opt_set, afl->regression_helper_ls[i]);
        pres_cond[selected_pres_cond->conds_count].is_negated = false;
        pres_cond[selected_pres_cond->conds_count].end_of_condition = true;
        pres_cond[selected_pres_cond->conds_count].next_operator = 0;

        enqueue(afl->presence_condition_queue, pres_cond, gsl_vector_get(c, i), selected_pres_cond->conds_count + 1); // Last parameter needs to be updated
      }
    }
  }

  gsl_vector_free(std_err);
  gsl_matrix_free(X);
  gsl_vector_free(y);
  gsl_vector_free(c);
  gsl_matrix_free(cov);
  gsl_multifit_linear_free(work);
  ck_free(res);
  ck_free(afl->encoded_scores);
  freeHashIntMap(afl->encoded_opt_set_hashmap);
  ck_free(afl->regression_helper_ls);
}

// void check_and_expand_matrix() {
//   // MTA: Implement this
// }

/* DEBUG: print encoded matrix*/
void print_encoded_matrix(afl_state_t *afl, u32 rows) {
  printf("Encoded Hashmap:\n");
  printHashIntMap(afl->encoded_opt_set_hashmap);
  printf("Printing ENCODED option setting matrix:\n");

  for(u16 c = 0; c < afl->encoded_opt_set_counter; c++) {
    printf("|%.8d|", c);
  }
  printf("| SCORES |");

  printf("\n");

  for (u16 i = 0; i < rows; i++) {
    printf("%d: ", i);
    for (u16 j = 0; j < afl->encoded_opt_set_counter; j++) {
      printf("|%f|", *afl->encoded_options[i][j]);
    }
    printf("|%f|", afl->encoded_scores[i]);
    printf("\n");
  }
  printf("\n");
}

void print_encoded_matrix_to_file(afl_state_t *afl, u32 rows, FILE *f) {
  fprintf(f, "Encoded Hashmap:\n");
  printHashIntMapToFile(afl->encoded_opt_set_hashmap, f);
  fprintf(f, "Printing ENCODED option setting matrix:\n");

  for(u16 c = 0; c < afl->encoded_opt_set_counter; c++) {
    fprintf(f, "|%.8d|", c);
  }
  fprintf(f, "| SCORES |");

  fprintf(f, "\n");

  for (u16 i = 0; i < rows; i++) {
    fprintf(f, "%d: ", i);
    for (u16 j = 0; j < afl->encoded_opt_set_counter; j++) {
      fprintf(f, "|%f|", *afl->encoded_options[i][j]);
    }
    fprintf(f, "|%f|", afl->encoded_scores[i]);
    fprintf(f, "\n");
  }

  fprintf(f, "=========================================================\n");

}
