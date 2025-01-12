// 투포인터를 쓸 필요 없음. 그냥 최소값을 찾아 빼주면 O(N)의 시간 복잡도를 얻을 수 있다.
// 투포인터와 큰 차이가 없는 이유는 투포인터도 O(N)이기 때문. 아주 약간의 공간복잡도 차이만 있을 듯
// 결과는 큰 차이 없으나 알고리즘 자체가 더 쉽다.
class Solution {
    public int maxProfit(int[] prices) {
        int minPrice = Integer.MAX_VALUE;
        int maxProfit = 0;

        for (int price : prices) {
            if (price < minPrice) {
                minPrice = price;
            } else {
                maxProfit = Math.max(maxProfit, price - minPrice);
            }
        }

        return maxProfit;
    }
}

// 처음 생각한 투포인터 방식
class Solution {
    public int maxProfit(int[] prices) {
        int left = 0;
        int right = 1; 
        int maxProfit = 0;

        while (right < prices.length) {
            if (prices[left] < prices[right]) {
                int profit = prices[right] - prices[left];
                maxProfit = Math.max(maxProfit, profit);
            } else {
                left = right;
            }
            right++;
        }

        return maxProfit;
    }
}
