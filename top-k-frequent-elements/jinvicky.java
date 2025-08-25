import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        /**
         * for문이 총 3번 필요하다. (1.빈도_초기화, 2.큐에 저장, 3.결과배열에 할당
         * 빈도_초기화 -> k:v로 쉽게 저장하는 자료구조
         * 큐에 저장  -> 최소 힙으로 정렬되는 우선순위 큐 선언 -> 큐 같은 자료구조에서 k:v를 하고 싶다면 new int[2]가 가장 쉬움
         * 결과배열에 할당 -> k개만큼 answer[]에 저장
         *
         * 문제는 상위 k개를 유지해야 하고 그를 위해서는 k개를 넘었을 때 빈도수가 낮은 순으로 flush하는 로직이 필요하다는 것.
         * 큐는 선입선출 -> 빈도수가 낮을 수록 위로 정렬되게 해야 flush했을 때 빈도수가 낮은 순서대로 사라진다.
         *
         * 결과배열에 할당할 때는 그냥 앞에서부터 하면 된다.
         * 이미 k개를 만족했고, 빈도수가 낮 -> 높 순서대로 그대로 쌓으면 된다.
         *
         * 우선순위큐에 할당할 때 [숫자, 빈도수]냐 [빈도수, 숫자] 냐는 별 상관이 없다.
         * 1. 우선순위 큐 초기화
         * 2. 결과배열에 값 할당할 때 참조하는 [인덱스]
         */
        int[] answer = new int[k];

        Map<Integer, Integer> map = new HashMap<>();
        for (int n : nums) {
            map.put(n, map.getOrDefault(n, 0) + 1);
        }
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);

        for (int key : map.keySet()) {
            pq.add(new int[]{map.get(key), key});
            if (pq.size() > k) {
                pq.poll();
            }
        }

        for (int i = 0; i < k; i++) {
            if (!pq.isEmpty()) {
                answer[i] = pq.poll()[1];
            }
        }
        return answer;
    }
}
