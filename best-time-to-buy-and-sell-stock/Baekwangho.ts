/**
일단 가장 단순하게 생각했을 때,
n^2 의 시간 복잡도를 가지면 모든 경우의 수를 확인가능하다.

function maxProfit(prices: number[]): number {
    let maximum = 0
    for(let i=0; i<prices.length-1; i++) {
        for(let j=i; j<prices.length; j++) {
            if(prices[j] - prices[i] > maximum) maximum = prices[j] - prices[i]
        }
    }
    return maximum
};
 */

/** 
하지만 시간 초과가 발생하니, 다른 방법을 써보자.
이익을 구하기 위해서는 가장 낮은 지점과 가장 큰 지점에 대한 탐색이 필요하다.
가장 낮은 지점은 큰 지점보다 앞에 위치해야 한다.

만약 투 포인터로 양 끝에서 오면서 왼쪽은 가장 낮은 것, 오른쪽은 가장 높은 것을 확인해서
두 포인터가 만날 때 차분을 구한다면?

function maxProfit(prices: number[]): number {
    let left = prices[0];
    let right = prices[prices.length-1];
    for (let i=0; i<prices.length; i++) {
        if (i > (prices.length - 1 - i)) {
            break
        }

        if (prices[i] < left) {
            left = prices[i]
        }

        if (prices[prices.length - 1 - i] > right) {
            right = prices[prices.length - 1 - i]
        }
    }

    return left > right ? 0 : right - left
}; 
*/

/**
[3,2,6,5,0,3] 와 같은 경우에 일반화 되지 못한다.
정답을 기준으로, 큰 값 이후에는 그보다 큰 값이 없어야 하고,
작은 값 이전에는 그보다 작은 값이 없어야 한다.

그렇다면 포인터를 이 기준에 맞게 급격히 옮겨볼까?
... 
힌트를 보고 왔다. 단순하게 최저값을 항상 갱신해주면 되는구나.
 */
function maxProfit(prices: number[]): number {
  let min = 10000;
  let max = 0;
  for (let i = 0; i < prices.length; i++) {
    if (prices[i] < min) {
      min = prices[i];
      continue;
    }

    if (prices[i] - min > max) {
      max = prices[i] - min;
    }
  }
  return max;
}
