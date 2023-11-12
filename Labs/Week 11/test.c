#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <stdio.h>

int main(int argc, char *argv[]) {
    // Start measuring time
    clock_t begin = clock();

    // Check if the correct number of arguments is passed
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <dimension>\n", argv[0]);
        return 1;
    }

    // Convert the argument to an integer and check if it's valid
    int dimension = atoi(argv[1]);
    if (dimension < 1) {
        fprintf(stderr, "Error: Dimension must be a positive integer.\n");
        return 1;
    }

    // Initialize random number generator
    srand((unsigned int)time(NULL));

    // Monte Carlo simulation to approximate the volume of the n-ball
    long long int iterations = 10000000;
    long long int tally = 0;
    for (long long int i = 0; i < iterations; i++) {
        double sum = 0.0;
        for (int j = 0; j < dimension; j++) {
            double x = (double)rand() / RAND_MAX * 2.0 - 1.0;
            sum += x * x;
        }
        if (sum < 1.0) {
            tally++;
        }
    }

    // Calculate the result
    double result = (double)tally / iterations * pow(2.0, dimension);
    printf("Volume of a %d-dimensional ball: %f\n", dimension, result);

    // End measuring time and calculate the duration
    clock_t end = clock();
    double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("Execution Time: %.2f seconds\n", time_spent);

    return 0;
}
