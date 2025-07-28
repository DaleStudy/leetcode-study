import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;

public class Geegong {


    /**
     * time complexity : O(n)
     * space complexity : o(n)
     * @param nums
     * @return
     */
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> uniques = new HashSet<>();

        for (int num : nums) {
            if (uniques.contains(num)) {
                return true;
            }

            uniques.add(num);
        }

        return false;
    }

}

