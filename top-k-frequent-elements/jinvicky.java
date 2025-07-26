import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // [풀이]
        // 1. <숫자: 빈도수>를 저장하는 HashMap과 [빈도수, 숫자]를 저장하는 PriorityQueue를 선언한다.
        // 2. HashMap에 숫자별로 빈도수를 함께 저장해서 해시테이블을 만든다.
        // [우선순위 큐에 사용된 자료구조]
        // 1. 별도 클래스를 선언
        // 2. 요구사항 자료형 배열을 선언한다.
        // 처음에는 별도 클래스를 선언했다가 값이 2개이며 알고리즘 로직 자체가 어려워서 int[] 구조로 풀이했다.
        // (주로 알고리즘이 어려우면 가독성이 나쁘더라도 자료구조를 단순화하는 습관이 있다)
        // [어려웠던 점]
        // 1. 우선순위 큐는 매번 요소가 추가될 때마다 내부 정렬을 수행하기 때문에 연산을 수행하면서 k개를 유지해야 한다.
        // 또한 기존 [빈도수, 숫자]를 버려야만 올바른 답을 도출할 수 있었다.
        // 2. [숫자, 빈도수]로 저장하는 것만 생각했더니 내부 정렬을 어떻게 하지 못해서 굉장히 고민했다. 정답은 반대였다.

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
