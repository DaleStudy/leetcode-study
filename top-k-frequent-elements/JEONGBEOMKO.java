import java.util.Arrays;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        
        Map<Integer, Integer> frequencyMap = new HashMap<>();
        for(int num : nums) {
            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
        }

        Map.Entry<Integer, Integer>[] arr = new Map.Entry[frequencyMap.size()];
        Iterator<Map.Entry<Integer, Integer>> iterator = frequencyMap.entrySet().iterator();
        for (int i=0; i<arr.length; i++) {
            arr[i] = iterator.next();
        }

        Arrays.sort(arr, (e1, e2) -> e2.getValue() - e1.getValue());

        int[] answer = new int[k];
        for (int i=0; i<k; i++) {
            answer[i] = arr[i].getKey();
        }

        return answer;
    }
}
