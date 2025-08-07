import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;

public class Geegong {


    public int[] topKFrequent(int[] nums, int k) {
        int[] result = new int[k];

        // key : num element in nums / value : frequency of num elements
        Map<Integer, Integer> numMap = new HashMap<>();

        // key : frequency of num elements / value : HashSet<Integer> num elements
        Map<Integer, HashSet<Integer>> frequencyMap = new HashMap<>();

        // most frequent numbers
        int maxCount = 0;

        // initialize numMap
        for (int num : nums) {
            if (numMap.containsKey(num)) {
                Integer alreadyCounted = numMap.get(num);
                numMap.put(num, alreadyCounted + 1);
            } else {
                numMap.put(num, 1);
            }
        }


        //numHashSetMap
        for (int num : numMap.keySet()) {
            int frequencyOfNum = numMap.get(num);
            maxCount = Math.max(maxCount, frequencyOfNum);

            if (frequencyMap.containsKey(frequencyOfNum)) {
                HashSet<Integer> alreadySet = frequencyMap.get(frequencyOfNum);
                alreadySet.add(num);

                frequencyMap.put(frequencyOfNum, alreadySet);

            } else {
                HashSet<Integer> newHashSet = new HashSet<>();
                newHashSet.add(num);

                frequencyMap.put(frequencyOfNum, newHashSet);
            }
        }


        // maxCount 부터 decreasing
        int resultIndex=0;
        for(int frequency=maxCount; frequency>=0; frequency--) {
            if (resultIndex >= result.length) {
                return result;
            }

            if (frequencyMap.containsKey(frequency)) {
                HashSet<Integer> numElements = frequencyMap.get(frequency);

                for (int numElement : numElements) {
                    result[resultIndex] = numElement;
                    resultIndex++;


                    if (resultIndex >= result.length) {
                        return result;
                    }
                }
            }
        }

        return result;
}

