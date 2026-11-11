import java.util.HashMap;
import java.util.Map;

/**
 시간 복잡도: O(n) - 최대 배열의 길이 n만큼 반복
 공간 복잡도: O(n) - 최대 배열의 길이 n만큼의 map 크기 사용
 */
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        int[] answer = new int[2];

        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(target - nums[i])) {
                answer[0] = map.get(target - nums[i]);
                answer[1] = i;
                // 찾은 경우 바로 return
                return answer;
            } else {
                map.put(nums[i], i);
            }
        }

        // 못 찾은 경우 null
        return null;
    }
}