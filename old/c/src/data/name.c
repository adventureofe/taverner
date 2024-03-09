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

#include "../../headers/sql/sql_manager.h"
#include "../../headers/data/list.h"
#include "../../headers/data/name.h"

/* callback for sqlite */
int name_callback(void *list, int argc, char **argv, char **azColName)
{
    //allocate memory for new element data
    Name* tmp = (Name*) malloc(sizeof(Name));

    //set data to whatever SQL is coming in from the database
    tmp->id = atoi(argv[0]);

    tmp->name = (char*)malloc(strlen(argv[1]) + 1);
    strcpy(tmp->name, argv[1]);

    tmp->gender = (char*)malloc(strlen(argv[2]) + 1);
    strcpy(tmp->gender, argv[2]);

    tmp->type = (char*)malloc(strlen(argv[3]) + 1);
    strcpy(tmp->type, argv[3]);



    //put the new data object into the linked list
    list_insert(list, tmp);

    return EXIT_SUCCESS;
}
