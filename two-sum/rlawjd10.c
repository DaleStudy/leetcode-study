int compare(const void* a, const void* b) { 
    return (*(int*)a - *(int*)b); // 오름차순
} 

bool containsDuplicate(int* nums, int numsSize) {
    qsort(nums, numsSize, sizeof(int), compare);

    for (int i = 1; i < numsSize; i++) {
        if (nums[i] == nums[i-1])
            return 1;
    }
    return 0;
}
