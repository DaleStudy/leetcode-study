/*
time complexity : O(n)
space complexity : O(n)
*/
class Solution {
    public int longestConsecutive(int[] nums) {
        int maxLen = 0;
        Set<Integer> numSet = new HashSet<Integer>();
        for (int num: nums) {
            numSet.add(num);
        }

        for (int num : numSet) {
            if (!numSet.contains(num - 1)){
                int continueCnt = 1;
                int current = num;

                while (numSet.contains(current + 1)) {
                    current++;
                    continueCnt++;
                }
                maxLen = Math.max(continueCnt, maxLen);
            }
        }        
        return maxLen;    
    }
}
