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
#include "../../headers/data/colour.h"

List* list_create(size_t size)
{
    List* new_list = (List*)malloc(sizeof(List));
    new_list->head = NULL;
    new_list->size = size;
    new_list->count = 0;
    return new_list;
}

void list_populate(Sql_Manager* sql_manager, List* list, char* table_name, int (*callback) (void*, int, char**, char**))
{
    char* sql_template = "SELECT * FROM vw_";
    char* sql_template_end = ";";

    //malloc space for sql_statement
    char* sql_statement = (char*) malloc(strlen(sql_template) + strlen(table_name) + strlen(sql_template_end) + 1);

    //concatonate strings and place in memory
    memcpy(sql_statement, sql_template, strlen(sql_template));
    memcpy(sql_statement + strlen(sql_template), table_name, strlen(table_name));
    memcpy(sql_statement + strlen(sql_template) + strlen(table_name), sql_template_end, strlen(sql_template_end) + 1);

    printf("LIST_CREATE_STATEMENT: %s\n", sql_statement);

    /* fill linked list using SQL */
    sql_manager_execute(sql_manager, sql_statement, list, callback);
}


void list_print(List* list)
{
    Node* tmp_node = list->head;

    while(tmp_node != NULL)
    {
        Colour* tmp = (Colour*)tmp_node->data;
        printf("ID(%d), NAME(%s)\n", tmp->id, tmp->name);
        tmp_node = tmp_node->next;
    }
}

void list_insert_front(List* list, void* data)
{
    Node* new_node = (Node*)malloc(sizeof(Node));
    new_node->data = (void*) data;
    new_node->next = list->head;
    list->head = new_node;
    list->count++;
}

void list_insert(List* list, void* data)
{
    //allocate a new node in memory. give it the data and initialize the "next" pointer
    Node* new_node = (Node*)malloc(sizeof(Node));
    new_node->data = (void*) data;
    new_node->next = NULL;

    // if the list is empty, the new node becomes the head
    if (list->head == NULL)
    {
        list->head = new_node;
        return;
    }

    // otherwise, add the new node to the end of the list
    // create temporary node pointer for list traversal
    Node* current_node = list->head;

    //traverse to the ened of the list
    while (current_node->next != NULL)
    {
        current_node = current_node->next;
    }

    //insert new entry at the end of the list
    current_node->next = new_node;
    list->count++;
}

void list_pop(List* list)
{
    if(list->count != 0)
    {
        Node* node = list->head;
        list->head = node->next;
        free(node);
        list->count--;
    }
}

void list_free(List* list)
{
    Node* node = list->head;
    while(node != NULL)
    {
        Node* next = node->next;
        free(node);
        node = next;
    }
    free(list);
}
