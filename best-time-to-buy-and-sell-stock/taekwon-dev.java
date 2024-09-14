/**
 *  시간 복잡도: O(n)
 *  - 문제 조건 1 <= prices.length <= 10^5 를 보고, 우선 O(n^2)는 피해야겠다는 생각을 우선하게 됨.
 *  - 결국 이 문제는 각 인덱스가 날짜 개념으로 적용되기 때문에, 순차적으로 흘러감. (최대 이익을 계산할 때 결국 각 일자 별로 내가 얼마의 이득을 봤는지를 계산하고, 이 중 최댓값을 고르면 되는 구조)
 *  - 따라서 한 번의 순회로 문제를 풀 수 있음
 *  공간 복잡도: O(1)
 */
class Solution {
    public int maxProfit(int[] prices) {
        int minPrice = prices[0];
        int maxProfit = 0;

        for (int i = 1; i < prices.length; i++) {
            if (prices[i] < minPrice) {
                minPrice = prices[i];
            }
            maxProfit = Math.max(maxProfit, prices[i] - minPrice);
        }

        return maxProfit;
    }
}
