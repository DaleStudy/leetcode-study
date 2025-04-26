
// NOTE: 팰린드롬은 알파벳 소문자와 "숫자" 까지 포함하는듯 하다.
// O(n) 알고리즘.
import java.util.stream.Collectors;

class Solution {
    public boolean isPalindrome(String s) {

        String filtered = s.chars()
        .filter(Character::isLetterOrDigit)
        .mapToObj(c -> String.valueOf((char) c))
        .map(String::toLowerCase)
        .collect(Collectors.joining());

        char[] cArr = filtered.toCharArray();

        int startIdx = 0;
        int endIdx = cArr.length - 1;
    
        while(startIdx < endIdx) {
            if(cArr[startIdx] != cArr[endIdx]) {
                return false;
            }
            
            startIdx++;
            endIdx--;
        }

        return true;
    }
}
