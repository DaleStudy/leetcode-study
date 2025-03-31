import java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> numberSet = new HashSet<>();
        for(int number : nums) {
            if(numberSet.contains(number)) {
                return true;
            }

            numberSet.add(number);
        }
        return false;
    }
}