/*
    TAVERNER
    By the_adventure_of_e λ
    https://github.com/adventureofe
*/

#ifndef NAME_LIST_H
#define NAME_LIST_H

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

/* struct definition */
typedef struct Name
{
    int id;
    char* name;
    char* gender;
    char* type;
} Name;

/* callback to populate element list */
int name_callback(void *list, int argc, char **argv, char **azColName);

/* return a pointer to found node (or return NULL if not found) */
Name* name_list_find(List* list, int id);

#endif
