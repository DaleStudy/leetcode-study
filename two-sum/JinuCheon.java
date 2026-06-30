// Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
// O(n2)
// class Solution1 {
//     public int[] twoSum(int[] nums, int target) {
//         int size = nums.length;
//         for (int i=0; i<size; i++) {
//             for (int j=0; j<size; j++) {
//                 if (i==j) continue;
//                 if (nums[i] + nums[j] == target) {
//                     return new int[]{i, j};
//                 }
//             }
//         }
//         throw new IllegalArgumentException();
//     }
// }


// I spent almost 20m thinking about this, but couldn't come up any ideas.
// Finally I asked to LLM, there was a crazy solution.
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int pair = target - nums[i];

            if (map.containsKey(pair)) {
                return new int[]{i, map.get(pair)};
            }

            map.put(nums[i], i);
        }
        throw new IllegalArgumentException();
    }
}
