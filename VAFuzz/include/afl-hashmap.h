#ifndef AFL_HASHMAP_H
#define AFL_HASHMAP_H

# include "afl-fuzz.h"
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
#define XXH_INLINE_ALL
#include "xxhash.h"
#undef XXH_INLINE_ALL

typedef struct HashIntNode {
    u8 *key;
    int value;
    struct HashIntNode *next;
    bool assigned;
} HashIntNode;

// Define the hashmap structure
typedef struct HashIntMap {
    HashIntNode *buckets[100];
} HashIntMap;



typedef struct HashOptNode {
    char *key;
    struct option_entry *option_payload;
    struct HashOptNode *next;
    bool assigned;
} HashOptNode;

// Define the hashmap structure
typedef struct HashOptMap {
    HashOptNode *buckets[100];
} HashOptMap;

// Initialize the hashmap
// For Encoded Matrix
HashIntMap * initHashIntMap();
void printHashIntMap(HashIntMap *map);
// Insert key-value pair into hashmap
void hashIntInsert(HashIntMap *map, const char *key, int value);
// Retrieve value associated with a key
int hashIntGet(HashIntMap *map, const char *key);
void freeHashIntMap(HashIntMap *map);
void printHashIntMapToFile(HashIntMap *map, FILE *f);



HashOptMap * initHashOptMap();
void printHashOptMap(HashOptMap *map);
// Insert key-value pair into hashmap
void hashOptInsert(HashOptMap *map, const char *key, struct option_entry *opt_entry);
// Retrieve value associated with a key
struct option_entry * hashOptGet(HashOptMap *map, const char *key);
struct option_entry** getAllOptionEntries(HashOptMap *map, int *numEntries);


#endif