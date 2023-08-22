/*
    TAVERNER
    By the_adventure_of_e λ
    https://github.com/adventureofe
*/

#ifndef ENGINE_H
#define ENGINE_H

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

#define SCREEN_WIDTH 1600
#define SCREEN_HEIGHT 900

//struct definition
typedef struct Engine
{
    int id;
    bool is_running;

    SDL_Window* window;
    SDL_Renderer* renderer;

} Engine;


//allocate memory for the engine
Engine* engine_create(void);

//update will run continuously in the game loop
void engine_update(void);

//print renderer contents on screen
void engine_render(Engine* engine);

//handle keyboard/mouse events
void engine_event_handler(Engine* engine);

//deallocate memory after use
void engine_destroy(Engine* engine);

#endif
