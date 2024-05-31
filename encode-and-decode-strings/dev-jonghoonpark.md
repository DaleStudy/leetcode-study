- 문제
  - 유료 : https://leetcode.com/problems/encode-and-decode-strings/
  - 무료 : https://www.lintcode.com/problem/659/
- time complexity : O(n)
- space complexity : O(n \* m), m은 각 문자열 길이의 평균
- 블로그 링크 : https://algorithm.jonghoonpark.com/2024/05/29/leetcode-271

```java
public String encode(List<String> strs) {
    StringBuilder sb = new StringBuilder();
    for (String str : strs) {
        sb.append(str.replace("%", "%25").replace(",", "%2C")).append(",");
    }
    return sb.length() > 0 ? sb.toString() : "";
}

public List<String> decode(String str) {
    List<String> decodedList = new ArrayList<>();
    if (str.length() > 0) {
        int commaIndex = str.indexOf(",");
        while (commaIndex > -1) {
            decodedList.add(str.substring(0, commaIndex).replace("%2C", ",").replace("%25", "%"));
            str = str.substring(commaIndex + 1);
            commaIndex = str.indexOf(",");
        }
    }
    return decodedList;
}
```
