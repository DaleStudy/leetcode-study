import java.util.*;
// 개선 방향
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set duplication = new HashSet<>();

        for(int n : nums){
            if(duplication.contains(n)){
               return true;
            }
            duplication.add(n);
        }
        return false;
    }
}


// 초기 문제 풀이
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);

        for(int i = 0; i < nums.length-1; i++){
            if(nums[i] == nums[i+1]) return true;
        }
        return false;
    }
}

