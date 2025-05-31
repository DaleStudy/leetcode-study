/*
    한 번의 순회로 위치마다의 최대곱과 최소 곱을 갱신
    시간복잡도는 O(n), 공간복잡도는 O(1)
*/
class Solution {
	public:
		int maxProduct(vector<int>& nums) {
			int ans = nums[0];
			int curMax = nums[0];
			int curMin = nums[0];
	
			// 1번째부터 마지막까지 순회
			for (int i = 1; i < nums.size(); i++) {
				// 음수를 곱하면 현재까지의 최대 곱이 최소가 되고, 최소 곱은 최대 곱으로 뒤바뀜
				if (nums[i] < 0)
					swap(curMax, curMin);
	
				curMax = max(nums[i], curMax * nums[i]);
				curMin = min(nums[i], curMin * nums[i]);
				ans = max(ans, curMax);
			}
			return (ans);
		}
	};
