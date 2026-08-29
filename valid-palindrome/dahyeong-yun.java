/**
 * [풀이 개요]
 * - 시간복잡도 : O(n)
 * - 공간복잡도 : O(1)
 */
class Solution {
    /**
     * [문제 풀이 아이디어]
     * - 주어진 문자열의 길이가 최대 10^5 이므로 10^8 까지 통과할 수 있다고 가정할 때, 시간복잡도는 O (n log n)까지 가능해 보임
     * - 문자열 s의 시작과 끝 인덱스가 각각 x, y 라고 할 때 s[x] == s[y], s[x+1] == s[y-1], s[x+2] == s[y-2], s[x+n] == s[y-n] (n은 문자열 중간 인덱스 까지) 와 같이 검증할 수 있음.
     * - 즉 투포인터 형태가 될 수 있어 보임. 
     * - 다만 알파벳이 아닌 문자는 제외하고 판단해야 하므로 포인터가 정확히 같은 값을 x, y에서 빼는 형태가 될 수는 없고, 비교 대상이 아닌 인덱스를 넘어가서 다음에 판단해야 함. 
     * - 이렇게 순회할 경우 문자열 길이 n의 1/2 를 순회하므로 시간복잡도는 O(n) 이 됨.
     * - 매 char 변수 이외에 추가 공간이 필요치 않으므로 공간복잡도는 O(1) 이 됨.
     */
    public boolean isPalindrome(String s) {
        int len = s.length();
        if(len == 1) return true;
        
        int left = 0;
        int right = len - 1;

        while(left < right) {
            char leftChar = Character.toLowerCase(s.charAt(left));
            char rightChar = Character.toLowerCase(s.charAt(right));

            // 문자가 아닌 경우 다음 인덱스 확인
            if(!Character.isLetterOrDigit(leftChar)) {
                left++;
            } else if(!Character.isLetterOrDigit(rightChar)) {
                right--;

            // 동일한 경우 다음 인덱스 확인
            } else if(leftChar == rightChar) {
                left++;
                right--;
            } else {
                return false;
            }
        }
        return true;
    }
}
