/**
Problem 217 : contains duplicate
Summary : 주어진 배열에서 중복이 있으면 true, 없으면 false

*/

class Solution {
    public boolean containsDuplicate(int[] nums) {
        long count = Arrays.stream(nums)
                        .distinct()
                        .count();
        
        return count != nums.length;
    }
}