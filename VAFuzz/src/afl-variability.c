#include "afl-variability.h"
#include <libgen.h>
#include "afl-presence-condition.h"
#include <limits.h>
#include <time.h>

// #include "afl-mutations.h"

int random_int(int min, int max) {
    return min + rand() % (max - min + 1);
}

double random_double(double min, double max) {
    double scale = rand() / (double) RAND_MAX;
    return min + scale * (max - min);
}

enum {

  /* 00 */ MUT_FLIPBIT,
  /* 01 */ MUT_INTERESTING8,
  /* 02 */ MUT_INTERESTING16,
  /* 03 */ MUT_INTERESTING16BE,
  /* 04 */ MUT_INTERESTING32,
  /* 05 */ MUT_INTERESTING32BE,
  /* 06 */ MUT_ARITH8_,
  /* 07 */ MUT_ARITH8,
  /* 08 */ MUT_ARITH16_,
  /* 09 */ MUT_ARITH16BE_,
  /* 10 */ MUT_ARITH16,
  /* 11 */ MUT_ARITH16BE,
  /* 12 */ MUT_ARITH32_,
  /* 13 */ MUT_ARITH32BE_,
  /* 14 */ MUT_ARITH32,
  /* 15 */ MUT_ARITH32BE,
  /* 16 */ MUT_RAND8,
  /* 17 */ MUT_CLONE_COPY,
  /* 18 */ MUT_CLONE_FIXED,
  /* 19 */ MUT_OVERWRITE_COPY,
  /* 20 */ MUT_OVERWRITE_FIXED,
  /* 21 */ MUT_BYTEADD,
  /* 22 */ MUT_BYTESUB,
  /* 23 */ MUT_FLIP8,
  /* 24 */ MUT_SWITCH,
  /* 25 */ MUT_DEL,
  /* 26 */ MUT_SHUFFLE,
  /* 27 */ MUT_DELONE,
  /* 28 */ MUT_INSERTONE,
  /* 29 */ MUT_ASCIINUM,
  /* 30 */ MUT_INSERTASCIINUM,
  /* 31 */ MUT_EXTRA_OVERWRITE,
  /* 32 */ MUT_EXTRA_INSERT,
  /* 33 */ MUT_AUTO_EXTRA_OVERWRITE,
  /* 34 */ MUT_AUTO_EXTRA_INSERT,
  /* 35 */ MUT_SPLICE_OVERWRITE,
  /* 36 */ MUT_SPLICE_INSERT,

  MUT_MAX

};
#define MUT_BIN_ARRAY_SIZE 256
u32 binary_array_argv[MUT_BIN_ARRAY_SIZE] = {MUT_FLIPBIT,
                                        MUT_FLIPBIT,
                                        MUT_FLIPBIT,
                                        MUT_FLIPBIT,
                                        MUT_FLIPBIT,
                                        MUT_FLIPBIT,
                                        MUT_FLIPBIT,
                                        MUT_FLIPBIT,
                                        MUT_FLIPBIT,
                                        MUT_FLIPBIT,
                                        MUT_FLIPBIT,
                                        MUT_INTERESTING8,
                                        MUT_INTERESTING8,
                                        MUT_INTERESTING8,
                                        MUT_INTERESTING8,
                                        MUT_INTERESTING8,
                                        MUT_INTERESTING8,
                                        MUT_INTERESTING8,
                                        MUT_INTERESTING8,
                                        MUT_INTERESTING8,
                                        MUT_INTERESTING16,
                                        MUT_INTERESTING16,
                                        MUT_INTERESTING16,
                                        MUT_INTERESTING16,
                                        MUT_INTERESTING16,
                                        MUT_INTERESTING16,
                                        MUT_INTERESTING16BE,
                                        MUT_INTERESTING16BE,
                                        MUT_INTERESTING16BE,
                                        MUT_INTERESTING16BE,
                                        MUT_INTERESTING16BE,
                                        MUT_INTERESTING16BE,
                                        MUT_INTERESTING32,
                                        MUT_INTERESTING32,
                                        MUT_INTERESTING32,
                                        MUT_INTERESTING32,
                                        MUT_INTERESTING32,
                                        MUT_INTERESTING32,
                                        MUT_INTERESTING32BE,
                                        MUT_INTERESTING32BE,
                                        MUT_INTERESTING32BE,
                                        MUT_INTERESTING32BE,
                                        MUT_INTERESTING32BE,
                                        MUT_INTERESTING32BE,
                                        MUT_ARITH8_,
                                        MUT_ARITH8_,
                                        MUT_ARITH8_,
                                        MUT_ARITH8_,
                                        MUT_ARITH8_,
                                        MUT_ARITH8_,
                                        MUT_ARITH8_,
                                        MUT_ARITH8_,
                                        MUT_ARITH8_,
                                        MUT_ARITH8,
                                        MUT_ARITH8,
                                        MUT_ARITH8,
                                        MUT_ARITH8,
                                        MUT_ARITH8,
                                        MUT_ARITH8,
                                        MUT_ARITH8,
                                        MUT_ARITH8,
                                        MUT_ARITH8,
                                        MUT_ARITH8,
                                        MUT_ARITH16_,
                                        MUT_ARITH16_,
                                        MUT_ARITH16_,
                                        MUT_ARITH16_,
                                        MUT_ARITH16_,
                                        MUT_ARITH16_,
                                        MUT_ARITH16BE_,
                                        MUT_ARITH16BE_,
                                        MUT_ARITH16BE_,
                                        MUT_ARITH16BE_,
                                        MUT_ARITH16BE_,
                                        MUT_ARITH16BE_,
                                        MUT_ARITH16,
                                        MUT_ARITH16,
                                        MUT_ARITH16,
                                        MUT_ARITH16,
                                        MUT_ARITH16,
                                        MUT_ARITH16,
                                        MUT_ARITH16BE,
                                        MUT_ARITH16BE,
                                        MUT_ARITH16BE,
                                        MUT_ARITH16BE,
                                        MUT_ARITH16BE,
                                        MUT_ARITH16BE,
                                        MUT_ARITH32_,
                                        MUT_ARITH32_,
                                        MUT_ARITH32_,
                                        MUT_ARITH32_,
                                        MUT_ARITH32_,
                                        MUT_ARITH32_,
                                        MUT_ARITH32BE_,
                                        MUT_ARITH32BE_,
                                        MUT_ARITH32BE_,
                                        MUT_ARITH32BE_,
                                        MUT_ARITH32BE_,
                                        MUT_ARITH32BE_,
                                        MUT_ARITH32,
                                        MUT_ARITH32,
                                        MUT_ARITH32,
                                        MUT_ARITH32,
                                        MUT_ARITH32,
                                        MUT_ARITH32,
                                        MUT_ARITH32BE,
                                        MUT_ARITH32BE,
                                        MUT_ARITH32BE,
                                        MUT_ARITH32BE,
                                        MUT_ARITH32BE,
                                        MUT_ARITH32BE,
                                        MUT_RAND8,
                                        MUT_RAND8,
                                        MUT_RAND8,
                                        MUT_RAND8,
                                        MUT_RAND8,
                                        MUT_RAND8,
                                        MUT_RAND8,
                                        MUT_RAND8,
                                        MUT_RAND8,
                                        MUT_CLONE_COPY,
                                        MUT_CLONE_COPY,
                                        MUT_CLONE_COPY,
                                        MUT_CLONE_COPY,
                                        MUT_CLONE_COPY,
                                        MUT_CLONE_COPY,
                                        MUT_CLONE_COPY,
                                        MUT_CLONE_COPY,
                                        MUT_CLONE_COPY,
                                        MUT_CLONE_COPY,
                                        MUT_CLONE_COPY,
                                        MUT_CLONE_COPY,
                                        MUT_CLONE_COPY,
                                        MUT_CLONE_COPY,
                                        MUT_CLONE_FIXED,
                                        MUT_CLONE_FIXED,
                                        MUT_CLONE_FIXED,
                                        MUT_CLONE_FIXED,
                                        MUT_CLONE_FIXED,
                                        MUT_CLONE_FIXED,
                                        MUT_CLONE_FIXED,
                                        MUT_OVERWRITE_COPY,
                                        MUT_OVERWRITE_COPY,
                                        MUT_OVERWRITE_COPY,
                                        MUT_OVERWRITE_COPY,
                                        MUT_OVERWRITE_COPY,
                                        MUT_OVERWRITE_COPY,
                                        MUT_OVERWRITE_COPY,
                                        MUT_OVERWRITE_COPY,
                                        MUT_OVERWRITE_COPY,
                                        MUT_OVERWRITE_COPY,
                                        MUT_OVERWRITE_FIXED,
                                        MUT_OVERWRITE_FIXED,
                                        MUT_OVERWRITE_FIXED,
                                        MUT_OVERWRITE_FIXED,
                                        MUT_OVERWRITE_FIXED,
                                        MUT_BYTEADD,
                                        MUT_BYTEADD,
                                        MUT_BYTEADD,
                                        MUT_BYTEADD,
                                        MUT_BYTEADD,
                                        MUT_BYTEADD,
                                        MUT_BYTESUB,
                                        MUT_BYTESUB,
                                        MUT_BYTESUB,
                                        MUT_BYTESUB,
                                        MUT_BYTESUB,
                                        MUT_BYTESUB,
                                        MUT_FLIP8,
                                        MUT_FLIP8,
                                        MUT_FLIP8,
                                        MUT_FLIP8,
                                        MUT_SWITCH,
                                        MUT_SWITCH,
                                        MUT_SWITCH,
                                        MUT_SWITCH,
                                        MUT_SWITCH,
                                        MUT_SWITCH,
                                        MUT_DEL,
                                        MUT_DEL,
                                        MUT_DEL,
                                        MUT_DEL,
                                        MUT_DEL,
                                        MUT_DEL,
                                        MUT_DEL,
                                        MUT_DEL,
                                        MUT_DEL,
                                        MUT_EXTRA_OVERWRITE,
                                        MUT_EXTRA_OVERWRITE,
                                        MUT_EXTRA_OVERWRITE,
                                        MUT_EXTRA_OVERWRITE,
                                        MUT_EXTRA_OVERWRITE,
                                        MUT_EXTRA_OVERWRITE,
                                        MUT_EXTRA_OVERWRITE,
                                        MUT_EXTRA_OVERWRITE,
                                        MUT_EXTRA_OVERWRITE,
                                        MUT_EXTRA_OVERWRITE,
                                        MUT_EXTRA_INSERT,
                                        MUT_EXTRA_INSERT,
                                        MUT_EXTRA_INSERT,
                                        MUT_EXTRA_INSERT,
                                        MUT_EXTRA_INSERT,
                                        MUT_EXTRA_INSERT,
                                        MUT_EXTRA_INSERT,
                                        MUT_EXTRA_INSERT,
                                        MUT_EXTRA_INSERT,
                                        MUT_EXTRA_INSERT,
                                        MUT_EXTRA_INSERT,
                                        MUT_EXTRA_INSERT,
                                        MUT_AUTO_EXTRA_OVERWRITE,
                                        MUT_AUTO_EXTRA_OVERWRITE,
                                        MUT_AUTO_EXTRA_OVERWRITE,
                                        MUT_AUTO_EXTRA_OVERWRITE,
                                        MUT_AUTO_EXTRA_OVERWRITE,
                                        MUT_AUTO_EXTRA_OVERWRITE,
                                        MUT_AUTO_EXTRA_OVERWRITE,
                                        MUT_AUTO_EXTRA_OVERWRITE,
                                        MUT_AUTO_EXTRA_OVERWRITE,
                                        MUT_AUTO_EXTRA_INSERT,
                                        MUT_AUTO_EXTRA_INSERT,
                                        MUT_AUTO_EXTRA_INSERT,
                                        MUT_AUTO_EXTRA_INSERT,
                                        MUT_AUTO_EXTRA_INSERT,
                                        MUT_AUTO_EXTRA_INSERT,
                                        MUT_AUTO_EXTRA_INSERT,
                                        MUT_AUTO_EXTRA_INSERT,
                                        MUT_AUTO_EXTRA_INSERT,
                                        MUT_AUTO_EXTRA_INSERT,
                                        MUT_AUTO_EXTRA_INSERT,
                                        MUT_SPLICE_OVERWRITE,
                                        MUT_SPLICE_OVERWRITE,
                                        MUT_SPLICE_OVERWRITE,
                                        MUT_SPLICE_OVERWRITE,
                                        MUT_SPLICE_OVERWRITE,
                                        MUT_SPLICE_OVERWRITE,
                                        MUT_SPLICE_OVERWRITE,
                                        MUT_SPLICE_OVERWRITE,
                                        MUT_SPLICE_OVERWRITE,
                                        MUT_SPLICE_OVERWRITE,
                                        MUT_SPLICE_OVERWRITE,
                                        MUT_SPLICE_OVERWRITE,
                                        MUT_SPLICE_OVERWRITE,
                                        MUT_SPLICE_INSERT,
                                        MUT_SPLICE_INSERT,
                                        MUT_SPLICE_INSERT,
                                        MUT_SPLICE_INSERT,
                                        MUT_SPLICE_INSERT,
                                        MUT_SPLICE_INSERT,
                                        MUT_SPLICE_INSERT,
                                        MUT_SPLICE_INSERT,
                                        MUT_SPLICE_INSERT,
                                        MUT_SPLICE_INSERT,
                                        MUT_SPLICE_INSERT,
                                        MUT_SPLICE_INSERT,
                                        MUT_SPLICE_INSERT,
                                        MUT_SPLICE_INSERT};

