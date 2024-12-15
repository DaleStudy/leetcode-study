#include <stdlib.h>
#include <stdio.h>

/*
	시간복잡도

		이중for문
		=> O(N^2)

	공간복잡도

		dp만큼 malloc
		=> O(N)
*/

int rob(int* nums, int numsSize) {
    int *dp;
	int	max_before;
	int	max = 0;

	dp = malloc(numsSize * sizeof(int));
	for (int i = 0; i < numsSize; i++)
	{
		max_before = 0;
		for (int j = 0; j < i - 1; j++)
			if (dp[j] > max_before)
				max_before = dp[j];
		dp[i] = nums[i] + max_before;
	}
	for (int i = 0; i < numsSize; i++)
		if (dp[i] > max)
			max = dp[i];
	free(dp);
	return (max);
}
