import java.util.HashSet;

class Solution {
    // The problem is to check if there are any duplicate elements in the array.
    // So, I decided to use HashSet because it has O(1) time complexity for add and contains operations which are good to use for checking duplicates.
    public boolean containsDuplicate(int[] nums) {
        // the element type of the array is int, so create Integer HashSet
        // O(n) space complexity
        HashSet<Integer> exists = new HashSet<Integer>();
        // the nums array has length up to 10^5, so use int type
        // O(n) time complexity average
        // worst case: O(n log n) if many elements hash to the same bucket
        for(int i = 0; i < nums.length; i++){
            int num = nums[i];
            
            if(exists.contains(num)){
                return true;
            }else{
                exists.add(num);
            }
        }
        return false;
    }
}
