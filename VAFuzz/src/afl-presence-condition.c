#include "afl-presence-condition.h"
#include "afl-variability.h"
#include "afl-hashmap.h"
#include <limits.h>

void swap(struct config_queue_entry *a, struct config_queue_entry *b) {
  struct config_queue_entry temp = *a;
  *a = *b;
  *b = temp;
}

// Utility function to heapify the tree
void heapify(struct presence_condition_q *pq, u32 index) {
  u32 largest = index;
  u32 left = 2 * index + 1;
  u32 right = 2 * index + 2;

  if (left < pq->size && pq->heap[left].priority > pq->heap[largest].priority)
    largest = left;

  if (right < pq->size && pq->heap[right].priority > pq->heap[largest].priority)
    largest = right;

  if (largest != index) {
    swap(&pq->heap[index], &pq->heap[largest]);
    heapify(pq, largest);
  }
}

struct config_queue_entry negate_presence_condition(struct config_queue_entry entry) {
  for (u32 i = 0; i < entry.conds_count; i++) {
    entry.pres_conds[i].single_opt_set.is_negated = 1;
    if (strcmp(entry.pres_conds[i].single_opt_set.type, "bool") == 0) {
      if (entry.pres_conds[i].single_opt_set.bool_val == 0) {
        entry.pres_conds[i].single_opt_set.bool_val = 1;
      } else {
        entry.pres_conds[i].single_opt_set.bool_val = 0;
      }
    }
  }

  return entry;
}


// Initialize the Priority Queue
struct presence_condition_q *create_priority_queue(int capacity) {
  struct presence_condition_q *pq = (struct presence_condition_q *)malloc(
      sizeof(struct presence_condition_q));
  pq->heap = (struct config_queue_entry *)malloc(
      sizeof(struct config_queue_entry) * capacity);
  pq->size = 0;
  pq->capacity = capacity;
  pq->lowest_priority_index = __DBL_MAX__;
  return pq;
}

// Insert an struct config_queue_entry into the Priority Queue
void enqueue(struct presence_condition_q      *pq,
             struct presence_condition_single *pres_cond, double priority,
             int conds_count) {
  if (pq->size == pq->capacity) {
    printf("Queue is full, removing least priority presence condition if new priority is greater.\n");
    if (priority < pq->lowest_priority_index) {
      printf("New priority is less than lowest priority, not adding to queue\n");
      return;
    } else {
      struct config_queue_entry min = dequeue_min(pq); // Needs testing
      printf("Removing: ");
      print_presence_cond(min);

      // update lowest priority index
      for (u32 i = 0; i < pq->size; i++) {
        if (pq->heap[i].priority < pq->lowest_priority_index) {
          pq->lowest_priority_index = pq->heap[i].priority;
        }
      }
    }
  }

  if (pq->lowest_priority_index > priority) {
    pq->lowest_priority_index = priority;
  }
  for (u32 i = 0; i < pq->size; i++) {
    struct config_queue_entry cur_entry = pq->heap[i];
    if (pq->heap[i].conds_count == conds_count){  
      bool is_same = true;

      for (u32 j = 0; j < conds_count; j++) {
        struct presence_condition_single cur_cond = pq->heap[i].pres_conds[j];
        if (compare_option_setting(&pq->heap[i].pres_conds[j], &pres_cond[j]) == 0) {
          is_same = false;
          break;
        }
      }
      if (is_same) {
          printf("Duplicate found, update priority if necessary\n");
          printf("Working on: ");
          print_presence_cond(pq->heap[i]);
          pq->heap[i].priority = priority;
          pq->heap[i].conds_count = conds_count;
          heapify(pq, i);
          return;
      }
    }
  }


  pq->heap[pq->size].pres_conds = pres_cond;
  pq->heap[pq->size].priority = priority;
  pq->heap[pq->size].conds_count = conds_count;
  int i = pq->size;
  pq->size++;

  while (i && pq->heap[i].priority > pq->heap[(i - 1) / 2].priority) {
    swap(&pq->heap[i], &pq->heap[(i - 1) / 2]);
    i = (i - 1) / 2;
  }
}

