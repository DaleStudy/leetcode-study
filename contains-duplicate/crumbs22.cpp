#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

/*
	TC: O(n)
		벡터 nums의 모든 요소를 해시 테이블에 삽입하는 과정에서 O(n)만큼 소요됨	
	SC: O(n)

	풀이 방법 : nums의 중복요소를 거른 uset을 만들고, 
				nums와 uset의 크기가 서로 다르다면 nums에 중복 요소가 하나 이상 존재한다.
*/

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
		unordered_set<int> uset(nums.begin(), nums.end());
		return (nums.size() != uset.size());
    }
};
