class Solution {
    /**
     *   사고의 흐름:
     *   - Map 이용해서 각 키 값 별로 몇 개가 있는지 저장하자.
     *   - 일단 주어진 모든 배열을 확인해야 한다.
     *   - 정렬이 필요하겠다.
     *   - Map의 값을 기준으로 정렬을 하는데, 키 값도 같이 따라와야겠네?
     *     - Comparable? Comparator? (하 ... 이거 어떻게 했더라..)
     *
     *   시간 복잡도: O(NlogN)
     *   - ArrayList sort() 는 Merge Sort
     *   - Merge Sort 는 O(NlogN)
     *
     *   공간 복잡도: O(N)
     *   - 최악의 경우 주어진 배열의 모든 원소가 자료구조에 저장되므로 O(N)
     */
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int num: nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        List<Map.Entry<Integer, Integer>> list = new ArrayList<>(map.entrySet());
        list.sort(new Comparator<Map.Entry<Integer, Integer>>() {
            @Override
            public int compare(Map.Entry<Integer, Integer> e1, Map.Entry<Integer, Integer> e2) {
                return e2.getValue().compareTo(e1.getValue());
            }
        });

        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = list.get(i).getKey();
        }

        return result;
    }
}
