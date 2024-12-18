import java.util.*;
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> count = new HashMap<>();
        for(int i=0;i<nums.length;i++){
            count.put(nums[i],count.getOrDefault(nums[i],0)+1);
        }
        List<Integer> sortedCount = new ArrayList<>(count.keySet());
        sortedCount.sort((a,b)->count.get(b)-count.get(a));//value 기준 키 정렬
        int[] answer = new int[k];
        for(int i=0;i<k;i++){
            answer[i] = sortedCount.get(i);
        }
        
        return answer;
    }
}
