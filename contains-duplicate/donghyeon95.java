import java.util.*;

class Solution {
	public boolean containsDuplicate(int[] nums) {
		/*
		* -- 풀이 --
		* nums를 순회하면서 HashSet에 데이터를 넣어서 중복되었는 지 확인한다.
		*
		* -- 시간 복잡도 --
		* 길이 N인 nums를 순환하는데 대한 시간 복잡도 => O(N)
		* hashSet의 add에 대한 시간 복잡도 => O(1)
		* 전체 시간 복잡도 O(1)*O(N) =O(n)
		* ------------------------------------------
		*
		* -- 공간 복잡도 --
		* 길이 N인 nums를 넣을 Hashset이 있어야 하기에 O(N)
		* -------------------------------------------
		*/

		// 중복을 확인할 수 있는 set 선언
		HashSet<Integer> hashSet = new HashSet<>();

		for (int num: nums) {
			// set에 있다면
			if (!hashSet.add(num)) return true;
		}

		return false;
	}
}

