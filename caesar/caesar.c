#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>


int main(int argc, string argv[])
{
    if (argc == 2)
    {
        bool digit_check = false;

        int k = atoi(argv[1]);

        for (int i = 0; i < strlen(argv[1]); i++)
        {
            if (isdigit(argv[1][i]))
            {
                digit_check = true;
            }
            else
            {
                printf("Usage: ./caesar key\n");
                return 1;
            }
        }

        if (digit_check == true)
        {
            string input = get_string("plaintext: ");
            for (int i = 0; i < strlen(input); i++)
            {
                if (isupper(input[i]))
                {
                    input[i] = ((input[i] - 65 + k) % 26) + 65;
                }
                else if (islower(input[i]))
                {
                    input[i] = ((input[i] - 97 + k) % 26) + 97;
                }
            }
            printf("ciphertext: %s", input);
            printf("\n");
            return 0;
        }
    }
    else
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
}