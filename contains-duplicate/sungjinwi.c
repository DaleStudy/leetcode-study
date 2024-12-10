#include <stdlib.h>
#include <stdbool.h>

int compare(void const *a, void const *b)
{
    return (*(int *)a - *(int *)b);
}

bool containsDuplicate(int* nums, int numsSize) {
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

/*
	시간 복잡도

	qsort(퀵소트)를 통해 O(n log n)을 한 번 수행 + while문을 한 번 돌아서 O(n)만큼의 복잡도를 가짐

	최종 시간 복잡도 : O(n log n)
	
	============================

	공간 복잡도

	추가적으로 할당하는 메모리가 없으므로 O(1)의 복잡도를 가진다

	최종 공간 복잡도 : O(1)
*/
