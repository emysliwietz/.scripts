#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

char *fanspin_file_location = "/proc/acpi/ibm/fan";
FILE *ff;
char *is_on_file = "/tmp/fanspin";

void toggle() {
	ff = fopen(fanspin_file_location, "w");
	if (access(is_on_file, F_OK) != -1) {
		fprintf(ff, "level auto");
		remove(is_on_file);
		
	} else {
		fprintf(ff, "level full-speed");
		fopen(is_on_file, "w");
	}
	fclose(ff);
}

void main(int argc, char *argv[]) {
  toggle();
}
