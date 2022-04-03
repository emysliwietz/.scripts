#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

FILE *f;

void rootwrite(char *filename) {
  char buffer[1024];
  f = fopen(filename, "w");
  while(read(STDIN_FILENO, buffer, 1024) > 0) {
    fprintf(f, "%s", buffer);
  }
  fclose(f);
}

void main(int argc, char *argv[]) {
  if (argc != 2) {
    printf("%s %s %s", "Usage: ", argv[0], " [filename]\nWrites stdin to file\n");
  } else {
    rootwrite(argv[1]);
  }
}