// Remove the struct config_queue_entry with the highest priority from the
// Priority Queue
struct config_queue_entry dequeue_top(struct presence_condition_q *pq) {
  if (pq->size == 0) {
    printf("Queue is empty\n");
    struct config_queue_entry temp = {-1, NULL};
    return temp;
  }

  struct config_queue_entry root = pq->heap[0];
  pq->heap[0] = pq->heap[pq->size - 1];
  pq->size--;
  heapify(pq, 0);

  return root;
}


struct config_queue_entry dequeue_min(struct presence_condition_q *pq) {
  if (pq->size == 0) {
    printf("Queue is empty\n");
    struct config_queue_entry temp = {-1, NULL};
    return temp;
  }

  struct config_queue_entry min = pq->heap[0];
  u32 min_index = 0;
  for (u32 i = 0; i < pq->size; i++) {
    if (pq->heap[i].priority < min.priority) {
      min = pq->heap[i];
      min_index = i;
    }
  }

  for (u32 i = min_index; i < pq->size - 1; i++) {
    pq->heap[i] = pq->heap[i + 1];
  }

  pq->size--;

  return min;
}


struct config_queue_entry peek(struct presence_condition_q *pq) {
  if (pq->size == 0) {
    printf("Queue is empty\n");
    struct config_queue_entry temp = {-1, NULL};
    return temp;
  }

  return pq->heap[0];
}

struct config_queue_entry random_entry(struct presence_condition_q *pq) {
  if (pq->size == 0) {
    printf("Queue is empty\n");
    struct config_queue_entry temp = {-1, NULL};
    return temp;
  } else {
    u32 random_index = rand() % pq->size;
    return pq->heap[random_index];
  }
}

// Function to print the elements of the Priority Queue
void print_priority_queue(struct presence_condition_q *pq) {
  if (pq->size == 0) {
    printf("Priority Queue is empty\n");
    return;
  }

  printf("Priority Queue:\n");
  for (u32 i = 0; i < pq->size; i++) {
    struct config_queue_entry entry = pq->heap[i];
    print_presence_cond(entry);
  }
  printf("\n");
}

void print_queue_to_file(struct presence_condition_q *pq, FILE *f) {
  if (pq->size == 0) {
    fprintf(f, "Priority Queue is empty\n");
    return;
  }

  fprintf(f, "Priority Queue:\n");
  for (u32 i = 0; i < pq->size; i++) {
    struct config_queue_entry entry = pq->heap[i];
    print_presence_cond_to_file(entry, f);
  }
  fprintf(f, "=========================================================\n");
}
  

