/**
 [문제풀이]
 - 대문자 -> 소문자 변환
 - 소문자가 아닌 문자면 넘어가고, 소문자만 체크
 - 숫자는 넘어갈 수 없다.
 - 소문자 input, reverse input 비교

 - 풀이1
 time: O(N), space: O(1)
 class Solution {
 public boolean isPalindrome(String s) {
 if (s.trim().length() == 0) {
 return true;
 }

 s = s.toLowerCase();
 int left = 0;
 int right = s.length() - 1;
 while (left < right) {
 while (left < right && !Character.isLetterOrDigit(s.charAt(left))) {
 left++;
 }
 while (left < right && !Character.isLetterOrDigit(s.charAt(right))) {
 right--;
 }

 if (s.charAt(left) != s.charAt(right)) {
 return false;
 }
 left++;
 right--;
 }
 return true;
 }
 }

 - 풀이2
 time: O(N), space: O(1)

 [회고]
 중간에 공백을 replace하면 안좋을 것 같은데..
 -> 알파벳인지를 비교해서 인덱스를 바꾸자!

 for문만 고집하지 말고, while문도 사용해보자!
 (처음에 for문으로 풀다가 스파게티가 되어버렸ㄷ..)

 !!! String.toLowerCase() 로 소문자로 변환하는 것이 좋은 방법일까?? !!!
 */

class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        int left = 0;
        int right = s.length() - 1;
        while (left < right) {
            if (!Character.isLetterOrDigit(s.charAt(left))) {
                left++;
                continue;
            }
            if (!Character.isLetterOrDigit(s.charAt(right))) {
                right--;
                continue;
            }

            if (s.charAt(left) != s.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
