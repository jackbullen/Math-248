#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <stdio.h>

#define MESH_SIZE 9999999

int main() {
    srand(time(0)); // seed the random number generator
    int tally = 0;
    for(int i = 0; i < MESH_SIZE; i++) {
        double x = (double)rand()/RAND_MAX*2.0 - 1.0;
        double y = (double)rand()/RAND_MAX*2.0 - 1.0;
        double z = (double)rand()/RAND_MAX*2.0 - 1.0;
        if(x*x + y*y + z*z < 1) {
            tally++;
        }
    }
    double result = (double)tally / MESH_SIZE * 8;
    printf("%f\n", result);
    return 0;
}