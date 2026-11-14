// 풀이 1 - set에 요소를 넣으면서 동일한 값을 insert하는지 여부 체크
// TC: O(n) - 최대 nums의 길이만큼 insert하는 시간이 소요
// SC: O(n) - set에 최대 nums의 길이 만큼 저장
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> s;
        
        for (int num : nums) {
            // set에 insert할 때의 .second는
            // 새로 삽입됐으면 true, 이미 있었으면 false 리턴
            if (!s.insert(num).second) {
                return true;
            }
        }

        return false;
    }
};

// 풀이 2 - sort한 후 근접 요소 비교
// TC: O(n log n) - sorting 비용 n log n > for문 비용 n
// SC: O(log n) - std::sort는 introsort 방식을 쓰므로 log n의 재귀 스택을 사용
//              - introsort란? 퀵소트로 시작해서, 재귀가 너무 깊어지면 힙소트로, 작은 구간은 삽입정렬로 처리하는 하이브리드 정렬
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        sort(nums.begin(), nums.end());  // 먼저 sorting

        for (int i=0; i < int(nums.size()) - 1; i++) {
            if (nums[i] == nums[i + 1]) {  // 인접 요소끼리 비교
                return true;
            }
        }

        return false;
    }
};
