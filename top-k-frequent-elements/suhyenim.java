/* [5th/week01] 347. Top K Frequent Elements

1. 문제 요약
링크: https://leetcode.com/problems/top-k-frequent-elements/description/
가장 빈도가 높은 k개의 숫자를 배열로 반환

2. 풀이 로직
풀이1: 빈도 HashMap을 만들고 -> 높은 빈도 순으로 key 정렬 -> top k까지만 배열로 반환
성공: Time: 17 ms (12.72%), Space: 48.9 MB (34.62%)
=> 시간 복잡도: O(nlogn), 공간 복잡도: O(n)

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>();
        for(int n : nums) {
            if(!count.containsKey(n)) {
                count.put(n, 1);
            } else {
                count.put(n, count.get(n) + 1);
            }
        }

        List<Integer> keys = new ArrayList<>(count.keySet());
        keys.sort((a, b) -> count.get(b) - count.get(a));

        int[] answer = new int[k];
        for (int i = 0; i < k; i++){
            answer[i] = keys.get(i);
        }
        
        return answer;
    }
}

3. TIL
value값 기준으로 key를 내림차순 정렬하는 방법: keys.sort((a, b) -> count.get(b) - count.get(a));

*/

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>();
        for(int n : nums) {
            if(!count.containsKey(n)) {
                count.put(n, 1);
            } else {
                count.put(n, count.get(n) + 1);
            }
        }

        List<Integer> keys = new ArrayList<>(count.keySet());
        keys.sort((a, b) -> count.get(b) - count.get(a));

        int[] answer = new int[k];
        for (int i = 0; i < k; i++){
            answer[i] = keys.get(i);
        }
        
        return answer;
    }
}
