import java.util.*;



public class Geegong {


    /**
     * Map 으로 빈도수를 key , 빈도수에 해당되는 num 들을 list 로 저장
     * key (빈도수) 를 sorting
     * k 만큼 골라낸다
     * Time Complexity : O(N) + O(N logN) + O(N)
     *    - O(N) : nums 만큼 iterate
     *    - O(N log N) : sorting
     *    - O(N) : frequency 그룹핑된 그룹 갯수만큼 iterate
     * @param nums
     * @param k
     * @return int[]
     */
    public int[] topKFrequent(int[] nums, int k) {

        // key : frequency , value : list of nums
        Map<Integer, List<Integer>> map = new HashMap<>();
        Arrays.sort(nums);
        int current = nums[0];
        int count = 1;

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == current) {
                count++;
            } else {
                map.computeIfAbsent(count, el -> new ArrayList<>()).add(current);
                current = nums[i];
                count = 1;
            }
        }

        // Add last group
        map.computeIfAbsent(count, el -> new ArrayList<>()).add(current);

        List<Integer> sortedFrequency = map.keySet().stream().sorted(Comparator.reverseOrder()).toList();
        List<Integer> result = new ArrayList<>();
        for (int index=0; index<sortedFrequency.size(); index++ ) {
            int mostFrequency = sortedFrequency.get(index);
            List<Integer> numsOfFreq = map.get(mostFrequency);

            for(int innerIndex = 0; innerIndex<numsOfFreq.size(); innerIndex++) {
                if (result.size() == k) {
                    return result.stream().mapToInt(Integer::intValue).toArray();
                }

                result.add(numsOfFreq.get(innerIndex));
            }

        }

        return result.stream().mapToInt(Integer::intValue).toArray();

// 아래 문제풀이는 예전 기수에 풀었던 방법으로 Map 으로 빈도수와 num을 관리하는 값을 가지긴 하나
// sorting은 하지 않고 maxNumOfFrequency를 구하여 순차적으로 작은 값들을 꺼내서 k만큼 리턴한다
//        int[] result = new int[k];
//
//        // key : num element in nums / value : frequency of num elements
//        Map<Integer, Integer> numMap = new HashMap<>();
//
//        // key : frequency of num elements / value : HashSet<Integer> num elements
//        Map<Integer, HashSet<Integer>> frequencyMap = new HashMap<>();
//
//        // most frequent numbers
//        int maxCount = 0;
//
//        // initialize numMap
//        for (int num : nums) {
//            if (numMap.containsKey(num)) {
//                Integer alreadyCounted = numMap.get(num);
//                numMap.put(num, alreadyCounted + 1);
//            } else {
//                numMap.put(num, 1);
//            }
//        }
//
//
//        //numHashSetMap
//        for (int num : numMap.keySet()) {
//            int frequencyOfNum = numMap.get(num);
//            maxCount = Math.max(maxCount, frequencyOfNum);
//
//            if (frequencyMap.containsKey(frequencyOfNum)) {
//                HashSet<Integer> alreadySet = frequencyMap.get(frequencyOfNum);
//                alreadySet.add(num);
//
//                frequencyMap.put(frequencyOfNum, alreadySet);
//
//            } else {
//                HashSet<Integer> newHashSet = new HashSet<>();
//                newHashSet.add(num);
//
//                frequencyMap.put(frequencyOfNum, newHashSet);
//            }
//        }
//
//
//        // maxCount 부터 decreasing
//        int resultIndex=0;
//        for(int frequency=maxCount; frequency>=0; frequency--) {
//            if (resultIndex >= result.length) {
//                return result;
//            }
//
//            if (frequencyMap.containsKey(frequency)) {
//                HashSet<Integer> numElements = frequencyMap.get(frequency);
//
//                for (int numElement : numElements) {
//                    result[resultIndex] = numElement;
//                    resultIndex++;
//
//
//                    if (resultIndex >= result.length) {
//                        return result;
//                    }
//                }
//            }
//        }
//
//        return result;
    }
}

