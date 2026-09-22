/**
  * TC : O(min(m, n))
  *   - m, n 중에 더 작은 수의 -1 을 한 만큼 순회하므로 O(min(m, n))
  * SC : O(1)
  *   - 유의미한 공간 생성이 없음.
  */
class Solution {
    public int uniquePaths(int m, int n) {
        int selectCount = Math.min(m - 1, n - 1); // 선택할 개수 (r)
        int totalCount = m + n - 2;               // 선택 가능한 총 개수 (n)

        long combination = 1;
        for (int i = 1; i <= selectCount; i++) {
            combination = combination * (totalCount - selectCount + i) / i;
        }

        return (int) combination;
    }
}
