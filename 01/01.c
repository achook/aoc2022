#include <stdio.h>
#include <string.h>

void compareCalories(int * maxCalories, int * currentCalories) {
    if (*currentCalories > *maxCalories) {
        *maxCalories = *currentCalories;
    }
}

int main() {
    FILE *f = fopen("data.txt", "r");
    char buf[20];
    int calories;

    int maxCalories = 0;
    int currentCalories = 0;

    while (fgets(buf, 100, f) != NULL) {
        if (strlen(buf) == 1) {
            compareCalories(&maxCalories, &currentCalories);
            currentCalories = 0;
        } else {
            sscanf(buf, "%d", &calories);
            currentCalories += calories;
        }

    }
    fclose(f);

    compareCalories(&maxCalories, &currentCalories);

    printf("Max calories: %d\n", maxCalories);

    return 0;
}