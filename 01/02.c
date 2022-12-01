#include <stdio.h>
#include <string.h>

void compareCalories (int * top1, int * top2, int * top3, int * currentCalories) {
    if (*currentCalories > *top1) {
        *top3 = *top2;
        *top2 = *top1;
        *top1 = *currentCalories;
    } else if (*currentCalories > *top2) {
        *top3 = *top2;
        *top2 = *currentCalories;
    } else if (*currentCalories > *top3) {
        *top3 = *currentCalories;
    }
}

int main() {
    // FILE *f = fopen("test.txt", "r");
    FILE *f = fopen("input.txt", "r");
    char buf[20];
    int calories;

    int top1 = 0;
    int top2 = 0;
    int top3 = 0;

    int currentCalories = 0;

    while (fgets(buf, 100, f) != NULL) {
        if (strlen(buf) == 1) {
            compareCalories(&top1, &top2, &top3, &currentCalories);
            currentCalories = 0;
        } else {
            sscanf(buf, "%d", &calories);
            currentCalories += calories;
        }

    }
    fclose(f);

    compareCalories(&top1, &top2, &top3, &currentCalories);

    printf("Top 1 calories: %d\n", top1);
    printf("Top 2 calories: %d\n", top2);
    printf("Top 3 calories: %d\n", top3);
    printf("Total calories: %d\n", top1+top2+top3);

    return 0;
}