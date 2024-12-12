class Solution {
    public boolean isPalindrome(String s) {

        // 문자열 s의 대문자를 소문자로 치환한다.
        String lowerCase = s.toLowerCase();
        // 소문자 a-z, 숫자 0-9에 해당하지 않는 문자를 지운다.
        String alphanumeric = lowerCase.replaceAll("[^a-z0-9]", "");
        // 뒤집은 문자열을 만든다.
        String reverse = new StringBuilder(alphanumeric).reverse().toString();
        // 두 문자열을 비교한다.
        boolean isEqual = alphanumeric.equals(reverse);
        
        return isEqual;
    }
}