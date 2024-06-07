/**
 * time: O(n^2)
 * space: O(n)
 *
 * - time: becasue of two nested loop and inner loop having a linear time complexity.
 * - space: because of a HashSet to store the triplets.
 */
class Solution {

    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        int i = 0, j, k;
        int ni = 0, nj, nk;
        Set<List<Integer>> res = new HashSet<>();
        while (i < nums.length && ni <= 0) {
            ni = nums[i];
            j = i + 1;
            k = nums.length - 1;
            while (j < k) {
                nj = nums[j];
                nk = nums[k];
                int sum = ni + nj + nk;
                if (sum < 0) {
                    j++;
                } else if (sum > 0) {
                    k--;
                } else {
                    res.add(List.of(ni, nj, nk));
                    j++;
                }
            }
            i++;
        }
        return res.stream()
                  .toList();
    }
}
