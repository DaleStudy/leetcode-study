class Solution {
    /*
     * 초반 풀이 시 while문 내에서 left<right 미체크로 오류 / 조건 추가
     * 중복 while문 사용하지 않는 방법이 있는지 고민
     * 
     * 시간복잡도 : O(n)
     */
    public boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length()-1;

        while(left < right) {
            while(left<right && !Character.isLetterOrDigit(s.charAt(left))) {
                left++;
            }
            while(left<right && !Character.isLetterOrDigit(s.charAt(right))) {
                right--;
            }

            if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) {
                return false;
            }
            
            left++;
            right--;
        }
        return true;
    }
}

