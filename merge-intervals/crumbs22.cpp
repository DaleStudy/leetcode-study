/*
	이전 interval의 끝점과 현재 interval의 시작점을 비교해서 구간 겹침을 판단
	구간이 겹친다면 prev를 갱신
	구간이 겹치지 않을 때 반환 벡터 res에 prev 추가하고 기준점 갱신
	intervals를 한 번 반복하므로 시간복잡도 O(n)과 처음 정렬에 O(nlogn) 소요되므로
	최종 시간 복잡도는 O(nlogn)
	추가적으로 사용하는 공간은 반환배열밖에 없으므로 O(1)의 공간복잡도 가짐
*/

class Solution {
	public:
		vector<vector<int>> merge(vector<vector<int>>& intervals) {
			vector<vector<int>> res;
	
			sort(intervals.begin(), intervals.end());
	
			vector<int> prev = intervals[0];
			for (auto i : intervals) {
				if (i[0] <= prev[1]) {
					prev[0] = min(prev[0], i[0]);
					prev[1] = max(prev[1], i[1]);
				} else {
					res.push_back(prev); // 이전 병합 구간 저장
					prev = i; // 새로운 기준 시작
				}
			}
			res.push_back(prev);
	
			return res;
		}
	};