// Choices helper
void deep_copy_array(u8 **src, u8 ***dest) {
    size_t num_strings = 0;
    u8 **temp_dest = NULL;

    // Count the number of strings in the source array
    while (src[num_strings] != NULL) {
        num_strings++;
    }

    // Allocate memory for the destination array
    temp_dest = (u8 **)malloc((num_strings + 1) * sizeof(u8 *));
    if (temp_dest == NULL) {
        // Handle memory allocation failure
        return;
    }

    // Copy each string from the source array to the destination array
    for (size_t i = 0; i < num_strings; i++) {
        size_t len = strlen((char *)src[i]);
        temp_dest[i] = (u8 *)malloc((len + 1) * sizeof(u8));
        if (temp_dest[i] == NULL) {
            // Handle memory allocation failure
            for (size_t j = 0; j < i; j++) {
                free(temp_dest[j]);
            }
            free(temp_dest);
            return;
        }
        strcpy((char *)temp_dest[i], (char *)src[i]);
    }

    // Terminate the destination array with a NULL pointer
    temp_dest[num_strings] = NULL;

    // Assign the destination array pointer to the caller's variable
    *dest = temp_dest;
}

// Utilities
// Adds the path of config.seed to afl state
void set_temp_config_file_path(afl_state_t *afl) {
  char *target_path = strcpy(ck_alloc(strlen(afl->fsrv.target_path) + 1), afl->fsrv.target_path);
  char *target_dir = dirname((char *)target_path);
  char *temp_config_file_path = ck_alloc(strlen(target_dir) + 13);
  strcpy(temp_config_file_path, target_path);
  strcat(temp_config_file_path, "/config.seed");

  // create the file if it doesn't exist
  if (access(temp_config_file_path, F_OK) == -1) {
    FILE *f = fopen(temp_config_file_path, "w");
    if (f == NULL) {
      PFATAL("Unable to create config.seed file");
    }

    fprintf(f, " \n");

    fclose(f);
  }

  afl->temp_config_file_path = ck_alloc(strlen(temp_config_file_path) + 1);
  strcpy(afl->temp_config_file_path, temp_config_file_path);
  ck_free(target_path);
  ck_free(temp_config_file_path);
}


void copy_option_entry(struct option_entry *dest, struct option_entry *src) {
  dest->opt = strdup(src->opt);
  dest->type = strdup(src->type);
  dest->id = src->id;
  // dest->choices = src->choices; // MTA: Need to copy each string for choices
  if(src->isChoice){
    deep_copy_array(src->choices, &dest->choices);
  }
  dest->intRangeMax = src->intRangeMax;
  dest->intRangeMin = src->intRangeMin;
  dest->realRangeMax = src->realRangeMax;
  dest->realRangeMin = src->realRangeMin;
  dest->strSize = src->strSize;
}


void copy_option_setting(struct option_setting *dest, struct option_setting *src) {
  dest->opt = strdup(src->opt);
  dest->bool_val = src->bool_val;
  dest->int_val = src->int_val;
  dest->real_val = src->real_val;
  dest->type = strdup(src->type);
  if (src->str_val != NULL) {
    dest->str_val = strdup(src->str_val);
  }
  dest->is_static = src->is_static;
  dest->is_negated = src->is_negated;
}

u8 compare_option_setting(struct option_setting *opt_set1, struct option_setting *opt_set2) {
  if (strcmp(opt_set1->opt, opt_set2->opt) != 0) {
    return 0;
  }

  if (strcmp(opt_set1->type, opt_set2->type) != 0) {
    return 0;
  }

  if (strcmp(opt_set1->type, "bool") == 0) {
    if (opt_set1->bool_val != opt_set2->bool_val) {
      return 0;
    }
  } else if (strcmp(opt_set1->type, "intnum") == 0) {
    if (opt_set1->int_val != opt_set2->int_val) {
      return 0;
    }
  } else if (strcmp(opt_set1->type, "realnum") == 0) {
    if (opt_set1->real_val != opt_set2->real_val) {
      return 0;
    }
  } else {
    if (strcmp(opt_set1->str_val, opt_set2->str_val) != 0) {
      return 0;
    }
  }

  if (opt_set1->is_negated != opt_set2->is_negated) {
    return 0;
  }

  return 1;
}


