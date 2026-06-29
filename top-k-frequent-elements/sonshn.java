
/**
 * 풀이
 * 1. 빈도수 계산
 * - HashMap<Integer, Integer>을 사용하여 각 숫자의 등장 횟수를 저장
 * - Key는 숫자, Value는 해당 숫자의 빈도수
 * 2. 고유 숫자 저장
 * - counter.keySet()을 ArrayList로 변환하여 중복 없이 숫자들만 저장
 * 3. 빈도수 기준 내림차순 정렬
 * - list.sort((a, b) -> Integer.compare(counter.get(b), counter.get(a)))
 * - HashMap에 저장된 빈도수를 기준으로 많이 등장한 숫자가 앞에 오도록 정렬
 * 4. 상위 k개 반환
 * - 정렬된 리스트의 앞에서부터 k개의 숫자를 result 배열에 담아 반환
 * 
 * 시간 복잡도: O(n log n)
 * 공간 복잡도: O(n)
 */
class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        Map<Integer, Integer> counter = new HashMap<>();

        for (int num : nums) {
            counter.put(num, counter.getOrDefault(num, 0) + 1);
        }

        List<Integer> list = new ArrayList<>(counter.keySet());

        // 빈도수 내림차순 정렬
        list.sort((a, b) -> Integer.compare(counter.get(b), counter.get(a)));

        int[] result = new int[k];

        for (int i = 0; i < k; i++) {
            result[i] = list.get(i);
        }

        return result;
    }
}
