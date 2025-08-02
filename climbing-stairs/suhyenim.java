/* [5th/week02] 70. Climbing Stairs

1. 문제 요약
링크: https://leetcode.com/problems/climbing-stairs/description/
한 번에 1칸이나 2칸을 올라갈 수 있을 때, n칸을 올라가는 방법의 수는?

2. 문제 풀이
풀이1: 1, 2칸을 올라가는 방법의 수는 이미 알기 때문에, "n칸을 올라가는 방법의 수 = n-2칸을 올라가는 방법의 수 + n-1칸을 올라가는 방법의 수"를 반복 
성공: Time: 0 ms (100%), Space: 40.4 MB (50.46%)
=> 시간 복잡도: O(n), 공간 복잡도: O(n)

class Solution {
    public int climbStairs(int n) {
        Map<Integer, Integer> dp = new HashMap<>();
        dp.put(1, 1);
        dp.put(2, 2);
        for (int i = 3; i <= n; i++){
            dp.put(i, dp.get(i - 2) + dp.get(i - 1));
        }
        return dp.get(n);
    }   
}

풀이2: 풀이1과 논리는 같지만, HashMap을 사용하지 않음으로써 공간 복잡도를 낮춤
성공: Time: 0 ms (100%), Space: 40.1 MB (97.08%)
=> 시간 복잡도: O(n), 공간 복잡도: O(1)

class Solution {
    public int climbStairs(int n) {
        if (n < 3){
            return n;
        }
        int n1 = 1, n2 = 2;
        for (int i = 0; i < n - 2; i++){
            int n3 = n1 + n2;
            n1 = n2;
            n2 = n3;
        }
        return n2;
    }   
}

풀이3: 풀이1은 반복문(bottom-up) DP이고, 풀이3은 재귀+메모이제이션(top-down) DP임
성공: Time: 0 ms (100%), Space: 40.5 MB (50.46%)
=> 시간 복잡도: O(n), 공간 복잡도: O(n)

class Solution {
    private Map<Integer, Integer> memo = new HashMap<>();

    public int climbStairs(int n) {
        if (memo.containsKey(n)) {
            return memo.get(n);
        }

        if (n < 3) {
            return n;
        }

        int result = climbStairs(n - 1) + climbStairs(n - 2);
        memo.put(n, result);
        return result;
    }
}

3. TIL
재귀에다가 메모이제이션을 더하면
=> 큰 문제는 재귀적으로 쪼개서 풀되, 이미 계산한 작은 문제의 결과는 메모(map)에 저장해두었다가 꺼내 쓸 수 있기 때문에
=> 중복 계산을 방지함으로써 시간 복잡도를 아낄 수 있다.

*/

class Solution {
    public int climbStairs(int n) {
        Map<Integer, Integer> dp = new HashMap<>();
        dp.put(1, 1);
        dp.put(2, 2);
        for (int i = 3; i <= n; i++){
            dp.put(i, dp.get(i - 2) + dp.get(i - 1));
        }
        return dp.get(n);
    }   
}
