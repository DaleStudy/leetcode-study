/*
브루트 포스틑 이중 반복문을 사용하므로 시간 복잡도가 O(n^2)
-> map에 (값, 인덱스)로 저장 후 배열을 반복하며 합이 target인 값을 찾는다.
*/
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numberMap = new HashMap<>();
        for (int i=0; i<nums.length; i++) {
            numberMap.put(nums[i], i);
        }

        for(int i=0; i<nums.length; i++) {
            int operand = target - nums[i];
            if (numberMap.containsKey(operand) && numberMap.get(operand) != i) { // 자기 자신은 제외
                return new int[] { numberMap.get(target - nums[i]), i };
            }
        }

        return new int[] {};
    }
}

/*
class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int i=0; i<nums.length-1; i++) {
            for(int j=i+1; j<nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[] { i, j };
                }
            }
        }

        return new int[] {};
    }
}
*/
