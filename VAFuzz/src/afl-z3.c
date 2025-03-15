#include "afl-z3.h"
#include "afl-fuzz.h"
#include "common.h"
#include <dirent.h>
#include <Python.h>
#include <string.h>

void split_and_remove_ext(const u8 *path, u8 *directory, u8 *filename) {
    const u8 *last_slash = strrchr(path, '/');  // For UNIX-like systems
    if (last_slash != NULL) {
      if (strlen(last_slash) == strlen(path)) {
        // The file is in root directory
        strncpy(directory, "/\0", 2);
      } else {
        // Copy the directory part
        strncpy(directory, path, last_slash - path);
        directory[last_slash - path] = '\0';  // Null-terminate the directory string
      }
      // Copy the filename part
      strcpy(filename, last_slash + 1);
    } else {
      // No directory part, only filename
      strcpy(directory, "");
      strcpy(filename, path);
    }

    // Remove the '.py' extension if it exists
    u8 *dot = strrchr(filename, '.');
    if (dot != NULL && strcmp(dot, ".py") == 0) {
        *dot = '\0';  // Terminate the filename at the extension
    }
}


void get_init_info(afl_state_t *afl, u8* z3_solver_path) {
  u8 directory[256];
  u8 filename[256];
  u8 add_to_sys[256];

  split_and_remove_ext(z3_solver_path, directory, filename);
  printf("Directory: %s\n", directory);
  snprintf(add_to_sys, sizeof(add_to_sys), "import sys; sys.path.append('%s')", directory);
  PyObject *pName, *pModule, *pFunc;
  PyObject *pArgs, *pValue, *pConfigs, *pVarmap, *pPresenceCondition;

  // Py_Initialize();
  // PyRun_SimpleString("import sys; sys.path.append('.')");
  PyRun_SimpleString(add_to_sys);

  pName = PyUnicode_DecodeFSDefault(filename);
  pModule = PyImport_Import(pName);
  Py_DECREF(pName);

  printf("Filename: %s\n", filename);

  if (pModule == NULL) {
    PyErr_Print();
    PFATAL("Python API: Failed to locate pModule");
  }

  pFunc = PyObject_GetAttrString(pModule, "init_info");
  afl->req_config_pfunc = PyObject_GetAttrString(pModule, "request_config_generation");
  afl->send_feedback_pfunc = PyObject_GetAttrString(pModule, "send_feedback");
  afl->send_data_feedback_pfunc = PyObject_GetAttrString(pModule, "analyze_feedback_data");

  if (!pFunc || !PyCallable_Check(pFunc)) {
    PFATAL("Python API: Failed to locate pfunc");
    Py_XDECREF(pFunc);
    Py_DECREF(pModule);
  }

  // Call the function without arguments
  pValue = PyObject_CallObject(pFunc, NULL);
  if (pValue == NULL) {
    Py_DECREF(pFunc);
    Py_DECREF(pModule);
    PyErr_Print();
    PFATAL("Python API: Call failed");
    return;
  }

  // Success
  if (!PyList_Check(pValue)) {
    PFATAL("Python API: pValues is not a list");
  }

  afl->options_count = PyLong_AsLong(PyList_GetItem(pValue, 0));

  Py_DECREF(pFunc);
  Py_DECREF(pModule);
  Py_DECREF(pValue);
  // Py_Finalize();

  printf("Options count: %d\n", afl->options_count);
}

