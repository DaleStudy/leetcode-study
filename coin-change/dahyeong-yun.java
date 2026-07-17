/**
 * [풀이 개요]
 * - 시간복잡도 : O(N * amount) (N: 동전 종류의 개수, 최대 12 * 10,000 = 120,000번 연산)
 * - 공간복잡도 : O(amount) (DP 테이블 크기)
 */
class Solution {
    /**
     * [문제 풀이 아이디어]
     * - amount를 금액이라고 해석했을 때, 금액을 만들 수 있는 최소 코인의 갯수를 구하는 문제.
     * - 가짓 수를 의미하는 배열을 동해 동적 프로그래밍 방식으로 풀 수 있음.
     * - 바깥 루프에서는 코인을, 안쪽 루프에서는 수를 차례로 순회함.
     * - 이때 모든 수에 대해 각 코인으로 만들 수 있는 최저 수를 계산해서 넣고, 코인의 액면 값 만큼 적은 횟수에서 해당 코인을 더해서 만들 수 있는 수와 비교한 최솟값을 구함. 
     * - 시간 복잡도는 코인의 수 * 금액의 수 이므로, 문제의 제약에 따라 12 * 10,000 = 120000 이 된다.
     */
    public int coinChange(int[] coins, int amount) {
        int[] methods = new int[amount + 1]; // 금액별 코인의 최소 갯수
        Arrays.fill(methods, amount+1);

        methods[0] = 0; // 금액 0원을 만들기 위해서는 코인을 안쓰면 됨.
        for(int i=0; i<coins.length; i++) {
            int coin = coins[i];
            for(int j=1; j <= amount; j++) {
                if(j >= coin) {
                    methods[j] = Math.min(methods[j], methods[j - coin] + 1);
                }
            }
        }

        return methods[amount] == amount + 1 ? -1 :  methods[amount];
    }
}