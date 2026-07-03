import java.util.*;

class Solution {
    // TC: O(n log n)
    // SC: O(n)
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>();
        for ( int i = 0; i < nums.length; i++){
            count.put(nums[i], count.getOrDefault(nums[i],0)+ 1);
        }

        PriorityQueue<Integer> heap = new PriorityQueue<>((a,b) -> count.get(a) - count.get(b));

        for ( int key : count.keySet()){
            heap.offer(key);
            if ( heap.size() > k ){
                heap.poll();
            }
        }

        int[] result = new int[k];
        for ( int i = 0; i < k; i++){
            result[i] = heap.poll();
        }
        return result;
    }
}