void request_configs(afl_state_t *afl, u8* pres_cond_file_path, u8* z3_solver_path, u8 config_number){
  ACTF("REQESTING CONFIGS");
  // u8 directory[256];
  // u8 filename[256];
  // u8 add_to_sys[256];

  // split_and_remove_ext(z3_solver_path, directory, filename);
  // snprintf(add_to_sys, sizeof(add_to_sys), "import sys; sys.path.append('%s')", directory);
  // PyObject *pName, *pModule, *pFunc;
  PyObject *pArgs, *pValue, *pConfigs, *pZ3Configs, *pVarmap, *pPresenceCondition, *pEnergy;

  // Py_Initialize();
  // // PyRun_SimpleString("import sys; sys.path.append('.')");
  // PyRun_SimpleString(add_to_sys);

  // pName = PyUnicode_DecodeFSDefault(filename);
  // if(pName == NULL) {
  //   PFATAL("Python API: Failed to decode filename");
  // }

  // pModule = PyImport_Import(pName);
  // Py_DECREF(pName);

  // if (pModule != NULL) {
  // if (pModule != NULL) {
    // pFunc = PyObject_GetAttrString(pModule, "request_config_generation");

    if (afl->req_config_pfunc && PyCallable_Check(afl->req_config_pfunc)) {
      
      // Create a Python tuple to hold the arguments
      pArgs = PyTuple_New(4);            
      PyObject *pPresCondsPath = PyUnicode_DecodeFSDefault(pres_cond_file_path);
      PyObject *configs_to_gen = PyUnicode_DecodeFSDefault("50");
      PyObject *config_num = PyLong_FromLong(config_number);
      PyObject *pPcRandSelection = PyFloat_FromDouble(afl->pc_rand_selection);
      char *str = PyUnicode_AsUTF8(pPresCondsPath);

      // Set the Python string as the first (and only) argument
      PyTuple_SetItem(pArgs, 0, pPresCondsPath);
      PyTuple_SetItem(pArgs, 1, configs_to_gen); // <<<<< Configs to generate
      PyTuple_SetItem(pArgs, 2, config_num);
      PyTuple_SetItem(pArgs, 3, pPcRandSelection);
      
      
      // Call the function with the arguments
      pValue = PyObject_CallObject(afl->req_config_pfunc, pArgs);        // Decrease reference count for pArgs (pDataPath is "stolen" by PyTuple_SetItem)
      Py_DECREF(pArgs);
      if (pValue != NULL) {
        if (PyList_Check(pValue)) {
          Py_ssize_t size = PyList_Size(pValue);
          if (size != 5) {
            PFATAL("Python API: Expected list of size 5");
          }

          pConfigs = PyList_GetItem(pValue, 0);
          pVarmap = PyList_GetItem(pValue, 1);
          pPresenceCondition = PyList_GetItem(pValue, 2);
          pZ3Configs = PyList_GetItem(pValue, 3);

          if (!PyList_Check(pConfigs)) {
             PFATAL("Python API: Expected list of strings");
          }
          if (!PyDict_Check(pVarmap)) {
             PFATAL("Python API: Expected dictionary");
          }
          if (pPresenceCondition == NULL) {
            PFATAL("Python API: Presence condition is NULL");
          }
          // pPresenceCondition is a tuple (int, string)
          if (!PyTuple_Check(pPresenceCondition)) {
            PFATAL("Python API: Presence condition is not a tuple");
          }
          if (!PyList_Check(pZ3Configs)) {
             PFATAL("Python API: z3 configs expected list of strings");
          }

          // get first part of the tuple
          afl->presence_condition_energy_used = abs(PyLong_AsLong(PyTuple_GetItem(pPresenceCondition, 0)));
          printf("Presence condition energy used: %d\n", afl->presence_condition_energy_used);
          if (afl->presence_condition_energy_used == 0) {
            afl->execs_per_selection = afl->execs_per_selection_default;
          } else {
            afl->execs_per_selection = (afl->presence_condition_energy_used * 5000 < 100000) ? 
              afl->presence_condition_energy_used * 5000 : 100000;
          }

          // get second part of the tuple
          pPresenceCondition = PyTuple_GetItem(pPresenceCondition, 1);

          // check if pPresCond is an empty string
          if (PyUnicode_Check(pPresenceCondition)) {
            const char *str = PyUnicode_AsUTF8(pPresenceCondition);
            if (str != NULL) {
              if (strlen(str) == 0) {
                afl->presence_condition_used = NULL;
              } else {
                afl->presence_condition_used = ck_alloc(sizeof(u8) * (strlen(str) + 1));
                afl->presence_condition_used = strdup(PyUnicode_AsUTF8(pPresenceCondition));
                afl->presence_condition_used[strlen(PyUnicode_AsUTF8(pPresenceCondition))] = '\0';
                // printf("Presence condition used: %s\n", afl->presence_condition_used);
              }
            } else {
              PFATAL("Python API: Error converting presence condition to string");
            }
          } else {
            PFATAL("Python API: Presence condition is not a string");
          }

          PyObject *key, *value;
          Py_ssize_t pos = 0;
          u32 mapsize = get_map_size();

          Py_ssize_t config_count = PyList_Size(pConfigs);
          afl->size_of_inject_arr = config_count;

          afl->configs_to_inject_str = ck_alloc(sizeof(u8 *) * config_count);
          afl->z3_configs_to_inject_str = ck_alloc(sizeof(u8 *) * config_count);
          if (afl->configs_to_inject_str == NULL) {
            PFATAL("afl->configs_to_inject mem alloc failed");
          }
          if (afl->z3_configs_to_inject_str == NULL) {
            PFATAL("afl->z3_configs_to_inject_str mem alloc failed");
          }

          afl->configs_to_inject_local_bitmap = ck_alloc(sizeof(u8 *) * config_count);
          if (afl->configs_to_inject_local_bitmap == NULL) {
            PFATAL("afl->configs_to_inject_local_bitmap mem alloc failed");
          }

          for (int i = 0; i < config_count; i++) {
            PyObject *item = PyList_GetItem(pConfigs, i);
            PyObject *item_z3 = PyList_GetItem(pZ3Configs, i);

            if (PyUnicode_Check(item) && PyUnicode_Check(item_z3)) {
              const char *str = PyUnicode_AsUTF8(item);
              const char *str_z3 = PyUnicode_AsUTF8(item_z3);

              if (str != NULL && str_z3 != NULL) {
                // afl->configs_to_inject[i].config_string = ck_alloc(sizeof(u8) * (strlen(str) + 1));
                // strcpy(afl->configs_to_inject[i].config_string, str);
                afl->configs_to_inject_str[i] = strdup(str);
                afl->z3_configs_to_inject_str[i] = strdup(str_z3);
                printf("Stored string %zd: %s<\n", i, afl->configs_to_inject_str[i]);
                printf("Stored z3 string %zd: %s<\n", i, afl->z3_configs_to_inject_str[i]);

                if(afl->configs_to_inject_str[i] == NULL || afl->z3_configs_to_inject_str[i] == NULL) {
                  PFATAL("Failed to add string to config_entry");
                }
              } else {
                printf("Error converting string at index %zd\n", i);
              }
            } else {
              printf("Item at index %zd is not a string\n", i);
            }
          }


          Py_ssize_t dict_size = PyDict_Size(pVarmap);
          int dict_size_int = dict_size;
          if (dict_size_int == 0) {
            afl->index_to_analyze = ck_alloc(sizeof(int *) * 1);
            afl->variables_to_analyze = ck_alloc(sizeof(u8 *) * 1);
            afl->sizes_of_index_to_analyze = ck_alloc(sizeof(int) * 1);
          } else {
          afl->index_to_analyze = ck_alloc(sizeof(int *) * dict_size_int);
          afl->variables_to_analyze = ck_alloc(sizeof(u8 *) * dict_size_int);
          afl->sizes_of_index_to_analyze = ck_alloc(sizeof(int) * dict_size_int);
          }
          
          if (afl->index_to_analyze == NULL || afl->variables_to_analyze == NULL) {
            PFATAL("afl->index_to_analyze or afl->variables_to_analyze mem alloc failed");
          }
          // printf("Dict size: %zd\n", dict_size_int);


          while (PyDict_Next(pVarmap, &pos, &key, &value)) {

            if (PyUnicode_Check(key)) {
              const char *key_str = PyUnicode_AsUTF8(key);
              if (key_str != NULL) {
                // printf("Key: %s\n", key_str);
                afl->variables_to_analyze[pos - 1] = ck_alloc(sizeof(u8) * (strlen(key_str) + 1));
                strcpy(afl->variables_to_analyze[pos - 1], key_str);
                // printf("Stored variable at index %zd: %s\n", pos, afl->variables_to_analyze[pos - 1]);

                // Check if the value is a list of integers
                if (PyList_Check(value)) {
                  Py_ssize_t value_size = PyList_Size(value);
                  // printf("Value size: %zd\n", value_size);

                  afl->index_to_analyze[pos - 1] = ck_alloc(sizeof(int) * value_size);
                  if (afl->index_to_analyze[pos - 1] == NULL) {
                    PFATAL("afl->index_to_analyze[pos] mem alloc failed");
                  }

                  afl->sizes_of_index_to_analyze[pos - 1] = value_size;

                  for (Py_ssize_t i = 0; i < value_size; i++) {
                    PyObject *item = PyList_GetItem(value, i);
                    if (PyLong_Check(item)) {
                      int int_value = (int) PyLong_AsLong(item);
                      afl->index_to_analyze[pos - 1][i] = int_value;
                      // printf("Stored integer at index %zd: %d\n", i, afl->index_to_analyze[pos - 1][i]);
                    } else {
                        // printf("Value at index %zd is not an integer\n", i);
                    }
                  }
                } else {
                    // printf("Value for key %s is not a list\n", key_str);
                }
              } else {
                // printf("Error converting key to string\n");
              }
            } else {
                // printf("Key is not a string\n");
            }

            afl->size_of_analyze_arr = dict_size_int;
          }

          // data association
          if (config_number != 2) {
            for (int i = 0; i < afl->queued_items; i++) {
              afl->queue_buf[i]->favored = 0;
            }
            

            PyObject *favoured_lst;
            favoured_lst = PyList_GetItem(pValue, 3);
            Py_ssize_t ls_length = PyList_Size(favoured_lst);
            for (Py_ssize_t i = 0; i < ls_length; i++) {
              PyObject *item = PyList_GetItem(favoured_lst, i); // Borrowed reference

              // Check if the item is an integer or float
              if (PyLong_Check(item)) {
                  int value = PyLong_AsLong(item);
                  // printf("Value: %d\n", value);
                  afl->queue_buf[value]->favored = 1;
              }
            }
          }

        } else {
          // printf("Returned value is not a list\n");
        }    
        Py_DECREF(pValue);        
      } else {
        // Py_DECREF(pFunc);
        // Py_DECREF(pModule);
        PyErr_Print();
        fprintf(stderr, "Call failed\n");
        PFATAL("Python API: Call failed");
        // Py_XDECREF(pFunc);
        // Py_DECREF(pModule);
        
        return;
      }
      // Py_DECREF(pFunc);    
    } else {
      PFATAL("Python API: Failed to locate pfunc");

    }

    // Py_DECREF(pModule);
  // } else {
  //   PyErr_Print();
  //   printf("\n");
  //   PFATAL("Python API: Failed to locate pModule");
  // }

  // Py_XDECREF(pFunc);
  // Py_XDECREF(pModule);
  // Py_Finalize();

  ACTF("Configs requested successfully\n");
}


