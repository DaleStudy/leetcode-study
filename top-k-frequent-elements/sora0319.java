import java.util.*;
// 다른 방안
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map <Integer,Integer> counting = new HashMap<>();

        for(int n : nums){
            if(!counting.containsKey(n)){
                counting.put(n,0);
            }
            counting.put(n, counting.get(n)+1);
        }

        List<Map.Entry<Integer,Integer>>countList = new LinkedList<>(counting.entrySet());
        countList.sort(Map.Entry.comparingByValue(Comparator.reverseOrder()));
        
        int[] answer = countList.stream()
        .limit(k)
        .mapToInt(Map.Entry::getKey)
        .toArray();
        return answer;
    }
}


// 초안
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

