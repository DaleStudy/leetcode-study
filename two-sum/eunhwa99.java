// 문제 요구사항 -> O(n^2) 보다 작은 시간복잡도로 구현 필요
// 문제를 보자마자 생각난 것 -> 이분탐색 (2 원소 합이 target 인 것을 구해야 하므로)
// 이분 탐색 시간 복잡도 -> 정렬(O(nlogn)) + 이분탐색 (log(n)) -> nlogn
// 공간 복잡도 -> 배열 크기 만큼 공간 필요 (n)

import java.util.Arrays;
import java.util.HashMap;

class ValueIndex implements Comparable<ValueIndex> {
    int value;
    int index;

    // ValueIndex 객체를 정렬할 때 value 기준으로 오름차순 정렬
    @Override
    public int compareTo(ValueIndex other) {
        return Integer.compare(this.value, other.value);
    }
}

class Solution {

    public int[] twoSum(int[] nums, int target) {
        int size = nums.length;
        ValueIndex[] valueIndex = new ValueIndex[size];
        for (int i = 0; i < size; ++i) {
            valueIndex[i] = new ValueIndex();
            valueIndex[i].value = nums[i];
            valueIndex[i].index = i; // 정렬 전 original index 저장
        }
        Arrays.sort(valueIndex); // 정렬
        int left = 0;
        int right = nums.length - 1;

        while (left < right) {
            int leftVal = valueIndex[left].value;
            int rightVal = valueIndex[right].value;
            int sum = leftVal + rightVal;

            if (sum < target) { // target 보다 합이 작으면, left 값이 커져야 함
                left += 1;
            } else if (sum > target) {
                right -= 1; // target 보다 합이 크면, right 값이 작아져야 함
            } else { // sum = target 이면 끝!
                break;
            }
        }

        return new int[]{valueIndex[left].index, valueIndex[right].index};
    }
}


/**
 * hashMap을 이용한 O(n) 방법도 있다고 해서 추가 구현해보았습니다. (시간/공간 복잡도 O(n))
 */

class Solution {

    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> numMap = new HashMap<>();
        int left = 0, right = 0;
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i]; // 현재 숫자와 합쳐서 target을 만드는 숫자

            // 이미 그 숫자가 해시맵에 있다면, 두 인덱스를 반환
            if (numMap.containsKey(complement)) {
                left = numMap.get(complement);
                right = i;
                break;
            }

            // 해시맵에 현재 숫자와 인덱스를 추가
            numMap.put(nums[i], i);
        }

        return new int[]{left, right};

    }
}
