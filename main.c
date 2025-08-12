#include <stdio.h>
#include <string.h>

#define TABLE_SIZE 10

struct Person {
    char name[50];
    int age;
};

struct Person hashTable[TABLE_SIZE][50]; // 50 max people per bucket
int bucketCount[TABLE_SIZE] = { 0 };

unsigned int hash(char* name) {
    unsigned int hash = 0;
    for (int i = 0; name[i] != '\0'; i++) {
        hash = hash * 31 + name[i];
    }
    return hash % TABLE_SIZE;
}

int main() {
    while (1) {
        char name[50];
        int age;

        printf("Enter name (or 'exit' to stop): ");
        scanf_s("%49s", name, (unsigned)_countof(name));
        if (strcmp(name, "exit") == 0) break;

        printf("Enter age: ");
        scanf_s("%d", &age);

        unsigned int index = hash(name);
        int count = bucketCount[index];

        if (count < 50) {
            strcpy_s(hashTable[index][count].name, sizeof(hashTable[index][count].name), name);
            hashTable[index][count].age = age;
            bucketCount[index]++;
        }
        else {
            printf("Bucket full! Cannot insert more people.\n");
        }
    }
    return 0;
}
