/*
    Problem: https://leetcode.com/problems/top-k-frequent-elements/
    Description: return the k most frequent elements
    Concept: Array, Hash Table, Divide and Conquer, Sorting, Heap (Priority Queue), Bucket Sort, Counting, Quickselect
    Time Complexity: O(n log k), Runtime: 15ms
    Space Complexity: O(n), Memory: 48.64MB
*/
import java.util.*;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>();
        for(int num : nums){
            count.put(num, count.getOrDefault(num, 0)+1);
        }

        PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.comparingInt(count::get));
        for (int num : count.keySet()) {
            pq.offer(num);
            if (pq.size() > k) pq.poll();
        }

        int[] answer = new int[k];
        for(int i=0; i<k; i++) {
            answer[i] = pq.poll();
        }
        return answer;
    }
}
