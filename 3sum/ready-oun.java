import java.util.Arrays; 
import java.util.ArrayList; 
import java.util.List; 

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums); 
        List<List<Integer>> result = new ArrayList<>(); 

        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue; 

            int left = i + 1; 
            int right = nums.length - 1; 

            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right]; 

                if (sum == 0) {
                    
                    // result.add(Arrays.asList(nums[i], nums[left], nums[right])); 
                    List<Integer> triplet = new ArrayList<>(); 
                    triplet.add(nums[i]); 
                    triplet.add(nums[left]); 
                    triplet.add(nums[right]); 

                    result.add(triplet); 

                    while (left < right && nums[left] == nums[left + 1]) left++; 
                    while (left < right && nums[right] == nums[right - 1]) right--; 

                    left++;
                    right--; 
                    
                } else if (sum < 0) {
                    left++;     
                } else {
                    right--; 
                }
            }
        }
        return result; 
    }   
}

/**
    Two pointers - fix 1 and use 2 ptrs
    nums[i] + nums[L] + nums[R] == 0
    no duplicates 

    1. sort array
    2. skip repeats
        - nums[i] == nums[i - 1] 
        - nums[left] == nums[left + 1]
        - nums[right] == nums[right - 1] 
    3. check if sum == 0
    4. move L right if sum < 0 
    5. move R left if sum > 0 else 

    List<Integer>: [0, 0, 0]
    List<List<Integer>>: [[0, 0, 0], [-2, -3, 5]] 
    nums.length - 2까지만 반복: for no out of bounds 
        (last 2 val for left, right each)
 */
