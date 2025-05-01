/**
[문제풀이]
- 작은수를 두고, 큰수에 뺀 값을 구하자.
time: O(N), space: O(1)

[회고]
이번 문제는 난이도가 easy인 덕분에 무리없이 풀었던 것 같다.
 */
class Solution {
    public int maxProfit(int[] prices) {
        int min = prices[0];
        int max = 0;
        for (int i = 1; i < prices.length; i++) {
            if (min > prices[i]) {
                min = prices[i];
                continue;
            }
            max = Math.max(max, prices[i] - min);
        }
        return max;
    }
}

