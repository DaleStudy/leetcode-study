/**
 *  시간 복잡도: O(n)
 *  - n = 5 경우를 가정하고 생각해보기
 *  - 3층 계단 -> 2층, 1층 계산 (이 경우는 이미 메모되어 있어서 별도로 계산하진 않음)
 *  - 4층 계단 -> 3층, 2층 계산 (2층은 메모에 있는 것 활용)
 *  - 5층 계단 -> 4층, 3층 계산 (3층은 메모에 있는 것 활용)
 *  - ...
 *  - 각 단계 별로 (메모를 활용해) 아직 계산되지 않은 것을 한 번씩 호출하게 되므로 O(n)
 *  - 근데 만약 메모를 사용하지 않으면? (중복 호출이 많이 일어남 ... O(n^2))
 *
 *  공간 복잡도: O(n)
 */
class Solution {
    public int climbStairs(int n) {
        int[] memo = new int[n + 1];
        return climbStairs(n, memo);
    }

    public int climbStairs(int n, int[] memo) {
        if (n == 1) return 1;
        if (n == 2) return 2;

        if (memo[n] > 0) return memo[n];

        memo[n] = climbStairs(n - 1, memo) + climbStairs(n - 2, memo);
        return memo[n];
    }
}
