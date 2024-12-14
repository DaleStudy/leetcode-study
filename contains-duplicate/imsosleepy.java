// 중복제거를 위해 set을 적극적으로 활용해야할 듯...
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> numSet = new HashSet<>();

        for (int num : nums) {
            if (numSet.contains(num)) {
                return true;
            }
            numSet.add(num);
        }

        return false;
    }
}
