/**
 * 풀이
 * - 아래와 같은 배열 memo를 이용하여 이중 반복문을 실행하는 풀이입니다
 * - memo[i]: nums[i]로 끝나는 subsequence 중에서 길이가 가장 긴 subsequence의 길이
 * 
 * Big O
 * - N: 배열 nums의 길이
 * - Time complexity: O(N^2)
 * - Space complexity: O(N)
 */

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> memo;
        memo.push_back(1);

        int res = 1;
        for (int i = 1; i < nums.size(); ++i) {
            int tmp = 1;
            for (int j = 0; j < i; ++j) {
                if (nums[j] < nums[i]) tmp = max(tmp, memo[j] + 1);
            }
            memo.push_back(tmp);
            res = max(res, tmp);
        }

        return res;
    }
};

/**
 * 풀이
 * - wikipedia의 pseudo code를 참고하였습니다
 *   달레님 블로그에 실린 풀이를 통해서 훨씬 간단하게 문제에서 요구하는 바를 구할 수 있으므로, 문제의 풀이만을 원하신다면 달레님 블로그를 추천드리고
 *   좀 더 general하고 확장성 있는 알고리즘에 대해 궁금하신 분들께서는 wiki도 읽어보시는 걸 추천드립니다 (이해하는 데에는 시간이 좀 걸렸습니다)
 *   
 *   제가 읽고 이해한 결과 wiki 풀이와 달레님 풀이의 비교는 다음과 같습니다
 *   
 *   공통점: 문제에서 요구하는 바를 구할 수 있음 (LIS의 길이)
 *   차이점: wiki 풀이는 문제에서 요구하는 바를 구하는 것에 비해 overkill입니다 (이 문제에서는 굳이 필요 없는 부분이 꽤 있음)
 *         대신, wiki 풀이는 확장성이 좀 더 넓은 풀이입니다 (각 길이에 해당하는 increasing subsequence를 재구축할 수 있음)  
 * 
 *   관심 있으신 분들께서는 한 번 읽어보시는 것을 추천합니다 :)
 * - 참고: https://en.wikipedia.org/wiki/Longest_increasing_subsequence#Efficient_algorithms
 * 
 * - memo[l]: 현재 nums[i]를 탐색중이라고 할 때, l <= i인 l에 대하여
 *            길이가 l인 increasing subsequence들의 마지막 원소 중에서
 *            가장 최소값인 nums[k]의 인덱스 k
 *            nums를 순차적으로 탐색해 나감에 따라 계속 갱신되며 정렬된 상태를 유지하게 됩니다 (if x < y then nums[memo[x]] < nums[memo[y]])
 * 
 * - predec[i]: nums[i]를 마지막 원소로 하는 가장 긴 increasing subsequence에서 nums[i] 바로 앞에 오는 원소의 index
 * 
 * - nums를 순차적으로 탐색하며, 현재 탐색 중인 nums[i]를 마지막 원소로 삼는 가장 긴 Increasing subsequence를 찾습니다
 *   가장 긴 Increasing subsequence는 memo 배열에 대해 이분탐색을 실행하여 알아낼 수 있습니다
 * 
 * Big O
 * - N: 배열 nums의 길이
 * 
 * - Time complexity: O(NlogN)
 *   - nums의 각 원소마다 memo에 대해 이분탐색을 실행하므로 N이 증가함에 따라 실행 시간은 N * logN 형태로 증가합니다
 * - Space complexity: O(N)
 *   - memo 배열의 크기는 N이 증가함에 따라 선형적으로 증가합니다
 *  (- predec 배열의 크기 또한 N이 증가함에 따라 선형적으로 증가합니다)
 */

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();

        vector<int> memo(n + 1, -1);

        // vector<int> predec(n, -1);
        // 각 길이에 맞는 increasing subsequence를 재구축할 때 쓰입니다

        int max_len = 0;
        for (int i = 0; i < nums.size(); ++i) {
            int lo = 1;
            int hi = max_len + 1;
            while (lo < hi) {
                int mid = lo + (hi - lo) / 2;
                if (nums[memo[mid]] < nums[i]) lo = mid + 1;
                else hi = mid;
            }
            // 위 이분탐색을 마치면 lo == hi인데
            // lo (혹은 hi)가 의미하는 바는 `nums[i]가 마지막 원소인 increasing subsequence 중에 길이가 가장 긴 녀석의 길이` 입니다
            int curr_len = lo;
            // 이해하기 쉽게끔 curr_len이라는 변수를 선언해줍니다

            // predec[i] = memo[curr_len - 1];
            // nums[i]가 마지막으로 오는 가장 긴 increasing subsequence에서 nums[i]의 바로 전 원소의 index를 기록해줍니다
            // 
            memo[curr_len] = i;

            if (curr_len > max_len) {
                // 만약 이전까지 찾았던 max_len보다 더 길이가 긴 increasing subsequence를 max_len
                max_len = curr_len;
            }
        }

        return max_len;

    // 길이 L짜리 increasing subsequence 중 하나를 재구축하려면 아래처럼 하면 됩니다
    // [P...P[memo[L]], ..., P[P[memo[L]]], P[memo[L]] ,memo[L]]

    //     vector<int> s(L, -1);
    //     int k = memo[L];
    //     for (int i = L - 1; i >= 0; --i) {
    //         s[i] = nums[k];
    //         k = predec[k];
    //     }
    }
};
