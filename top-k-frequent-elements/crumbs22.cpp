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
			auto tmp = umap.find(nums[i]);
			if (tmp != umap.end())
				tmp->second += 1;
			else
				umap.insert(make_pair(nums[i], 1));
		}
		vector<pair<int,int>> vec(umap.begin(), umap.end()); // map을 vector로 이동
		sort(vec.begin(), vec.end(), cmp);

		vector<int> result;
		for (int i = 0; i < k; i++)
			result.push_back(vec[i].first);
		return (result);
    }
};
