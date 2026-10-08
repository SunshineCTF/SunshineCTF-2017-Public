#include <stdlib.h>
#include <stdio.h>

int main(int argc, char** argv) {
	(void)argc; (void)argv;
	char buf0[10];
	float var0;
	fgets(buf0, sizeof(buf0), stdin);
	var0 = atof(buf0);
	if (var0 < 37.35928559) {
		printf("Too low just like you're chances of reaching the bottom.\n");
		exit(0);
	}
	
	if (var0 > 37.35928559) {
		printf("Too high just like your hopes of reaching the bottom.\n");
		exit(0);
	}
	else {
		FILE* flag;
		char rflag[50];
		flag = fopen("flag.txt", "r");
		while (fgets(rflag, sizeof(rflag), flag)) {
			printf("%s", rflag);
		}
	}
	return 0;
}
