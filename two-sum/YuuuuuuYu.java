/**
 * Runtime: 3ms
 * Time Complexity: O(n)
 *
 * Memory: 46.97MB
 * Space Complexity: O(n)
 *
 * Approach: HashMap을 사용하여 짝을 이루는 값(pair) 검사
 * - 배열을 순회하면서 각 원소의 짝을 계산
 * - 짝이 HashMap에 존재하는지 검사
 */
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map <Integer, Integer> map = new HashMap<>();
        for (int i=0; i<nums.length; i++) {
            int pair = target-nums[i];
            if (map.containsKey(pair) && map.get(pair) != i) {
                return new int[]{i, map.get(pair)};
            }
            map.put(nums[i], i);
        }

        return new int[]{};
    }
}
