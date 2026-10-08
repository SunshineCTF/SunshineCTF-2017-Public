#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>

struct nova {
	char pulsar[50];
	int cluster;
	int *ion;
};

static int rand_fd;
static int moar_rand(void) {
	int ret;
	if(read(rand_fd, &ret, sizeof(&ret)) != sizeof(&ret)) {
		abort();
	}
	return ret;
}

int main(int argc, char** argv) {
	(void)argc; (void)argv;
	int solar_wind;
	
	rand_fd = open("/dev/urandom", O_RDONLY);
	
	struct nova *centari, *castor, *vega;
	
	centari = malloc(sizeof(struct nova));
	centari->ion = malloc(9);
	centari->cluster = 0;
	
	castor = malloc(sizeof(struct nova));
	castor->ion = malloc(9);
	castor->cluster = 0;
	
	
	vega = malloc(sizeof(struct nova));
	vega->ion = malloc(9);
	vega->cluster = 0;
	
	printf("%p\n", centari->ion);
	centari->cluster = moar_rand() & 0x7fffffff;
	solar_wind = centari->cluster;
	
	free(centari->ion);
	centari->ion = NULL;
	
	free(centari);
	centari = NULL;
	
	fgets((char*)castor->ion, 100, stdin);
	
	if (*vega->ion == solar_wind) {
		char rflag[50];
		FILE* flag = fopen("flag.txt", "r");
		if(!flag) {
			perror("flag.txt");
			abort();
		}
		
		while (fgets(rflag, sizeof(rflag), flag)) {
			printf("%s", rflag);
		}
	}
	else {
		printf("You see %d at %p.\n", *vega->ion, vega->ion);
	}
	return 0;
}
