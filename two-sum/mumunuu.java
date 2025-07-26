import java.util.HashMap;
import java.util.Map;

class Solution {
    /**
     * 배열의 요소 2개를 더해서 target 숫자들을 만들고 인덱스를 반환
     * 같은 숫자를 여러번 사용할 수 없고, 해답은 반드시 존재함
     * Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?
     */

    /*
    // naive 한 풀이법. O(n^2)
    public int[] twoSum(int[] nums, int target) {
        // naive 한 방법: 나를 제외한 나머지 숫자가 있는지 찾음
        for (int i=0; i<nums.length-1; i++) {
            for (int k=i+1; k<nums.length; k++) {
                if (nums[i] + nums[k] == target) {
                    return new int[]{i,k};
                }
            }
        }
        return new int[]{};
    }
    */


    // 처음에 Map<Integer, List<Integer>>라고 생각했지만 그냥 Integer, Integer로 가능함
    public int[] twoSum(int[] nums, int target) {

        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {

            int needValue = target - nums[i];
            if (map.containsKey(needValue)) {
                return new int[]{map.get(needValue), i};
            }
            map.put(nums[i], i); // 항상 현재 인덱스를 나중에 저장

        }

        return new int[]{}; // 절대 도달하지 않음 (문제 조건상 정답이 항상 존재)

    }

}
