import java.util.*;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> numberCheck = new HashSet<>();

        for(int num : nums){
            if(numberCheck.contains(num)){
                return true;
            }
            numberCheck.add(num);
        }
        return false;
    }
}
