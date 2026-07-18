// 문제 풀이 흐름
// 맨처음에 생각한 풀이는
// 누적합을 기준으로,
// 누적합의 오른쪽 최대 - 왼쪽 최소 의 값이 제일 큰걸 구하면 된다고 생각했음.
// 예를 들어서 nums = [-2,1,-3,4,-1,2,1,-5,4] 라면
// 누적합은 [-2 -1 -4 0 -1 1 2 -3] 이 되는데, 값의 최대는 2에서 -4를 뺸 6이 최대라고 생각했음.
// 그래서 어느 한 좌표(왼쪽)를 순회하면서
// 이 인덱스의 오른쪽(왼쪽 인덱스 +1 부터 끝까지)의 누적합의 최소를 구하면 된다고 생각했음.
//      이 위를 구하기 위해서 누적합에 대해 세그먼트 트리를 구축해두려고 했음.
// 그러면 세그먼트 트리 만드는데 nlogn + 1중 for 문 * log n 조회니까 최대 nlogn의 시간복잡도로 문제를 풀수있음 / 공간복잡도는 O(n log n)이 될것.

// 근데 제시된 풀이를 보니까 1차원 DP로 푸는것을 봤음.
// DP[i] = Math.max(nums[i], DP[i - 1] + nums[i]);
// 혹은 = nums[i] + (DP[i - 1] > 0) ? DP[i - 1] : 0; 이 되겠지.
// 이렇게 하면 시간복잡도 O(n) 공간복잡도 O(n)이라 내 풀이보다 훨씬좋다

class Solution {

	public int maxSubArray(int[] nums) {
		int[] DP = new int[nums.length + 1];
		int maxSum = - 200000;

		for (int i = 0 ; i < nums.length; i ++) {
			DP[i + 1] = nums[i] + (DP[i] > 0 ? DP[i] : 0);
			maxSum = Math.max(maxSum, DP[i + 1]);
		}

		return maxSum;
	}
}
