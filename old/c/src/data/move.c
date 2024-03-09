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
#include "../../headers/data/element.h"
#include "../../headers/data/move.h"

/* callback for sqlite */
int move_callback(void *list, int argc, char **argv, char **azColName)
{
    //allocate memory for new element data
    Move* tmp = (Move*) malloc(sizeof(Move));

    //set data to whatever SQL is coming in from the database
    tmp->id = atoi(argv[0]);

    tmp->name = (char*)malloc(strlen(argv[1]) + 1);
    strcpy(tmp->name, argv[1]);

    //put the new data object into the linked list
    list_insert(list, tmp);

    return EXIT_SUCCESS;
}

/*
int move_callback(void *list, int argc, char **argv, char **azColName)
{
    Move *tmp = (Move*) malloc(sizeof(Move));

    tmp->id = atoi(argv[0]);

    tmp->name = (char*)malloc(strlen(argv[1]) + 1);
    strcpy(tmp->name, argv[1]);

    tmp->element_id = atoi(argv[2]);

    tmp->type = atoi(argv[3]);
    tmp->priority = atoi(argv[4]);
    tmp->category = atoi(argv[5]);
    tmp->ai_prompt = atoi(argv[6]);
    tmp->effect = atoi(argv[7]);
    tmp->chance = atoi(argv[8]);

    list_insert(head, tmp);
    return EXIT_SUCCESS;
}
*/
