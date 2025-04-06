/**
 * <a href="https://leetcode.com/problems/house-robber/">week01-5.house-robber</a>
 * <li> Description: the maximum amount of money you can rob if you cannot rob two adjacent houses  </li>
 * <li> Concept: Array, Dynamic Programming     </li>
 * <li> Time Complexity: O(n), Runtime: 0ms     </li>
 * <li> Space Complexity: O(1), Memory: 41.1MB  </li>
 */

class Solution {
    public int rob(int[] nums) {
        if(nums.length==1) {
            return nums[0];
        }

        List<Integer> money = new ArrayList<>();
        money.add(nums[0]);
        money.add(Math.max(nums[0], nums[1]));

        for(int i=2; i<nums.length; i++) {
            money.set(0, Math.max(money.get(0)+nums[i], money.get(1)));
            Collections.swap(money, 0 , 1);
        }

        return money.get(1);
    }
}
