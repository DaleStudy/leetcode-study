- 문제: https://leetcode.com/problems/minimum-window-substring/
- 풀이: https://algorithm.jonghoonpark.com/2024/07/29/leetcode-76

## 버전 1

```java
class Solution {
    public String minWindow(String s, String t) {
        if (s.length() < t.length()) {
            return "";
        }

        Map<Character, Integer> counter = new HashMap<>();

        for (int i = 0; i < t.length(); i++) {
            counter.merge(t.charAt(i), 1, Integer::sum);
        }

        int start = 0;

        int minLength = 0;
        int minStart = 0;

        for (int i = 0; i < s.length(); i++) {
            // update counter
            char currentChar = s.charAt(i);

            Integer count = counter.get(currentChar);
            if (count != null) {
                counter.merge(currentChar, -1, Integer::sum);
            } else {
                continue;
            }

            // check all count is 0 -> update min;
            while (validate(counter)) {
                int currentLength = i + 1 - start;
                if (minLength > currentLength || minLength == 0) {
                    minStart = start;
                    minLength = currentLength;
                }

                // try to move start to start + 1
                // increase count if front char exist in counter
                count = counter.get(s.charAt(start));
                if (count != null) {
                    if (count == 0) {
                        break;
                    }

                    counter.put(s.charAt(start), count + 1);
                }
                start++;
            }
        }

        return s.substring(minStart, minStart + minLength);
    }

    private boolean validate(Map<Character, Integer> counter) {
        for (int count : counter.values()) {
            if (count > 0) {
                return false;
            }
        }
        return true;
    }
}
```

### TC, SC

문제에 다음과 같이 제시되어 있다.

```java
m == s.length
n == t.length
```

시간 복잡도는 `O(n * m)`, 공간 복잡도는 `O(n)` 이다.

## 버전 2: 성능 우선 버전

사실 이 버전은 실제 어플리케이션에서는 쓰지 않을지도 모르겠다. 이해하는데 좀 더 시간이 걸릴 것 같기 때문이다.

```java
class Solution {
    public String minWindow(String s, String t) {
        if (s.length() < t.length()) {
            return "";
        }

        Integer[] counter = new Integer[123]; // 적당히 넉넉한 배열 할당

        char[] mustContainCharArray = t.toCharArray();
        for (char mustContainChar : mustContainCharArray) {
            int count = counter[mustContainChar] == null ? 0 : counter[mustContainChar];
            count = count + 1;
            counter[mustContainChar] = count;
        }

        int start = 0;

        int minLength = 0;
        int minLengthFrom = 0;

        for (int i = 0; i < s.length(); i++) {
            char currentChar = s.charAt(i);

            Integer count = counter[currentChar];
            if (count != null) {
                count = count - 1;
                counter[currentChar] = count;
            }

            // check all count is 0 -> update min;
            while (validate(counter)) {
                int currentLength = i + 1 - start;
                if (minLength > currentLength || minLength == 0) {
                    minLengthFrom = start;
                    minLength = currentLength;
                }

                // try to move start to start + 1
                // increase count if front char exist in counter
                count = counter[s.charAt(start)];
                if (count != null) {
                    if (count == 0) {
                        break;
                    }

                    counter[s.charAt(start)] = count + 1;
                }
                start++;
            }
        }

        return s.substring(minLengthFrom, minLengthFrom + minLength);
    }

    private boolean validate(Integer[] counter) {
        for (int i = 65; i < counter.length; i++) { // 65부터 알파벳이 시작하기 때문에 그 이전 값은 의미없다.
            Integer count = counter[i];
            if (count == null) {
                continue;
            }

            if (count > 0) {
                return false;
            }
        }
        return true;
    }
}
```

### TC, SC

문제에 다음과 같이 제시되어 있다.

```java
m == s.length
n == t.length
```

시간 복잡도는 `O(n*m)`, 공간 복잡도는 `O(1)` 이다. 표현상으로는 시간복잡도는 동일하나 실제 실행 시간은 줄어들었고, 공간복잡도는 줄어들게 되었다.
