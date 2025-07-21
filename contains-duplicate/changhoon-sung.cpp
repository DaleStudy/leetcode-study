/*
contains-duplicate
요구사항: 주어진 입력에서 중복된 원소가 존재하는지 여부를 참/거짓으로 반환.
접근 1: 가장 단순한 방법은 다른 vector input_list를 두고, 입력 반복마다 전체 스캔해서 중복 여부를 체크하는 것입니다.
	input_list의 스캔 비용 O(N)을 모든 입력에 대해 반복하므로 총 시간 복잡도는 O(N^2)입니다.
	공간 복잡도는 입력과 같으므로 O(N)입니다.
접근 2: 원소의 존재 여부를 더 빠르게 체크하는 방법은 set을 사용하는 것입니다.
	set은 중복 원소를 검출하는데 효과적인 자료구조로, 내부 구현에 따라 비용과 특성이 다릅니다.
	- C++에서 ordered_{set, map}은 정렬을 유지하는 search tree를 사용하므로 쿼리와 삽입, 삭제 비용이 평균 O(log(N))입니다.
	  search tree의 구현에 따라 최악의 경우 쿼리 비용이 O(N)까지 증가할 수 있습니다.
	- C++에서 unordered_{set, map}은 해시 및 버킷 구조를 사용합니다. 이 경우, 평균적인 쿼리, 삽입, 삭제 비용은 O(1)입니다.
	우리의 요구사항은 입력에 대한 별도의 정보를 저장할 필요가 없으므로 unordered_set으로 중복 검사를 수행하는 것이 비용 효율적입니다.
	최악의 경우 모든 입력을 확인해야 합니다. N개의 입력에 대해 각각 쿼리와 입력을 수행하므로, 총 시간 복잡도는 O(N), 공간 복잡도도 입력만큼인 O(N)입니다.
*/

#include <vector>
#include <unordered_set>

class Solution {
   public:
    bool containsDuplicate(std::vector<int>& nums) {
        std::unordered_set<int> s;

        for (auto it = nums.begin(); it != nums.end(); it++) {
            int x = *it;
            if (s.find(x) != s.end())
                return true;
			else
				s.insert(x);
        }
		return false;
    }
};