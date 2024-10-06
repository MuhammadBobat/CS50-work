#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int n;
    do
    {
        n = get_int("Height of pyramid:");
    }
    while (n < 1 || n > 8);

    for (int i = 0; i < n; i++)
    {
        for (int g = n - 1; g > i; g--)
        {
            printf(" ");
        }
        for (int j = -1; j < i; j++)
        {
            printf("#");
        }
        printf("\n");
    }

}