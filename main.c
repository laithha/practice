#include <stdio.h>

int main() {
    int n = 0;
    int inputNumber = 0;
    int max = 0;

    printf("How many numbers do you want to enter: ");
    scanf_s("%d", &n);

    for (int i = 0; i < n; i++) {
        printf("Enter number %d: ", i + 1);
        scanf_s("%d", &inputNumber);

        if (i == 0 || inputNumber > max) {
            max = inputNumber;
        }
    }

    printf("The largest number is %d\n", max);
    return 0;
}
