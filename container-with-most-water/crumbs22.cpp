#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

class Solution {
	public:
		int maxArea(vector<int>& height) {
			int left = 0;
			int right = height.size() - 1;
			int maxArea = 0;

			while (left < right) {

				int area = (right - left) * std::min(height[left], height[right]);
				if (area > maxArea)
					maxArea = area;
				
				if (height[left] < height[right])
					left++;
				else
					right--;

			}
			return (maxArea);
		}
	};
