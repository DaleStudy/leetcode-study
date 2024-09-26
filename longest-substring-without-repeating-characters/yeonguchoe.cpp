class Solution {
public:
    int lengthOfLongestSubstring(string s) {

        int current_max = 0;
        int pivot = 0;
        int checker = 0;

        int current_length = 0;
        while (pivot < s.size()) {
            set<char> included;
            included.insert(s[pivot]);
            checker = pivot + 1;
            while (checker < s.size() and
                   included.find(s[checker]) == included.end()) {
                included.insert(s[checker]);
                checker += 1;
            }
            current_length = checker - pivot;
            current_max = max(current_max, current_length);
            pivot += 1;
        }
        return current_max;
    }
    // 시간 복잡도: O(n)
    // 공간 복잡도: O(n)
};
