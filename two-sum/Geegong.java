import java.util.HashMap;
import java.util.Map;

public class Geegong {

    /**
     * time complexity : O(n)
     * space complexity : O(n)
     * @param nums
     * @param target
     * @return
     */
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        int[] result = new int[2];

        // if target = -9 / num = 1 , num = -10
        for (int index=0; index<nums.length; index++) {
            map.put(nums[index], index);
        }

        for (int index=0; index<nums.length; index++) {
            int difference = target - nums[index];

            if (map.containsKey(difference)
                    && map.get(difference) != index) {
                result[0] = index;
                result[1] = map.get(difference);
                return result;
            }
        }

        return result;
    }
}

