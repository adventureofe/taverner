/*
    TAVERNER
    By the_adventure_of_e λ
    https://github.com/adventureofe
*/

#ifndef SPECIES_LIST_H
#define SPECIES_LIST_H

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>
#include <string.h>
#include <time.h>
#include <uchar.h>
#include <stdint.h>

#include <SDL2/SDL_image.h>
#include <stdbool.h>
#include <sqlite3.h>

#include "list.h"
#include "element.h"

/* struct definition */
typedef struct Species
{
    int id;
    char* name;
    int fav_element_1_id;
    Element* fav_element_1;
    int fav_element_2_id;
    Element* fav_element_2;
    int weight_min;
    int weight_max;
    int length_min;
    int length_max;
    int rarity;
    struct Species* next;
} Species;



void species_list_init(List* species_list, List* element_list);

void species_list_insert(List** head, Species* species);

/* callback to populate species list */
int species_callback(void *list, int argc, char **argv, char **azColName);

/* return a pointer to found node (or return NULL if not found) */
Species* species_list_find(List* list, int id);

#endif

