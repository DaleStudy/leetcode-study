import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Sol35229 {

    public boolean containsDuplicate(int[] nums) {
        Set<Integer> duplicateCheck = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            if (duplicateCheck.contains(nums[i])) {
                return true;
            }
            duplicateCheck.add(nums[i]);
        }
        return duplicateCheck.size() != nums.length;
    }

    public boolean containsDuplicate2(int[] nums) {
        Arrays.sort(nums);
        for (int i = 0; i < nums.length-1; i++) {
            if (nums[i] == nums[i+1]) {
                return true;
            }
        }
        return false;
    }

}
