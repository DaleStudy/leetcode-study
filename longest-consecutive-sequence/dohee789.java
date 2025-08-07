/*
https://leetcode.com/problems/longest-consecutive-sequence/
 */
class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for(int num: nums){
            set.add(num);
        }

        int maxLength = 0;
        for(int num: set){
            if(!set.contains(num-1)){
                int currentNum = num;
                int length = 1;
                while(set.contains(currentNum+1)){
                    currentNum++;
                    length++;
                }
                maxLength = Math.max(maxLength,length);
            }
        }
        return maxLength;
    }
}

