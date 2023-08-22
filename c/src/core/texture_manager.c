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

#include "../../headers/core/engine.h"
#include "../../headers/core/texture_manager.h"

//Generate hash value by summing ascii characters
unsigned int hash(char* name)
{
    int length = strnlen(name, MAX_NAME);

    unsigned int hash_value = 0;

    for(int i = 0; i < length; i++)
    {
        hash_value += name[i];

        //times by char to make more random and then modulus by table_size so it fits in hash table
        hash_value = (hash_value * name[i]) % TEXTURE_MAP_SIZE;
    }
    return hash_value;
}

// empty table by filling it with null pointers
void texture_manager_init(Texture_Manager* texture_manager)
{
    for(int i = 0; i < TEXTURE_MAP_SIZE; i++)
    {
        texture_manager->map[i] = NULL;
    }
}

void texture_manager_print(Texture_Manager* texture_manager)
{
    for(int i = 0; i < TEXTURE_MAP_SIZE; i++)
    {
        if(texture_manager->map[i] == NULL)
        {
            printf("\t%i\t~\n", i);
        }
        else
        {
            Texture_Hash *tmp = texture_manager->map[i];
            while(tmp != NULL)
            {
                printf("\t%i\t%s -> ", i, tmp->name);
                tmp = tmp->next;
            }
            printf("\n");
        }
    }
}

bool texture_manager_insert(Texture_Manager* texture_manager, Texture_Hash* texture_hash)
{

    //null check
    if(texture_hash == NULL)
    {
        return false;
    }

    //compute hash function
    int index = hash(texture_hash->name);

    texture_hash->next = texture_manager->map[index];
    texture_manager->map[index] = texture_hash;

    return true;
}

//allocate memory for the texture manager and fill it's hashmap with null pointers
Texture_Manager* texture_manager_create(void)
{
    Texture_Manager* texture_manager = (Texture_Manager*) malloc(sizeof(Texture_Manager));
    texture_manager_init(texture_manager);
    return texture_manager;
}

bool texture_manager_load(Engine* engine, Texture_Manager* texture_manager, char* name, char* file_name)
{
    SDL_Surface* surface = IMG_Load(file_name);
    if(surface == NULL)
    {
        SDL_Log("Failed to load %s %s\n", file_name, SDL_GetError());
        return false;
    }

    SDL_Texture* texture = SDL_CreateTextureFromSurface(engine->renderer, surface);
    if(texture == NULL)
    {
        SDL_Log("Failed to create texture %s \n", SDL_GetError());
        return false;
    }

    Texture_Hash* texture_hash = (Texture_Hash*) malloc(sizeof(Texture_Hash));
    strcpy(texture_hash->name, name);
    texture_hash->texture = texture;

    //insert record into hash table
    texture_manager_insert(texture_manager, texture_hash);
    return true;
}

/*
void texture_manager_draw(Engine* engine, Texture_Manager* texture_manager, char* id, int x, int y, int width, int height, SDL_RendererFlip flip)
{
    int placeholder_hash_id = 0;
    SDL_Rect src_rect = {0, 0, width, height};
    SDL_Rect des_rect = {x, y, width, height};
    SDL_RenderCopyEx(engine->renderer, placeholder_hash_id, &src_rect, &des_rect, 0, NULL, flip);
}
*/

void texture_manager_destroy(Texture_Manager* texture_manager)
{
    free(texture_manager);
}
