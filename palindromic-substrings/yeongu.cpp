// TC: O(n^2) For문 안에서 while문 사용하는 함수 호출
// SC: O(1)

class Solution {
public:
    int find_palindrome1(string& original_text, int index) {
        int cnt = 0;
        int left_ptr = index, right_ptr = index;

        while (left_ptr >= 0 and right_ptr < original_text.size() and
               original_text[left_ptr] == original_text[right_ptr]) {
            cnt += 1;
            left_ptr -= 1;
            right_ptr += 1;
        }
        return cnt;
    }

    int find_palindrome2(string& original_text, int index) {
        int cnt = 0;
        int left_ptr = index, right_ptr = index + 1;

        while (left_ptr >= 0 and right_ptr < original_text.size() and
               original_text[left_ptr] == original_text[right_ptr]) {
            cnt++;
            left_ptr--;
            right_ptr++;
        }
        return cnt;
    }

    int countSubstrings(string& s) {
        int output = 0;
        for (int i = 0; i < s.size(); i++) {
            output += find_palindrome1(s, i);
        }
        for (int i = 0; i < s.size() - 1; i++) {
            output += find_palindrome2(s, i);
        }
        return output;
    }
};
