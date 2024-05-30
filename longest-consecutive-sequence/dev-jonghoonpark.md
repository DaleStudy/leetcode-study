- 문제 : https://leetcode.com/problems/longest-consecutive-sequence/
- time complexity : O(n)
- space complexity : O(n)
- 블로그 링크 : https://algorithm.jonghoonpark.com/2024/05/28/leetcode-128

```java
public int longestConsecutive(int[] nums) {
    Set<Integer> set = new HashSet<>();

    for(int num : nums) {
        set.add(num);
    }

    int max = 0;
    for(int num : set) {
        if (!set.contains(num - 1)) {
            int current = 1;
            while (set.contains(num + 1)) {
                current++;
                num++;
            }
            max = Math.max(current, max);
        }
    }

    return max;
}
```
