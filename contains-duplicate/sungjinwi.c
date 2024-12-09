#include <stdlib.h>
#include <stdbool.h>

int compare(void const *a, void const *b)
{
    return (*(int *)a - *(int *)b);
}

bool containsDuplicate(int* nums, int numsSize) {\
	int	i;

	i = 0;
    qsort(nums, numsSize, sizeof(int), compare);
	while (i < numsSize - 1)
	{
		if (nums[i] == nums[i + 1])
			return (1);
		i++;
	}
	return (0);
}
