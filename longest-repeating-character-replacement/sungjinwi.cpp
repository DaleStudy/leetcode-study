/*
    s는 영어 대문자만 포함 : 26의 크기를 가진 vector counts에 빈도 저장
    
    left, right 통해 슬라이딩 윈도우 기법 적용

    1. right 위치의 문자 빈도 수를 증가시키고 maxCnt를 업데이트한다
        - maxCnt는 현재까지 윈도우를 움직이면서 윈도우 내에 한가지 문자의 최대 빈도수

    2. (윈도우의 크기 - maxCnt) > k일 때 최대 대체 가능한 문자의 수를 넘어섰으므로 윈도우의 크기를 줄임
        : s[left]의 빈도 감소 및 left를 전진
    
    3. ans는 max(현재 윈도우의 크기, 기존 최대 크기 ans) 로 업데이트

    
    - ans의 증가는 maxCnt가 증가 | 최대빈도문자와 다른 문자가 k개 이하일 때 -> (maxCnt ~ maxCnt + k)로 업데이트
        이 때는 while 루프를 수행하지 않음

    - while (right - left + 1 - maxCnt > k) -> 실제 이 조건을 만족하는 윈도우에서는 대체해야할 문자가 k보다 많이 존재할 수도 있다
        다만 윈도우의 크기를 maxCnt + k개로 제한하기 때문에 실제 답보다 더 크게 업데이트 될 수 없다
        매번 윈도우 내의 최대빈도문자를 계산하지 않아도 되기 때문에 살짝 최적화 O(26n) -> O(n)

    s의 길이 : N

    TC : O(N)

    SC : O(1)
        상수(26) 크기의 배열
*/

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int characterReplacement(string s, int k) {
        vector<int> counts(26, 0);
        int left = 0, right = 0, maxCnt = 0, ans = 0;

        for(; right < s.size(); right++) {
            maxCnt = max(maxCnt, ++counts[s[right] - 'A']);

            while (right - left + 1 - maxCnt > k) {
                --counts[s[left] - 'A'];
                left++;
            }
            ans = max(ans, right - left + 1);
        }
        return ans;
    }
};
