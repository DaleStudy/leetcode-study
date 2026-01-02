import java.util.HashMap;
import java.util.Map;

public class Geegong {

    /**
     * time complexity : O(n)
     * space complexity : O(n)
     * @param nums
     * @param target
     * @return int[]
     */
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        // key : value, value = index
        Map<Integer, Integer> maps = new HashMap<Integer, Integer>();

        for(int index=0; index<nums.length; index++) {
            int findOne = target - nums[index];
            if (maps.containsKey(findOne)) {
                result[0] = maps.get(findOne);
                result[1] = index;
                return result;
            }

            maps.put(nums[index], index);
        }

        return result;
    }
}

