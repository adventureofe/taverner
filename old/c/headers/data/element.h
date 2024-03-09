/*
    TAVERNER
    By the_adventure_of_e λ
    https://github.com/adventureofe
*/

#ifndef ELEMENT_LIST_H
#define ELEMENT_LIST_H

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
#include "colour.h"

/* struct definition */
typedef struct Element
{
    int id;
    char* name;
    int type;
    int colour_id;
    Colour* colour;
} Element;

/* callback to populate element list */
int element_callback(void *list, int argc, char **argv, char **azColName);

/* return a pointer to found node (or return NULL if not found) */
Element* element_list_find(List* list, int id);

#endif
