class Solution {
    /**
     *   시간 복잡도: O(log N)
     *   - 주어진 수를 2로 나누는 행위를 반복 (주어진 수가 0이 될 때까지)
     *   - 이는 반대로 보면 2를 몇 번 곱해야 N이 나오는지를 확인하는 과정과 같음 (로그의 의미..ㅎ)
     *   - 또 생각해보니까 Binary Search Tree 에서 특정 값을 조회할 때와 같은 흐름이었던 것 같음!
     *
     *   공간 복잡도: O(1)
     *   - 자료구조를 활용하지 않음
     */
    public int hammingWeight(int n) {
        int result = 0;
        while (n >= 1) {
            if ((n % 2) == 1) {
                result++;
            }
            n /= 2;
        }

        return result;
    }
}