// 문제 풀이 흐름
// 각 숫자가 몇개가 나왔는지 계속해서 저장하고, 바로 확인할 수 있는 자료구조가 필요
// -> HashMap

// N = nums.length 라 할때
// 시간복잡도 : O(NlogN)
// 공간복잡도 : O(N)

class Solution {
	public int[] topKFrequent(int[] nums, int k) {
		Map<Integer, Integer> numberCount = new HashMap<>();

		for (int number : nums) {
			int countOfCurrentNumber = numberCount.getOrDefault(number, 0);
			numberCount.put(number, countOfCurrentNumber + 1);
		}

		List<Integer> numbers = new ArrayList<>(numberCount.keySet());

		numbers.sort((first, second) ->
							 Integer.compare(numberCount.get(second), numberCount.get(first))
		);

		int[] answer = new int[k];

		for (int i = 0 ; i < k ; i ++) {
			answer[i] = numbers.get(i);
		}

		return answer;
	}
}
