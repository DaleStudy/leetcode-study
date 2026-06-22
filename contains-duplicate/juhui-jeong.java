/*

// 첫번째 풀이
class Solution {
    public boolean containsDuplicate(int[] nums) {
        for (int i=0; i < nums.length; i++) {
            for (int j=i+1; j < nums.length; j++) {
                if (nums[i] == nums[j]) return true;
            }
        }
        return false;
    }
}

// 두번째 풀이
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set set = new HashSet<Integer>();
        for (int i=0; i < nums.length; i++) {
            set.add(nums[i]);
        }

        if (set.size() != nums.length) return true;
        return false;
    }
}

*/

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>();        
        for (int i=0; i < nums.length; i++) {
            if (!set.add(nums[i])) return true;
        }
        return false;
    }
}