void send_feedback(afl_state_t *afl, u8* z3_solver_path) {
  ACTF("SENDING FEEDBACK");

  u8 directory[256];
  u8 filename[256];
  u8 add_to_sys[256];


  split_and_remove_ext(z3_solver_path, directory, filename);
  snprintf(add_to_sys, sizeof(add_to_sys), "import sys; sys.path.append('%s')", directory);
  
  // PyObject *pName, *pModule, *pFunc, *pArgs, *pValue;
  PyObject *pArgs, *pValue;
  PyObject *config_list, *final_trace_list, *pPresCondUsed, *p_virgin_bits, *p_argv_havoc_feedback;
  // Py_Initialize();
  // PyRun_SimpleString(add_to_sys);

  // pName = PyUnicode_DecodeFSDefault(filename);
  // pModule = PyImport_Import(pName);
  // Py_DECREF(pName);

  // if (pModule == NULL) {
  //   PFATAL("Python API: Failed to locate pModule");
  // }

  // pFunc = PyObject_GetAttrString(pModule, "send_feedback");
  if (!afl->send_feedback_pfunc || !PyCallable_Check(afl->send_feedback_pfunc)) {
    PFATAL("Python API: Failed to locate pfunc");
    // Py_XDECREF(pFunc);
    // Py_DECREF(pModule);
  }

  // create Python list for strings
  config_list = PyList_New(afl->size_of_inject_arr);
  p_argv_havoc_feedback = PyUnicode_DecodeFSDefault("0");

  if (afl->havoc_argv) {
    printf("HAVOC ARGV\n");
    // set value to int 1
    p_argv_havoc_feedback = PyUnicode_DecodeFSDefault("1");
    for (int i = 0; i < afl->size_of_inject_arr; i++) {
      PyList_SetItem(config_list, i, PyUnicode_DecodeFSDefault(afl->configs_to_inject_str[i]));
    }
  } else {
    for (int i = 0; i < afl->size_of_inject_arr; i++) {
      PyList_SetItem(config_list, i, PyUnicode_DecodeFSDefault(afl->z3_configs_to_inject_str[i]));
    }
  }
  
  if (afl->presence_condition_used == NULL) {
    pPresCondUsed = PyUnicode_DecodeFSDefault("");
  } else {
    pPresCondUsed = PyUnicode_DecodeFSDefault(afl->presence_condition_used);
  }

  // create Python list for integers
  final_trace_list = PyList_New(afl->size_of_inject_arr);
  
  for (int i = 0; i < afl->size_of_inject_arr; i++) {
    PyList_SetItem(final_trace_list, i, PyList_New(afl->fsrv.map_size));

    for (int j = 0; j < afl->fsrv.map_size; j++) {
      if (afl->fsrv.trace_bits[j] == 0) {
        afl->configs_to_inject_local_bitmap[i][j] = 0;
      }

      PyObject *trace_bit = PyLong_FromLong(afl->configs_to_inject_local_bitmap[i][j]);

      // if (afl->configs_to_inject_local_bitmap[i][j]) {
      //   printf("(IDX: %d, Trace: %d, Virgin: %d, fsrv: %d), ", j, 
      //          afl->configs_to_inject_local_bitmap[i][j], afl->virgin_bits[j],
      //          afl->fsrv.trace_bits[j]);
      // }

      PyList_SetItem(PyList_GetItem(final_trace_list, i), j, trace_bit);
    }
    printf("\n");
  }

  p_virgin_bits = PyList_New(afl->fsrv.map_size);
  for (int i = 0; i < afl->fsrv.map_size; i++) {
    PyObject *trace_bit = PyLong_FromLong(afl->virgin_bits[i]);
    PyList_SetItem(p_virgin_bits, i, trace_bit);
  }

  pArgs = PyTuple_New(5);
  PyTuple_SetItem(pArgs, 0, config_list);
  PyTuple_SetItem(pArgs, 1, final_trace_list);
  PyTuple_SetItem(pArgs, 2, pPresCondUsed);
  PyTuple_SetItem(pArgs, 3, p_virgin_bits);
  PyTuple_SetItem(pArgs, 4, p_argv_havoc_feedback);


  pValue = PyObject_CallObject(afl->send_feedback_pfunc, pArgs);
  Py_DECREF(pArgs);

  if (pValue != NULL) {
    Py_DECREF(pValue);
    int result = PyLong_AsLong(pValue);
    if (result == 0) {
      printf("Feedback sent successfully\n");
    } else {
      PFATAL("Feedback failed\n");
    }
  } else {
    // Py_DECREF(pFunc);
    // Py_DECREF(pModule);
    PyErr_Print();
    PFATAL("Python API: Call failed");
    return;
  }

  // Py_XDECREF(pFunc);
  // Py_DECREF(pModule);
  // Py_Finalize();

  ACTF("Feedback sent successfully\n");
}


