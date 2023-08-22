/*
    TAVERNER
    By the_adventure_of_e λ
    https://github.com/adventureofe

    With help from Madsycode's C++ SDL 2D game Engine tutorial series
    https://www.youtube.com/watch?v=oDIk8EGmDYQ&list=PL-K0viiuJ2RctP5nlJlqmHGeh66-GOZR_&index=4
    adapted to use C

    TODO: waaay to much stuff going on in this main file that has to be stored elsewhere
*/

#include <stdio.h>
#include <stdlib.h>
#include <SDL2/SDL.h>
#include <SDL2/SDL_image.h>
#include <stdbool.h>
#include <sqlite3.h>
#include <string.h>

#include "headers/core/engine.h"
#include "headers/core/texture_manager.h"

#include "headers/sql/sql_manager.h"

#include "headers/data/list.h"

#include "headers/data/colour.h"
#include "headers/data/element.h"
#include "headers/data/species.h"
#include "headers/data/move.h"
#include "headers/data/name.h"

// print all included cmd args (removes unused variable warning)
void arg_print(int argc, char** argv)
{
    for(int i = 1; i < argc; i++)
    {
        printf("arg[%d]: %s", i, argv[i]);
    }
    if(argc > 1)
    {
        printf("\n");
    }
}

//code for creating a rect
/*
SDL_SetRenderDrawColor(*renderer, 255, 255, 255, 255);
SDL_Rect rect = {20, 20, 20, 20};
SDL_RenderFillRect(*renderer, &rect);
*/

int main(int argc, char **argv)
{
    arg_print(argc, argv);

    /* create SQL manager */
    Sql_Manager* sql_manager = sql_manager_create();

    List* colour_list = list_create(sizeof(Colour));
    list_populate(sql_manager, colour_list, "colour", colour_callback);
    //list_print(colour_list);

    List* element_list = list_create(sizeof(Element));
    list_populate(sql_manager, element_list, "element", element_callback);
    //list_print(element_list);

    List* species_list = list_create(sizeof(Species));
    list_populate(sql_manager, species_list, "species", species_callback);
    //list_print(species_list);

    List* move_list = list_create(sizeof(Move));
    list_populate(sql_manager, move_list, "move", move_callback);
    //list_print(move_list);

    List* name_list = list_create(sizeof(Name));
    list_populate(sql_manager, name_list, "name", name_callback);
    list_print(name_list);

    //setting up SDL2
    Engine* engine = engine_create();
    Texture_Manager* texture_manager = texture_manager_create();

    texture_manager_load(engine, texture_manager, "cobra", "../assets/faces/reptile/cobra/cobra_01.jpg");
    texture_manager_load(engine, texture_manager, "avocet", "../assets/faces/bird/avocet/avocet_01.jpg");
    texture_manager_load(engine, texture_manager, "dragon", "../assets/faces/reptile/dragon/dragon_01.jpg");
    texture_manager_load(engine, texture_manager, "penguin", "../assets/faces/bird/penguin/penguin_01.jpg");
    texture_manager_load(engine, texture_manager, "snake", "../assets/faces/reptile/snake/snake_01.jpg");
    texture_manager_load(engine, texture_manager, "anteater", "../assets/faces/mammal/anteater/anteater_01.jpg");
    texture_manager_load(engine, texture_manager, "badger", "../assets/faces/mammal/badger/badger_01.jpg");
    texture_manager_print(texture_manager);

/*
    //game loop
    while(engine->is_running == true)
    {
        engine_update();
        engine_render(engine);
        engine_event_handler(engine);
    }
*/


    //clean up
    engine_destroy(engine);
    texture_manager_destroy(texture_manager);
    return EXIT_SUCCESS;
}
