class Solution {
    public String longestPalindrome(String s) {
        /**
        1.문제: 가장 긴 팰린드롬 string 찾기.
        2.조건: 
        - s 문자열 길이 최소 1, 최대 1000
        - 답이 1개가 아닐수도있음. 여러개중 1개만 반환해도 ok
        - s 는 digit, English letters 로 구성
        3.풀이
        - stack 사용 -> TLE 발생
        - expand around center (각 중심에서 양쪽으로 확장하여 체크)
        - 길이 = 1 이면 바로 return
        Palindrome은 substring 기준이라 전체 문자열 길이와 무관하게 홀수/짝수 케이스가 모두 존재할 수 있기 때문에, 두 경우를 모두 확인해야 합니다.

        Time: O(n²) -> palindrome method 에서 최대 n 번 돌 수 있으므로
        Space: O(1)
         */
    
        int n = s.length();
         if(n == 1) return s;
         //가운데 문자에서 시작 e.g "babad" n = 5, answer = "b"
         String answer = "";
         
        for(int i = 0; i < n; i++) {
            //홀수 e.g "b". 중심이 1개
            String odd = palindrome(s, i, i);
            //짝수 e.g. "ab". 중심이 2개
            String even = palindrome(s, i, i + 1);

            String longer = odd.length() > even.length() ? odd : even;
            if(longer.length() > answer.length()) {
                answer = longer;
            }
        }
        return answer;
    }
    String palindrome(String s, int start, int end) {
        while(start >= 0 && end < s.length() && s.charAt(start) == s.charAt(end)) {
            start--;
            end++;
        }
        return s.substring(start+1, end);
    }
}
