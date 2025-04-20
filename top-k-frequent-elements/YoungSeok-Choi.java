import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


// O(nlogn) 시간복잡도.

class Solution {    
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freqMap = new HashMap<>();
        int[] res = new int [k];

        for(int i = 0; i < nums.length; i++) {
            if(freqMap.containsKey(nums[i])) {
                freqMap.put(nums[i], freqMap.get(nums[i]) + 1);
            } else {
                freqMap.put(nums[i], 1);
            }
        }

        List<Map.Entry<Integer, Integer>> entList = new ArrayList<>(freqMap.entrySet());

        entList.sort((a, b) -> b.getValue().compareTo(a.getValue()));
        
        for(int i = 0; i < res.length; i++) {
            res[i] = entList.get(i).getKey();
        }

        return res;
    }
}
