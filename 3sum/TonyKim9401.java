// TC: O(n^2)
// SC: O(n)
public class Solution {
    public List<List<Integer>> threeSum(int[] nums) {

        Arrays.sort(nums);

        List<List<Integer>> output = new ArrayList<>();
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; ++i) map.put(nums[i], i);

        for (int i = 0; i < nums.length - 2; ++i) {
            if (nums[i] > 0) break;

            for (int j = i + 1; j < nums.length - 1; ++j) {
                int cValue = -1 * (nums[i] + nums[j]);

                if (map.containsKey(cValue) && map.get(cValue) > j) {
                    output.add(List.of(nums[i], nums[j], cValue));
                }
                j = map.get(nums[j]);
            }

            i = map.get(nums[i]);
        }

        return output;
    }
}
