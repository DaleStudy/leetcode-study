- 문제 : https://leetcode.com/problems/3sum/
- time complexity : O(n^2)
- space complexity : O(1) (결과값을 고려하지 않은 알고리즘 자체의 공간 복잡도)
- 블로그 링크 : https://algorithm.jonghoonpark.com/2024/05/07/leetcode-15

```java
public List<List<Integer>> threeSum(int[] nums) {
    Arrays.sort(nums);

    List<List<Integer>> result = new ArrayList<>();

    int lastOne = Integer.MIN_VALUE;
    for (int i = 0; i < nums.length - 1; i++) {
        int num = nums[i];
        if (lastOne == num) {
            continue;
        }

        twoSum(result, nums, i);
        lastOne = num;
    }

    return result;
}

public void twoSum(List<List<Integer>> result, int[] nums, int targetIndex) {
    int target = -nums[targetIndex];

    int i = targetIndex + 1;
    int j = nums.length - 1;
    while (i < j) {
        int twoSum = nums[i] + nums[j];

        if (target > twoSum) {
            i++;
        }

        if (target < twoSum) {
            j--;
        }

        if (target == twoSum) {
            result.add(List.of(-target, nums[i], nums[j]));
            int current = nums[i];
            while (i < nums.length - 2 && current == nums[i + 1]) {
                i++;
            }
            i++;
        }
    }
}
```
