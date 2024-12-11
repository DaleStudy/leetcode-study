import java.util.*;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        //value값을 통한 key 정렬
        List<Integer> list = new ArrayList<>(map.keySet());
        list.sort((a,b)->map.get(b) - map.get(a));

        //상위 k개 key 추출
        int[] res = new int[k];
        for (int i = 0; i < k; i++) {
            res[i] = list.get(i);
        }
        return res;
    }
}
