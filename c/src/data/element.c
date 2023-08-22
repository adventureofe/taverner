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

/* callback for sqlite */
int element_callback(void *list, int argc, char **argv, char **azColName)
{
    //allocate memory for new element data
    Element* tmp = (Element*) malloc(sizeof(Element));

    //set data to whatever SQL is coming in from the database
    tmp->id = atoi(argv[0]);

    tmp->name = (char*)malloc(strlen(argv[1]) + 1);
    strcpy(tmp->name, argv[1]);

    //put the new data object into the linked list
    list_insert(list, tmp);

    return EXIT_SUCCESS;
}

/*
Element* element_list_find(List* list, int id)
{
    List* tmp = list;

    while(tmp->data != NULL)
    {
        Element* data = (Element*) tmp->data;

        if(data->id == id)
        {
            return data;
        }
        tmp = tmp->next;
    }
    return NULL;
}
*/
