/*
1. 문제 이해
nums 가 n 개 주어졌을때 0부터 n 까지의 숫자중 빠진 숫자를 리턴

2. 알고리즘
정렬 nlogn 후 for문을 돌고 1씩 증가하면서 아닐 경우 해당 번호 반환 -> 이거 말고 set 사용

set 으로 숫자 넣고 contains로 찾아서 진행

3. 예외

4. 구현

array 정렬
1씩 증가
찾기

추가 팔로업 -> o(n) 에서 가능한가 ?

set 사용 ?
key 를 통해 해당 key 가 존재하면 계속 for 문 진행
없다면 해당 숫자 반환
어차피 SET 도 map 사용함
정렬 없으므로 o(n) 으로 탐색 가능 set.contains 는 O(1)

*/

import java.util.*;

class Solution {
    public int missingNumber(int[] nums) {
        /*
        Array 풀이
        Arrays.sort(nums);

        for (int i=0; i<nums.length; i++) {
            if (nums[i] != i) {
                return i;
            }
        }

        return nums.length;
        */
        Set<Integer> set = new HashSet<>();

        for (int i: nums) {
            set.add(i);
        }

        for (int i=0; i<nums.length; i++) {
            if (set.contains(i)) {
                continue;
            }
            return i;
        }

        return nums.length;
    }
}

