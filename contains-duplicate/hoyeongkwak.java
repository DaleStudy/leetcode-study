/*
time complexity : O(n)
space complexity : O(n)
*/
class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> uniqueNums = new HashSet<Integer>();

        for (int num:nums) {
            if (!uniqueNums.add(num)) {
                return true;
            }
        }
        return false;
    }
}
