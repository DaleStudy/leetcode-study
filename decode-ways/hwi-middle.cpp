class Solution {
public:
    int numDecodings(string s) {
        int d[101];
        int len = s.size();

        if (s[0] == '0') // 0으로 시작할 수 없음
        {
            return 0;
        }

        d[0] = 1; // 빈 문자열 -> 1가지 방법
        d[1] = 1; // 첫 문자 -> 1가지 방법 (0이 아닌건 확인했음)

        for (int i = 2; i <= len; ++i) 
        {
            d[i] = 0;

            // 0이 아니어서 단독으로 해석 가능한 경우
            if (s[i - 1] != '0')
            {
                d[i] += d[i - 1];
            }

            // 앞글자와 조합해서 유효한 두 자리가 될 수 있는 경우
            if (s[i - 2] == '1' || (s[i - 2] == '2' && s[i - 1] <= '6')) 
            {
                d[i] += d[i - 2];
            }
        }

        return d[len];
    }
};
