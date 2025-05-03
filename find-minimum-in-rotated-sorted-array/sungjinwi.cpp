/*
    풀이 :
        O(logN)의 시간복잡도를 달성하기 위해 이진탐색

        case 1: nums[mid] < nums[right]
            mid부터 right까지는 정렬된 상태
            따라서 min은 인덱스 left부터 mid에 존재할 가능성이 있으므로 right = mid로 업데이트

        case 2: else
            mid와 right 사이에 min이 오도록 rotate 되어있는 상태
            left부터 mid까지는 min이 존재할 수 없으므로 left = mid + 1로 업데이트

        이 두 조건문에 따라 최소값이 포함된 쪽만 남기면 결국 left == right이 되고 이 인덱스의 수를 return

    nums의 길이: N

    TC : O(logN)
        반으로 나눠서 탐색하는 이진탐색이므로 log2(N)의 시간복잡도를 가진다
    
    SC : O(1)
*/

class Solution {
    public:
        int findMin(vector<int>& nums) {
            int left = 0;
            int right = nums.size() - 1;
            while (left < right)
            {
                int mid = (left + right) / 2;
                if (nums[left] < nums[right])
                    return nums[left];
                else
                {
                    if (nums[mid] < nums[right])
                        right = mid;
                    else
                        left = mid + 1;
                }
            }
            return nums[left];
        }
    };
