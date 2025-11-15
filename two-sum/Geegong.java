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


//        Map<Integer, Integer> map = new HashMap<>();
//        int[] result = new int[2];
//
//        // if target = -9 / num = 1 , num = -10
//        for (int index=0; index<nums.length; index++) {
//            map.put(nums[index], index);
//        }
//
//        for (int index=0; index<nums.length; index++) {
//            int difference = target - nums[index];
//
//            if (map.containsKey(difference)
//                    && map.get(difference) != index) {
//                result[0] = index;
//                result[1] = map.get(difference);
//                return result;
//            }
//        }
//
//        return result;
    }
}

