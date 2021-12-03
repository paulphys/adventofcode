#include "stdio.h"
#include "string.h"

int main() {
    FILE *file = fopen("input.txt", "r");
    int x,y = 0;
    char line[32] = "";
    while(fgets(line, sizeof(line), file)) {
        char command[32] = "";
        int movement;
        sscanf(line, "%s %d", command, &movement);
        if (strcmp(command, "forward") == 0) {
            x += movement;
        } else if (strcmp(command, "up") == 0) {
            y -= movement;
        } else if (strcmp(command, "down") == 0) {
            y += movement;
        } else {
            return 1;
        }
    }
    printf("Sumbarine position X:%d Y:%d Mul: %d", x, y, x * y);
    fclose(file);
    return 0;
}

