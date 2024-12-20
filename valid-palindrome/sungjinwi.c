#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <stdbool.h>

/*
	문자열 s의 길이를 N이라고 할 때

	시간복잡도

		for문 두 번 돌려서 2N

		=> N
=================
	공간복잡도
	
		두 번 복사하면서 2N

		=> N
*/

bool isPalindrome(char* s) {
    char    *alnumDup = calloc(strlen(s) + 1, sizeof(char));
    char    *revDup;
    int     j = 0;

    for (int i = 0; s[i]; i++)
    {
        if (isalnum(s[i]))
        {
            alnumDup[j] = tolower(s[i]);
            j++;
        }
    }
    revDup = calloc(strlen(alnumDup) + 1, sizeof(char));
    j = 0;
    for (int i = strlen(alnumDup); i; i--)
        revDup[j++] = alnumDup[i - 1];
    if (strcmp(alnumDup, revDup))
	{
		free(alnumDup);
		free(revDup);
        return (false);
	}
    else
	{
		free(alnumDup);
		free(revDup);
        return (true);
	}
}
