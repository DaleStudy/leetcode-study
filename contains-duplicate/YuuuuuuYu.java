/**
 * Runtime: 14ms
 * Time Complexity: O(n)
 *
 * Memory: 93.59MB
 * Space Complexity: O(n)
 *
 * Approach: HashSet을 사용하여 중복 검사
 * - 배열을 순회하면서 각 원소를 HashSet에 저장
 * - 이미 존재하는 원소를 발견하면 즉시 true 반환
 */
class Solution {
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

