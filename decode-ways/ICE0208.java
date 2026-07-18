class Solution {
    private String s;
    private Integer[] memo;

    /**
     * 현재 위치에서 숫자 한 자리 또는 두 자리를 해석하며 가능한 경우의 수를 구한다.
     * 각 index의 결과를 memo에 저장하여 동일한 위치를 중복 계산하지 않는다.
     *
     * 시간 복잡도: O(n) - 각 index를 한 번씩만 계산한다.
     * 공간 복잡도: O(n) - memo 배열과 최대 n 깊이의 재귀 호출 스택
     */
    public int numDecodings(String s) {
        this.s = s;
        this.memo = new Integer[s.length()];

        return dfs(0);
    }

    private int dfs(int index) {
        // 문자열 끝까지 유효하게 해석한 경우
        if (index == s.length()) {
            return 1;
        }

        // 0으로 시작하는 코드는 해석할 수 없다.
        if (s.charAt(index) == '0') {
            return 0;
        }

        if (memo[index] != null) {
            return memo[index];
        }

        // 현재 숫자 한 자리만 해석하는 경우
        int count = dfs(index + 1);

        // 현재 숫자와 다음 숫자를 함께 해석하는 경우
        if (index + 1 < s.length()) {
            int twoDigitNumber =
                    (s.charAt(index) - '0') * 10
                    + (s.charAt(index + 1) - '0');

            if (twoDigitNumber <= 26) {
                count += dfs(index + 2);
            }
        }

        memo[index] = count;
        return count;
    }
}
