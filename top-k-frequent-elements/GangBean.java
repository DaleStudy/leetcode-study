import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        /**
            k번째로 많이 등장한 숫자를 구하는 문제.
            구해야 하는 것.
            1. 등장횟수의 순위
            2. k번째 순위에 해당하는 수의 값

            1. 등장 횟수를 구하는 방법: 전체를 순회해 숫자별 등장 횟수를 저장 -> O(N)
            2. 등장 횟수의 순위를 구하는 방법: 등장 횟수에 대해 sort 
                -> O(MlogM) where N = M(M+1) / 2
                -> logN = logM + log(M+1) + C
                -> M = N^(1/2)
                -> O(MlogM) = O(N^1/2logN) (??? 여기가 맞는지 모르겠네요..)
            3. 역 인덱스를 구해 매핑되는 수를 구함 -> O(N)

            전체: O(N)
         */
        Map<Integer, Integer> numToCount = new HashMap<>();
        for (int num : nums) { // O(N)
            numToCount.put(num, numToCount.getOrDefault(num, 0) + 1);
        }

        Map<Integer, List<Integer>> countToNum = new HashMap<>();
        for (Map.Entry<Integer, Integer> entry: numToCount.entrySet()) {
            List<Integer> numList = countToNum.getOrDefault(entry.getValue(), new ArrayList<>());
            numList.add(entry.getKey());
            countToNum.put(entry.getValue(), numList);
        } // O(logN): because sum of all counts is equal to N

        List<Integer> countRank = countToNum.keySet().stream().sorted(Collections.reverseOrder()).collect(Collectors.toList()); 
        // O(MlogM) where N = M(M+1) / 2

        int[] ret = new int[k];
        int idx = 0;
        int rank = 0;
        while (idx < k) { // O(k) <= O(N)
            for (int num : countToNum.get(countRank.get(rank++))) {
                ret[idx++] = num;
            }
        }
        return ret;
    }
}
