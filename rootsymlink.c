#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void main(int argc, char *argv[]) {
  if (argc != 3) {
    printf("%s %s %s", "Usage: ", argv[0], " [source] [dest]\nCreates a symbolic link\n");
  } else {
    remove(argv[2]);
    symlink(argv[1], argv[2]);
  }
}