// Function to generate configurations based on the presence conditions
void generate_configurations(struct config_queue_entry *queue_entry,
                             afl_state_t *afl, u128 config_count, 
                             u8 negated_pres_cond) {
  if (negated_pres_cond == 0) {
  afl->config_count = config_count;
  } else {
    afl->config_count = config_count * 2;
  }

  afl->static_opt_set_count = 0;

  u8 static_opt_set_idx[afl->options_count];
  for (u8 i = 0; i < afl->options_count; i++) {
    static_opt_set_idx[i] = 0;
  }

  struct option_setting *static_opt_set[afl->options_count]; // MTA This is issue 1
  for (u8 i = 0; i < afl->options_count; i++) {
    static_opt_set[i] = ck_alloc(sizeof(struct option_setting));
  }
  
  // Need to call again because the number of configurations has changed
  generate_settings_matrix(afl);
  generate_config_scores_matrix(afl);

  // Find the option columns that are present in the presence condition
  // Starting code
  struct presence_condition_single *pres_cond;
  if (queue_entry != NULL && queue_entry->pres_conds != NULL) {
    pres_cond = queue_entry->pres_conds;

  // Account for ORs and NOTs
    u128 idx = -1;
    do {
      idx++;
      u128 j = hashOptGet(afl->options_hashmap, pres_cond[idx].single_opt_set.opt)->id;
      static_opt_set_idx[j] = 1;
      afl->static_opt_set_count++;
      static_opt_set[j] = &pres_cond[idx].single_opt_set;

    } while (pres_cond[idx].end_of_condition == false);
  }

  for (u128 i = 0; i < config_count; i++) {
    for (u8 j = 0; j < afl->options_count; j++) {
      if (static_opt_set_idx[j] == 1) {
        copy_option_setting(afl->option_setting_matrix[i][j],
                            static_opt_set[j]);

        if (negated_pres_cond == 1) {
          copy_option_setting(afl->option_setting_matrix[i + config_count][j], static_opt_set[j]);
          afl->option_setting_matrix[i + config_count][j]->is_negated = true;

          if (!strcmp(afl->option_setting_matrix[i + config_count][j]->type, "bool")) {
            if (afl->option_setting_matrix[i + config_count][j]->bool_val == 0) {
              afl->option_setting_matrix[i + config_count][j]->bool_val = 1;
            } else {
              afl->option_setting_matrix[i + config_count][j]->bool_val = 0;
            }
          }

        }
      }
    }
  }

  // For each element in hashmap
  struct option_entry** all_option_entries = getAllOptionEntries(afl->options_hashmap, &afl->options_count);
  for (u8 k = 0; k < afl->options_count; k++) {
    if(static_opt_set_idx[all_option_entries[k]->id] != 1 || queue_entry == NULL) {
      // If not static opt set, then generate random value for each row
      struct option_entry *current_option = all_option_entries[k];
      
      struct option_setting *opt_set = ck_alloc(sizeof(struct option_setting));
      
      if (opt_set == NULL) {
        PFATAL("Unable to allocate memory for option setting");
        exit(1);
      }
      // check for what type.
      opt_set->opt = ck_alloc(strlen(current_option->opt) + 1);

      // check for what type.
      opt_set->opt = ck_alloc(strlen(current_option->opt) + 1);
      memcpy(opt_set->opt, current_option->opt, strlen(current_option->opt) + 1);
      memcpy(opt_set->opt, current_option->opt, strlen(current_option->opt) + 1);
      opt_set->opt[strlen(current_option->opt)] = '\0';

      srand(time(NULL));


      if (strcmp(current_option->type, "bool") == 0) {
        for (u128 i = 0; i < config_count; i++) {
          u8 random_value = rand() % 2;
          opt_set->bool_val = random_value;
          opt_set->type = "bool";
          copy_option_setting(afl->option_setting_matrix[i][current_option->id], opt_set);
          if (negated_pres_cond == 1) {
            copy_option_setting(afl->option_setting_matrix[i + config_count][current_option->id], opt_set);
          }
        }
      } else if (strcmp(current_option->type, "intnum") == 0) {

        for (u128 i = 0; i < config_count; i++) {
          u8 random_value = rand() % (current_option->intRangeMax - current_option->intRangeMin + 1) +
                            current_option->intRangeMin;
          opt_set->int_val = random_value;
          opt_set->type = "intnum";
          copy_option_setting(afl->option_setting_matrix[i][current_option->id], opt_set);
          if (negated_pres_cond == 1) {
            copy_option_setting(afl->option_setting_matrix[i + config_count][current_option->id], opt_set);
          }
        }
      } else if (strcmp(current_option->type, "realnum") == 0) {
        for (u128 i = 0; i < config_count; i++) {
          double scaled = (double)rand() / current_option->realRangeMax;
          double random_value = scaled * (current_option->realRangeMax - current_option->realRangeMin) + 
                                current_option->realRangeMin;
          opt_set->real_val = random_value;
          opt_set->type = "realnum";
          copy_option_setting(afl->option_setting_matrix[i][current_option->id], opt_set);
          if (negated_pres_cond == 1) {
            copy_option_setting(afl->option_setting_matrix[i + config_count][current_option->id], opt_set);
          }
        }
      } else if (strcmp(current_option->type, "choice") == 0) {
        for (u128 i = 0; i < config_count; i++) {          
          opt_set->str_val = current_option->choices[0]; 
          opt_set->type = "choice";
          copy_option_setting(afl->option_setting_matrix[i][current_option->id], opt_set);
          if (negated_pres_cond == 1) {
            copy_option_setting(afl->option_setting_matrix[i + config_count][current_option->id], opt_set);
          }
        }
      } else if (strcmp(current_option->type, "string") == 0) {
        for (u128 i = 0; i < config_count; i++) {
          opt_set->str_val = randomString(10, i);
          opt_set->type = "string";
          copy_option_setting(afl->option_setting_matrix[i][current_option->id], opt_set);
          if (negated_pres_cond == 1) {
            copy_option_setting(afl->option_setting_matrix[i + config_count][current_option->id], opt_set);
          }
        }
      }

      ck_free(opt_set->opt);
      ck_free(opt_set);
    }
  } 

  print_option_setting_matrix(afl);
}