char* randomString(int length, u128 seed) {
    char* str = (char*)malloc((length + 1) * sizeof(char)); // Allocate memory for the string (+1 for null terminator)
    if (str == NULL) {
        printf("Memory allocation failed.\n");
        exit(1);
    }

    const char charset[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"; // Characters to choose from
    int charset_size = sizeof(charset) - 1; // Size of the character set

    srand(time(NULL) * seed); // Seed the random number generator

    // Generate random characters and fill the string
    for (int i = 0; i < length; ++i) {
        int index = rand() % charset_size; // Generate a random index within the character set
        str[i] = charset[index]; // Assign a random character from the character set to the string
    }

    str[length] = '\0'; // Null-terminate the string
    return str;
}


u32 count_lines_in_file(u8 *file_name) {
  char c;
  u32 counter = 0;


  ACTF("Counting lines in file: %s", file_name);
  FILE *file = fopen(file_name, "r");
  if (file == NULL) {
    PFATAL("Unable to open file: %s", file_name);
  }
  for (c = getc(file); c != EOF; c = getc(file)) {
    if (c == '\n')
    counter += 1;
  }

  return counter;
}





/* Read grammar file */
void read_grammar_file(afl_state_t *afl) {
    ACTF("Reading grammar file...");
    if (!afl->grammar_file) {
        fprintf(stderr, "Error: Grammar file not provided.\n");
        return;
    }

    // Open the grammar file
    FILE *fp = fopen(afl->grammar_file, "r");
    if (!fp) {
        fprintf(stderr, "Error: Unable to open grammar file.\n");
        return;
    }

    char buffer[30000];
    size_t len = fread(buffer, 1, sizeof(buffer), fp);
    fclose(fp);

    if (len <= 0) {
        fprintf(stderr, "Error: Unable to read from file.\n");
        return;
    }

    // Parse the JSON string
    struct json_tokener *tok = json_tokener_new();
    struct json_object *json_obj = json_tokener_parse_ex(tok, buffer, len);
    if (!json_obj) {
        fprintf(stderr, "Error: Unable to parse JSON.\n");
        json_tokener_free(tok);
        return;
    }
    json_tokener_free(tok);

    // Get the "options" array
    struct json_object *options_arr = json_object_object_get(json_obj, "options");
    if (!options_arr || !json_object_is_type(options_arr, json_type_array)) {
        fprintf(stderr, "Error: Missing or invalid 'options' array.\n");
        json_object_put(json_obj);
        return;
    }

    // Loop through each option object and parse it
    int i;
    struct json_object *option;
    struct json_object *opt_obj;
    struct json_object *type_obj;
    struct json_object *range_obj;
    struct json_object *connector_obj;

    u32 tot_options = json_object_array_length(options_arr);
    afl->options_count = tot_options;
    afl->options_holder = ck_alloc(sizeof(u8*) * tot_options);

    if (afl->options_holder == NULL) {
      PFATAL("Unable to allocate memory for options holder");
    }

    afl->options_type = ck_alloc(sizeof(u8*) * tot_options);
    if (afl->options_type == NULL) {
      PFATAL("Unable to allocate memory for options types");
    }

    afl->options_ranges = ck_alloc(sizeof(int*) * tot_options);
    for (int i = 0; i < tot_options; i++) {
      afl->options_ranges[i] = ck_alloc(sizeof(int) * 2);    
      if (afl->options_ranges[i] == NULL) {
        PFATAL("Unable to allocate memory for options ranges");
      }
    }

    if (afl->options_ranges == NULL) {
      PFATAL("Unable to allocate memory for options ranges");
    }

    afl->options_choices = ck_alloc(sizeof(u8**) * tot_options);
    if (afl->options_choices == NULL) {
      PFATAL("Unable to allocate memory for options choices");
    }

    afl->options_connectors = ck_alloc(sizeof(u8*) * tot_options);
    if (afl->options_connectors == NULL) {
      PFATAL("Unable to allocate memory for options connectors");
    }

    afl->options_choices_count = ck_alloc(sizeof(int) * tot_options);
    if (afl->options_choices_count == NULL) {
      PFATAL("Unable to allocate memory for options choices count");
    }

    for (i = 0; i < tot_options; i++) {
      option = json_object_array_get_idx(options_arr, i);
      opt_obj = json_object_object_get(option, "opt");
      type_obj = json_object_object_get(option, "type");
      connector_obj = json_object_object_get(option, "connector");

      if (!connector_obj) {
        connector_obj = json_object_new_string("=");
      }

      if (opt_obj && type_obj && connector_obj) {
        const u8 *opt_str = json_object_get_string(opt_obj);
        const u8 *type_str = json_object_get_string(type_obj);
        const u8 *connector_str = json_object_get_string(connector_obj);

        // todo: Add to option hashmap
        afl->options_holder[i] = ck_alloc(strlen(opt_str) + 1);
        afl->options_type[i] = ck_alloc(strlen(type_str) + 1);
        afl->options_connectors[i] = ck_alloc(strlen(connector_str) + 1);

        strcpy(afl->options_holder[i], opt_str);
        strcpy(afl->options_type[i], type_str);
        strcpy(afl->options_connectors[i], connector_str);

        // if realnum or intnum, get the range
        if (strcmp(type_str, "realnum") == 0 || strcmp(type_str, "intnum") == 0) {
          range_obj = json_object_object_get(option, "range");
          
          if (!range_obj) {
            fprintf(stderr, "Error: Missing range for numeric type option %s\n", opt_str);
            continue;
          }

          // Get the array elements
          struct json_object *range_start = json_object_array_get_idx(range_obj, 0);
          struct json_object *range_end = json_object_array_get_idx(range_obj, 1);
          
          if (!range_start || !range_end) {
            fprintf(stderr, "Error: Invalid range format for option %s\n", opt_str);
            continue;
          }

          // Handle both integer and real number types
          afl->options_ranges[i][0] = json_object_get_int(range_start);
          afl->options_ranges[i][1] = json_object_get_int(range_end);

          printf("Range for %s: %d to %d\n", 
                opt_str,
                afl->options_ranges[i][0], 
                afl->options_ranges[i][1]);
        } else if (strcmp(type_str, "choice") == 0) {
          struct json_object *choices_obj = json_object_object_get(option, "choices");
          if (!choices_obj) {
            PFATAL("Missing choices for choice type option");
            continue;
          }

          u32 num_choices = json_object_array_length(choices_obj);
          afl->options_choices_count[i] = num_choices;

          afl->options_choices[i] = ck_alloc(sizeof(u8*) * num_choices);
          if (afl->options_choices[i] == NULL) {
            PFATAL("Unable to allocate memory for options choices");
          }

          for (int j = 0; j < num_choices; j++) {
            struct json_object *choice = json_object_array_get_idx(choices_obj, j);
            const u8 *choice_str = json_object_get_string(choice);
            afl->options_choices[i][j] = ck_alloc(strlen(choice_str) + 1);
            strcpy(afl->options_choices[i][j], choice_str);

            // print the choices
            printf("Choice %d: %s\n", j, afl->options_choices[i][j]);
          }


        }
      } else {
        fprintf(stderr, "Error: Missing required fields in option object.\n");
      }

      // print connector
      printf("Connector: %s\n", afl->options_connectors[i]);
    } // end of for loop


    json_object_put(json_obj);
    OKF("Grammar file read successfully");

    for (int i = 0; i < afl->options_count; i++) {
      printf("Option %d: %s ", i, afl->options_holder[i]);
      printf("Type: %s\n", afl->options_type[i]);
    }
}


// bitmap looks like 010110101 where each index corresponds to an option
u8* bitmap_to_config(afl_state_t *afl, u8* bitmap) {
  srand(time(NULL));
  u8 *config = ck_alloc(sizeof(u8) * 5000);
  if (config == NULL) {
    PFATAL("Unable to allocate memory for config");
  }
  strcpy(config, "");

  double iters_raw = (double)afl->options_count / 8.0;
  u128 iters = ceil(iters_raw);
  
  for (u128 idx = 0; idx < iters_raw; idx++) {
    for (int i = 0; i < 8; i++) {
      u8 bin_val =  (bitmap[idx] >> i) & 1;

      if (i + (idx * 8) >= afl->options_count) {
        break;
      }
      if (bin_val != 0) {
        if (strcmp(afl->options_type[i + (idx * 8)], "bool") == 0) {
          strcat(config, afl->options_holder[i + (idx * 8)]);
          strcat(config, " ");
        } else if (strcmp(afl->options_type[i + (idx * 8)], "choice") == 0) {
          strcat(config, afl->options_holder[i + (idx * 8)]);
          strcat(config, afl->options_connectors[i + (idx * 8)]);
          int choice_idx = random_int(0, afl->options_choices_count[i + (idx * 8)] - 1);
          strcat(config, afl->options_choices[i + (idx * 8)][choice_idx]);
          strcat(config, " ");
        } else if (strcmp(afl->options_type[i + (idx * 8)], "realnum") == 0) {
          strcat(config, afl->options_holder[i + (idx * 8)]);
          strcat(config, afl->options_connectors[i + (idx * 8)]);
          
          int range_min = afl->options_ranges[i + (idx * 8)][0];
          int range_max = afl->options_ranges[i + (idx * 8)][1];
          int random_val = random_int(range_min, range_max);

          char buffer[20];  // Enough space for an integer
          sprintf(buffer, "%d", random_val);
          strcat(config, buffer);
          strcat(config, " ");
          
        } else if (strcmp(afl->options_type[i + (idx * 8)], "intnum") == 0) {
          strcat(config, afl->options_holder[i + (idx * 8)]);
          strcat(config, afl->options_connectors[i + (idx * 8)]);

          int range_min = afl->options_ranges[i + (idx * 8)][0];
          int range_max = afl->options_ranges[i + (idx * 8)][1];
          double random_val = random_double(range_min, range_max);

          char buffer[32];  // Larger buffer for floating-point numbers
          sprintf(buffer, "%f", random_val);
          strcat(config, buffer);
          strcat(config, " ");
        }
      }
    }
  }

  return config;
}


// NEEDS TO GET ON BOARD WITH THE NEW HAVOC STUFF
u8* config_to_bitmap(afl_state_t *afl, u8* config) {
  double iters_raw = (double)afl->options_count / 8.0;
  u128 iters = ceil(iters_raw);
  u8 *bitmap = ck_alloc(sizeof(u8) * iters);

  if (bitmap == NULL) {
    PFATAL("Unable to allocate memory for bitmap");
  }

  memset(bitmap, 0, iters);


  for (u32 opt_idx = 0; opt_idx < afl->options_count; opt_idx++) {
    u128 byte_idx = opt_idx / 8;
    u8 bit_position = opt_idx % 8;
    
    if (strstr(config, afl->options_holder[opt_idx]) != NULL) {
      bitmap[byte_idx] |= (1 << bit_position);
    }
  }

  return bitmap;
}


void argv_havoc(afl_state_t *afl, u8* cur_bitmap) {
  u32 len = ceil((double)afl->options_count/8), temp_len;
  u8 *out_buf = ck_alloc(sizeof(u8) * len);

  temp_len = len;

  // print current bitmap
  for (int i = 0; i < len; i++) {
    printf("0x%02x ", cur_bitmap[i]);
  }

  if (!cur_bitmap || !afl->options_holder) {
    if (!afl->options_holder) {
      PFATAL("Option holder is NULL");
    } else {
      PFATAL("Curbitmap is NULL");
    }

    PFATAL("Invalid input to argv_havoc");
    return;
  }

  u8 *temp_buf = ck_alloc(sizeof(u8) * afl->options_count);
  if (temp_buf == NULL) {
    PFATAL("Unable to allocate memory for temp_buf");
  }

  if (afl->stage_max < HAVOC_MIN) { 
    afl->stage_max = HAVOC_MIN; 
  }

  u32 stack_max = 1 << (1 + rand_below(afl, afl->havoc_stack_pow2)), rand_max;
  u32 *mutation_array = (unsigned int *)&binary_array_argv;

  // afl->configs_to_inject_str = ck_alloc(sizeof(u8 *) * afl->stage_max);
  u8 **config_holder = ck_alloc(sizeof(u8 *) * afl->stage_max);
  afl->configs_to_inject_local_bitmap = ck_alloc(sizeof(u8 *) * afl->stage_max);
  int size_of_config_holder = afl->stage_max;


  for (afl->stage_cur = 0; afl->stage_cur < afl->stage_max; ++afl->stage_cur) {
    u32 use_stacking = 1 + rand_below(afl, stack_max);
    afl->stage_cur_val = use_stacking;

    for (u128 i = 0; i < use_stacking; ++i) {


retry_havoc_step: {
      // u32 r = rand_below(afl, rand_max), item;
      u32 r = rand_below(afl, MUT_BIN_ARRAY_SIZE), item;


      switch (mutation_array[r]) {

        case MUT_FLIPBIT: {

          /* Flip a single bit somewhere. Spooky! */
          u8  bit = rand_below(afl, 8);
          u32 off = rand_below(afl, temp_len);
          out_buf[off] ^= 1 << bit;
          break;

        }

        case MUT_INTERESTING8: {

          /* Set byte to interesting value. */

          item = rand_below(afl, sizeof(interesting_8));
          out_buf[rand_below(afl, temp_len)] = interesting_8[item];
          break;

        }

        case MUT_INTERESTING16: {

          /* Set word to interesting value, little endian. */

          if (unlikely(temp_len < 2)) { break; }  // no retry

          item = rand_below(afl, sizeof(interesting_16) >> 1);
          *(u16 *)(out_buf + rand_below(afl, temp_len - 1)) =
              interesting_16[item];

          break;

        }

        case MUT_INTERESTING16BE: {

          /* Set word to interesting value, big endian. */

          if (unlikely(temp_len < 2)) { break; }  // no retry

          item = rand_below(afl, sizeof(interesting_16) >> 1);
          *(u16 *)(out_buf + rand_below(afl, temp_len - 1)) =
              SWAP16(interesting_16[item]);

          break;

        }

        case MUT_INTERESTING32: {

          /* Set dword to interesting value, little endian. */

          if (unlikely(temp_len < 4)) { break; }  // no retry

          item = rand_below(afl, sizeof(interesting_32) >> 2);
          *(u32 *)(out_buf + rand_below(afl, temp_len - 3)) =
              interesting_32[item];

          break;

        }

        case MUT_INTERESTING32BE: {

          /* Set dword to interesting value, big endian. */

          if (unlikely(temp_len < 4)) { break; }  // no retry

          item = rand_below(afl, sizeof(interesting_32) >> 2);
          *(u32 *)(out_buf + rand_below(afl, temp_len - 3)) =
              SWAP32(interesting_32[item]);

          break;

        }

        case MUT_ARITH8_: {

          /* Randomly subtract from byte. */

          item = 1 + rand_below(afl, ARITH_MAX);
          out_buf[rand_below(afl, temp_len)] -= item;
          break;

        }

        case MUT_ARITH8: {

          /* Randomly add to byte. */

          item = 1 + rand_below(afl, ARITH_MAX);
          out_buf[rand_below(afl, temp_len)] += item;
          break;

        }

        case MUT_ARITH16_: {

          /* Randomly subtract from word, little endian. */

          if (unlikely(temp_len < 2)) { break; }  // no retry

          u32 pos = rand_below(afl, temp_len - 1);
          item = 1 + rand_below(afl, ARITH_MAX);


          *(u16 *)(out_buf + pos) -= item;

          break;

        }

        case MUT_ARITH16BE_: {

          /* Randomly subtract from word, big endian. */

          if (unlikely(temp_len < 2)) { break; }  // no retry

          u32 pos = rand_below(afl, temp_len - 1);
          u16 num = 1 + rand_below(afl, ARITH_MAX);

          *(u16 *)(out_buf + pos) =
              SWAP16(SWAP16(*(u16 *)(out_buf + pos)) - num);

          break;

        }

        case MUT_ARITH16: {

          /* Randomly add to word, little endian. */

          if (unlikely(temp_len < 2)) { break; }  // no retry

          u32 pos = rand_below(afl, temp_len - 1);
          item = 1 + rand_below(afl, ARITH_MAX);

          *(u16 *)(out_buf + pos) += item;

          break;

        }

        case MUT_ARITH16BE: {

          /* Randomly add to word, big endian. */

          if (unlikely(temp_len < 2)) { break; }  // no retry

          u32 pos = rand_below(afl, temp_len - 1);
          u16 num = 1 + rand_below(afl, ARITH_MAX);

          *(u16 *)(out_buf + pos) =
              SWAP16(SWAP16(*(u16 *)(out_buf + pos)) + num);

          break;

        }

        case MUT_ARITH32_: {

          /* Randomly subtract from dword, little endian. */

          if (unlikely(temp_len < 4)) { break; }  // no retry

          u32 pos = rand_below(afl, temp_len - 3);
          item = 1 + rand_below(afl, ARITH_MAX);

          *(u32 *)(out_buf + pos) -= item;

          break;

        }

        case MUT_ARITH32BE_: {

          /* Randomly subtract from dword, big endian. */

          if (unlikely(temp_len < 4)) { break; }  // no retry

          u32 pos = rand_below(afl, temp_len - 3);
          u32 num = 1 + rand_below(afl, ARITH_MAX);

          *(u32 *)(out_buf + pos) =
              SWAP32(SWAP32(*(u32 *)(out_buf + pos)) - num);

          break;

        }

        case MUT_ARITH32: {

          /* Randomly add to dword, little endian. */

          if (unlikely(temp_len < 4)) { break; }  // no retry

          u32 pos = rand_below(afl, temp_len - 3);
          item = 1 + rand_below(afl, ARITH_MAX);

          *(u32 *)(out_buf + pos) += item;

          break;

        }

        case MUT_ARITH32BE: {

          /* Randomly add to dword, big endian. */

          if (unlikely(temp_len < 4)) { break; }  // no retry

          u32 pos = rand_below(afl, temp_len - 3);
          u32 num = 1 + rand_below(afl, ARITH_MAX);

          *(u32 *)(out_buf + pos) =
              SWAP32(SWAP32(*(u32 *)(out_buf + pos)) + num);

          break;

        }

        case MUT_RAND8: {

          /* Just set a random byte to a random value. Because,
             why not. We use XOR with 1-255 to eliminate the
             possibility of a no-op. */

          u32 pos = rand_below(afl, temp_len);
          item = 1 + rand_below(afl, 255);
          out_buf[pos] ^= item;
          break;

        }

        case MUT_CLONE_COPY: {

          if (likely(temp_len + HAVOC_BLK_XL < MAX_FILE)) {

            /* Clone bytes. */

            u32 clone_len = choose_block_len(afl, temp_len);
            u32 clone_from = rand_below(afl, temp_len - clone_len + 1);
            u32 clone_to = rand_below(afl, temp_len);

            u8 *new_buf =
                afl_realloc(AFL_BUF_PARAM(out_scratch), temp_len + clone_len);
            if (unlikely(!new_buf)) { PFATAL("alloc"); }

            /* Head */

            memcpy(new_buf, out_buf, clone_to);

            /* Inserted part */

            memcpy(new_buf + clone_to, out_buf + clone_from, clone_len);

            /* Tail */
            memcpy(new_buf + clone_to + clone_len, out_buf + clone_to,
                   temp_len - clone_to);

            out_buf = new_buf;
            afl_swap_bufs(AFL_BUF_PARAM(out), AFL_BUF_PARAM(out_scratch));
            temp_len += clone_len;

          } else if (unlikely(temp_len < 8)) {

            break;

          } else {

            goto retry_havoc_step;

          }

          break;

        }

        case MUT_CLONE_FIXED: {

          if (likely(temp_len + HAVOC_BLK_XL < MAX_FILE)) {

            /* Insert a block of constant bytes (25%). */

            u32 clone_len = choose_block_len(afl, HAVOC_BLK_XL);
            u32 clone_to = rand_below(afl, temp_len);
            u32 strat = rand_below(afl, 2);
            u32 clone_from = clone_to ? clone_to - 1 : 0;
            item = strat ? rand_below(afl, 256) : out_buf[clone_from];

            u8 *new_buf =
                afl_realloc(AFL_BUF_PARAM(out_scratch), temp_len + clone_len);
            if (unlikely(!new_buf)) { PFATAL("alloc"); }

            /* Head */

            memcpy(new_buf, out_buf, clone_to);

            /* Inserted part */

            memset(new_buf + clone_to, item, clone_len);

            /* Tail */
            memcpy(new_buf + clone_to + clone_len, out_buf + clone_to,
                   temp_len - clone_to);

            out_buf = new_buf;
            afl_swap_bufs(AFL_BUF_PARAM(out), AFL_BUF_PARAM(out_scratch));
            temp_len += clone_len;

          } else if (unlikely(temp_len < 8)) {

            break;

          } else {

            goto retry_havoc_step;

          }

          break;

        }

        case MUT_OVERWRITE_COPY: {

          /* Overwrite bytes with a randomly selected chunk bytes. */

          if (unlikely(temp_len < 2)) { break; }  // no retry

          u32 copy_from, copy_to,
              copy_len = choose_block_len(afl, temp_len - 1);

          do {

            copy_from = rand_below(afl, temp_len - copy_len + 1);
            copy_to = rand_below(afl, temp_len - copy_len + 1);

          } while (unlikely(copy_from == copy_to));

          memmove(out_buf + copy_to, out_buf + copy_from, copy_len);

          break;

        }

        case MUT_OVERWRITE_FIXED: {

          /* Overwrite bytes with fixed bytes. */

          if (unlikely(temp_len < 2)) { break; }  // no retry

          u32 copy_len = choose_block_len(afl, temp_len - 1);
          u32 copy_to = rand_below(afl, temp_len - copy_len + 1);
          u32 strat = rand_below(afl, 2);
          u32 copy_from = copy_to ? copy_to - 1 : 0;
          item = strat ? rand_below(afl, 256) : out_buf[copy_from];


          memset(out_buf + copy_to, item, copy_len);

          break;

        }

        case MUT_BYTEADD: {

          /* Increase byte by 1. */

          out_buf[rand_below(afl, temp_len)]++;
          break;

        }

        case MUT_BYTESUB: {

          /* Decrease byte by 1. */

          out_buf[rand_below(afl, temp_len)]--;
          break;

        }

        case MUT_FLIP8: {

          /* Flip byte with a XOR 0xff. This is the same as NEG. */
          out_buf[rand_below(afl, temp_len)] ^= 0xff;
          break;

        }

        case MUT_SWITCH: {

          if (unlikely(temp_len < 4)) { break; }  // no retry

          /* Switch bytes. */

          u32 to_end, switch_to, switch_len, switch_from;
          switch_from = rand_below(afl, temp_len);
          do {

            switch_to = rand_below(afl, temp_len);

          } while (unlikely(switch_from == switch_to));

          if (switch_from < switch_to) {

            switch_len = switch_to - switch_from;
            to_end = temp_len - switch_to;

          } else {

            switch_len = switch_from - switch_to;
            to_end = temp_len - switch_from;

          }

          switch_len = choose_block_len(afl, MIN(switch_len, to_end));


          u8 *new_buf = afl_realloc(AFL_BUF_PARAM(out_scratch), switch_len);
          if (unlikely(!new_buf)) { PFATAL("alloc"); }

          /* Backup */

          memcpy(new_buf, out_buf + switch_from, switch_len);

          /* Switch 1 */

          memcpy(out_buf + switch_from, out_buf + switch_to, switch_len);

          /* Switch 2 */

          memcpy(out_buf + switch_to, new_buf, switch_len);

          break;

        }

        case MUT_DEL: {

          /* Delete bytes. */

          if (unlikely(temp_len < 2)) { break; }  // no retry

          /* Don't delete too much. */

          u32 del_len = choose_block_len(afl, temp_len - 1);
          u32 del_from = rand_below(afl, temp_len - del_len + 1);

          memmove(out_buf + del_from, out_buf + del_from + del_len,
                  temp_len - del_from - del_len);

          temp_len -= del_len;

          break;

        }

        case MUT_SHUFFLE: {

          /* Shuffle bytes. */

          if (unlikely(temp_len < 4)) { break; }  // no retry

          u32 len = choose_block_len(afl, temp_len - 1);
          u32 off = rand_below(afl, temp_len - len + 1);


          for (u32 i = len - 1; i > 0; i--) {

            u32 j;
            do {

              j = rand_below(afl, i + 1);

            } while (unlikely(i == j));

            unsigned char temp = out_buf[off + i];
            out_buf[off + i] = out_buf[off + j];
            out_buf[off + j] = temp;

          }

          break;

        }

        case MUT_DELONE: {

          /* Delete bytes. */

          if (unlikely(temp_len < 2)) { break; }  // no retry

          /* Don't delete too much. */

          u32 del_len = 1;
          u32 del_from = rand_below(afl, temp_len - del_len + 1);


          memmove(out_buf + del_from, out_buf + del_from + del_len,
                  temp_len - del_from - del_len);

          temp_len -= del_len;

          break;

        }

        case MUT_INSERTONE: {

          if (unlikely(temp_len < 2)) { break; }  // no retry

          u32 clone_len = 1;
          u32 clone_to = rand_below(afl, temp_len);
          u32 strat = rand_below(afl, 2);
          u32 clone_from = clone_to ? clone_to - 1 : 0;
          item = strat ? rand_below(afl, 256) : out_buf[clone_from];

          u8 *new_buf =
              afl_realloc(AFL_BUF_PARAM(out_scratch), temp_len + clone_len);
          if (unlikely(!new_buf)) { PFATAL("alloc"); }

          /* Head */

          memcpy(new_buf, out_buf, clone_to);

          /* Inserted part */

          memset(new_buf + clone_to, item, clone_len);

          /* Tail */
          memcpy(new_buf + clone_to + clone_len, out_buf + clone_to,
                 temp_len - clone_to);

          out_buf = new_buf;
          afl_swap_bufs(AFL_BUF_PARAM(out), AFL_BUF_PARAM(out_scratch));
          temp_len += clone_len;

          break;

        }

        case MUT_ASCIINUM: {

          if (unlikely(temp_len < 4)) { break; }  // no retry

          u32 off = rand_below(afl, temp_len), off2 = off, cnt = 0;

          while (off2 + cnt < temp_len && !isdigit(out_buf[off2 + cnt])) {

            ++cnt;

          }

          // none found, wrap
          if (off2 + cnt == temp_len) {

            off2 = 0;
            cnt = 0;

            while (cnt < off && !isdigit(out_buf[off2 + cnt])) {

              ++cnt;

            }

            if (cnt == off) {

              if (temp_len < 8) {

                break;

              } else {

                goto retry_havoc_step;

              }

            }

          }

          off = off2 + cnt;
          off2 = off + 1;

          while (off2 < temp_len && isdigit(out_buf[off2])) {

            ++off2;

          }

          s64 val = out_buf[off] - '0';
          for (u32 i = off + 1; i < off2; ++i) {

            val = (val * 10) + out_buf[i] - '0';

          }

          if (off && out_buf[off - 1] == '-') { val = -val; }

          u32 strat = rand_below(afl, 8);
          switch (strat) {

            case 0:
              val++;
              break;
            case 1:
              val--;
              break;
            case 2:
              val *= 2;
              break;
            case 3:
              val /= 2;
              break;
            case 4:
              if (likely(val && (u64)val < 0x19999999)) {

                val = (u64)rand_next(afl) % (u64)((u64)val * 10);

              } else {

                val = rand_below(afl, 256);

              }

              break;
            case 5:
              val += rand_below(afl, 256);
              break;
            case 6:
              val -= rand_below(afl, 256);
              break;
            case 7:
              val = ~(val);
              break;

          }

          // fprintf(stderr, "val: %u-%u = %ld\n", off, off2, val);

          char buf[20];
          snprintf(buf, sizeof(buf), "%" PRId64, val);

          // fprintf(stderr, "BEFORE: %s\n", out_buf);

          u32 old_len = off2 - off;
          u32 new_len = strlen(buf);

          if (old_len == new_len) {

            memcpy(out_buf + off, buf, new_len);

          } else {

            u8 *new_buf = afl_realloc(AFL_BUF_PARAM(out_scratch),
                                      temp_len + new_len - old_len);
            if (unlikely(!new_buf)) { PFATAL("alloc"); }

            /* Head */

            memcpy(new_buf, out_buf, off);

            /* Inserted part */

            memcpy(new_buf + off, buf, new_len);

            /* Tail */
            memcpy(new_buf + off + new_len, out_buf + off2, temp_len - off2);

            out_buf = new_buf;
            afl_swap_bufs(AFL_BUF_PARAM(out), AFL_BUF_PARAM(out_scratch));
            temp_len += (new_len - old_len);

          }

          // fprintf(stderr, "AFTER : %s\n", out_buf);
          break;

        }

        case MUT_INSERTASCIINUM: {

          u32 len = 1 + rand_below(afl, 8);
          u32 pos = rand_below(afl, temp_len);
          /* Insert ascii number. */
          if (unlikely(temp_len < pos + len)) {

            if (unlikely(temp_len < 8)) {

              break;

            } else {

              goto retry_havoc_step;

            }

          }


          u64  val = rand_next(afl);
          char buf[20];
          snprintf(buf, sizeof(buf), "%llu", val);
          memcpy(out_buf + pos, buf, len);

          break;

        }

        case MUT_EXTRA_OVERWRITE: {

          if (unlikely(!afl->extras_cnt)) { goto retry_havoc_step; }

          /* Use the dictionary. */

          u32 use_extra = rand_below(afl, afl->extras_cnt);
          u32 extra_len = afl->extras[use_extra].len;

          if (unlikely(extra_len > temp_len)) { goto retry_havoc_step; }

          u32 insert_at = rand_below(afl, temp_len - extra_len + 1);

          memcpy(out_buf + insert_at, afl->extras[use_extra].data, extra_len);

          break;

        }

        case MUT_EXTRA_INSERT: {

          if (unlikely(!afl->extras_cnt)) { goto retry_havoc_step; }

          u32 use_extra = rand_below(afl, afl->extras_cnt);
          u32 extra_len = afl->extras[use_extra].len;
          if (unlikely(temp_len + extra_len >= MAX_FILE)) {

            goto retry_havoc_step;

          }

          u8 *ptr = afl->extras[use_extra].data;
          u32 insert_at = rand_below(afl, temp_len + 1);


          out_buf = afl_realloc(AFL_BUF_PARAM(out), temp_len + extra_len);
          if (unlikely(!out_buf)) { PFATAL("alloc"); }

          /* Tail */
          memmove(out_buf + insert_at + extra_len, out_buf + insert_at,
                  temp_len - insert_at);

          /* Inserted part */
          memcpy(out_buf + insert_at, ptr, extra_len);
          temp_len += extra_len;

          break;

        }

        case MUT_AUTO_EXTRA_OVERWRITE: {

          if (unlikely(!afl->a_extras_cnt)) { goto retry_havoc_step; }

          /* Use the dictionary. */

          u32 use_extra = rand_below(afl, afl->a_extras_cnt);
          u32 extra_len = afl->a_extras[use_extra].len;

          if (unlikely(extra_len > temp_len)) { goto retry_havoc_step; }

          u32 insert_at = rand_below(afl, temp_len - extra_len + 1);

          memcpy(out_buf + insert_at, afl->a_extras[use_extra].data, extra_len);

          break;

        }

        case MUT_AUTO_EXTRA_INSERT: {

          if (unlikely(!afl->a_extras_cnt)) { goto retry_havoc_step; }

          u32 use_extra = rand_below(afl, afl->a_extras_cnt);
          u32 extra_len = afl->a_extras[use_extra].len;
          if (unlikely(temp_len + extra_len >= MAX_FILE)) {

            goto retry_havoc_step;

          }

          u8 *ptr = afl->a_extras[use_extra].data;
          u32 insert_at = rand_below(afl, temp_len + 1);


          out_buf = afl_realloc(AFL_BUF_PARAM(out), temp_len + extra_len);
          if (unlikely(!out_buf)) { PFATAL("alloc"); }

          /* Tail */
          memmove(out_buf + insert_at + extra_len, out_buf + insert_at,
                  temp_len - insert_at);

          /* Inserted part */
          memcpy(out_buf + insert_at, ptr, extra_len);
          temp_len += extra_len;

          break;

        }

        case MUT_SPLICE_OVERWRITE: {

          if (unlikely(afl->ready_for_splicing_count <= 1)) {

            goto retry_havoc_step;

          }

          /* Pick a random queue entry and seek to it. */

          u32 tid;
          do {

            tid = rand_below(afl, afl->queued_items);

          } while (unlikely(tid == afl->current_entry ||

                            afl->queue_buf[tid]->len < 4));

          /* Get the testcase for splicing. */
          struct queue_entry *target = afl->queue_buf[tid];
          u32                 new_len = target->len;
          u8                 *new_buf = queue_testcase_get(afl, target);

          /* overwrite mode */

          u32 copy_from, copy_to, copy_len;

          copy_len = choose_block_len(afl, new_len - 1);
          if (copy_len > temp_len) copy_len = temp_len;

          copy_from = rand_below(afl, new_len - copy_len + 1);
          copy_to = rand_below(afl, temp_len - copy_len + 1);

          memmove(out_buf + copy_to, new_buf + copy_from, copy_len);

          break;

        }

        case MUT_SPLICE_INSERT: {

          if (unlikely(afl->ready_for_splicing_count <= 1)) {

            goto retry_havoc_step;

          }

          if (unlikely(temp_len + HAVOC_BLK_XL >= MAX_FILE)) {

            goto retry_havoc_step;

          }

          /* Pick a random queue entry and seek to it. */

          u32 tid;
          do {

            tid = rand_below(afl, afl->queued_items);

          } while (unlikely(tid == afl->current_entry ||

                            afl->queue_buf[tid]->len < 4));

          /* Get the testcase for splicing. */
          struct queue_entry *target = afl->queue_buf[tid];
          u32                 new_len = target->len;
          u8                 *new_buf = queue_testcase_get(afl, target);

          /* insert mode */

          u32 clone_from, clone_to, clone_len;

          clone_len = choose_block_len(afl, new_len);
          clone_from = rand_below(afl, new_len - clone_len + 1);
          clone_to = rand_below(afl, temp_len + 1);

          u8 *temp_buf =
              afl_realloc(AFL_BUF_PARAM(out_scratch), temp_len + clone_len + 1);
          if (unlikely(!temp_buf)) { PFATAL("alloc"); }


          /* Head */

          memcpy(temp_buf, out_buf, clone_to);

          /* Inserted part */

          memcpy(temp_buf + clone_to, new_buf + clone_from, clone_len);

          /* Tail */
          memcpy(temp_buf + clone_to + clone_len, out_buf + clone_to,
                 temp_len - clone_to);

          out_buf = temp_buf;
          afl_swap_bufs(AFL_BUF_PARAM(out), AFL_BUF_PARAM(out_scratch));
          temp_len += clone_len;

          break;

        }

      }
    }

    }

    // bitmap to config
  // for (int i = 0; i < len; i++) {
  //    for (int j = 7; j >= 0; j--) {
  //      printf("%d", (out_buf[i] >> j) & 1);
  //    }
  //    printf(" ");
  //  }

  //  printf("\n");

  //   printf("Len: %d\n", len);
  //   printf("Temp Len: %d\n", temp_len);
    u8 *config = bitmap_to_config(afl, out_buf);

  //   printf("Config: %s\n", config);

  //   u8 *bitmap = config_to_bitmap(afl, config);
  //   for (int i = 0; i < len; i++) {
  //    for (int j = 7; j >= 0; j--) {
  //      printf("%d", (bitmap[i] >> j) & 1);
  //    }
  //    printf(" ");
  //  }

  //  printf("\n");
    
    // afl->configs_to_inject_str[afl->stage_cur] = strdup(config);
    config_holder[afl->stage_cur] = strdup(config);
  }


  if (size_of_config_holder > 50) {
    afl->size_of_inject_arr = 50;
    afl->configs_to_inject_str = ck_alloc(sizeof(u8 *) * afl->size_of_inject_arr);
    afl->havoc_argv_scores = ck_alloc(sizeof(u128) * afl->size_of_inject_arr);
    memset(afl->havoc_argv_scores, 0, sizeof(u128) * afl->size_of_inject_arr);

    for (u16 i = 0; i < afl->size_of_inject_arr; i++) {
      u32 rand_idx = rand_below(afl, size_of_config_holder);
      afl->configs_to_inject_str[i] = strdup(config_holder[rand_idx]);
      // printf("Config %d: %s\n", i, afl->configs_to_inject_str[i]);
    }
  } else {
    afl->size_of_inject_arr = size_of_config_holder;
    afl->configs_to_inject_str = ck_alloc(sizeof(u8 *) * size_of_config_holder);
    afl->havoc_argv_scores = ck_alloc(sizeof(u128) * afl->size_of_inject_arr);
    memset(afl->havoc_argv_scores, 0, sizeof(u128) * afl->size_of_inject_arr);


    for (u16 i = 0; i < size_of_config_holder; i++) {
      afl->configs_to_inject_str[i] = strdup(config_holder[i]);
    }
  }

  // for (u16 i = 0; i < afl->size_of_inject_arr; i++) {
  //   printf("Config %d: %s\n", i, afl->configs_to_inject_str[i]);
  // }

  // ck_free(out_buf);
  ck_free(temp_buf);
}


//  Generate a 2d matrix using provided grammar with each column being an option,
//  each row being a configuration, and each cell containing an option setting
void generate_settings_matrix(afl_state_t *afl) {
  if (afl->options_count > 0) {
    // Generate the correlation matrix
    ACTF("Generating option setting matrix...");
    afl->option_setting_matrix = ck_alloc(sizeof(struct option_setting **) * afl->config_count);
    if (afl->option_setting_matrix == NULL) {
      PFATAL("Unable to allocate memory for correlation matrix");
    }

    // printf("%d\n", afl->config_count);
    for (u16 i = 0; i < afl->config_count; i++) {
      afl->option_setting_matrix[i] = ck_alloc(sizeof(struct option_setting *) * afl->options_count);
      if (afl->option_setting_matrix[i] == NULL) {
        PFATAL("Unable to allocate memory in ROW for option setting matrix");
      }

      for (u16 j = 0; j < afl->options_count; j++) {
        afl->option_setting_matrix[i][j] = ck_alloc(sizeof(struct option_setting));
        if (afl->option_setting_matrix[i][j] == NULL) {
          PFATAL("Unable to allocate memory in COLUMN for option setting matrix");
        }
      }
    }

  } else {
      BADF("No options detected");
  }

  OKF("Correlation matrix generated successfully");
}


void generate_config_scores_matrix(afl_state_t *afl) {
  ACTF("Generating config scores matrix...");
  afl->config_scores = ck_alloc(sizeof(double *) * afl->config_count);
  if (afl->config_scores == NULL) {
    PFATAL("Unable to allocate memory for config score matrix");
  }

  for (u16 i = 0; i < afl->config_count; i++) {
    afl->config_scores[i] = ck_alloc(sizeof(double) * afl->config_score_row_size);
    if (afl->config_scores[i] == NULL) {
      PFATAL("Unable to allocate memory in ROW for config score matrix");
    }
  }

  afl->config_score_expansion_counter = 1;

  afl->config_scores_lengths = ck_alloc(sizeof(u32 *) * afl->config_count);

  for (u16 i = 0; i < afl->config_count; i++) {
    afl->config_scores_lengths[i] = 0;
  }
}

void expand_config_scores_matrix(afl_state_t *afl) {
  ACTF("Expanding config scores matrix...");
  for (u16 i = 0; i < afl->config_count; i++) {
    // afl->config_scores[i] = ck_realloc(afl->config_scores[i], sizeof(double) * 
    //                         afl->config_score_row_size * 
    //                         afl->config_score_expansion_counter);
    double *tmp = ck_realloc(afl->config_scores[i], sizeof(double) * 
                            afl->config_score_row_size * 
                            afl->config_score_expansion_counter);
    if(tmp) {
      afl->config_scores[i] = tmp;
    } else {
      PFATAL("Failed to allocate memory during config score matrix expansion");
    }


    // if (afl->config_scores[i] == NULL) {
    //   PFATAL("Failed to allocate memory during config score matrix expansion");
    // }
  }
}


void free_settings_matrix(afl_state_t *afl) {
  if (afl == NULL || afl->option_setting_matrix == NULL) {
    return;
  }

  for (u16 i = 0; i < afl->config_count; i++) {
    if (afl->option_setting_matrix[i] != NULL) {
      for (u16 j = 0; j < afl->options_count; j++) {
        if (afl->option_setting_matrix[i][j] != NULL) {
          ck_free(afl->option_setting_matrix[i][j]);
        }
      }
      ck_free(afl->option_setting_matrix[i]);
    }
  }

  ck_free(afl->option_setting_matrix);
  afl->option_setting_matrix = NULL;

  OKF("Option setting matrix freed successfully");
}


void read_config_file(afl_state_t *afl) {
    ACTF("Reading configuration file");
    if (afl->configuration_file) {
        u8 line[4096]; // Todo: Change this to a macro or make dynamic

        // Opening config file
        FILE *config_file = fopen(afl->configuration_file, "r");
        if (config_file == NULL) {
            PFATAL("Unable to open configuration file");
        }
        // Reading the file line by line
        u16 i = 0;
        while (fgets(line, sizeof(line), config_file) != NULL) {
            // ACTF("Reading line: %s", line);
            // Remove the newline character from the line
            line[strcspn(line, "\n")] = 0;
            // ACTF("Removed newlines");
            // for each line, we will break it down to tokens of options and option settings
            u8 *token = strtok(line, " ");
            ACTF("Token: %s", token);
            while (token != NULL) { // Not a single token is being read, failing at first opt_set in config file
              struct option_entry *current_option = hashOptGet(afl->options_hashmap, token);
              // ACTF("Retrieved option");
              // printf("This: %s\n", token);


              if (current_option != NULL) {
                struct option_setting *opt_set = ck_alloc(sizeof(struct option_setting));
                
                if (opt_set == NULL) {
                  PFATAL("Unable to allocate memory for option setting");
                  exit(1);
                }
                // check for what type.
                opt_set->opt = ck_alloc(strlen(current_option->opt) + 1);
                // opt_set->opt = current_option->opt; //wont work
                // printf("%d\n", sizeof(current_option->opt));
                // printf("%d\n", sizeof(opt_set->opt));
                // printf("%s\n", current_option->opt);
                memcpy(opt_set->opt, current_option->opt, strlen(current_option->opt) + 1);
                opt_set->opt[strlen(current_option->opt)] = '\0';
                // strcpy(opt_set->opt, current_option->opt);
                // int t1 = sizeof(current_option->opt);
                // opt_set->opt = ck_strdup(current_option->opt);

                u8 *type = current_option->type;
                u32 id = current_option->id;
                // ACTF("Type: %s", type);
                // ACTF("ID: %d", id);
                if (!strcmp(type, "bool")) {
                  opt_set->type = "bool";
                  opt_set->bool_val = true;
                  // printf("parsed bool\n");
                } else if (!strcmp(type, "intnum")) {
                    // printf("parsing intnum\n");
                  token = strtok(NULL, " ");
                  // ACTF("INT setting: %s", token);
                  opt_set->type = "intnum";
                  opt_set->int_val = atoi(token);
                  // ACTF("Parsed intnum: %d", opt_set->int_val);
                } else if (!strcmp(type, "realnum")) {
                  token = strtok(NULL, " ");
                  opt_set->type = "realnum";
                  opt_set->real_val = atof(token);
                } else if (!strcmp(type, "string")) {
                  token = strtok(NULL, " ");
                  opt_set->type = "string";
                  opt_set->str_val = strdup(token);
                } else if (!strcmp(type, "choice")) {
                  token = strtok(NULL, " ");
                  opt_set->type = "choice";
                  opt_set->str_val = strdup(token);
                } else {
                  printf("Invalid type for option: %s", token);
                }
                ACTF("Storing option setting in matrix");
                
                // afl->option_setting_matrix[i][id] = ck_alloc(sizeof(struct option_setting));
                copy_option_setting(afl->option_setting_matrix[i][id], opt_set);
                ACTF("Stored option setting in matrix");
                ck_free(opt_set->opt);
                ck_free(opt_set);
              } else {
                FATAL("Option: %s not found in grammar file", token);
              }
              
                token = strtok(NULL, " ");
            }

            i++;
        }

        afl->config_count = i;
        afl->initial_config_count = i;


        fclose(config_file);
        OKF("Successfully read a total of %d configurations", afl->config_count);
        OKF("Option setting matrix populated successfully");

    } else {
        BADF("Configuration file not found in current AFL++ state");
    }
}

// Just for testing
// void read_config_str_file(afl_state_t *afl) {
//   afl->size_of_inject_arr = 6;
//   FILE *config_file = fopen(afl->configuration_file, "r");
//   if (config_file == NULL) {
//     PFATAL("Unable to open configuration file");
//   }
//   u8 line[256];

//   afl->configs_to_inject = ck_alloc(sizeof(u8 *) * 6);
//   u32 counter = 0;

//   while(fgets(line, sizeof(line), config_file)) {
//     if(strcmp(line, "\n") == 0) {
//       continue;
//     }
//     afl->configs_to_inject[counter] = strdup(line);
//     counter++;
//   }
// }


/* DEBUG: print option setting matrix*/
void print_option_setting_matrix(afl_state_t *afl) {
  printHashOptMap(afl->options_hashmap);
  ACTF("Printing option setting matrix:\n");

  for (u16 i = 0; i < afl->config_count; i++) {
    printf("%d : ", i);
    for (u16 j = 0; j < afl->options_count; j++) {
      struct option_setting opt_set = *afl->option_setting_matrix[i][j];

      if (opt_set.opt == NULL) {
        printf("|      N     |", j);
      } else {
        if (opt_set.is_negated) {
          printf("!");
        }

        if (!strcmp(opt_set.type, "bool")) {
        printf("|ID: %d Set: %d|", j, afl->option_setting_matrix[i][j]->bool_val);
        } else if (!strcmp(opt_set.type, "choice")) {
          printf("|ID: %d Set: %s|", j, afl->option_setting_matrix[i][j]->str_val);
        } else if (!strcmp(opt_set.type, "intnum")) {
          printf("|ID: %d Set: %d|", j, afl->option_setting_matrix[i][j]->int_val);
        } else if (!strcmp(opt_set.type, "realnum")) {
          printf("|ID: %d Set: %f|", j, afl->option_setting_matrix[i][j]->real_val);
        } else if (!strcmp(opt_set.type, "string")) {
          printf("|ID: %d Set: %s|", j, afl->option_setting_matrix[i][j]->str_val);
        }
      }
    }
    printf("\n");
  }
  printf("\n");
}


void print_config_score(afl_state_t *afl) {
  print_config_score_lengths(afl);

  for (int i = 0; i < afl->config_count; i++) {
    for (int j = 0; j < afl->config_scores_lengths[i]; j++) {
      printf("[%d,%d]=%f ", i, j, afl->config_scores[i][j]);
    }
    printf("\n");
  }
  printf("\n");
}


void print_config_score_lengths(afl_state_t *afl) {
  ACTF("Config Score Row Lengths:");
  for (int i = 0; i < afl->config_count; i++) {
    printf("%d, ", afl->config_scores_lengths[i]);  
  }
  printf("\n");
}



void config_calibration_helper(afl_state_t *afl) {
  afl->config_scores = ck_alloc(sizeof(double) * afl->config_count * afl->queued_items);
  if (afl->config_scores == NULL) {
    PFATAL("Unable to allocate memory for config scores");
  }

  u32 config_count = afl->config_count;
  u8 injected_config_flag = 0;
  
  for (u32 i = 0; i < config_count; i++) {
    injected_config_flag = inject_config_to_fsrv(afl, afl->option_setting_matrix[i]);    

    if (injected_config_flag != 0) {
      double* perf_scores = calibrate_config_case(afl);
      afl->config_scores[i] = perf_scores; 
    } else {
      FATAL("Unable to inject configuration to fsrv");
    }
  }
}


u8 inject_config_to_fsrv(afl_state_t *afl, struct option_setting **opt_setting_row) {
  FILE *temp_config_file = fopen(afl->temp_config_file_path, "w");
  if (temp_config_file == NULL) {
    PFATAL("Unable to open temp config file");
    return 0;
  }
  // generate configuration strings
  // struct option_setting **opt_setting_row = afl->option_setting_matrix[j];

  u8 *config_string = "";
  for(u32 j = 0; j < afl->options_count; j++) {
    struct option_setting * opt_set = opt_setting_row[j];
    if (opt_set->opt == NULL) {
      continue;
    } else {
      u8 *opt = opt_set->opt;
      u8 *type = hashOptGet(afl->options_hashmap, opt)->type;

      if (opt_set->is_negated && strcmp(type, "bool")){
        continue;
      }

      if (!strcmp(type, "choice") || !strcmp(type, "string")) {
      config_string = alloc_printf("%s %s %s ", config_string, opt, opt_set->str_val);
      } else if (!strcmp(type, "intnum")) {
        config_string = alloc_printf("%s %s %d ", config_string, opt, opt_set->int_val);
      } else if (!strcmp(type, "realnum")) {
          config_string = alloc_printf("%s %s %f ", config_string, opt, opt_set->real_val);
      } else if (!strcmp(type, "bool") && opt_set->bool_val) {
          config_string = alloc_printf("%s %s ", config_string, opt);
      }
    }
    
  }
  ACTF("Config string: %s", config_string);
  fprintf(temp_config_file, "%s", config_string);
  fclose(temp_config_file);
  return 1;
}

u8 inject_config_str_to_fsrv(afl_state_t *afl, u8 *config) {
  FILE *temp_config_file = fopen(afl->temp_config_file_path, "w");
  if (temp_config_file == NULL) {
    PFATAL("Unable to open temp config file");
    return 0;
  }
  fprintf(temp_config_file,  "%s", config);
  fclose(temp_config_file);
  return 1;
}

double* calibrate_config_case(afl_state_t *afl) {
  // take a bunch of testcases from the queue
  double* perf_scores = ck_alloc(sizeof(double) * afl->queued_items);

  u32 temp = 0;

  
  for (u32 idx = 0; idx < afl->queued_items; ++idx) {
    // for each testcase
    struct queue_entry *q;
    u32 use_tmout = afl->fsrv.exec_tmout;
    u8 fault = 0;
    q = afl->queue_buf[idx];

    u8 *use_mem;

    u32 read_len = MIN(q->len, (u32)MAX_FILE);
    use_mem = afl_realloc(AFL_BUF_PARAM(in), read_len);
    // read the file and store the result in use_mem
    
  u8 res = calibrate_case(afl, q, use_mem, 1, 0);
  perf_scores[idx] = calculate_score(afl, q);
  printf("Score: %f\n", perf_scores[idx]);
  }


  return perf_scores;
}


// Steps:
// 0. (not first run) Generate configs from pres cond
// 1. Score current configuration
// 2. Generate Encoded Matrix
// 3. Run Linear Regression

struct config_queue_entry variability_driver(afl_state_t *afl, bool first_run, u32 max_iters, struct config_queue_entry selected_pres_cond) {
  if (first_run) {
    set_temp_config_file_path(afl);
    // config_calibration_helper(afl);
    // afl->encoded_opt_set_hashmap = initHashIntMap();
    // print_encoded_matrix(afl, afl->config_count);

    afl->presence_condition_queue = create_priority_queue(200); // This cannot be run frequently as the queue needs to be preserved
    
    // run_regression_analysis(afl, NULL, 2);    
    // print_priority_queue(afl->presence_condition_queue);


    // Logging
    // Clearing current cache
    char *target_path = strcpy(ck_alloc(strlen(afl->fsrv.target_path) + 1), afl->fsrv.target_path);
    char *target_dir = dirname((char *)target_path);
    char *temp_sel_and_que_path = ck_alloc(strlen(target_dir) + 24);
    char *temp_encoded_path = ck_alloc(strlen(target_dir) + 25);


    strcpy(temp_sel_and_que_path, target_path);
    strcpy(temp_encoded_path, target_path);

    strcat(temp_sel_and_que_path, "/queue_and_selected.txt");
    strcat(temp_encoded_path, "/encoded_matrix_logs.txt");

    FILE *f1 = fopen(temp_sel_and_que_path, "w");
    FILE *f2 = fopen(temp_encoded_path, "w");
    FILE *f3 = fopen("va_driver_execution_logs", "w");
    if (f1 == NULL) {
      printf("Error opening file 1!\n");
      exit(1);
    }
    if (f2 == NULL) {
      printf("Error opening file 2!\n");
      exit(1);
    }

    if (f3 == NULL) {
      printf("Error opening file 3!\n");
      exit(1);
    }

    time_t cur_time;
    time(&cur_time);
    char time_string[80];
    struct tm *time_info;
    time_info = localtime(&cur_time);
    strftime(time_string, sizeof(time_string), "%Y-%m-%d %H:%M:%S", time_info);
    fprintf(f3, "Entry time: %s (%ld) \n", time_string, (long)cur_time);

    fclose(f1);
    fclose(f2);
    fclose(f3);

    afl->second_run = true;
  } 
  
  // if (afl->current_iter <= afl->initial_config_count) {
    // Inject the configuration to the fuzzer
    // inject_config_to_fsrv(afl, afl->option_setting_matrix[afl->current_iter - 1]);
    // afl->current_iter++;
  // } else 
  
  if (afl->current_iter > afl->initial_config_count) {
    afl->current_iter = 1;
    // Logging start
    char *target_path = strcpy(ck_alloc(strlen(afl->fsrv.target_path) + 1), afl->fsrv.target_path);
    char *target_dir = dirname((char *)target_path);
    char *temp_sel_and_que_path = ck_alloc(strlen(target_dir) + 24);
    char *temp_encoded_path = ck_alloc(strlen(target_dir) + 25);


    strcpy(temp_sel_and_que_path, target_path);
    strcpy(temp_encoded_path, target_path);

    strcat(temp_sel_and_que_path, "/queue_and_selected.txt");
    strcat(temp_encoded_path, "/encoded_matrix_logs.txt");

    FILE *f1 = fopen(temp_sel_and_que_path, "a");
    FILE *f2 = fopen(temp_encoded_path, "a");

    if (f1 == NULL) {
      printf("Error opening file 1!\n");
      exit(1);
    }

    if (f2 == NULL) {
      printf("Error opening file 2!\n");
      exit(1);
    }
    printHashOptMap(afl->options_hashmap);

    // Logging end
    // free_settings_matrix(afl);

    // DEBUG This whole loop is WIP
    if (afl->second_run) {
      afl->encoded_opt_set_hashmap = initHashIntMap();
      // generate_encoded_matrix(afl, afl->config_count * afl->config_score_row_size, afl->options_count, 2);
      print_config_score(afl);
      u32 rows = generate_encoded_matrix(afl, 2);
      print_encoded_matrix(afl, rows);  
      print_encoded_matrix_to_file(afl, rows, f2);
      run_regression_analysis(afl, NULL, 2);    
      print_priority_queue(afl->presence_condition_queue);
      print_queue_to_file(afl->presence_condition_queue, f1);

      afl->second_run = false;
    } else {
      u32 iters = 0;
      while (iters < max_iters) {
        print_config_score(afl);
        printf("\n");
        print_option_setting_matrix(afl);

        // We need to add randomness to the bottom selection, and pass the presence condition to here.
        // srand(time(NULL));
        // int random_number = rand() % 100;
        // struct config_queue_entry selected_pres_cond;

        // if (random_number < 70) {
        //   selected_pres_cond = peek(afl->presence_condition_queue);
          
        //   printf("Selected: ");
        //   print_presence_cond(selected_pres_cond);
        //   printf("\n");
        // } else {
        //   selected_pres_cond = random_entry(afl->presence_condition_queue);
        //   printf("Random:");
        //   print_presence_cond(selected_pres_cond);
        //   printf("\n");
        // }

        // fprintf(f1, "Iteration: %d\n", iters);
        // fprintf(f2, "Iteration: %d\n", iters);
        // fprintf(f1, "Selected Presence Condition: ");
        // print_presence_cond_to_file(selected_pres_cond, f1);

        // Should already have the required data in the matrix and scores
        // generate_configurations(&selected_pres_cond, afl, 3, 1);
        // config_calibration_helper(afl);

        // Positive
        u32 rows;
        ACTF("==========Positive==========");
        fprintf(f1, "==========Positive==========");
        fprintf(f2, "==========Positive==========");
        printf("SELECTED: ");
        print_presence_cond(selected_pres_cond);
        print_option_setting_matrix(afl);
        afl->encoded_opt_set_hashmap = initHashIntMap();
        rows = generate_encoded_matrix(afl, 0);
        print_encoded_matrix(afl, rows);
        print_encoded_matrix_to_file(afl, rows, f2);
        run_regression_analysis(afl, &selected_pres_cond, 0);
        print_priority_queue(afl->presence_condition_queue);
        print_queue_to_file(afl->presence_condition_queue, f1);
        
        // Negation
        ACTF("==========Negation==========");
        fprintf(f1, "==========Negation==========");
        fprintf(f2, "==========Negation==========");
        printf("SELECTED: ");
        print_presence_cond(selected_pres_cond);
        print_option_setting_matrix(afl);
        afl->encoded_opt_set_hashmap = initHashIntMap();
        rows = generate_encoded_matrix(afl, 1);
        print_encoded_matrix(afl, rows);
        print_encoded_matrix_to_file(afl, rows, f2);
        run_regression_analysis(afl, &selected_pres_cond, 1);
        print_priority_queue(afl->presence_condition_queue);
        print_queue_to_file(afl->presence_condition_queue, f1);
        
        // Whole
        ACTF("==========Whole==========");
        fprintf(f1, "==========Whole==========");
        fprintf(f2, "==========Whole==========");
        printf("SELECTED: ");
        print_presence_cond(selected_pres_cond);
        print_option_setting_matrix(afl);
        afl->encoded_opt_set_hashmap = initHashIntMap();
        rows = generate_encoded_matrix(afl, 2);
        print_encoded_matrix(afl, rows);
        print_encoded_matrix_to_file(afl, rows, f2);
        run_regression_analysis(afl, &selected_pres_cond, 2);
        print_priority_queue(afl->presence_condition_queue);
        print_queue_to_file(afl->presence_condition_queue, f1);
        iters++;
      }
    }
    ck_free(afl->option_setting_matrix);

    // struct config_queue_entry top_pres_cond = peek(afl->presence_condition_queue);

    // MTA Optimization: Randomize for local optima
    // MTA todo: Continue of upper presence condition selection. We need to add randomness to this and send this above (somehow)
    // print_presence_cond(peek(afl->presence_condition_queue));
    srand(time(NULL));
    int random_number = rand() % 100;
    if (random_number < 70) {
      selected_pres_cond = peek(afl->presence_condition_queue);
        
      printf("Selected: ");
      print_presence_cond(selected_pres_cond);
      printf("\n");
    } else {
      selected_pres_cond = random_entry(afl->presence_condition_queue);
      printf("Random:");
      print_presence_cond(selected_pres_cond);
      printf("\n");
    }


    // fprintf(f1, "Iteration: %d\n", iters);
    // fprintf(f2, "Iteration: %d\n", iters);
    fprintf(f1, "Selected Presence Condition: ");
    print_presence_cond_to_file(selected_pres_cond, f1);

    print_queue_to_file(afl->presence_condition_queue, f1);
    fclose(f1);
    fclose(f2);

    ACTF("Configuration to use:");
    afl->initial_config_count = afl->configs_to_generate;
    generate_configurations(&selected_pres_cond, afl, afl->initial_config_count / 2, 1); // Current no negated
  }

  inject_config_to_fsrv(afl, afl->option_setting_matrix[afl->current_iter - 1]);
  afl->current_iter++;
  afl->config_score_row_counter = 0;

  time(afl->last_config_change);
  // Logging
  char time_string[80];
  struct tm *time_info;
  time_info = localtime(afl->last_config_change);
  strftime(time_string, sizeof(time_string), "%Y-%m-%d %H:%M:%S", time_info);
  FILE *f3 = fopen("va_driver_execution_logs", "a");
  if (f3 == NULL) {
    PFATAL("Error opening file 3!\n");
    exit(1);
  }
  fprintf(f3, "Exit time: %s (%ld) \n", time_string, (long)*afl->last_config_change);
  fclose(f3);

  return selected_pres_cond;
}


// needs optimization
void variable_analysis_all_combs(afl_state_t *afl) { // deprecated
  // data to send
  // (config, energy)
  
  // setup configs
  // u8 **configs = ck_alloc(sizeof(u8 *) * afl->size_of_inject_arr);
  // just send afl->configs_to_inject_str

  afl->energy_ls = ck_alloc(sizeof(u128) * afl->size_of_inject_arr);

  // printing traces
  // printf("\n");
  // for (int i = 0; i < afl->size_of_inject_arr; i++) {
  //   printf("[");
  //     for (int j = 0; j < afl->fsrv.map_size; j++) {
  //       printf("%.1d, ", afl->configs_to_inject_local_bitmap[i][j]);
  //     }
  //     printf("]\n");
  // }

  u128 total_configs = afl->size_of_inject_arr;
  
  for (int bit_idx = 0; bit_idx < afl->fsrv.map_size; bit_idx++) {
    int cur_min = INT_MAX;
    // find the min
    for (int trace_idx = 0; trace_idx < total_configs; trace_idx++) {
      cur_min = afl->configs_to_inject_local_bitmap[trace_idx][bit_idx] < cur_min ? 
        afl->configs_to_inject_local_bitmap[trace_idx][bit_idx] : cur_min;
    }

    // reduce the min from all traces
    for (int trace_idx = 0; trace_idx < total_configs; trace_idx++) {
      afl->configs_to_inject_local_bitmap[trace_idx][bit_idx] = afl->configs_to_inject_local_bitmap[trace_idx][bit_idx] - cur_min;
    }
  }

  // number of bits associated with each config is the energy
  int energy = 0;

  for (int trace_idx = 0; trace_idx < total_configs; trace_idx++) {
    energy = 0;
    for (int bit_idx = 0; bit_idx < afl->fsrv.map_size; bit_idx++) {
      if (afl->configs_to_inject_local_bitmap[trace_idx][bit_idx] > 0) {
        energy++;
      }
    }
    afl->energy_ls[trace_idx] = energy;
  }

  return;
  // send energy and configs
  
  
  
  
  
  
  
  
  
  
  
  
  
  u8 *var_present = ck_alloc(sizeof(u8) * afl->fsrv.map_size);
  u8 *var_absent = ck_alloc(sizeof(u8) * afl->fsrv.map_size);
  u8 *var_final_trace = ck_alloc(sizeof(u8) * afl->fsrv.map_size);
  u8 **set_negation_bitmap = ck_alloc(sizeof(int *) * afl->size_of_analyze_arr);

  for (int i = 0; i < afl->size_of_analyze_arr; i++) {
    set_negation_bitmap[i] = ck_alloc(sizeof(int) * total_configs);
  }

  for (int var_idx = 0; var_idx < afl->size_of_analyze_arr; var_idx++) {
    printf("Analyzing variable: %s\n", afl->variables_to_analyze[var_idx]);

    for (int bit_idx = 0; bit_idx < afl->fsrv.map_size; bit_idx++) {
      int cur_min = INT_MAX;

      for (int trace_idx = 0; trace_idx < afl->sizes_of_index_to_analyze[var_idx]; trace_idx++) {
        set_negation_bitmap[var_idx][afl->index_to_analyze[var_idx][trace_idx]] = 1;

        // printf("afl->index_to_analyze[var_idx][trace_idx]: %d\n", afl->index_to_analyze[var_idx][trace_idx]);
        // printf("traces[afl->index_to_analyze[var_idx][trace_idx]][bit_idx]: %d\n", traces[afl->index_to_analyze[var_idx][trace_idx]][bit_idx]);
        cur_min = afl->configs_to_inject_local_bitmap[afl->index_to_analyze[var_idx][trace_idx]][bit_idx] < cur_min ? 
          afl->configs_to_inject_local_bitmap[afl->index_to_analyze[var_idx][trace_idx]][bit_idx] : cur_min;
        
        // printf("Cur_min: %d\n", cur_min);
      }

      var_present[bit_idx] = cur_min;
    }

    // printing var_present
    printf("Present: ");
    for (int i = 0; i < afl->fsrv.map_size; i++) {
      printf("%d ", var_present[i]);
    }
    printf("\n");


    // Absent = Min(all absent traces)
    for (int bit_idx = 0; bit_idx < afl->fsrv.map_size; bit_idx++) {
      int cur_min = INT_MAX;

      for (int trace_idx = 0; trace_idx < total_configs; trace_idx++) {
        if (set_negation_bitmap[var_idx][trace_idx] == 1) {
          continue;
        }
        cur_min = afl->configs_to_inject_local_bitmap[trace_idx][bit_idx] < cur_min ? 
          afl->configs_to_inject_local_bitmap[trace_idx][bit_idx] : cur_min;
      }

      var_absent[bit_idx] = cur_min;
    }
    // printing var_absent
    printf("Absent: ");
    for (int i = 0; i < afl->fsrv.map_size; i++) {
      printf("%d ", var_absent[i]);
    }
    printf("\n");

    // printing the negation bitmap
    for (int i = 0; i < afl->size_of_analyze_arr; i++) {
      for (int j = 0; j < total_configs; j++) {
        printf("%d ", set_negation_bitmap[i][j]);
      }
      printf("\n");

    }
    


    // Data portion delete
    for (int trace_idx = 0; trace_idx < afl->fsrv.map_size; trace_idx++) {
      var_final_trace[trace_idx] = (var_present[trace_idx] == var_absent[trace_idx]) ? 
         0 : abs(var_present[trace_idx] - var_absent[trace_idx]);
    }

    // print the final trace
    printf("Final trace: ");
    for (int i = 0; i < afl->fsrv.map_size; i++) {
      printf("%d ", var_final_trace[i]);
    }
    printf("\n");
  }
}