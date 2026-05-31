import java.util.*;
/**
 * 1 .문제 정의

 배열이 있는데 여기서 각 숫자가 등장한 빈도수를 체크하고 K번째 까지 높은 빈도로 등장한 수를 리턴하는 문제입니다.

 - n의 길이는 1 ~ 10000

 * 2. naive algorithm 도출

 배열을 순회함면서 Map에 넣으면서 빈도수를 체크.
 빈도수 계산이 끝나고 나면 빈도수를 기준으로 내림차순 정렬

 *
 * 3. 시간&공간복잡도 분석
 * O(N) + O(M) + O(M log M) + O(K) = O(N + N log N) = O(N log N)

 * 4. 코드작성
 */
class sangyyypark {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++) {
            int num = nums[i];
            if(map.containsKey(num)) {
                map.put(num, map.get(num) + 1);
            }
            else {
                map.put(num,1);
            }
        }

        List<Integer> keySet = new ArrayList<>(map.keySet());
        keySet.sort(new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return map.get(o2).compareTo(map.get(o1));
            }
        });

        int [] result = new int[k];
        int index = 0;
        for(int i = 0; i < k; i++) {
            result[index] = keySet.get(i);
            index++;
        }
        return result;
    }
}

