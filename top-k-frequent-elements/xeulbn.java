import java.util.*;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> countMap = new HashMap<>();

        for(int i=0;i<nums.length;i++){
            countMap.put(nums[i],countMap.getOrDefault(nums[i],0)+1);
        }
        PriorityQueue<Integer> pq = new PriorityQueue<>(
                (a,b)-> countMap.get(a) - countMap.get(b)
        );

        for(int num: countMap.keySet()){
            pq.offer(num);

            if(pq.size()>k){
                pq.poll();
            }
        }

        int[] answer = new int[k];

        for (int i = 0; i < k; i++) {
            answer[i] = pq.poll();
        }

        return answer;

    }
}
