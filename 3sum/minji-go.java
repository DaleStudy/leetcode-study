/**
 * <a href="https://leetcode.com/problems/3sum/">week02-4.3sum</a>
 * Description: return all the triplets (i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0)
 * Concept: Array, Two Pointers, Sorting
 * Time Complexity: O(N²), Runtime 2021ms
 * Space Complexity: O(N), Memory 53.9MB
 */

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int i=0; i<nums.length; i++){
            map.put(nums[i], i);
        }

        Set<List<Integer>> triplets = new HashSet<>();
        for(int i=0; i<nums.length-2; i++){
            for(int j=i+1; j<nums.length-1; j++){
                int sum = nums[i]+nums[j];
                if(map.containsKey(-sum) && map.get(-sum) > j){
                    List<Integer> list = Arrays.asList(nums[i],nums[j],-sum);
                    Collections.sort(list);
                    triplets.add(list);
                }
            }
        }

        return new ArrayList<>(triplets);
    }
}
