import java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> count = new HashSet<>();
        boolean answer = false;
        for(int num : nums){
            if(count.contains(num)) {
                answer = true;
                break;
            }
            count.add(num);
        }
        return answer;
    }
}