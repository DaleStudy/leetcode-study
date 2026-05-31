class Solution {
    public int maxProfit(int[] prices) {
        // 1. 0번을 제외하고 max 를 찾고 
        // 2. 0 ~ max 범위에서 min을 찾는다 => 2n
        // 3. max - min > 0 이면 값 리턴, max - min <=0 이면 0 리턴
        /*
        if (prices.length == 1) {
            return 0;
        }

        int max = 1;
        for (int i = 1; i < prices.length; i++) {
            if (prices[max] <= prices[i]) {
                max = i;
            }
        }

        int min = max - 1;
        for (int i = max - 1; i >= 0; i--) {
            if (prices[i] < prices[min]) {
                min = i;
            }
        }
        int result = prices[max] - prices[min];
        return result > 0 ? result : 0;
        */
        // 위 풀이 실패 케이스 : [3,3,5,0,0,3,1,4]
        // -> i가 max 일 때 i 이전까지 반복문으로 최대값 구하기 => n^2
        // -> Time Limit Exceeded 발생
        // -> i 이전까지 범위에서 최소값을 구해서 값을 구할까?
        /*
        int result = 0;
        for (int i = 1; i < prices.length; i++) {
            for (int j = 0; j < i; j++) {
                int cur = prices[i] - prices[j];
                if (result < cur) {
                    result = cur;
                }
            }
        }
        return result;
        */
        // i 이전까지 범위에서 최소값을 구해서 배열로 만들기
        int curMin = prices[0];
        int result = 0;
        for (int i = 0; i < prices.length; i++) {
            if (curMin > prices[i]) {
                curMin = prices[i];
            }
            // System.out.println(curMin);
            if (result < prices[i] - curMin) {
                result = prices[i] - curMin;
            }
            // System.out.println(">>" + result);
        }
        return result;
    }
}
