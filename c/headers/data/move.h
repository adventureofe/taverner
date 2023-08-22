/*
    TAVERNER
    By the_adventure_of_e λ
    https://github.com/adventureofe
*/

#ifndef MOVE_LIST_H
#define MOVE_LIST_H

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
typedef struct Move
{
    int id;
    char* name;
    int element_id;
    Element* element;
    int type;
    int priority;
    int category;
    int ai_prompt;
    int effect;
    int chance;
} Move;

/* callback to populate element list */
int move_callback(void *list, int argc, char **argv, char **azColName);

/* return a pointer to found node (or return NULL if not found) */
Move* move_list_find(List* list, int id);

#endif
