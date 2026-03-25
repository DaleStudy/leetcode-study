import java.util.*;
//goal : 두개의 인덱스 반환
class Solution {
    static int[] answer = new int[2];
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> maps = new HashMap<>();//num , index
        for(int i = 0; i < nums.length; i++){
            int t = target - nums[i]; //새로운 타겟
            //O(1)으로 다음 부분 찾기
            if (maps.containsKey(t)){
                answer[0] = i;
                answer[1] = maps.get(t);

                Arrays.sort(answer);
                return answer;
            }

            maps.put(nums[i], i);
        }

        return answer;

    }
}
