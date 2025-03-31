/*
# Time Complexity: O(n^2)
# Space Complexity: O(1)
*/

class Solution {
    public List<List<Integer>> threeSum1(int[] nums) { // solution 1
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

    public List<List<Integer>> threeSum(int[] nums) { // solution 2
        int n = nums.length;
        Arrays.sort(nums);
        Set<List<Integer>> ans = new HashSet<>();

        for (int i = 0; i < n - 2; i++) {
            int l = i + 1;
            int r = n - 1;
            int target = -nums[i];
            while (l < r) {
                int sum = nums[l] + nums[r];
                if (sum == target) {
                    ans.add(new ArrayList<>(Arrays.asList(nums[i], nums[l], nums[r])));
                    l++;
                    r--; // 또 다른 (l, r) 조합이 있을 수 있으므로, loop를 계속 이어간다.
                } else if (sum < target) {
                    l++;
                } else {
                    r--;
                }
            }
        }

        return new ArrayList<>(ans);
    }
}
