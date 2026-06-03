class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        // 시작 시간이 빠른 순으로 정렬
        int n = intervals.size();
        sort(intervals.begin(), intervals.end(), [](vector<int>& a, vector<int>& b)
        {
            return a[0] < b[0];
        });

        // 회의실이 부족할 때 마다 하나씩 추가
        // rooms에는 각 회의실을 마지막으로 이용한 회의의 종료 시간이 들어있음
        vector<int> rooms;
        rooms.push_back({intervals[0][1]});

        for (int i = 1; i < n; ++i)
        {
            bool found = false;
            for (auto& room : rooms)
            {
                // 빈 회의실을 찾은 경우
                if (room <= intervals[i][0])
                {
                    room = intervals[i][1];
                    found = true;
                    break;
                }
            }

            // 빈 회의실을 찾지 못한 경우
            if (!found)
            {
                rooms.push_back(intervals[i][1]);
            }
        }

        return rooms.size();
    }
};
