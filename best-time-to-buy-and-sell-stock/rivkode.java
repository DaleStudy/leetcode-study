/*
1. 문제 이해
주식을 가장 작은 값에 사서 최고값에 팔아야 한다.
단순히 주식에서 최고값을 파는게 아니다. 구매 시간과 판매 시간이 정해져있으므로 반드시 산 시각보다 후에 팔아야 한다.

2. 알고리즘
2중 for loop ?

3. 구현

포인터를 하나씩 왼쪽에서 오른쪽으로 이동하며 이후 오른쪽 값들을 대입하여 뺴본다. 즉 무식하게 다 돈다

4. 예외
만약 모든 값이 음수라면 0을 리턴한다
10만이라서 2중 루프 돌면 시간초과 나지 않을까 ?
-> 아 .. 200/212 케이스에서 Time limit Exceeded 발생하네

그러면 다른 알고리즘으로 접근해야한다.
답지 참고
직관을 이용해야하네
i 번째 시기에 최대 수익을 얻으려면 i 번째 날 전 중 최저가를 찾아서 빼면 된다.
*/

import java.util.*;

class Solution {
    public int maxProfit(int[] prices) {
        int max = 0;
        int min = prices[0];

        for (int i=1; i<prices.length; i++) {
            int profit = prices[i] - min;
            max = Math.max(profit, max);
            // 어떻게 항상 Min을 찾을까 하였지만 루프를 돌때마다 i 를 기준으로 min을 찾아내면 됨
            min = Math.min(prices[i], min);
        }

        // for (int i=0; i<prices.length - 1; i++) {
        //     for (int j=i; j<prices.length; j++) {
        //         int buy = prices[i];
        //         int sell = prices[j];
        //         int profit = sell - buy;
        //         if (profit <= 0) {
        //             continue;
        //         }
        //         max = Math.max(max, profit);
        //     }
        // }
        
        return max;
    }
}
