class Solution {
public:
    int findMin(vector<int>& nums) {
        return solve(nums, 0, nums.size() - 1);
    }

    int solve(vector<int>& num, int start, int end)
    {
        if (end - start < 2)
        {
            return min(num[start], num[end]);
        }

        // 중간 인덱스 계산
        int mid = (start + end) / 2;

        // 오름차순 정렬이 깨지기 시작한 부분 -> 최솟값 발견
        if  (num[mid] < num[mid - 1])
        {
            return num[mid];
        }

        // 왼쪽 영역이 정렬되어 있는 경우
        if (num[start] <= num[mid])
        {
            // 그리고 오른쪽 영역까지도 정렬된 경우
            if (num[mid] <= num[end])
            {
                // 가장 왼쪽에 있는 값이 최솟값
                return num[start];
            }

            // 왼쪽 영역만 정렬된 경우
            // 오른쪽 영역에서 정렬이 깨지는 부분 찾으러 가기
            return solve(num, mid + 1, end);
        }

        // 오른쪽 영역이 정렬된 경우
        // 왼쪽 영역에서 정렬이 깨지는 부분 찾으러 가기
        return solve(num, start, mid - 1);
    }
};
