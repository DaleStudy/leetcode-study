- https://leetcode.com/problems/missing-number/
- time complexity : O(n)
- space complexity : O (n)
- https://algorithm.jonghoonpark.com/2024/05/25/leetcode-268

```java
public int missingNumber(int[] nums) {
    int[] counts = new int[nums.length + 1];

    for(int num : nums) {
        counts[num] = 1;
    }

    for(int i = 0; i < counts.length; i ++){
        if(counts[i] == 0) {
            return i;
        }
    }

    return -1;
}
```

등차수열로 푸는 방법도 있는 재밌는 문제.

```java
public int missingNumber(int[] arr) {
    int sum = 0;
    int max = (arr.length * (arr.length + 1)) / 2;
    for (int i = 0; i < arr.length; i++) {
        sum += arr[i];
    }
    return max - sum;
}
```
