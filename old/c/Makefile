CC = clang
CFLAGS = -Wall -Wextra -pedantic -Wno-gnu-statement-expression
SDL = -lSDL2 -lSDL2_image -lsqlite3
EXEC = taverner

output: main.o engine.o texture_manager.o sql_manager.o list.o colour.o element.o species.o move.o name.o
	$(CC) $(CFLAGS) $(SDL) main.o engine.o texture_manager.o sql_manager.o list.o colour.o element.o species.o move.o name.o -o $(EXEC)

main.o: main.c
	$(CC) -c $(CFLAGS) $(SDL) main.c

engine.o: src/core/engine.c headers/core/engine.h
	$(CC) -c $(CFLAGS) $(SDL) ./src/core/engine.c

texture_manager.o: src/core/texture_manager.c headers/core/texture_manager.h
	$(CC) -c $(CFLAGS) $(SDL) ./src/core/texture_manager.c

sql_manager.o: src/sql/sql_manager.c headers/sql/sql_manager.h
	$(CC) -c $(CFLAGS) $(SDL) ./src/sql/sql_manager.c

list.o: src/data/list.c headers/data/list.h
	$(CC) -c $(CFLAGS) $(SDL) ./src/data/list.c

colour.o: src/data/colour.c headers/data/colour.h
	$(CC) -c $(CFLAGS) $(SDL) ./src/data/colour.c

element.o: src/data/element.c headers/data/element.h
	$(CC) -c $(CFLAGS) $(SDL) ./src/data/element.c

species.o: src/data/species.c headers/data/species.h
	$(CC) -c $(CFLAGS) $(SDL) ./src/data/species.c

move.o: src/data/move.c headers/data/move.h
	$(CC) -c $(CFLAGS) $(SDL) ./src/data/move.c

name.o: src/data/name.c headers/data/name.h
	$(CC) -c $(CFLAGS) $(SDL) ./src/data/name.c

clean:
	rm *.o taverner
