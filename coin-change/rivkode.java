/*
1. 문제 이해
숫자들을 조합해서 타겟 넘버를 만족하는 가장 작은 코인의 개수를 반환
만족하는 조합이 없다면 -1 반환

배열 정렬 후 작은 숫자부터 시작해서 더하며 타겟넘버와 일치하는지 체크
일치한다면 그때의 코인 개수를 기존 개수와 비교 및 초기화
만약 크다면 return 하여 다음 숫자로 이동

2. 예외 상황

output이 12가 되는 경우와 0이 되는 경우는 각각 무슨 경우일까 ?

12가 되는 경우는 어떤 조합으로도 타겟넘버를 만들지 못했을 경우

0이 되는 경우는 amount가 0일 경우 아무 숫자도 반환되면 안될 경우이므로 가장 처음 초기화 되고 바로 리턴됨.

3. 알고리즘
dfs

4. 구현
수도 코드
dfs(사용한 코인 개수, 지금까지의 값)
현재 값 == 타겟 값 체크
맞다면 최소값 초기화
반환

for coins
지금까지의 값 + 새로운 코인 <= 타겟 값
맞다면 dfs(사용한 코인 개수 + 1, 지금까지의 값 + 새로운 코인)

dp

재귀로 풀었으니 Time limit이 걸리지 않기 위해 dp로도 풀 수 있는 점을 고려할 수 있다.

dp 점화식을 만들어 보자
n 원을 만들기 위한 동전의 최소 개수이므로 
n이 만들고 싶은 금액, coin이 현재 선택한 동전이라고 할때
dp[n] = min(dp[n], dp[n-coin] + 1) 이 나온다.
n-coin 이 나오게된 이유는 n을 만들기 위해 특정 숫자에서 coin 더하여 n 을 만들어야 하기 때문이다.
x + coin = n -> x = n - coin 식이 만들어 진다.
해당 n-coin 을 만들기 위한 최소값에서 coin을 더했으므로 1을 더해줌으로써
선택한 coin 에서 n 을 만들기 위한 최소 개수를 얻을 수 있기 때문이다.

*/

import java.util.*;

class Solution {
    private int min;
    public int coinChange(int[] coins, int amount) {
        // int maxLength = 12;
        // min = maxLength + 1;
        // dfs(0, 0, amount, coins);
        // if (min == 13) {
        //     return -1;
        // }

        int[] dp = new int[amount + 1];
        

        for (int i=1; i<dp.length; i++) {
            dp[i] = amount + 1; // 최대값보다 1을 더하여 무효한 값(최대값보다 클 수 없음)을 임의로 넣어준다.
        }
        dp[0] = 0;
        // coin 들을 순회하며 각 코인들을 루프마다 해당 동전으로 최적화를 한다. 그래서 3번째 동전을 돌때에는 이전 1, 2번째의 동전들에 대해 누적된 결과를 얻게 된다.
        for (int c : coins) {
            // c 부터 시작하는 이유는 가지고 있는 코인보다 적은 n 을 만들 수 없기 때문
            for (int n = c; n < amount + 1; n++) {
                dp[n] = Math.min(dp[n], dp[n-c] + 1);
            }
        }

        if (dp[amount] == amount + 1) {
            return -1;
        }

        return dp[amount];
    }


    // 시간 초과 발생
    // public void dfs(int count, long total, int amount, int[] coins) {
    //     if (total == amount) {
    //         min = Math.min(min, count);
    //         return;
    //     }

    //     for (int coin: coins) {
    //         if (total + coin <= amount) {
    //             dfs(count + 1, total + coin, amount, coins);
    //         }
    //     }
    // }
}

