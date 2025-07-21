import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Map;

public class Geegong {

    public int[] topKFrequent(int[] nums, int k) {
        int[] result = new int[k];

        // key : key / value : count
        Map<Integer, Integer> keyMap = new HashMap<>();

        // key : count / value : HashSet<Integer> keys
        Map<Integer, HashSet<Integer>> countMap = new HashMap<>();

        // 가장 많이 출연한 친구
        int maxCount = 0;

        for (int num : nums) {
            int countToBePut = 0;

            if (keyMap.containsKey(num)) {
                Integer alreadyCounted = keyMap.get(num);
                countToBePut = alreadyCounted + 1;
                keyMap.put(num, countToBePut);

                checkCountMapAndPutCount(countMap, num, countToBePut);
            } else {
                countToBePut = 1;
                keyMap.put(num, countToBePut);
                checkCountMapAndPutCount(countMap, num, countToBePut);
            }

            maxCount = Math.max(maxCount, countToBePut);
        }


        // 가장 큰 숫자부터 꺼내볼까요오오오 우후
        int kIndex=0;
        for (int index=maxCount; index >= 0; index--) {
            if (kIndex >= k) {
                return result;
            }

            if (countMap.containsKey(index)) {
                HashSet<Integer> hashNums = countMap.get(index);
                Iterator<Integer> iterator = hashNums.iterator();
                while(iterator.hasNext()) {

                    if (kIndex >= k) {
                        return result;
                    }

                    result[kIndex] = iterator.next();
                    kIndex++;
                }

            }

        }

        return result;


    }

    public void checkCountMapAndPutCount(Map<Integer, HashSet<Integer>> countMap, int key, int count) {
        if (countMap.containsKey(count)) {
            HashSet<Integer> already = countMap.get(count);
            already.add(key);
        } else {
            HashSet<Integer> newSet = new HashSet<>();
            newSet.add(key);
            countMap.put(count, newSet);
        }

    }

}

