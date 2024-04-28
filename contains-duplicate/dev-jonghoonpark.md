- https://leetcode.com/problems/contains-duplicate/
- time complexity : O(n)
- space complexity : O(n)
- https://algorithm.jonghoonpark.com/2024/04/24/leetcode-217

```java
import java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> numSet = new HashSet<>();
        for (int num : nums) {
            if (numSet.contains(num)) {
                return true;
            }
            numSet.add(num);
        }
        return false;
    }
}
```
