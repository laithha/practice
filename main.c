/*
Problem 1: Print numbers from 1 to n (input from user)
 /*int num = 0;
    printf("Enter a number to print from 1 to your number: ");
    scanf_s("%d", &num);
    for (int i = 1; i <= num; i++) {
        printf("%d\n", i);
    }
    return 0;

Problem 2: Calculate and print the sum of n numbers (input one by one)
    solution:
    int num = 0;
    int sum = 0;
    int input;

    printf("Enter the number of numbers you want to sum: ");
    scanf_s("%d", &num);

    for (int i = 0; i < num; i++) {
        printf("Enter number %d: ", i + 1);
        scanf_s("%d", &input);
        sum += input;
    }

    printf("The sum is %d\n", sum);

Hints:

Use a for loop for printing

Use input() and int() conversion

Accumulate sum in a variable
*/

#include <stdio.h>

int main() {
/*Ask the user how many numbers they want to sum (read n).

Read n numbers one by one.

Calculate the sum of all those numbers.

Print the final sum.
*/
    int input = 0;
    int var = 0;
    int sum = 0;

    printf("how many numbers do you want: ");
    scanf_s("%d", &input);

    for (int i = 0;i < input;i++) {
        printf("enter number %d:", i + 1);
        scanf_s("%d", &var);
        sum += var;
    }
    printf(" the sum of all of the numbers is %d:", sum);

}
