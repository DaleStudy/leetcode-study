/*
    Problem:
    Given an integer array nums, 
    return true if any value appears at least twice in the array, 
    and return false if every element is distinct.

    Input: nums = [1,2,3,1]
    Output: true

    Constraints:
    1 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
*/

// 처음 생각한 코드
/*
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i+1; j < nums.size(); j++) {
                if (nums[i]==nums[j]) {
                    return true;
                }
            }
        }

        return false;
    }
};

int main() {
    vector<int> arr;
    int sz;
    cin >> sz;
    for (int i = 0; i < sz; i++) {
        int nm;
        cin >> nm;
        arr.push_back(nm);
    }


    Solution s;\
    if (s.containsDuplicate(arr))
        cout << "true";
    else 
        cout << "false";

    return 0;
}
*/

// O(n^2) 시간 복잡도를 개선해보자
/*
    set 을 이용해서 중복이 있다면 배열의 길이가 줄어들테니
    이를 통해 중복을 판단할 수 있다고 생각했다.
*/
/*
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

class Solution {
public: 
    bool containsDuplicate(vector<int>& nums) {
        // set과 유사하게 만들기 위해서 사용
        sort(nums.begin(), nums.end());
        for (size_t i = 1; i < nums.size(); i++) {
            if (nums[i] == nums[i-1]) return true;
        }
        return false;
    }
};


int main() {   
    size_t sz;
    cin >> sz;

    vector<int> arr;
    for (int i = 0; i < sz; i++) {
        int num;
        cin >> num;
        arr.push_back(num);
    }

    Solution sol;
    if (sol.containsDuplicate(arr)) {
        cout << "true";
    } else {
        cout << "false";
    }
}
*/

// 이보다 더 좋은 방법이 있다고 gpt의 리뷰가 있었다.
/*
    unordered_set<int> 를 이용한다.
    해시 테이블 자료구조를 이용하여 구현 되어 있는 것.
    정렬은 못하지만 탐색하는데에 O(1) 이라는 장점이 있어 이를 활용한다.
    -> 빠른 탐색 굿
*/


#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> copy_set;
        for (int x : nums) {
            if (copy_set.count(x)) return true;
            copy_set.insert(x);
        }
        return false;
    }
};

int main() {
    int n;
    cin >> n;

    vector<int> nums;
    nums.reserve(n);

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        nums.push_back(x);
    }

    Solution sol;
    cout << (sol.containsDuplicate(nums) ? "true" : "false");

    return 0;
}
