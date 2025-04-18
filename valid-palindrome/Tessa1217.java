/** 대문자 문자들을 소문자로 변환하고, 알파벳이 아닌 문자들을 제거했을 때 앞뒤가 똑같이 읽히는 구문을 palindrome이라고 한다.
 주어진 구문이 palindrome인지 여부를 확인하여 boolean 값을 반환하세요.
 */
class Solution {

    // 투 포인터 활용 시간 복잡도: O(n), 공간복잡도: O(n)
    public boolean isPalindrome(String s) {


        int left = 0;
        int right = s.length() - 1;

        while (left < right) {
            // 문자 또는 숫자 아닐 시
            while (left < right && !Character.isLetterOrDigit(s.charAt(left))) {
                left++;
            }
            while (left < right && !Character.isLetterOrDigit(s.charAt(right))) {
                right--;
            }
            // 양 포인터 일치하지 않을 경우 리턴
            if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) {
                return false;
            }

            left++;
            right--;

        }
        return true;
    }

    // char 배열 활용 풀이: 시간 복잡도: O(n), 공간복잡도: O(n)
    // public boolean isPalindrome(String s) {
    //     // non-alphanumeric (숫자 포함 - test case "0P")
    //     char[] convertArr = s.toLowerCase().replaceAll("[^a-z0-9]", "").toCharArray();
    //     int maxIdx = convertArr.length - 1;
    //     for (int i = 0; i <= maxIdx; i++) {
    //         if (convertArr[i] != convertArr[maxIdx - i]) {
    //             return false;
    //         }
    //     }
    //     return true;
    // }

    // StringBuffer reverse() 활용
    // public boolean isPalindrome(String s) {
    //     // non-alphanumeric (숫자 포함 - test case "0P")
    //     String convertedString = s.toLowerCase().replaceAll("[^a-z0-9]", "");
    //     StringBuffer sb = new StringBuffer(convertedString);
    //     return convertedString.equals(sb.reverse().toString());
    // }
}

