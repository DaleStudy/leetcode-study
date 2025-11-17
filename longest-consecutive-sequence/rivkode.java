/*
1. 문제 이해
1씩 증가하는 가장 긴 배열을 구하는 문제

2. 예외 케이스
똑같은 수만 나올 경우? 1이어야 함
모두 아닐 경우 0이어야 함

[1, 2, 3, 5, 7, 7, 7, 8, 9, 10]
1, 2, 3, 0, 0, 0, 0, 1, 2, 3

3. 알고리즘
dp 로 접근 ?
그냥 구현인 것 같기도
아니 일단 정렬을 해야함
아 Arrays.sort() 하면 시간이 nlogn 아닌가 ?
정렬 하고 순차적으로 가다가 끊기면 다시 0으로 초기화 하고 순차적으로 세야하는거 아닌가 ?
즉

a. 정렬
b. for 문 돌면서 이전 값과 1만큼 차이나는지 체크 후 차이나면 cnt 증가 아니면 cnt 를 이전 최댓값과 비교해서 크면 초기화 아니면 그대로

4. 구현
*/

import java.util.*;

class Solution {
    public int longestConsecutive(int[] nums) {
        Arrays.sort(nums);

        int max = 0;
        int tmpMax = 0;
        boolean isSame = false;

        if (nums.length == 1) {
            return 1;
        }

        if (nums.length == 0) {
            return 0;
        }

        for (int i=0; i<nums.length - 1; i++) {
            int cur = nums[i];
            int next = nums[i+1];

            if (Math.abs(next - cur) == 1) {
                tmpMax += 1;
            } else if ((next - cur) == 0) {
                isSame = true;
                continue;
            } else {
                max = Math.max(max, tmpMax);
                tmpMax = 0;
            }
        }

        max = Math.max(max, tmpMax);

        return max + 1;
    }
}



