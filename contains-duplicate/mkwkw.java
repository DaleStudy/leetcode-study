//using map

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Map<Integer, Boolean> appearance = new HashMap<>();

        for(int i=0; i<nums.length; i++)
        {
            if(appearance.containsKey(nums[i]))
            {
                return true;
            }
            else
            {
                appearance.put(nums[i], true);
            }
        }

        return false;
    }
}
