// 풀이 방법
// 1. 인덱스 x까지의 최소값을 저장하는 배열 1개와, 인덱스 x부터의 최대값을 저장하는 배열 1개를 만든다.
// 2. 1번에서 만든 두 배열에 값을 채운다.
// 3. 두 배열을 각각 인덱스 별로 차를 구하고, 그 중 최댓값을 구한다.

// 시간 복잡도
// O(n) : 배열을 2번 순회하므로 O(n)이다.
// 공간 복잡도
// O(n) : 최소값과 최대값을 저장하는 배열을 만들었으므로 O(n)이다.

class Solution {
    public int maxProfit(int[] prices) {
        int len = prices.length;
        int[] minArr = new int[len];
        int[] maxArr = new int[len];

        for(int i=0;i<len;i++){
            if(i==0){
                minArr[i] = prices[i];
                maxArr[len-i-1] = prices[len-i-1];
            }else{
                minArr[i] = Math.min(minArr[i-1], prices[i]);
                maxArr[len-i-1] = Math.max(maxArr[len-i], prices[len-i-1]);
            }
        }

        int result = 0;
        for(int i=0;i<len;i++){
            result = Math.max(result, maxArr[i]-minArr[i]);
        }
        return result;
    }
}


// 2nd solution 
// 시간 복잡도: O(n)
// 공간 복잡도: O(1) 

class Solution{
    public int maxProfit(int[] prices){
        int len = prices.length;
        int buy = prices[0];
        int result = 0;

        for(int i=1;i<len;i++){
            if(prices[i]<buy){ // 더 저렴한 주식이 있으므로
                buy = prices[i]; // 이 주식을 산다.
            }else{
                result = Math.max(result, prices[i]-buy); // 현재 주식을 팔았을 때 이득이 더 크다면 판다.
            }
        }
        return result;
    }
}
