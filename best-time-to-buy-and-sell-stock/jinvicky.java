/**
 * 한글주석만 보고 코드를 작성해본다.
 * 조건문 안의 조건만 코드를 비우거나, 조건문만 남기고 안의 액션코드를 비우고 다시 작성해본다.
 *
 */
class Solution {
    public int maxProfit(int[] prices) {
        /**
         max라는 메모이제이션 변수를 int로 선언한다.
         dp로 모든 경우의 수를 고려할 것이다.
         주식의 최소가격을 담은 변수를 int로 선언한다. 맨 처음에 prices[0] 값이 되면 좋겠다.
         */
        int max = 0; // dp memoization 변수
        int min = prices[0]; // 주식 배열의 최소값
        for (int i = 1; i < prices.length; i++) {
            /**
             현재 주식은 팔 때의 주식 가격을 나타낸다.
             max값은 (기존 최대이익, 최소주식을 현재 주식값에 팔았을 때의 이익) 중 더 큰 값으로 업데이트된다.
             현재 주식값이 기존 최소 주식값보다 작다면 현재 주식값으로 최솟값을 업데이트한다.
             */
            int currentMax = prices[i] - min;
            max = Math.max(max, currentMax);
            if (prices[i] < min) {
                min = prices[i];
            }
        }

        return max;
    }
}
