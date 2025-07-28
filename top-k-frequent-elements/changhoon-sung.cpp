/*
top-k-frequent-elements
요구사항: 주어진 입력에 대해 k번째 빈도를 가지는 원소를 모두 반환하라.
접근 1: 가장 단순한 접근법은 모든 원소에 대해 map으로 빈도를 세는 것입니다.
	ordered_map에서 삽입 비용은 자료구조 길이가 K일 때 O(logK)으로, N회 삽입 연산으로 O(NlogK) 인데,
	이때 모든 원소가 유일한 경우 K=N이므로 최악의 경우 O(NlogN) 입니다.
	그리고 정렬된 맵에서 k 위치를 찾는 lower_bound 연산 비용은 O(logN)으로, 총 O(NlogN)입니다.
	unordered_map은 삽입 비용이 O(1)이지만, N회 삽입 연산 이후, k를 찾기 위해 카운트를 정렬해야 한다는 점에서
	보편적인 정렬 비용 O(Nlog(N))이 발생합니다.
접근 2: 총 비용이 O(NlogN)보다 낮아지려면 정렬 자료구조의 입력 비용이 O(logN)보다 낮거나,
	정렬 비용이 O(NlogN)보다 낮아야 합니다.
	한 가지 아이디어는 정렬 자료구조의 입력을 비용을 낮추는 필터 및 셋 기반 블랙리스트를 도입할 수 있다는 것입니다.
	- k초과 원소 필터: k보다 높은 빈도를 가지는 원소를 자료구조에서 제거 및 블랙리스트
	- k도달 불가 원소 필터: 현재 조회중인 입력에 대해 남은 원소의 수가 모두 해당 원소더라도 k에 미치지 못 하는 경우 제거 및 블랙리스트
	필터에 해당하는 원소가 M개일 때, 필터 비용은 해시셋 조회 O(1), 삽입 비용은 O(log(N-M))으로
	모든 입력에 대한 총 비용은 O(Nlog(N-M))입니다.
	공간 복잡도는 최악의 경우에도 입력의 상수배이므로 O(N)입니다.
접근 3: 우리가 원하는 것이 k 빈도 딱 하나라는 것을 고려하면, 해당 빈도를 키로 원소를 반환받는 구조를 생각해볼 수 있습니다.
	아이디어는 원소-카운팅맵으로 전체 입력에 대해 비용 O(N)으로 카운팅하고, 이를 바탕으로 카운팅-원소 해시맵으로 <빈도, 원소셋>을 빌드하는겁니다.
	해당 빌드 비용은 최대 N개 원소에 대해 조회+삽입 O(1) 이므로 O(N)입니다.
	필요한 정보는 카운팅-원소 해시맵으로 O(1) 조회 및 O(N) 반환합니다.
	공간 복잡도는 최악의 경우에도 입력의 상수배이므로 O(N)입니다.
*/

#include <vector>
#include <unordered_map>
#include <unordered_set>

class Solution {
public:
    std::vector<int> topKFrequent(std::vector<int>& nums, int k) {
		std::unordered_map<int, int> elementCountMap;
		std::unordered_map<int, std::unordered_set<int>> countElementMap;
		std::vector<int> ans;

		for(auto it = nums.begin(); it != nums.end(); it++) {
			int x = *it;
			elementCountMap[x]++;
		}

		for(auto it = elementCountMap.begin(); it != elementCountMap.end(); it++) {
			int x = it->first;
			int count = it->second;
			countElementMap[count].insert(x);
		}

		const std::unordered_set<int>& kFreqSet = countElementMap[k];	// avoid copy
		for(auto it = kFreqSet.begin(); it != kFreqSet.end(); it++) {
			int x = *it;
			ans.push_back(x);
		}
		return ans;
    }
};
