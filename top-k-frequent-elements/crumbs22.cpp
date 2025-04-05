#include <iostream>
#include <vector>
#include <unordered_map>
#include <sort>

using namespace std;

/*
	TC: O(nlogn)
		- 해시맵에 요소 삽입: O(n)
		- 해시맵을 벡터로 변환: O(n)
		- 벡터 정렬: O(nlogn) ... sort()
		=> 전체 시간 복잡도는 O(nlogn)
	SC: O(n)
		- 해시맵 저장 공간: O(n)
		- 벡터 변환 공간: O(n)
		=> 전체 공간 복잡도는 O(n)

	풀이 방법: nums를 순회하며 각 숫자의 빈도를 해시맵 umap에 저장하고, 해시맵을 pair 형태의 벡터로 변환한다
			그리고 umap을 빈도기준으로 정렬하고 상위 k개 숫자를 추출해서 반환한다
*/

bool cmp(const pair<int, int>& a, const pair<int, int>& b)
{
	if (a.second == b.second)
		return a.first < b.first;
	return a.second > b.second;
}

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> umap;

		for (int i = 0; i < nums.size(); i++)
		{
			auto tmp = umap.find(nums[i]); // umap에 nums[i]가 존재하는지 탐색
			if (tmp != umap.end()) // 이미 존재한다면 개수 + 1 하고
				tmp->second += 1;
			else // 존재하지 않는다면 nums[i]를 umap에 삽입한다
				umap.insert(make_pair(nums[i], 1));
		}
		vector<pair<int,int>> vec(umap.begin(), umap.end()); // map을 vector로 이동
		sort(vec.begin(), vec.end(), cmp); // vec를 개수에 따라 오름차순 정렬해준다

		vector<int> result;
		for (int i = 0; i < k; i++) // 정렬된 vec배열의 앞에서부터 k개까지 탐색해서 반환한다
			result.push_back(vec[i].first);
		return (result);
    }
};
