/*
    Problem: https://leetcode.com/problems/3sum/
    Description: return all the triplets (i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0)
    Concept: Array, Two Pointers, Sorting
    Time Complexity: O(N²), Runtime 1107ms
    Space Complexity: O(N), Memory 54.20MB
*/
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Map<Integer, Integer> number = new HashMap<>();
        for(int i=0; i<nums.length; i++) {
            number.put(nums[i], number.getOrDefault(nums[i], 0)+1);
        }

        Arrays.sort(nums);
        Set<List<Integer>> set = new HashSet<>();
        List<List<Integer>> triplets = new ArrayList<>();
        List<Integer> lastTriplet = null;
        for(int i=0; i<nums.length-1; i++) {
            for(int j=i+1; j<nums.length; j++){
                int twoSum = nums[i]+nums[j];
                if(nums[j]>-twoSum) continue;

                int count = number.getOrDefault(-twoSum,0);
                if(nums[i]==-twoSum) count--;
                if(nums[j]==-twoSum) count--;
                if(count<=0) continue;

                List<Integer> triplet = List.of(nums[i], nums[j], -twoSum);
                int setSize = set.size();
                set.add(triplet);
                if(setSize != set.size()) triplets.add(triplet);
            }
        }
        return triplets;
    }
}
