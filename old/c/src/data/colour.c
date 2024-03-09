/*
    TAVERNER
    By the_adventure_of_e λ
    https://github.com/adventureofe
*/

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>
#include <string.h>
#include <time.h>
#include <stdint.h>

#include <SDL2/SDL.h>
#include <SDL2/SDL_image.h>
#include <sqlite3.h>

#include "../../headers/data/list.h"
#include "../../headers/sql/sql_manager.h"
#include "../../headers/data/colour.h"

/* callback to populate a list with colour data from SQL database */
int colour_callback(void *list, int argc, char **argv, char **azColName)
{
    //allocate memory for new colour data
    Colour* tmp = (Colour*) malloc(sizeof(Colour));

    //set data to whatever SQL is coming in from the database
    tmp->id = atoi(argv[0]);

    tmp->name = (char*)malloc(strlen(argv[1]) + 1);
    strcpy(tmp->name, argv[1]);

    tmp->r = atoi(argv[2]);
    tmp->g = atoi(argv[3]);
    tmp->b = atoi(argv[4]);

    //put the new data object into the linked list
    list_insert(list, tmp);

    return EXIT_SUCCESS;
}
