/*
two-sum
요구사항: 주어진 배열에서 두 수의 합이 타겟을 만들 수 있는지 확인하고, 해당 원소를 반환하라.
접근 1: 가장 단순한 방법은 입력에 대해 모든 combination을 확인하는 것입니다.
	시간 복잡도는 입력 스캔 O(N)을 N개의 원소에 대해 수행하므로 O(N^2)입니다.
	공간 복잡도는 입력 레퍼런스를 그대로 사용하며, 추가로 저장 및 관리하는 자료구조가 없으므로 O(1)입니다.
접근 2: 한 가지 아이디어는 임의의 입력 X에 대해 합이 `target`이 되도록 하는 pair는 유일하게 결정된다는 것입니다.
	따라서, 합을 구하는 대신, 주어진 입력에 대한 페어 존재 유무를 검사하는 것으로 문제를 전환할 수 있습니다.
	수의 범위가 충분히 크므로, 배열 대신 해시 기반 unordered_set으로 페어 존재 여부 쿼리 및 삽입을 O(1)에 수행할 수 있습니다.
	최악의 경우, 모든 입력에 대해 unordered_set 쿼리 및 삽입을 수행하므로 총 시간 복잡도는 O(N), 공간 복잡도는 입력과 같으므로 O(N)입니다.
*/

#include <vector>
#include <unordered_set>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
		std::unordered_set<int> s;

		for(auto it = nums.begin(); it != nums.end(); it++) {
			int x = *it;
			if (s.find(target - x) != s.end()) {
				return std::vector<int>(x, target-x);
			} else {
				s.insert(x);
			}
		}
		
		// 문제의 조건에서 단 하나의 솔루션이 반드시 존재한다고 가정하므로, 이곳에 도달하지 않음.
		throw std::runtime_error("No two sum solution found");
    }
};