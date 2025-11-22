/*
1. 문제분석
3개의 수를 더해서 0을 만들자

2. 예외 케이스

3. 알고리즘
2포인터 활용

4. 구현

[-4, -1, -1, 0, 1, 2]

배열을 정렬하고 2개의 포인터를 잡은 뒤 더한 값의 -한 값이 배열 내에 존재하는지 체크
배열의 i 값과 2개 포인터를 모두 더한 값이 음수라면 left를 우측으로 이동
배열의 i 값과 2개 포인터를 모두 더한 값이 양수라면 right를 좌측으로 이동 
*/

import java.util.*;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        Set<List<Integer>> set = new HashSet<>();

        for (int i=0; i<nums.length; i++) {
            // target 변수 세팅
            int target = nums[i];
            int left = i+1;
            int right = nums.length - 1;

            // left, right 포인터 서로 이동
            while (left < right) {
                int leftInt = nums[left];
                int rightInt = nums[right];

                if ((target + leftInt + rightInt) == 0) {
                    List<Integer> temp = new ArrayList<>();
                    temp.add(target);
                    temp.add(leftInt);
                    temp.add(rightInt);

                    set.add(temp);

                    // 일치할 경우 해당 선택된 인덱스에 대해 추가로 확인하기 위해서 left, right 값 변경
                    left += 1;
                    right -= 1;
                } else if ((target + leftInt + rightInt) < 0) {
                    left += 1;
                } else if ((target + leftInt + rightInt) > 0) {
                    right -= 1;
                }
            }
        }

        return set.stream().collect(Collectors.toList());
    }
}

