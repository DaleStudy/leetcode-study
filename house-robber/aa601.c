int rob(int* nums, int numsSize) {
	int	*dp;
	int	max;
	int	i;
	int	j;

	// dp에 nums 복사
	dp = malloc(sizeof(int) * numsSize);
	if (!dp)
		return (0);
	i = -1;
	while (++i < numsSize) {
		dp[i] = nums[i];
    }
	
	// dp 시작
	i = 0;
	j = 0;
	while (++i < numsSize) {
		j = 0;
		max = dp[i];
		while (j + 1 < i) {
			if (max < dp[i] + dp[j])
				max = dp[i] + dp[j];
			++j;
		}
		dp[i] = max;
	}

	// dp 배열의 최종 max값 리턴
	i = -1;
	max = dp[0];
	while (++i < numsSize) {
		if (max < dp[i])
			max = dp[i];
	}
    free(dp);
	return (max);
}

