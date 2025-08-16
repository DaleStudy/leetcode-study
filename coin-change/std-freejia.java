/** 
 * BFS 는 너비 우선이므로, 가장 얕은 깊이로 목표 금액을 만족하면 '최소 동전 개수'를 사용한 것입니다. 
 * 너비 == 사용한 동전 개수 
 * 
 * Queue<Integer> 동전 금액 '합' 을 관리합니다 
 * 
 * 목표 금액이 amount 일 때, 
 * 0 부터 amount 까지의 합을 체크할 boolean[] 을 활용합니다. 
 * 합계 금액이 '이미 만들어본 합' 이면 boolean[] 에 체크하여 중복방문을 방지하기 위함.
 * 
  */
class Solution {
    public int coinChange(int[] coins, int amount) {
        if (amount == 0) return 0; // 목표 금액 0인 경우, '0개' 리턴

        Arrays.sort(coins); // 작은 동전부터 더해본다

        // 이미 만들어본 '합' 은 지나가도록.
        boolean[] visitedAmount = new boolean[amount + 1];
        // 합
        Queue<Integer> amountQueue = new ArrayDeque<>();

        amountQueue.add(0); // 시작 금액 0
        visitedAmount[0] = true;

        int coinCount = 0; // 사용한 동전 개수

        while(!amountQueue.isEmpty()) {
            coinCount++; // 사용한 동전 개수 1개 증가

            int queueSize = amountQueue.size();

            for(int i = 0; i < queueSize; i++) {
                // 현재 금액 합 
                int currentAmount = amountQueue.poll();

                // 모든 코인을 더해본다
                for(int coin : coins) {
                    // 코인을 더해 본 합.
                    int tempAmount = currentAmount + coin;

                    if (tempAmount == amount) return coinCount; // 최소 동전 개수 찾음

                    // 처음 만든 합 이고, 목표 금액보다 적은 합이라면,
                    if (tempAmount < amount && !visitedAmount[tempAmount]) {
                        visitedAmount[tempAmount] = true;
                        amountQueue.add(tempAmount);
                    }
                }
            }
        }
        return -1;
    }
}
