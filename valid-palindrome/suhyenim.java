/* [5th/week03] 125. Valid Palindrome

1. 문제 요약
링크: https://leetcode.com/problems/valid-palindrome/description/
주어진 문자열에서 대->소문자 & 숫자만 남겼을 때, 앞으로 읽어도 뒤에서 읽어도 동일한 문자열이면 true 반환

2. 문제 풀이
제출1: 소문자와 숫자만 남긴 새로운 문자열 만들고 -> 양끝에서 안쪽으로 문자 비교
성공: 시간 복잡도는 O(n), 공간 복잡도는 O(n)
=> Time: 2 ms (98.53%), Space: 45.3 MB (19.59%)

class Solution {
    public boolean isPalindrome(String s) {
        List<Integer> arr = new ArrayList<>();
        for (char c : s.toCharArray()) {
            if (c >= 'A' && c <= 'Z') {
                c = (char)(c + 32);
                arr.add((int)c);
            }
            else if ((c >= 'a' && c <= 'z') || (c >= '0' && c <= '9')) {
                arr.add((int)c);
            }
        }
        for (int i = 0; i < arr.size() / 2; i++) {
            if (arr.get(i) != arr.get(arr.size() - 1 - i)) {
                return false;
            }
        }
        return true;
    }
}

풀이2: 제출1과 로직 동일하지만 공간 복잡도 낮춤 (새로운 문자열 생성 안하고 진행하기 때문)
성공: 시간 복잡도는 O(n), 공간 복잡도는 O(1)
=> Time: 2 ms (98.59%), Space: 45.4 MB (14.48%)

class Solution {
    public boolean isPalindrome(String s) {
        int low = 0;
        int high = s.length() - 1;
        while (low < high) {
            while (low < high && !Character.isLetterOrDigit(s.charAt(low))) {
                low++;
            }
            while (low < high && !Character.isLetterOrDigit(s.charAt(high))) {
                high--;
            }
            if (Character.toLowerCase(s.charAt(low)) != Character.toLowerCase(s.charAt(high))) {
                return false;
            }
            low++;
            high--;
        }
        return true;
    }
}


3. TIL
아스키 코드 정리
- 대문자: A(65) ~ Z(90)
- 소문자: a(97) ~ z(122)
- 숫자: 0(48) ~ 9(57)

*/

class Solution {
    public boolean isPalindrome(String s) {
        List<Integer> arr = new ArrayList<>();
        for (char c : s.toCharArray()) {
            if (c >= 'A' && c <= 'Z') {
                c = (char)(c + 32);
                arr.add((int)c);
            }
            else if ((c >= 'a' && c <= 'z') || (c >= '0' && c <= '9')) {
                arr.add((int)c);
            }
        }
        for (int i = 0; i < arr.size() / 2; i++) {
            if (arr.get(i) != arr.get(arr.size() - 1 - i)) {
                return false;
            }
        }
        return true;
    }
}
