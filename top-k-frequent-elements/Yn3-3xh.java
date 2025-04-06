/*
[문제풀이]
time: O(N log N), space: O(N + k)
- 주어진 Nums의 중복된 수의 갯수를 Map에 담고,
- 역정렬하면,
- k만큼 뽑기
class Solution1 {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> counting = new HashMap<>();
        for (int num: nums) {
            int numCount = counting.getOrDefault(num, 0) + 1;
            counting.put(num, numCount);
        }

        List<Map.Entry<Integer, Integer>> sortedCounting = new ArrayList<>(counting.entrySet());
        sortedCounting.sort(Map.Entry.comparingByValue(Comparator.reverseOrder()));

        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = sortedCounting.get(i).getKey();
        }

        return result;
    }
}

time: O(N log k), space: O(N + k)
- PriorityQueue 사용
- value로 역정렬 설정
- key로 queue에 add

[회고]
첫번째 풀이는 역정렬 하는 부분이 미숙했고,
두번째 풀이는 PriorityQueue를 사용하는데 처음 써본다.. (익히자!)
*/
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> counting = new HashMap<>();
        for (int num: nums) {
            int numCount = counting.getOrDefault(num, 0) + 1;
            counting.put(num, numCount);
        }

        Queue<Integer> queue = new PriorityQueue<>((count1, count2) ->
                counting.get(count2) - counting.get(count1));
        queue.addAll(counting.keySet());

        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = queue.poll();
        }
        return result;
    }
}
