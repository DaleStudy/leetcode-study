import java.util.*;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        int n = nums.length;
        Arrays.sort(nums);
        List<List<Integer>> answers = new ArrayList<>();
        Set<List<Integer>> answer = new HashSet<>();
        for(int i = 0 ; i < n ; i++){
            if (nums[i] > 0) break;
            if (i > 0 && nums[i] == nums[i-1]) continue;
            int left = i + 1;
            int right = n - 1;
            while(left < right){
                int sum = nums[left] + nums[right] + nums[i];

                
                if (sum > 0) right--;
                else if (sum < 0) left++;
                else{
                    answer.add(new ArrayList<>(List.of(nums[i],nums[left], nums[right])));
                    while(left < right && nums[left] == nums[left+1]) left++;
                    while(left < right && nums[right] == nums[right-1]) right--;
                    left++;
                    right--;
                }
            }
        }
        
        answers = new ArrayList<>(answer);

        return answers;
    }
}
