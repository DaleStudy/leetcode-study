/*
# Time Complexity: O(m * n), where m = text1.length(), n = text2.length()
# Space Complexity: O(m * n)

DP로 접근했습니다.
text1[0..i], text2[0..j]의 LCS의 길이를 lcs[i][j]라고 정의하겠습니다. (0 <= i < m, 0 <= j < n)
lcs[i - 1][j - 1], lcs[i - 1][j], lcs[i][j - 1]을 미리 구해두었다면, lcs[i][j]는 아래처럼 O(1)에 계산할 수 있습니다.

1. text1[i] != text2[j]인 경우
lcs[i - 1][j] 를 기준으로 생각해보면, text1[i] != text2[j]이기 때문에, text1[0..i-1]에 text1[i]를 추가한다 해도, LCS의 길이에는 변화가 없습니다.
마찬가지로 lcs[i][j - 1] 을 기준으로, text2[0..j-1]에 text2[j]를 추가해도, LCS의 길이에는 변화가 없습니다.
따라서 lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1]) 로 구할 수 있습니다.

2. text1[i] == text2[j]인 경우
이 경우에는, lcs[i - 1][j - 1]에서 구한 LCS에 1글자가 추가되므로, lcs[i][j] = lcs[i - 1][j - 1] + 1 로 구할 수 있습니다.

3. i = 0 혹은 j = 0인 경우의 예외 로직을 추가하면, LCS의 길이를 구하는 2차원 DP를 구현할 수 있습니다.

*/

class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int m = text1.length();
        int n = text2.length();
        int[][] lcs = new int[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (text1.charAt(i) == text2.charAt(j)) {
                    if (i == 0 || j == 0) {
                        lcs[i][j] = 1;
                    } else {
                        lcs[i][j] = lcs[i - 1][j - 1] + 1;
                    }
                } else {
                    if (i == 0 && j == 0) {
                        lcs[i][j] = 0;
                    } else if (i == 0) {
                        lcs[i][j] = lcs[i][j - 1];
                    } else if (j == 0) {
                        lcs[i][j] = lcs[i - 1][j];
                    } else {
                        lcs[i][j] = Math.max(lcs[i][j - 1], lcs[i - 1][j]);
                    }
                }
            }
        }

        return lcs[m - 1][n - 1];
    }
}
