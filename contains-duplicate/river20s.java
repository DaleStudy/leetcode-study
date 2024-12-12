import java.util.HashSet;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        
        for (int num : nums) {
		        if (!set.add(num)) {
				        return true;
		        }
		    }
		    
		    return false;
    }
}