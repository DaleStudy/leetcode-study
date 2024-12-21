/*
    Problem: https://leetcode.com/problems/3sum/
    Description: return all the triplets (i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0)
    Concept: Array, Two Pointers, Sorting
    Time Complexity: O(N²), Runtime 70ms
    Space Complexity: O(N), Memory 51.63MB
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
            if(i>0 && nums[i]==nums[i-1]) continue;

            for(int j=i+1; j<nums.length; j++){
                if(j>i+1 && nums[j]==nums[j-1]) continue;

                int target = -(nums[i]+nums[j]);
                if(nums[j]>target) continue;

                int count = number.getOrDefault(target,0);
                if(nums[i]==target) count--;
                if(nums[j]==target) count--;
                if(count<=0) continue;

                List<Integer> triplet = List.of(nums[i], nums[j], target);
                if(triplet.equals(lastTriplet)) continue;
                lastTriplet = triplet;
                triplets.add(triplet);
            }
        }
        return triplets;
    }
}
