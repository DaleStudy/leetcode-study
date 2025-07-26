import java.util.*;

// 개선안
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> checkNums = new HashMap<>();

        for(int i = 0; i < nums.length; i++){
            if(checkNums.containsKey(target - nums[i])){
                int place = checkNums.get(target - nums[i]);
                return new int[]{place, i};
            }
            checkNums.put(nums[i], i);
        }
        return new int[]{};
    }
}


// 초기 구성안
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> element = new HashMap<>();

        for(int i = 0; i < nums.length; i++){
            element.put(i, nums[i]);
        }

        int[] result = new int[2];
        int n = 0;
        for(int i = 0; i < nums.length; i++){
            element.remove(i);
            n = target - nums[i];
            if(element.containsValue(n)){
                result[0] = i;
                break;
            }
        }

        for(int i = 0; i < nums.length; i++){
            if(nums[i] == n && i != result[0]){
                result[1] = i;
                break;
            }
        }
        return result;
    }
}

