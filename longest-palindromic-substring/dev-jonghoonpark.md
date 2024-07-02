- 문제: https://leetcode.com/problems/longest-palindromic-substring/
- 풀이: https://algorithm.jonghoonpark.com/2024/07/01/leetcode-5

## brute force 방식 (beats 12.41%)

```java
class Solution {
    public String longestPalindrome(String s) {
        int start = 0;
        int end = start;

        String max = "";

        char[] charArray = s.toCharArray();
        while (true) {
            if (end == s.length()) {
                break;
            }

            if (charArray[start] == charArray[end]) {
                int tempStart = start;
                int tempEnd = end;

                boolean isPalindrome = true;
                while (tempEnd >= tempStart) {
                    if (charArray[tempStart] != charArray[tempEnd]) {
                        isPalindrome = false;
                        break;
                    }
                    if (tempStart == tempEnd) {
                        break;
                    }
                    tempStart = tempStart + 1;
                    tempEnd = tempEnd - 1;
                }

                if (isPalindrome) {
                    String temp = s.substring(start, end + 1);
                    if (temp.length() > max.length()) {
                        max = temp;
                    }
                }
            }

            end++;
            if (end == s.length()) {
                start = start + 1;
                end = start;
            }

            if (start == s.length()) {
                break;
            }
        }

        return max;
    }
}
```

### TC, SC

시간 복잡도는 O(n^2)이고, 공간 복잡도는 O(n)이다.

## brute force 방식 개선 (beats 48.52%)

아래 부분이 부분이다.

```java
start = start + 1;
end = start + max.length();
```

다음 end 값을 `start + max.length()` 로 두어 연산을 많이 줄일 수 있었고 꽤 큰 차이가 발생된다.

```java
class Solution {
    public String longestPalindrome(String s) {
        int start = 0;
        int end = start;

        String max = "";

        char[] charArray = s.toCharArray();
        while (start < s.length() && end < s.length()) {
            if (charArray[start] == charArray[end]) {
                int tempStart = start;
                int tempEnd = end;

                boolean isPalindrome = true;
                while (tempEnd >= tempStart) {
                    if (charArray[tempStart] != charArray[tempEnd]) {
                        isPalindrome = false;
                        break;
                    }
                    if (tempStart == tempEnd) {
                        break;
                    }
                    tempStart = tempStart + 1;
                    tempEnd = tempEnd - 1;
                }

                if (isPalindrome) {
                    String temp = s.substring(start, end + 1);
                    if(temp.length() > max.length()) {
                        max = temp;
                    }
                    end = end + 1;
                } else {
                    if (s.indexOf(charArray[start], end) > -1) {
                        end = end + 1;
                    } else {
                        start = start + 1;
                        end = start + max.length();
                    }
                }
            } else {
                end++;
                if (end == s.length()) {
                    start = start + 1;
                    end = start + max.length();
                }

                if (start == s.length()) {
                    break;
                }
            }

            if (end == s.length()) {
                start = start + 1;
                end = start + max.length();
            }
        }

        return max;
    }
}
```

### TC, SC

시간 복잡도는 O(n^2)이고, 공간 복잡도는 O(n)이다.

빅오 표기법 상으로는 동일하나, 실행 시간이 매우 단축되었다.

## best solution (beats 95.84%)

하나의 포인터를 사용하여, 각 문자를 중심으로 Palindrome 이 발생할 수 있는 케이스를 조사한다.

```java
class Solution {
    public String longestPalindrome(String s) {
        String max = "";

        char[] charArray = s.toCharArray();
        for (int i = 0; i < s.length(); i++) {
            char currentChar = charArray[i];
            int left = i;
            int right = i;

            while (right < s.length() - 1 && currentChar == charArray[right + 1]) {
                right++;
            }

            while (left > 0 && right < s.length() - 1 && charArray[left - 1] == charArray[right + 1]) {
                left--;
                right++;
            }

            String temp = s.substring(left, right + 1);
            if (temp.length() > max.length()) {
                max = temp;
            }
        }

        return max;
    }
}
```

### TC, SC

시간 복잡도는 평균적으로 O(n)이다. palindrome 의 길이가 n 에 가까워질수록 시간 복잡도는 O(n^2) 에 가까워 진다.
공간 복잡도는 O(n)이다.

빅오 표기법 상으로도 개선이 된 방식이다. 실제로 시간도 더 단축되었다.
