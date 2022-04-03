#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))
#define USAGE 1
#define MEMORY 2

unsigned int max_brightness;
unsigned int current_brightness;
char *max_brightness_file_location = "/sys/class/backlight/intel_backlight/max_brightness";
char *current_brightness_file_location = "/sys/class/backlight/intel_backlight/brightness";
FILE *bf;

void init() {
  FILE *fp = fopen(max_brightness_file_location, "r");
  fscanf(fp, "%d", &max_brightness);
  fclose(fp);
  bf = fopen(current_brightness_file_location, "r+");
  fscanf(bf, "%d", &current_brightness);
  fseek(bf, 0, SEEK_CUR);
}

void deinit() {
    fclose(bf);
}

void set(unsigned int brightness) {
  brightness = MAX(0, MIN(brightness, max_brightness));
  current_brightness = brightness;
  FILE *bf = fopen(current_brightness_file_location, "w");
  fprintf(bf, "%d", brightness);
}

void adjust(char up) {
  int adjust_by = 0;
  if (up) {
    if (current_brightness < 10)
      adjust_by = 1;
    else if (current_brightness == 10) {
      set(100);
      return;
    } else
      adjust_by = 100;
  } else {
    if (current_brightness <= 10)
      adjust_by = 1;
    else if (current_brightness <= 100) {
      set(10);
      return;
    } else
      adjust_by = 100;
  }
  set(up ? current_brightness + adjust_by : current_brightness - adjust_by);
}

void die(unsigned char mode, char *extra) {
  if (mode == USAGE) {
    printf("Usage: %s <up, down, set <number>>\n", extra);
    exit(-1);
  } else if (mode == MEMORY) {
    printf("Out of mem: %s\n", extra);
    exit(-1);
  }
}

void handle_args(int argc, char *argv[]) {
  if (argc == 2) {
    if (!strncmp(argv[1], "up", 2)) {
      adjust(1);
    } else if (!strncmp(argv[1], "down", 4)) {
      adjust(0);
    } else {
      die(USAGE, argv[0]);
    }
  } else if (argc == 3) {
    if (!strncmp(argv[1], "set", 3)) {
      unsigned int arg = atoi(argv[2]);
      set(arg);
    } else {
      die(USAGE, argv[0]);
    }
  } else {
    die(USAGE, argv[0]);
  }
}

void main(int argc, char *argv[]) {
  init();
  handle_args(argc, argv);
  printf("%d %d\n", current_brightness, max_brightness);
  deinit();
}
