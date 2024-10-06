#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string text = get_string("Text:  ");

    int letters = count_letters(text);

    int words = count_words(text);

    int sentences = count_sentences(text);

    float index = 0.0588 * ((float) letters / (float) words * 100) - 0.296 * ((float) sentences / (float) words * 100) - 15.8;
    if ((int) round(index) < 1.00)
    {
        printf("Before Grade 1\n");
    }
    else if ((int) round(index) >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", (int) round(index));
    }
}

int count_letters(string text)
{
    int letters = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
        if (isalpha(text[i]))
        {
            letters++;
        }
    return letters;
}

int count_words(string text)
{
    int words = 1;
    for (int i = 0, n = strlen(text); i < n; i++)
        if (isspace(text[i]))
        {
            words++;
        }
    return words;
}

int count_sentences(string text)
{
    int sentences = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
        if (text[i] == '!')
        {
            sentences++;
        }
        else if (text[i] == '?')
        {
            sentences++;
        }
        else if (text[i] == '.')
        {
            sentences++;
        }
    return sentences;
}