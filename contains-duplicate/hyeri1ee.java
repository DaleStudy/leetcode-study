import java.util.*;

class Solution {
    Set<Integer> save = new HashSet<>();//O(1)에 이미 등장했는지 판별 위함
    public boolean containsDuplicate(int[] nums) {

        for(int i=0; i<nums.length; i++){
            if (!save.contains(nums[i])) save.add(nums[i]);
            else return true;
        }
        return false;
    }
}

