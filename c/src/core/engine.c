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

#include "../../headers/core/engine.h"

//allocate memory for the engine
Engine* engine_create(void)
{
    Engine* engine = (Engine*) malloc(sizeof(Engine));

    //attempt to initialise SDL library
    if(SDL_Init(SDL_INIT_EVERYTHING) != 0)
    {
        SDL_Log("ERROR: SDL failed to initialise: %s\n", SDL_GetError());
        return NULL;
    }
    else
    {
        SDL_Log("SDL initialised Successfully\n");
        engine->is_running = true;

        //attempt to create window
        engine->window = SDL_CreateWindow("Taverner", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, SCREEN_WIDTH, SCREEN_HEIGHT, 0);
        if(engine->window == NULL)
        {
             SDL_Log("ERROR: failed to create SDL WINDOW: %s\n", SDL_GetError());
             return NULL;
        }
        else
        {
            SDL_Log("SDL WINDOW was created Successfully\n");

            //attempt to create renderer
            engine->renderer = SDL_CreateRenderer(engine->window, -1, SDL_RENDERER_ACCELERATED);

            if(engine->window == NULL)
            {
                SDL_Log("ERROR: failed to create SDL RENDERERe: %s\n", SDL_GetError());
                return NULL;
            }
            else
            {
                SDL_Log("SDL RENDERER was created Successfully\n");
            }
        }
    }
    return engine;
}

//update will run continuously in the game loop
void engine_update(void)
{
  //printf("u");
}

//printer renderer contents on screen
void engine_render(Engine* engine)
{
    SDL_SetRenderDrawColor(engine->renderer, 0, 0, 255, 255);

    //must clear renderer before presenting
    SDL_RenderClear(engine->renderer);

    SDL_RenderPresent(engine->renderer);

}

//handle keyboard/mouse events
void engine_event_handler(Engine* engine)
{
    SDL_Event event;
    SDL_PollEvent(&event);
    switch(event.type)
    {
        case SDL_QUIT:
            engine->is_running = false;
            break;
    }

}

//deallocate memory after use
void engine_destroy(Engine* engine)
{
    SDL_DestroyWindow(engine->window);
    SDL_DestroyRenderer(engine->renderer);
    free(engine);
}

