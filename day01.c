#include <stdio.h>
#include <stdlib.h>

#define BUFFER 16384
int main(void)
{
    FILE *f = fopen("inp.txt", "r");

    if (f == NULL)
    {
        printf("Could not open file\n");
        return 1;
    }

    int first_neg_i = 1, found = 0, floor = 0, matched;
    char c;

    while ((c = fgetc(f)) != EOF)
    {
        switch (c)
        {
        case '(':
            floor++;
            break;
        case ')':
            floor--;
            break;
        }

        if (!found && floor >= 0)
        {
            first_neg_i++;
        }
        else
        {
            found = 1;
        }
    }

    printf("Floor: %d Negative floor index: %d\n", floor, first_neg_i);
}