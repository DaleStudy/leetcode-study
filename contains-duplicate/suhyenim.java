/* [5th/week01] 217. Contains Duplicate

1. 문제 요약
링크: https://leetcode.com/problems/contains-duplicate/
배열에서 동일한 숫자가 2번 이상 존재하면 true 반환, 아니면 false 반환

2. 풀이 로직
제출1: 반복문을 중첩으로 돌리면서, 동일한 값을 발견하면 바로 true 반환
실패: Time Limit Exceeded 발생
=> 시간 복잡도: O(n^2), 공간 복잡도: O(1)
class Solution {
    public boolean containsDuplicate(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] == nums[j]) {
                    return true;
                }
            }
        }
        return false;
    }
}

풀이2: 크기를 오름차순으로 정렬해서, 바로 옆 숫자랑 겹치는지 확인
성공: Time: 21 ms (19.91%), Space: 56.4 MB (98.12%)
=> 시간 복잡도: O(nlog(n)), 공간 복잡도: O(1)
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 1; i++)
            if (nums[i] == nums[i + 1]) return true;
        return false;
    }
}

풀이3: 배열을 순회하면서 HashSet에 겹치는 숫자가 존재하면 true 반환, 아니라면 HashSet에 본(seen) 숫자로 추가
성공: Time: 14 ms (61.51%), Space: 58.2 MB (61.9%)
=> 시간 복잡도: O(n), 공간 복잡도: O(n)
class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> seen = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            if (seen.contains(nums[i])) return true;
            seen.add(nums[i]);
        }
        return false;
    }
}

3. TIL
그리고 메모리가 충분하고 빠른 속도가 필요할 때, HashSet을 사용해볼 수 있다.
하지만 메모리가 여유롭지 않다면, HashSet을 사용하는 방식보다는 기존의 정렬을 사용하는 방식이 알맞을 수 있다. 

*/

import java.util.Arrays;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 1; i++)
            if (nums[i] == nums[i + 1]) return true;
        return false;
    }
}
