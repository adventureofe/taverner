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
#include "../../headers/data/species.h"

/* callback for sqlite */
int species_callback(void *list, int argc, char **argv, char **azColName)
{
    //allocate memory for new species data
    Species* tmp = (Species*) malloc(sizeof(Species));

    //set data to whatever SQL is coming in from the database
    tmp->id = atoi(argv[0]);

    tmp->name = (char*)malloc(strlen(argv[1]) + 1);
    strcpy(tmp->name, argv[1]);

    //put the new data object into the linked list
    list_insert(list, tmp);

    return EXIT_SUCCESS;
}


/*
int species_callbaclk(void *list, int argc, char **argv, char **azColName)
{
    List **head = (List**) list;
    Species *tmp = (Species*) malloc(sizeof(Species));

    tmp->id = atoi(argv[0]);

    tmp->name = (char*)malloc(strlen(argv[1]) + 1);
    strcpy(tmp->name, argv[1]);

    tmp->fav_element_1_id = atoi(argv[2]);
    tmp->fav_element_2_id = atoi(argv[3]);

    tmp-> weight_min = atoi(argv[4]);
    tmp-> weight_max = atoi(argv[5]);
    tmp->length_min = atoi(argv[6]);
    tmp->length_max = atoi(argv[7]);
    tmp->rarity = atoi(argv[8]);

    species_list_insert(head, tmp);
    return 0;
}
*/
/*
void species_list_init(List* species_list, List* element_list)
{
    List* current = species_list;

    while(current != NULL)
    {
        Species* tmp = (Species*) current->data;
        tmp->fav_element_1 = element_list_find(element_list, tmp->fav_element_1_id);
        tmp->fav_element_2 = element_list_find(element_list, tmp->fav_element_2_id);
        current = current->next;
    }
}
*/
/*
void species_list_print(List* list)
{
    List* current = list;

    while (current != NULL)
    {
        Species* tmp = (Species*) current->data;
        printf("ID(%d), NAME(%s), FAV_ELEMENT_1(%s), FAV_ELEMENT_(%s), WEIGHT_MIN(%d) WEIGHT_MAX(%d), LENGTH_MIN(%d), LENGTH_MAX(%d) RARITY(%d)\n", tmp->id, tmp->name, tmp->fav_element_1->name, tmp->fav_element_2->name, tmp->weight_min, tmp->weight_max, tmp->length_min, tmp->length_max, tmp->rarity);
        current = current->next;
    }
}


Species* species_list_find(List* list, int id)
{
    List* tmp = list;

    while(tmp->data != NULL)
    {
        Species* data = (Species*) tmp->data;

        if(data->id == id)
        {
            return data;
        }
        tmp = tmp->next;
    }
    return NULL;
}

*/
