import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

// NOTE: 실행시간 1.5초..
// 시간 복잡도: O(n^2)
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {

        Arrays.sort(nums);
        Set<List<Integer>> result = new HashSet<>();

        for(int i = 0; i < nums.length - 2; i++) {
            int startIdx = i + 1;
            int endIdx = nums.length - 1;
            while(startIdx < endIdx) {
                int sum = nums[i] + nums[startIdx] + nums[endIdx];
                if(sum == 0) {
                    result.add(Arrays.asList(nums[i], nums[startIdx], nums[endIdx]));
                }

                if(sum > 0) {
                    endIdx--;
                } else {
                    startIdx++;
                }
            }
        }

        return new ArrayList<>(result);   
    }
}



//  309 / 314 testcases passed Time Limit Exceeded
// NOTE: 시간복잡도 O(n^3)
class WrongSolution {
    public List<List<Integer>> threeSum(int[] nums) {
        Set<List<Integer>> res = new HashSet<>();

        List<Integer> temp = new ArrayList<>();

        temp.remove(3);

        for(int i = 0; i < nums.length; i++) {
            for(int j = 0; j < i; j++) {
                for(int k = 0; k < j; k++) {

                    if((nums[i] + nums[j] + nums[k]) == 0) {
                        List<Integer> solution = Arrays.asList(nums[i], nums[j], nums[k]);
                        Collections.sort(solution);
                        res.add(solution);
                    }
                }
            }
        }


        return new ArrayList<>(res);
    }
}