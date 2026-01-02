/**
 * 시간복잡도 : O(n)
 * 공간복잡도 : O(n)
 */
public class kimjunyoung90 {
    public boolean isPalindrome(String s) {
        //1. 대문자를 소문자로 변환
        s = s.toLowerCase();

        //2. 영어 숫자 외 문자 제거
        s = s.replaceAll("[^a-z0-9]", "");

        //3. 앞에서 읽나 뒤에서 읽나 동일한지 확인(pointer 사용)
        int left = 0, right = s.length() - 1;
        while(left < right) {
            char leftChar = s.charAt(left);
            char rightChar = s.charAt(right);
            if(leftChar != rightChar) return false;
            left++;
            right--;
        }
        return true;
    }
}
