
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int i =0;i<nums.length;i++){
            map.put(nums[i], i);
        }

        for(int i = 0;i<nums.length;i++){
            int b = target - nums[i];
            if(map.containsKey(b) && map.get(b) != i){
                int j = map.get(b);
                return new int[]{i,j};
            }
        }
        return null;
    }
}
