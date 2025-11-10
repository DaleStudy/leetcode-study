import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        List<Integer> list = Arrays.stream(nums).boxed().collect(Collectors.toList());
        for (int i : nums) {
            int idx = list.indexOf(i);
            if (idx == -1) {
                continue;
            }
            list.remove(idx);
            if (list.contains(i)) {
                return true;
            }
        }
        return false;
    }
}