//1. using map
//2. using set : why? It doesn't have to use a pair of key and value.

class Solution {
    public boolean containsDuplicate(int[] nums) {
        //Map<Integer, Boolean> appearance = new HashMap<>();
        Set<Integer> appearance = new HashSet<>();

        for(int i=0; i<nums.length; i++)
        {
            if(appearance.contains(nums[i]))
            {
                return true;
            }
            else
            {
                appearance.add(nums[i]);
            }
        }

        return false;
    }
}
