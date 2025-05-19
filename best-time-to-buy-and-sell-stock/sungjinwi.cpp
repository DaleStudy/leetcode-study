/*
    풀이 :
        현재의 price에 도달하기 전 가장 작은 price를 min_cur로 업데이트
        price - min_cur가 저장되있는 max_profit보다 크면 값을 업데이트

    prices의 개수 N

    TC : O(N)

    SC : O(1)
*/


#include <vector>
using namespace std;

class Solution {
    public:
        int maxProfit(vector<int>& prices) {
            int min_cur = prices[0];
            int max_profit = 0;

            for (int& price : prices)
            {
                if (price < min_cur)
                {
                    min_cur = price;
                    continue ;
                }

                int profit = price - min_cur;
                if (profit > max_profit)
                    max_profit = profit;
            }
            return max_profit;
        }
    };
