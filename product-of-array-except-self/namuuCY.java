// 문제 풀이 흐름 :
// 전체의 합에서 자기 자신만 뺀것을 생각하듯이, 전체의 곱에서 자기 자신만 나눈 것을 생각하자
// 이때, 중요한 것은 integer overflow와 0이 여러번 나올 떄 예외처리
//  integer overflow : 문제에서는 답이 32 bit integer 라고 했지, 그 과정에서 생길 수 있는 곱들이 int범위라고 단정지을 수 없음
//  0의 개수에 따라 다르게 계산 :
//      0이 없을 때 : 상관없음.
//      1개만 있을 때 : 0인 곳에만 product 기입
//      2개만 있을 때 : 모두 0이 된다.

// n = nums.length 라 할때
// 시간복잡도 : O(n)
// 공간복잡도 : O(n)


class Solution {

	static {
		Solution warmup = new Solution();
		for (int i = 0; i < 500; ++i) {
			warmup.productExceptSelf(new int[2]);
		}
	}


	public int[] productExceptSelf(int[] nums) {
		int[] answer = new int[nums.length];

		Arrays.fill(answer, 1);

		int leftProduct = 1;
		for (int i = 0 ; i < nums.length - 1; i ++) {
			leftProduct *= nums[i];
			answer[i + 1] *= leftProduct;
		}

		int rightProduct = 1;
		for (int i = nums.length - 1 ; i > 0 ; i --) {
			rightProduct *= nums[i];
			answer[i - 1] *= rightProduct;
		}

		return answer;
	}

	public int[] prevSubmission(int[] nums) {
		int zeros = 0;
		long totalProduct = 1;

		for (int number : nums) {
			if (number == 0) {
				zeros ++;
			}
			totalProduct *= number;
		}

		int[] answer = new int[nums.length];

		if (zeros == 0) {
			for (int i = 0 ; i < nums.length; i ++ ) {
				answer[i] = (int) (totalProduct / nums[i]);
			}
		} else if (zeros == 1) {
			int nonZeroProduct = 1;
			int zeroIdx = -1;
			for (int i = 0 ; i < nums.length; i ++ ) {
				if (nums[i] == 0) {
					zeroIdx = i;
					continue;
				}
				nonZeroProduct *= nums[i];
			}
			answer[zeroIdx] = nonZeroProduct;
		}

		return answer;
	}
}
