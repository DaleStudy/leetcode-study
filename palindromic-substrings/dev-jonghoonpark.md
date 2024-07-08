- 문제: https://leetcode.com/problems/palindromic-substrings/
- 풀이: https://algorithm.jonghoonpark.com/2024/07/08/leetcode-647

```java
class Solution {
    public int countSubstrings(String s) {
        int count = 0;

        char[] charArray = s.toCharArray();
        for (int i = 0; i < s.length(); i++) {
            char currentChar = charArray[i];
            count++;

            int left = i;
            int right = i;

            while (right < s.length() - 1 && currentChar == charArray[right + 1]) {
                right++;
                count++;
            }

            while (left > 0 && right < s.length() - 1 && charArray[left - 1] == charArray[right + 1]) {
                left--;
                right++;
                count++;
            }
        }

        return count;
    }
}
```

### TC, SC

시간 복잡도는 평균적으로 O(n)이다. palindrome 의 길이가 n 에 가까워질수록 시간 복잡도는 O(n^2) 에 가까워 진다.
공간 복잡도는 O(n)이다.
