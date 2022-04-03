#include <stdlib.h>
#include <stdio.h>

void main(int argc, char* argv[]) {
  int percentage = atoi(argv[1]);
  int total = atoi(argv[2]);
  double ret = ((double) percentage)/100 * total;
  printf("%d", (int) ret);
}
