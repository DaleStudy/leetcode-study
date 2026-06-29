/**
 * HashSet을 사용하여 배열에 중복된 값이 있는지 확인
 * 시간 복잡도: O(n), 공간 복잡도: O(n)
 */
class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> distinctSet = new HashSet<>();

        for (int i = 0; i < nums.length; i++) {
            if (distinctSet.contains(nums[i])) return true;
            distinctSet.add(nums[i]);
        }

        return false;
    }
}