void send_data_feedback(afl_state_t *afl, u8* z3_solver_path) {
  ACTF("SENDING DATA FEEDBACK");

  // u8 directory[256];
  // u8 filename[256];
  // u8 add_to_sys[256];

  // split_and_remove_ext(z3_solver_path, directory, filename);
  // snprintf(add_to_sys, sizeof(add_to_sys), "import sys; sys.path.append('%s')", directory);
  
  if (!afl || !z3_solver_path) {
    fprintf(stderr, "Invalid input to send_data_feedback\n");
    return;
  }

  // Validate critical values
  if (afl->size_of_inject_arr <= 0 || afl->execs_per_selection <= 0) {
    fprintf(stderr, "Invalid inject array or exec per selection size\n");
    return;
  }



  // PyRun_SimpleString(add_to_sys);

  // PyObject *pName = NULL, *pModule = NULL, *pFunc = NULL, *pArgs = NULL, *pValue = NULL;
  PyObject *pArgs = NULL, *pValue = NULL;
  PyObject *config_list = NULL, *raw_config_list = NULL, *data_object_list = NULL, *pPresCondUsed = NULL;
  PyObject *id_cutoff = NULL, *pc_data_association = NULL, *pOutputDir = NULL, *p_argv_havoc_feedback = NULL;

  // Extensive error checking with detailed logging
  #define SAFE_PYCHECK(obj, msg) \
    do { \
      if (!(obj)) { \
        fprintf(stderr, "ERROR: %s\n", msg); \
        PyErr_Print(); \
        goto cleanup; \
      } \
    } while(0)

  // Filename and module import
  // pName = PyUnicode_DecodeFSDefault(filename);
  // SAFE_PYCHECK(pName, "Failed to decode filename");

  // pModule = PyImport_Import(pName);
  // SAFE_PYCHECK(pModule, "Failed to import Python module");

  // // Function lookup
  // pFunc = PyObject_GetAttrString(pModule, "analyze_feedback_data");
  SAFE_PYCHECK(afl->send_data_feedback_pfunc && PyCallable_Check(afl->send_data_feedback_pfunc),
   "Failed to find callable function");

  // Config list creation
  config_list = PyList_New(afl->size_of_inject_arr);
  raw_config_list = PyList_New(afl->size_of_inject_arr);
  SAFE_PYCHECK(config_list, "Failed to create config list");
  SAFE_PYCHECK(raw_config_list, "Failed to create raw config list");

  if(afl->havoc_argv) {
    p_argv_havoc_feedback = PyUnicode_DecodeFSDefault("1");
    for (int i = 0; i < afl->size_of_inject_arr; i++) {
      // Defensive check for string
      if (!afl->configs_to_inject_str[i]) {
        fprintf(stderr, "Null config string at index %d\n", i);
        PyList_SET_ITEM(config_list, i, PyUnicode_FromString(""));
        continue;
      }
      PyObject *item = PyUnicode_DecodeFSDefault(afl->configs_to_inject_str[i]);
      SAFE_PYCHECK(item, "Failed to decode config string");
      PyList_SET_ITEM(config_list, i, item);
    }
  } else {
    p_argv_havoc_feedback = PyUnicode_DecodeFSDefault("0");
    for (int i = 0; i < afl->size_of_inject_arr; i++) {
      // Defensive check for string
      if (!afl->z3_configs_to_inject_str[i]) {
        fprintf(stderr, "Null config string at index %d\n", i);
        PyList_SET_ITEM(config_list, i, PyUnicode_FromString(""));
        PyList_SET_ITEM(raw_config_list, i, PyUnicode_FromString(""));
        continue;
      }
      
      PyObject *item = PyUnicode_DecodeFSDefault(afl->z3_configs_to_inject_str[i]);
      PyObject *raw_item = PyUnicode_DecodeFSDefault(afl->configs_to_inject_str[i]);
      SAFE_PYCHECK(item, "Failed to decode config string");
      SAFE_PYCHECK(raw_item, "Failed to decode raw config string");
      PyList_SET_ITEM(config_list, i, item);
      PyList_SET_ITEM(raw_config_list, i, raw_item);
    }
  }

  // Data object list creation
  data_object_list = PyList_New(afl->size_of_inject_arr);
  SAFE_PYCHECK(data_object_list, "Failed to create data object list");

  for (int i = 0; i < afl->size_of_inject_arr; i++) {
    // Defensive check for data triples
    if (!afl->data_triples[i]) {
      fprintf(stderr, "Null data triples at index %d\n", i);
      PyList_SET_ITEM(data_object_list, i, PyList_New(0));
      continue;
    }

    PyObject *inner_list = PyList_New(afl->execs_per_selection);
    SAFE_PYCHECK(inner_list, "Failed to create inner list");
    
    for (int j = 0; j < afl->execs_per_selection; j++) {
      // Validate data triple
      PyObject *data_object = PyTuple_New(3);
      SAFE_PYCHECK(data_object, "Failed to create data tuple");

      PyTuple_SET_ITEM(data_object, 0, PyLong_FromLong(afl->data_triples[i][j].id));
      PyTuple_SET_ITEM(data_object, 1, PyLong_FromLong(afl->data_triples[i][j].new_bits));
      PyTuple_SET_ITEM(data_object, 2, PyLong_FromLong(afl->data_triples[i][j].crashed));
      
      PyList_SET_ITEM(inner_list, j, data_object);
    }
    
    PyList_SET_ITEM(data_object_list, i, inner_list);
  }

  // Remaining argument preparation
  pPresCondUsed = PyUnicode_DecodeFSDefault(
    afl->presence_condition_used ? afl->presence_condition_used : ""
  );
  SAFE_PYCHECK(pPresCondUsed, "Failed to create presence condition");

  id_cutoff = PyLong_FromLong(afl->queued_items - 1);
  SAFE_PYCHECK(id_cutoff, "Failed to create id cutoff");

  pc_data_association = PyLong_FromLong(
    afl->mutator_1_start ? 1 : afl->pc_data_asso
  );
  SAFE_PYCHECK(pc_data_association, "Failed to create pc data association");

  // Prepare arguments
  pArgs = PyTuple_New(8);
  SAFE_PYCHECK(pArgs, "Failed to create argument tuple");

  // set output dir
  pOutputDir = PyUnicode_DecodeFSDefault(afl->out_dir);

  PyTuple_SET_ITEM(pArgs, 0, config_list);
  PyTuple_SET_ITEM(pArgs, 1, data_object_list);
  PyTuple_SET_ITEM(pArgs, 2, pPresCondUsed);
  PyTuple_SET_ITEM(pArgs, 3, id_cutoff);
  PyTuple_SET_ITEM(pArgs, 4, pc_data_association);
  PyTuple_SET_ITEM(pArgs, 5, pOutputDir);
  PyTuple_SET_ITEM(pArgs, 6, p_argv_havoc_feedback);
  PyTuple_SET_ITEM(pArgs, 7, raw_config_list);

  // Reset pointers to avoid double-freeing
  config_list = NULL;
  raw_config_list = NULL;
  data_object_list = NULL;
  pPresCondUsed = NULL;
  id_cutoff = NULL;
  pc_data_association = NULL;

  // Call Python function with error checking
  pValue = PyObject_CallObject(afl->send_data_feedback_pfunc, pArgs);
  SAFE_PYCHECK(pValue, "Python function call failed");

  // Process result
  int result = PyLong_AsLong(pValue);
  if (result != 0) {
    fprintf(stderr, "Feedback processing returned non-zero: %d\n", result);
  }

cleanup:
  // Safe cleanup
  // Py_XDECREF(pName);
  // Py_XDECREF(pModule);
  // Py_XDECREF(pFunc);
  Py_XDECREF(pArgs);
  Py_XDECREF(pValue);
  Py_XDECREF(config_list);
  Py_XDECREF(raw_config_list);
  Py_XDECREF(data_object_list);
  Py_XDECREF(pPresCondUsed);
  Py_XDECREF(id_cutoff);
  Py_XDECREF(pc_data_association);
  // Py_XDECREF(pOutputDir);

  if (PyErr_Occurred()) {
    PyErr_Print();
    PFATAL("Python API: Call failed");
  }
}
