import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();

        Map<Integer, Integer> counter = new HashMap<>();
        for (int num : nums) {
            int count = counter.getOrDefault(num, 0);
            counter.put(num, count + 1);
        }

        Set<Integer> keySet = new HashSet<>(counter.keySet());
        for (int num1 : keySet) {
            int num1Count = counter.get(num1);
            if (num1Count > 1) {
                counter.put(num1, num1Count - 1);
            } else {
                counter.remove(num1);
            }

            for (int num2 : counter.keySet()) {
                int num3 = -num1 - num2;
                int count = counter.getOrDefault(num3, 0);
                if (((num2 == num3 && count >= 2) || (num2 != num3 && count >= 1)) && num3 >= num2) {
                    result.add(List.of(num1, num2, num3));
                }
            }

            counter.remove(num1);
        }

        return result;
    }
}
