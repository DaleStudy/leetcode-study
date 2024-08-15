class Solution {
    /**
     *   시간 복잡도: O(N)
     *   - 최악의 경우 주어진 배열의 마지막 원소까지 체크해야 함.
     *   - 중복 검사를 위해 Set 선택한 이유
     *     - O(1) 으로 탐색 가능
     *     - 데이터 순서 보장 필요 없음
     */
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int num: nums) {
            if (set.contains(num)) {
                return true;
            }
            set.add(num);
        }
        return false;
    }
}
