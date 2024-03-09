/*
    TAVERNER
    By the_adventure_of_e λ
    https://github.com/adventureofe
*/

#ifndef SQL_MANAGER_H
#define SQL_MANAGER_H

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

//struct definition
typedef struct Sql_Manager
{
    int id;
    sqlite3 *db;
    char* zErrMsg;
    int rc;
    int (*func)(void* data, char* sql, void* head);
} Sql_Manager;

//allocate memory for the texture manager and fill it's hashmap with null pointers
Sql_Manager* sql_manager_create(void);
void sql_manager_destroy(Sql_Manager* sql_manager);

// hash table print
void sql_manager_print(Sql_Manager* sql_manager);

void sql_manager_execute(Sql_Manager* sql_manager, char* sql, void* head, int(*func)(void* data, int argc, char** argv, char** error));

#endif
