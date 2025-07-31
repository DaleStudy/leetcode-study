import java.util.*;

public class Geegong {

    /**
     * Time complexity : O(n^2)
     * space complexity : O(n^2)
     * @param nums
     * @return
     */
    public List<List<Integer>> threeSum(int[] nums) {

        // 중복되는 값은 없어야 하기에 HashSet 으로 result
        HashSet<List<Integer>> result = new HashSet<>();

        // Key : 배열 원소 , value : List<String> 인덱스들
        // elementMap 은 two pointer 의 값을 더한 값에서 0이 되기 위한 요소를 찾기위해 사용될 것임
        // tc : O(n)
        Map<Integer, List<Integer>> elementMap = new HashMap<>();
        for (int index = 0; index<nums.length; index++) {
            int value = nums[index];
            if (elementMap.containsKey(value)) {
                List<Integer> indices = elementMap.get(value);
                indices.add(index);
                elementMap.put(value, indices);
            } else {
                List<Integer> newIndices = new ArrayList<>();
                newIndices.add(index);
                elementMap.put(value, newIndices);
            }
        }

        // leftIndex : 0에서 부터 시작하는 index
        // rightIndex : nums.length - 1에서부터 감소하는 index
        // leftIndex > rightIndex 되는 순간까지만 for문을 돌 것이다.
        // tc : O(N^2 / 2)
        for (int leftIndex=0; leftIndex < nums.length; leftIndex++) {
            for (int rightIndex=nums.length - 1; rightIndex >= 0; rightIndex--) {

                if (leftIndex >= rightIndex) {
                    break;
                }


                int leftValue = nums[leftIndex];
                int rightValue = nums[rightIndex];

                int neededValueToZero = -leftValue - rightValue;
                if (elementMap.containsKey(neededValueToZero)) {
                    // elementMap의 value 가 leftIndex, rightIndex 은 아닌지 확인

                    List<Integer> indices = elementMap.get(neededValueToZero);
                    // zero 를 만들 수 있는 세번쨰 인덱스가 있는지 확인
                    int thirdIndex = findThirdIndexToBeZero(leftIndex, rightIndex, indices);
                    if (-1 != thirdIndex) {
                        List<Integer> newOne = new ArrayList<>();
                        newOne.add(nums[leftIndex]);
                        newOne.add(nums[rightIndex]);
                        newOne.add(nums[thirdIndex]);
                        result.add(newOne.stream().sorted().toList());
                    }

                }

            }
        }

        return result.stream().toList();

    }

    public int findThirdIndexToBeZero(int leftIndex, int rightIndex, List<Integer> indices) {
        for (int index : indices) {
            if (index != leftIndex && index != rightIndex) {
                return index;
            }
        }

        return -1;
    }
}

