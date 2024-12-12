/*
    Problem: https://leetcode.com/problems/contains-duplicate/
    Description: return true if any value appears at least twice in the array
    Concept: Array, Hash Table, Sorting
    Time Complexity: O(n), Runtime: 10ms
    Space Complexity: O(n), Memory: 58.6MB
*/
import java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> count = new HashSet<>();
        boolean answer = false;
        for(int num : nums){
            if(count.contains(num)) {
                answer = true;
                break;
            }
            count.add(num);
        }
        return answer;
    }
}
