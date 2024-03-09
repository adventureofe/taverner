/*
    TAVERNER
    By the_adventure_of_e λ
    https://github.com/adventureofe
*/

#ifndef TEXTURE_MANAGER_H
#define TEXTURE_MANAGER_H

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

#include "engine.h"

#define MAX_NAME 50
#define TEXTURE_MAP_SIZE 10

//struct definition
typedef struct Texture_Hash
{
    char name[MAX_NAME];
    SDL_Texture* texture;

    //next pointer to create a linked list at a position (if collisions happen)
    struct Texture_Hash* next;
} Texture_Hash;

//struct definition
typedef struct Texture_Manager
{
    int id;
    bool is_running;
    Texture_Hash* map[TEXTURE_MAP_SIZE];
} Texture_Manager;

//allocate memory for the texture manager and fill it's hashmap with null pointers
Texture_Manager* texture_manager_create(void);
void texture_manager_destroy(Texture_Manager* texture_manager);

// empty hashmap by filling it with null pointers
void texture_manager_init(Texture_Manager* texture_manager);

// hash table print
void texture_manager_print(Texture_Manager* texture_manager);

bool texture_manager_load(Engine* engine,Texture_Manager* texture_manager, char* name, char* filename);
void texture_manager_drop(char* id);
void texture_manager_clean(void);
void texture_manager_draw(Engine* engine, Texture_Manager* texture_manager, char* name, int x, int y, int width, int height, SDL_RendererFlip flip);

#endif
