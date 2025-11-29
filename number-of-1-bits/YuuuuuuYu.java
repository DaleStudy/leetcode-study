/**
 * Runtime: 0ms
 * Time Complexity: O(log n)
 * - n을 2로 나누는 과정을 반복하므로 log n에 비례
 *
 * Memory: 42.32MB
 * Space Complexity: O(1)
 *
 * Approach: 비트 연산 (나눗셈 방식)
 * 1) n을 2로 나눈 나머지(n%2)를 확인하여 1의 개수를 카운트
 * 2) 마지막에 1은 무조건 남기 때문에 while문 종료 후 1을 더해줌
 */
class Solution {
    public int hammingWeight(int n) {
        int count = 0;
        while (n > 1) {
            count += n%2;
            n /= 2;
        }

        return count+1;
    }
}
