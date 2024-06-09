- 문제: https://leetcode.com/problems/longest-repeating-character-replacement/
- time complexity : O(n)
- space complexity : O(1)
- 블로그 주소 : https://algorithm.jonghoonpark.com/2024/04/29/leetcode-424

```java
class Solution {
    public int characterReplacement(String s, int k) {
        int[] counter = new int[26];
        int countOfMostFrequent = -1;

        int headPointer = 0;
        int tailPointer = 0;

        int maxLength = 0;

        while (headPointer < s.length()) {
            char head = s.charAt(headPointer);
            char tail = s.charAt(tailPointer);
            counter[head - 'A']++;
            headPointer++;

            countOfMostFrequent = Math.max(counter[head - 'A'], countOfMostFrequent);
            while (headPointer - tailPointer > countOfMostFrequent + k) {
                counter[tail - 'A']--;
                tailPointer++;
                tail = s.charAt(tailPointer);
            }

            maxLength = Math.max(maxLength, headPointer - tailPointer);
        }

        return maxLength;
    }
}
```
