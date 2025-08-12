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
/*Read an integer n from input (how many numbers to process).

Read n integers, one by one.

For each number, check if it is odd.

Keep a count of odd numbers.

After processing, print the count.
*/
    int input = 0;
    int count = 0;
    int odd = 0;

    printf("how many numbers do you want: ");
    scanf_s("%d", &input);

    for (int i = 0;i < input;i++) {
        printf("enter number %d:", i + 1);
        scanf_s("%d", &odd);
        if (odd % 2 != 0) {
            count++;
        }
    }
    printf("the number of odd numbers from the list is:%d", 
        count);

}
