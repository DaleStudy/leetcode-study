class Solution {
    public int countSubstrings(String s) {
        // 해당 substring 을 했을 때, 몇 개의 palidrome 이 존재하는 가 ?
        int answer = 0;

        for ( int lt = 0; lt < s.length(); lt++){
            for ( int rt = lt+1; rt <= s.length(); rt++){
                String curStr = s.substring(lt,rt);
                if (validatePalindrome(curStr)){
                    answer++;
                }
            }

        }
        return answer;
    }

    private boolean validatePalindrome(String s){
        int len = s.length();
        for ( int i = 0; i < len/2; i++){
            if ( s.charAt(i) != s.charAt(len -i -1)){
                return false;
            }
        }

        return true;
    }
}
