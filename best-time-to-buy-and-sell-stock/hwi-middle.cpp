class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int res = 0;
        int minPrice = prices[0];
        int len = prices.size();
        for (int i = 0; i < len; ++i)
        {
            res = max(res, prices[i] - minPrice); // 수익 최대화: 지금까지 가장 쌌던 날에 사서 오늘 팔기
            minPrice = min(minPrice, prices[i]); // '지금까지 가장 쌌던 날' 업데이트
        }

        return res;
    }
};