bool is_empty(struct presence_condition_q *pq) {
  if (pq->size == 0) {
    return true;
  } else {
    return false;
  }
}


void print_presence_cond(struct config_queue_entry entry) {
  for(u32 j = 0; j < entry.conds_count; j++) {
      if (entry.pres_conds[j].single_opt_set.is_negated == 1
          && strcmp(entry.pres_conds[j].single_opt_set.type, "bool")) {
        printf("!");
      }

      if (strcmp(entry.pres_conds[j].single_opt_set.type, "bool") == 0) {
        printf("(%s, %d)",
              entry.pres_conds[j].single_opt_set.opt,
              entry.pres_conds[j].single_opt_set.bool_val);
      } else if (strcmp(entry.pres_conds[j].single_opt_set.type, "intnum") == 0) {
        printf("(%s, %d)",
              entry.pres_conds[j].single_opt_set.opt,
              entry.pres_conds[j].single_opt_set.int_val);
      } else if (strcmp(entry.pres_conds[j].single_opt_set.type, "realnum") == 0) {
        printf("(%s, %f)",
              entry.pres_conds[j].single_opt_set.opt,
              entry.pres_conds[j].single_opt_set.real_val);
      } else if (strcmp(entry.pres_conds[j].single_opt_set.type, "choice") == 0) {
        printf("(%s, %s)",
              entry.pres_conds[j].single_opt_set.opt,
              entry.pres_conds[j].single_opt_set.str_val);
      } else if (strcmp(entry.pres_conds[j].single_opt_set.type, "string") == 0) {
        printf("(%s, %s)",
              entry.pres_conds[j].single_opt_set.opt,
              entry.pres_conds[j].single_opt_set.str_val);
      }

      if (entry.pres_conds[j].end_of_condition == false) {  
        if (entry.pres_conds[j].next_operator == 0) {
          printf(" AND ");
        } else {
          printf(" OR ");
        }
      } else {
        printf(" ");
      }
    }

    printf("%f ", entry.priority);
    printf("Conds count: %d\n", entry.conds_count);
}

void print_presence_cond_to_file(struct config_queue_entry entry, FILE *f) {
  for(u32 j = 0; j < entry.conds_count; j++) {
      if (entry.pres_conds[j].single_opt_set.is_negated == 1
          && strcmp(entry.pres_conds[j].single_opt_set.type, "bool")) {
        fprintf(f, "!");
      }

      if (strcmp(entry.pres_conds[j].single_opt_set.type, "bool") == 0) {
        fprintf(f, "(%s, %d)",
              entry.pres_conds[j].single_opt_set.opt,
              entry.pres_conds[j].single_opt_set.bool_val);
      } else if (strcmp(entry.pres_conds[j].single_opt_set.type, "intnum") == 0) {
        fprintf(f, "(%s, %d)",
              entry.pres_conds[j].single_opt_set.opt,
              entry.pres_conds[j].single_opt_set.int_val);
      } else if (strcmp(entry.pres_conds[j].single_opt_set.type, "realnum") == 0) {
        fprintf(f, "(%s, %f)",
              entry.pres_conds[j].single_opt_set.opt,
              entry.pres_conds[j].single_opt_set.real_val);
      } else if (strcmp(entry.pres_conds[j].single_opt_set.type, "choice") == 0) {
        fprintf(f, "(%s, %s)",
              entry.pres_conds[j].single_opt_set.opt,
              entry.pres_conds[j].single_opt_set.str_val);
      } else if (strcmp(entry.pres_conds[j].single_opt_set.type, "string") == 0) {
        fprintf(f, "(%s, %s)",
              entry.pres_conds[j].single_opt_set.opt,
              entry.pres_conds[j].single_opt_set.str_val);
      }

      if (entry.pres_conds[j].end_of_condition == false) {  
        if (entry.pres_conds[j].next_operator == 0) {
          fprintf(f, " AND ");
        } else {
          fprintf(f, " OR ");
        }
      } else {
        fprintf(f, " ");
      }
    }

    fprintf(f, "%f\n", entry.priority);
}

