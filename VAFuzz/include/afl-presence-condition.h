#ifndef AFL_PRESENCE_CONDITION_H
#define AFL_PRESENCE_CONDITION_H

#include <stdio.h>
#include <stdlib.h>
#include "afl-fuzz.h"


struct presence_condition_single {
  struct option_setting single_opt_set; // cannot be a pointer because we need to store the opt set somewhere
  bool is_negated;
  bool end_of_condition;
  u8 next_operator; // 0 = AND, 1 = OR
};

struct config_queue_entry {
  double priority;
  struct presence_condition_single *pres_conds;
  int conds_count;
};

struct presence_condition_entry {
  double priority;
  u8 *fname;
  u8 *pres_cond_str; // used for comparison
};

struct presence_condition_q {
  struct config_queue_entry *heap;
  u32 size;
  u32 capacity;
  double lowest_priority_index;
};

void swap(struct config_queue_entry*, struct config_queue_entry*);
void heapify(struct presence_condition_q*, u32);
struct presence_condition_q* create_priority_queue(int capacity);
void enqueue(struct presence_condition_q*, struct presence_condition_single *, double priority, int conds_count);
struct config_queue_entry dequeue_top(struct presence_condition_q* pq);
struct config_queue_entry dequeue_min(struct presence_condition_q* pq);
struct config_queue_entry peek(struct presence_condition_q* pq);
struct config_queue_entry random_entry(struct presence_condition_q *pq);
bool is_empty(struct presence_condition_q *pq);
void print_presence_cond_to_file(struct config_queue_entry entry, FILE *f);
void print_queue_to_file(struct presence_condition_q *pq, FILE *f);
void print_priority_queue(struct presence_condition_q*);
void generate_configurations(struct config_queue_entry *queue_entry, afl_state_t *afl, u128 config_count, u8 negated_pres_cond);
void print_presence_cond(struct config_queue_entry entry);

#endif