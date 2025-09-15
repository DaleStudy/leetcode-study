

class Solution {

    public int countSubstrings(String s) {
        int n = s.length();
        int count = 0;

        // 홀수와 짝수 통합 처리 (0부터 2n-1까지)
        for (int center = 0; center < 2 * n - 1; center++) {
            int left = center / 2;
            int right = left + center % 2;

            while (left >= 0 && right < n && s.charAt(left) == s.charAt(right)) {
                count++;
                left--;
                right++;
            }
        }

        return count;
    }

    // 더 가독성이 좋은 풀이

    /**
     * 1. 회문의 중심을 명확하게 분리한다.
     * 2. c는 회문의 중심후보가 된다. 1글자짜리 중심이거나 혹은 두 글자짜리 회문의 왼쪽 중심이다.
     * 3. c를 홀수 길이 회문의 중심으로 설정한다 -> expand(s,c,c)
     * 4. c부터 c+1까지 짝수 길이 회문의 왼쪽 중심으로 설정한다 -> expand(s,c,c+1)
     * <p>
     * 이렇게 하는 이유는 ABA와 ABBA 두 가지 경우를 모두 커버하기 위해서이다.
     */
    public int countSubstrings2(String s) {
        int n = s.length();
        int count = 0;
        for (int c = 0; c < n; c++) {
            count += expand(s, c, c);     // 홀수 길이 중심
            count += expand(s, c, c + 1); // 짝수 길이 중심
        }
        return count;
    }

    private int expand(String s, int L, int R) {
        int add = 0;
        while (L >= 0 && R < s.length() && s.charAt(L) == s.charAt(R)) {
            add++;
            L--;
            R++;
        }
        return add;
    }

    /**
     *  프라이빗 메서드 "확장" 선언
     *  1. L, R 포인터 인덱스를 받는다.
     *  2. 두 포인터가 문자열 내 유효한 범위에 있어야 한다.
     *  3. L과 R이 가리키는 문자가 같아야 한다.
     *  2와 3을 모두 만족한다면 회문
     */
}
