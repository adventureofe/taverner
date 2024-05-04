/* By theadventureofe

   main file

   the_adventure_of_e λ */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>
#include <string.h>
#include <time.h>

// print all included cmd args (removes warning)
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

int main(int argc, char** argv)
{
  arg_print(argc, argv);

  printf("Hello, World!\n");
  return EXIT_SUCCESS;
}
