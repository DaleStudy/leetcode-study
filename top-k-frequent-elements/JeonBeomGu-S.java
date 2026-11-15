import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * 시간 복잡도: O(nlogn) - 배열의 길이 n 만큼 반복문과 정렬
 * 공간 복잡도: O(n) - 배열의 길이 n 만큼의 맵, 리스트와 답을 저장할 배열의 크기 k
 *                  k는 최대 n을 넘지 못하므로 무시
 */

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap();
        for (int num : nums) {
            if (map.containsKey(num)) {
                map.put(num, map.get(num) + 1);
            } else {
                map.put(num, 1);
            }
        }

        List<Integer> list = new ArrayList<>(map.keySet());
        list.sort((a, b) -> map.get(b) - map.get(a));

        int[] answer = new int[k];
        for (int i = 0; i < k; i++) {
            answer[i] = list.get(i);
        }

        return answer;
    }
}
