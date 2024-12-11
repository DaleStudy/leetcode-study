#include <stdio.h>
#include <stdbool.h>

void	merge(int *nums, int left, int mid, int right)
{
	int	i;
	int	j;
	int	k;
	int	leftArr[mid - left + 1];
	int	rightArr[right - mid];

	i = -1;
	while (++i < mid - left + 1) // 왼쪽 분할된 부분 넣기
		leftArr[i] = nums[left + i];
	i = -1;
	while (++i < right - mid) // 오른쪽 분할된 부분 넣기
		rightArr[i] = nums[mid + i + 1];
	i = 0;
	j = 0;
	k = left; // **** nums배열인덱스 => left부터 시작
	// 나누어진 배열끼리 비교해서 nums배열 재배치
	while ((i < mid - left + 1) && (j < right - mid)) {
		if (leftArr[i] <= rightArr[j])
			nums[k] = leftArr[i++];
		else
			nums[k] = rightArr[j++];
		++k;
	}
	while (i < mid - left + 1) // left배열 남아있으면 마저 삽입
		nums[k++] = leftArr[i++];
	while (j < right - mid) // right배열 남아있으면 마저 삽입
		nums[k++] = rightArr[j++];
}

void	mergeSort(int *nums, int left, int right) {
	int	mid;

	if (left < right)
	{
		mid = (left + right) / 2;
		mergeSort(nums, left, mid); // 왼쪽분할
		mergeSort(nums, mid + 1, right); // 오른쪽분할
		merge(nums, left, mid, right);
	}
}

// void	printArr(int *arr, int size) {
// 	int	i;

// 	i = -1;
// 	while (++i < size)
// 		printf("%d ", arr[i]);
// }

bool containsDuplicate(int* nums, int numsSize) {
	int	i;

	mergeSort(nums, 0, numsSize - 1);
	i = -1;
	while (++i + 1 < numsSize) {
		if (nums[i] == nums[i + 1])
			return (true);
	}
	return (false);
}

int main()
{
	int arr[] = {0, 3, 0};
	int size;

	size = sizeof(arr) / sizeof(arr[0]);
	printf("%d\n", containsDuplicate(arr, size));
}
