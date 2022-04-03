#include <stdio.h>
#include <stdlib.h>

void die(char *progname) {
  printf("Usage: %s (Two of:) -t <total> -f <fraction> -p <part>\n", progname);
  exit(1);
}

void main(int argc, char *argv[]) {
  double total = -1.0;
  double fraction = -1.0;
  double part = -1.0;
  char integers = 0;

  if (argc < 5) {
    die(argv[0]);
  }
  
  for (int i = 0; i < argc ; i++) {
    if (argv[i][0] == '-') {
      switch (argv[i][1]) {
      case 't': total = atoi(argv[i+1]); break;
      case 'f': fraction = atoi(argv[i+1]); break;
      case 'p': part = atoi(argv[i+1]); break;
      case 'i': integers = 1; break;
      }
    }
  }

  printf("%d %d %d\n", total, fraction, part);
  double ret;
  fraction = integers ? fraction / 100 : fraction;
  if (total == -1.0) {
    ret = part * (1/fraction);
  } else if (fraction == -1.0) {
    ret = part / total;
  } else if (part == -1.0) {
    ret = fraction * total;
  } else {
    die(argv[0]);
  }
  printf("%d\n", integers ? (int) ret : ret);
}

