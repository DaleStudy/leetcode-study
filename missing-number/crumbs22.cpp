/*
    풀이방법: 0부터 n까지의 합은 n*(n + 1)/2 이라는 수학적 사실을 활용,
	nums 배열을 한 번만 순회하므로 시간복잡도는 O(n)
	추가적으로 사용하는 공간 없으므로 공간복잡도는 O(1)이다.
*/

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int res = n * (n + 1) / 2;

        for (int num : nums) {
            res -= num;
        }
        return (res);
    }
};
