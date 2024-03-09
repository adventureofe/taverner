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
#include <uchar.h>
#include <stdint.h>

#include <SDL2/SDL.h>
#include <SDL2/SDL_image.h>

#include <sqlite3.h>

#include "../../headers/sql/sql_manager.h"

Sql_Manager* sql_manager_create(void)
{
    printf("sqlite3 version: ");
    printf("%s\n", sqlite3_libversion());

    Sql_Manager* sql_manager = (Sql_Manager*) malloc(sizeof(Sql_Manager));
    sql_manager->rc = sqlite3_open("../sql/taverner.db", &sql_manager->db);

    if (sql_manager->rc != SQLITE_OK)
    {
        fprintf(stderr, "Cannot open database: %s\n", sqlite3_errmsg(sql_manager->db));
        sqlite3_close(sql_manager->db);
    }
    else
    {
        fprintf(stderr, "Opened database successfully\n");
    }

    sql_manager->zErrMsg = 0;
    return sql_manager;
}

void sql_manager_destroy(Sql_Manager* sql_manager)
{
    free(sql_manager);
    sqlite3_close(sql_manager->db);
}

void sql_manager_execute(Sql_Manager* sql_manager, char* sql, void* head, int(*func)(void* data, int argc, char** argv, char** error))
{
    sql_manager->rc = sqlite3_exec(sql_manager->db, sql, func, head, &sql_manager->zErrMsg);

    if( sql_manager->rc != SQLITE_OK )
    {
        fprintf(stderr, "SQL error: %s\n", sql_manager->zErrMsg);
        sqlite3_free(sql_manager->zErrMsg);
    }
    else
    {
        fprintf(stderr, "SQL statement executed successfully\n");
    }
}
