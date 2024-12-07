class Solution {
    public boolean isPalindrome(String s) {
        //정규식으로 영문,숫자 아닌 경우 "" 치환
        //StringBuilder를 통해 문자열 가공
        //거꾸로 뒤집은 것과 원래의 문자열이 일치할 경우 팰린드롬
        s = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        StringBuilder sb = new StringBuilder(s);
        if(sb.reverse().toString().equals(s)){
            return true;
        }

        return false;
    }
}


