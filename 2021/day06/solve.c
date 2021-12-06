#include <stdio.h>
#include <stdint.h>

#define cycle	7
#define life 	9

static uint64_t age[life] = {0};
static uint64_t population(const int days){
    static int day = 0;
    for (; day < days; ++day)
        age[(day + cycle) % life] += age[day % life];
    uint64_t fish = 0;
    for (int i = 0; i < life; ++i)
        fish += age[i];
    return fish;
}

int main(){
    FILE *f = fopen("input.txt", "r");
    int c = ',';
    while (c == ',') {
        age[fgetc(f) - '0']++;
        c = fgetc(f);
    }
    fclose(f);
    printf("Part 1: %llu\n", population(80));
    printf("Part 2: %llu\n", population(256));
    return 0;
}

