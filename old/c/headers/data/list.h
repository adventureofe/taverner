/*
    TAVERNER
    By the_adventure_of_e λ
    https://github.com/adventureofe

    a generic list type used to generate lists
*/

#ifndef LIST_H
#define LIST_H

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


#include "../sql/sql_manager.h"

/* struct definition */
typedef struct Node
{
    void *data;
    struct Node* next;
} Node;

typedef struct List
{
    struct Node* head;
    size_t size; //how to handle the type
    int count;
} List;

List* list_create(size_t size);
void list_populate(Sql_Manager* sql_manager, List* list, char* table_name, int (*callback) (void*, int, char**, char**));
void list_insert_front(List* list, void* data);
void list_insert(List* list, void* data);
void list_pop(List* list);
void list_free(List* list);
void list_print(List* list);

/* allocate memory for list */
//List* list_create(Sql_Manager* sql_manager, char* table_name, int (*callback)(void*, int, char**, char**));

#endif
