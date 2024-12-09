// 각 수의 개수를 카운트 하고 카운트 한 값을 기준으로 정렬하여 우선순위 큐로
// k개를 추출하여 result 리스트에 담는다.

// 시간복잡도 : O(NlogN)
// 공간복잡도 : O(N)


public class SolutionGotprgmer {

    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int num:nums){
            map.put(num,map.getOrDefault(num,0)+1);
        }
        PriorityQueue<Map.Entry<Integer, Integer>> pq = new PriorityQueue<>(
                (e1, e2) -> e2.getValue().compareTo(e1.getValue())
        );
        for (Map.Entry<Integer,Integer> entry : map.entrySet()){
            pq.offer(entry);
        }

        int[] result = new int[k];
        for(int ansIdx=0;ansIdx < k; ansIdx++){
            result[ansIdx] = pq.poll().getKey();
        }
        return result;
    }
}
