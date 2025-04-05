import java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> answer = new HashSet<>();
        for (int num : nums) {
            if (!answer.contains(num)) {
                answer.add(num);
            } else {
                return true;
            }
        }
        return false;
    }
}