/**
 * <a href="https://leetcode.com/problems/longest-increasing-subsequence/">week06-4.longest-increasing-subsequence</a>
 * <li>Description: return the length of the longest strictly increasing subsequence</li>
 * <li>Topics: Array, Binary Search, Dynamic Programming </li>
 * <li>Time Complexity: O(NLogN), Runtime 6ms            </li>
 * <li>Space Complexity: O(N), Memory 44.3MB            </li>
 */
class Solution {
    public int lengthOfLIS(int[] nums) {
        List<Integer> dp = new ArrayList<>();

        for(int num : nums){
            int idx = Collections.binarySearch(dp, num);

            if(idx < 0) {
                idx = -idx -1;
            }

            if(idx == dp.size()) {
                dp.add(num);
            } else {
                dp.set(idx, num);
            }
        }

        return dp.size();
    }
}
