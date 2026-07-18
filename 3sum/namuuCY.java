// 문제 풀이 흐름
// 세 개의 변수. 만약 brute-force(3중 for문 -> 3000 ^ 3 이어서 시간복잡도 너무 높음.) -> 어떤 한 값을 고정해서 변수를 줄이자.
// 그러면 나머지 두 개는? 투 포인터 같은거 쓰면 안되나?
// 근데 중복되는 경우에 대해서 어떻게 고려함?
// 중복되는 경우가 너무 많다..
// 우선 정렬 먼저 -> 이후 하나 고정하고 나머지 투포인터 생각
// 중복되는거 생각나는대로, 음...

// N = nums.length라 할때
// 시간 복잡도 정렬 + for문 1개 * 길이 N 투포인터
// = O(N^2)
// 공간 복잡도 두 가지로 설명
// - Arrays.sort() 로 정렬 시 필요한 추가 공간(or 스택)을 따질 경우 : O(log N)
// - 따지지 않을 경우 : O(1)

class Solution {

	int[] nums;
	List<List<Integer>> answer = new ArrayList<>();

	public List<List<Integer>> threeSum(int[] nums) {
		this.nums = nums;
		// 원본 배열 정렬
		Arrays.sort(nums);

		for (int fixed = 0; fixed < nums.length - 2; fixed++) {
			// fixed가 이전의 값과 동일할 경우 skip
			if (fixed > 0 && nums[fixed] == nums[fixed - 1]) continue;

			// fixed가 양수이면 뒤에도 무조건 양수이므로 break
			if (nums[fixed] > 0) break;

			searchByTwoPointer(fixed);
		}

		return answer;
	}

	private void searchByTwoPointer(int fixedIdx) {
		int leftIdx = fixedIdx + 1;
		int rightIdx = nums.length - 1;

		while (leftIdx < rightIdx) {
			int sum = nums[fixedIdx] + nums[leftIdx] + nums[rightIdx];

			if (sum == 0) {
				answer.add(Arrays.asList(
						nums[fixedIdx],
						nums[leftIdx],
						nums[rightIdx]
				));

				// 중복된것에 대해서 조정해줘야함.

				leftIdx ++;
				rightIdx --;

				while (leftIdx < rightIdx && nums[leftIdx] == nums[leftIdx - 1]) leftIdx++;
				while (leftIdx < rightIdx && nums[rightIdx] == nums[rightIdx + 1]) rightIdx--;
			} else if (sum < 0) {
				leftIdx ++;
			} else {
				rightIdx --;
			}
		}
	}
}
