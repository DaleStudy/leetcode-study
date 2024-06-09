- 문제: https://leetcode.com/problems/longest-substring-without-repeating-characters/
- time complexity : O(n)
- space complexity : O(n)
- 블로그 주소 : https://algorithm.jonghoonpark.com/2024/02/18/leetcode-3

```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.isEmpty()) {
            return 0;
        }

        Set<Character> set = new HashSet<>();
        int pointer = 0;
        int longest = 0;

        while (pointer < s.length()) {
            char _char = s.charAt(pointer);
            while (set.contains(_char)) {
                set.remove(s.charAt(pointer - set.size()));
            }
            set.add(_char);
            longest = Math.max(longest, set.size());
            pointer++;
        }

        return longest;
    }
}
```

## TC 추가 설명

내부 while이 있지만 O(n)으로 적을 수 있는 이유는 hashset의 경우 search 하는데 드는 비용이 O(1) 이기 때문이다.
