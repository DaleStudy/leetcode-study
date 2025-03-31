/*
[문제풀이]
time: O(N), space: O(N)
- 같은 수가 하나라도 있으면 true
- 모든 수가 다르면 false

[회고]
ArrayList vs Set
ArrayList: O(N^2), 매번 리스트를 처음부터 검색해야 하며, n번 반복
Set      : O(N)  , 내부적으로 해시 테이블을 사용하여 중복 확인을 O(1)에 수행
따라서 중복 검사에서 Set 더 효율적

set.add()의 return 자료형은 boolean 이다.
이후에는 if(!set.add()) 처럼 사용해도 좋을 듯.
*/
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            if (set.contains(num)) {
                return true;
            }
            set.add(num);
        }
        return false;
    }
}