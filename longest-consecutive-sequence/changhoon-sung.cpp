/*
longest-consecutive-sequence
요구사항: 주어진 비정렬 배열에서 가장 긴 연속 수열의 길이를 O(N)에 구하라.
접근 1: 가장 단순한 방법은 정렬 후 스캔하여 가장 긴 연속 구간을 찾는 것이다.
        정렬 비용 O(NlogN)에 스캔 O(N)으로 총 O(NlogN)이다. 비용 초과.
접근 2: 정렬하지 않고, 인접한 연속 원소 수열을 '하나의 덩어리'로 취급하기 위해 union-find할 수 있다.
		중복 원소는 무시한다.
        입력 x에 대해 x-1의 유니온을 찾는다.
            그러한 유니온이 존재하면 x를 추가한다. 그 이후 x+1 유니온이 존재하면 통합한다.
        그러한 유니온이 존재하지 않으면 x+1 유니온을 찾는다.
            그러한 유니온이 존재하면 x를 추가한다.
        인접한 앞 뒤 유니온이 존재하지 않으면 입력을 새로운 root union으로 초기화한다.

	비용:
        경로 압축과 높이 최소화 최적화를 적용하면, find 비용은 O(α(N))으로 최대 입력 N=10^5에 대해서 한 자리 상수만큼 충분히 낮다.
		유니온의 통합 비용은 O(1)이다.
        N개의 입력에 대해 O(1) 연산을 상수번 수행하므로 유니온 빌딩 시간 복잡도는 O(N)이다.
		사이즈 리스트를 스캔하여 가장 큰 유니온의 크기를 구한다. 이는 O(K) where K <= N이다.
		따라서 총 시간 복잡도는 O(N)이다.
		공간 복잡도도 입력 범위의 상수배이므로 O(N)이다.
*/

#include <unordered_map>
#include <vector>

#define max(a, b) ((a) > (b) ? (a) : (b))

class Solution {
   public:
	std::unordered_map<int, int> parent;
	std::unordered_map<int, int> size;

    int find(int x) {
        if (x == parent[x]) return x;
        return parent[x] = find(parent[x]);	// path compression
    }
    void union_sets(int x, int y) {
        int px = find(x);
        int py = find(y);

		if (px == py) return;

		// min height optimization
		if (size[px] > size[py]) {
			size[px] += size[py];
			parent[py] = px;
		} else {
			size[py] += size[px];
			parent[px] = py;
		}
    }
    int longestConsecutive(std::vector<int>& nums) {
		// build union
        for (auto it = nums.begin(); it != nums.end(); it++) {
            int x = *it;

			if (parent.find(x) != parent.end())
				continue;
			
            if (parent.find(x - 1) != parent.end()) {
                parent[x] = find(x - 1);
				size[parent[x]]++;
                if (parent.find(x + 1) != parent.end()) {
                    union_sets(x, x + 1);
                }
            } else if (parent.find(x + 1) != parent.end()) {
                parent[x] = find(x + 1);
				size[parent[x]]++;
			} else {
				parent[x] = x;
				size[x] = 1;
			}
        }

		// find largest set
		int max_size = 0;
		for(auto it = size.begin(); it != size.end(); it++) {
			auto sz = it->second;
			max_size = max(max_size, sz);
		}
		return max_size;
    }
};
