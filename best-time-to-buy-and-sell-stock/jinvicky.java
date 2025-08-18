class Solution {
    public int maxProfit(int[] prices) {
        /**
         max라는 메모이제이션 변수를 int로 선언한다.
         dp로 모든 경우의 수를 고려할 것이다.

         주식의 최소가격을 담은 변수를 int로 선언한다. 맨 처음에 prices[0] 값이 되면 좋겠다.


         */
        int max = 0;
        int minStock = prices[0];

        for (int i = 1; i < prices.length; i++) {
            /**
             현재 주식은 팔 때의 주식 가격을 나타낸다.
             max에는 현재 주식 가격 - 현재 최소 주식 가격의 값을 저장한다. (abs 금지)
             만약 현재 주식의 가격이 현재 최소 주식 가격보다 크다면
             현재 최소 주식의 가격으로 업데이트한다.
             */
            int prc = prices[i];
            max = Math.max(max, prc - minStock);

            if (minStock > prc) {
                minStock = prc;
            }
        }
        return max;
    }
}
