

// 문제 이해
// - 주어진 숫자열에 여러 숫자가 주어지고,
// - 두 번 이상 동일한 숫자가 나온다면 true, 그렇지 않다면 false
//
//
// 문제 해결을 위한 의식의 흐름
// - 맨처음에는 숫자 범위가 작다면 count를 위한 array를 생각
// 	- 숫자 범위가 int 범위 가까이 된다면, 시공간 복잡도 초과
// - 기록하고, query 가 빠르게 이뤄지는 자료구조 필요
// - count를 위해 숫자를 굳이 저장할 필요가 없고, 존재하는지만 확인하면 된다.
// 	-> Set 자료구조 필요성
//
// 시공간 복잡도
// TC: O(N)
// SC: O(N)
// - nums의 length를 N 이라 하면,
// - 시간복잡도 : O(N) - N번 순회, 매 query별로 이론상 O(1)
// - 공간복잡도 : O(N)


class Solution {
	public boolean containsDuplicate(int[] nums) {
		Set<Integer> numberContainer = new HashSet<>();

		for (int number : nums) {
			if (numberContainer.contains(number)) return true;
			numberContainer.add(number);
		}

		return false;
	}
}
