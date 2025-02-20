/*
# Time Complexity: O(n^2 * logn)
# Space Complexity: O(1)
*/

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        int n = nums.length;
        Arrays.sort(nums);
        Set<List<Integer>> ans = new HashSet<>();

        for (int i = 0; i < n - 2; i++) {
            for (int j = i + 1; j < n - 1; j++) {
                int target = -nums[i] - nums[j]; // nums[i], nums[j]와 더해서 합이 0이 되기 위해 nums[k]가 가져야하는 값
                int k = -1;
                int l = j + 1;
                int r = n - 1;
                while (l <= r) {
                    int m = (r - l) / 2 + l;
                    if (nums[m] == target) {
                        k = m;
                        break;
                    } else if (nums[m] < target) {
                        l = m + 1;
                    } else {
                        r = m - 1;
                    }
                }
                if (k != -1) { // binary search에서 target을 찾은 경우
                    ans.add(new ArrayList<>(Arrays.asList(nums[i], nums[j], nums[k])));
                }
            }
        }

        return new ArrayList<>(ans);
    }
}
