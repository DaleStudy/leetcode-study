/*
    Problem: https://leetcode.com/problems/longest-consecutive-sequence/
    Description: return the length of the longest consecutive elements sequence
    Concept: Array, Hash Table, Union Find
    Time Complexity: O(n), Runtime: 1141ms
    Space Complexity: O(n), Memory: 66.74MB
*/
import java.util.HashSet;
import java.util.Set;

class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for(int num: nums) {
            set.add(num);
        }

        int answer = 0;
        for(int num: nums){
            if(set.contains(num-1)){ //contains(): O(1)
                continue;
            }
            int length = 1;
            while (set.contains(num+length)){
                length++;
            }
            answer = Math.max(answer, length);
        }

        return answer;
    }
}
