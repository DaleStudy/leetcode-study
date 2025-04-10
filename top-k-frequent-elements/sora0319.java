import java.util.*;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> counts = new HashMap<>();
        List<Integer> ordering = new ArrayList<>();
        int[] results = new int[k];

        for(int n : nums){
            if(counts.containsKey(n)){
                counts.put(n, counts.get(n)+1);
                continue;
            }
            counts.put(n, 1);
            ordering.add(n);
        }

        ordering.sort((o1,o2) -> counts.get(o2) - counts.get(o1));
        for(int i = 0; i < k; i++){
            results[i] = ordering.get(i);
        }

        return results;
    }
}

