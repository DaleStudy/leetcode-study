// 입력된 문자 중 알파벳이나 숫자가 아닌 값들을 하나의 문자열로 만든다.
// 이때 모든 문자들을 소문자로 바꾼다.
// 역정렬한 값과 원래 값을 비교해 팰린드롬 유무를 출력한다.

// 알파벳 혹은 숫자가 아닌지 검사하는 문자 -> charToCheck

// 시간복잡도 : O(n)
// 공간복잡도 : O(n)

class Solution_Gotprgmer {
    public boolean validPalindrome(String s) {
        StringBuilder sb = new StringBuilder();
        for(char charToCheck : s.toCharArray()){
            if(!Character.isLetterOrDigit(charToCheck)){
                continue;
            }
            sb.append(Character.toLowerCase(charToCheck));
        }
        String originalDirection = sb.toString();
        String reDirection = sb.reverse().toString();

        return originalDirection.equals(reDirection);
    }
}
