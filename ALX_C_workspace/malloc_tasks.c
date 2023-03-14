#include "main.h"
#include <stdlib.h>

/**
 * Comments here for the customized functions below
*/
char *create_array(unsigned int size, char c)
{
    if (size == 0)
        return NULL;

    char *array = malloc(size * sizeof(char));
    if (array == NULL)
        return NULL;

    for (unsigned int i = 0; i < size; i++)
        *array++ = c;

    return array;
}
