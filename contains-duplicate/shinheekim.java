import java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> visited = new HashSet<>();

        for (int n : nums){
            if (!visited.add(n)){
                return true;
            }
        }
        return false; // 모든 값이 고유할 때
    }
}
