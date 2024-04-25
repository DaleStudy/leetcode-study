- https://leetcode.com/problems/valid-anagram/
- time complexity : O(nlogn)
- space complexity : O(n)
- https://algorithm.jonghoonpark.com/2024/04/24/leetcode-242

```java
import java.util.Arrays;

class Solution {
    public boolean isAnagram(String s, String t) {
        char[] temp1 = s.toCharArray();
        char[] temp2 = t.toCharArray();
        Arrays.sort(temp1);
        Arrays.sort(temp2);
        return Arrays.equals(temp1, temp2);
    }
}
```
