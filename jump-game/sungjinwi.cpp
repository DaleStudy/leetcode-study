/*
    풀이 :
        마지막 인덱스를 시작점으로 하는 변수 lastReachable 선언
        마지막 인덱스에 도달할 수 있는 가장 작은 인덱스를 저장
        위에서 내려오면서 lastReachable 높이에 점프해서 닿을 수 있는 가장 작은 높이를 새로운 lastReachable로 업데이트
        반복문이 끝나고 lastReachable == 0을 리턴한다

    nums의 길이 : N

    TC : O(N)
        for문 반복 1회
    
    SC : O(1)
        변수 lastReachable 외에 추가적인 메모리 할당 없음
*/

#include <vector>
using namespace std;

class Solution {
    public:
        bool canJump(vector<int>& nums) {
            int lastReachable = nums.size() - 1;
    
            for (int i = nums.size() - 2; i >= 0; i--) {
                if (i + nums[i] >= lastReachable)
                    lastReachable = i;
            }
    
            return lastReachable == 0;
        }
    };
