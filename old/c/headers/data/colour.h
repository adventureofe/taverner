/*
    TAVERNER
    By the_adventure_of_e λ
    https://github.com/adventureofe
*/

#ifndef COLOUR_LIST_H
#define COLOUR_LIST_H

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
typedef struct Colour
{
    int id;
    char* name;
    int r;
    int g;
    int b;
} Colour;

/* callback to populate a list with colour data from SQL database */
int colour_callback(void *list, int argc, char **argv, char **azColName);

#endif
