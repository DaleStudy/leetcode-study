class Solution {
	public int maxProfit(int[] prices) {
		int result = 0;
		int maxProfit = 0;
		int buyStock = prices[0];

		// 한번 돌면서 나보다 작은 것이 나올 때까지 이익을 본다


		for (int price: prices) {
			// 나보다 작은 게 나오면 MAX 이익을 갱신하고 거기부서 다시 시작한다.
			if (price < buyStock) {
				result = Math.max(result, maxProfit);
				maxProfit = 0;
				buyStock = price;
			} else {
				maxProfit = Math.max(price - buyStock, maxProfit);
			}
		}

		return Math.max(result, maxProfit);
	}
}

