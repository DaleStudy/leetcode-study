/*
Time complexity: O(n)
Space complexity: O(1)

i <= j 인 두 인덱스 i, j에 대해서, prices[j] - prices[i]를 최대화해야 한다.

1. i = 0부터 시작하여, 오른쪽으로 순회한다.
2. 현재 값이 max보다 크다면, max를 갱신하고, min과의 차이를 계산한다.
3. 현재 값이 min보다 작다면, min을 갱신하고, max 역시 같은 값으로 갱신한다. (과거로 돌아가서 팔 수는 없으므로)
*/
class Solution {
    public int maxProfit(int[] prices) {
        int min = 999999;
        int max = 0;
        int ans = 0;
        for (int i = 0; i < prices.length; i++) {
            if (prices[i] > max) {
                max = prices[i];
                if (max - min > ans) {
                    ans = max - min;
                }
            }
            if (prices[i] < min) {
                min = max = prices[i];
            }
        }

        return ans;
    }
}
