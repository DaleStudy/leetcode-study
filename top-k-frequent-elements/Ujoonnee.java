import java.util.Arrays;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // 배열의 숫자가 몇 번씩 등장하는지 저장
        Map<Integer, Integer> frequencyMap = new HashMap<>();
        for(int num : nums) {
            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
        }

        // Map 형식의 데이터를 [숫자, 빈도] 의 배열로 변환
        Map.Entry<Integer, Integer>[] arr = new Map.Entry[frequencyMap.size()];
        Iterator<Map.Entry<Integer, Integer>> iterator = frequencyMap.entrySet().iterator();
        for (int i=0; i<arr.length; i++) {
            arr[i] = iterator.next();
        }

        // 빈도 기준 내림차순 정렬
        Arrays.sort(arr, (e1, e2) -> e2.getValue() - e1.getValue());

        // k개만 꺼내기
        int[] answer = new int[k];
        for (int i=0; i<k; i++) {
            answer[i] = arr[i].getKey();
        }

        return answer;
    }
}
