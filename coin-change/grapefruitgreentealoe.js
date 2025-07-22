
//1. top-down
var coinChange = function(coins, amount) {
    if(amount == 0 ) return 0
    /*
    점화식 : dp[n] = Math.min(dp[n],dp[n-k]+1)
    */
    const dp = new Array(amount+1).fill(Math.pow(10,4));
    for(let c of coins){
        dp[c] = 1
    }
    function dfs(idx,coin){
        if(idx + coin > amount) return
        dp[idx+coin] = Math.min(dp[idx+coin],dp[idx]+1)
        if(idx + coin == amount){
            return 
        }else{
            for(let c of coins){
                //여기서 dfs를 안들어가는 방법은 없을까?
                dfs(idx+coin,c)
            }
        }
    }
    dfs(0,coins[0])

    if(dp[amount] > amount) return -1

    return dp[amount]
   
};

// 타임리밋에 걸린다. dfs의 가지치기가 덜 되어서 그렇다. 
// 그렇다면, 순차적인 dp를 좀더 활용하는 것이 좋아보인다. 현재로서는 메모이제이션의 이점을 제대로 활용할 수 없어보인다. 



//2. bottom-up
var coinChange = function(coins, amount) {
    coins = coins.filter(x=> x<=amount)
    if(amount == 0) return 0
    /*
    점화식 : dp[n] = Math.min(dp[n],dp[n-k]+1)
    */
    const dp = new Array(amount+1).fill(Math.pow(10,4)+1);
    dp[0] = 0
    //dfs를 쓰고 싶지 않다면, amount만큼의 for문을 돌면서 dp를 초기화해주면 된다. 
    for(let i=1; i <amount+1; i++){
        for(let coin of coins){
            if(i-coin >= 0){
                dp[i] = Math.min(dp[i-coin] + 1,dp[i])
            }
        }
    }
    if(dp[amount] > amount) return -1
    return dp[amount]
   
};

/**
dfs를 쓰고 싶지 않다면, amount만큼의 for문을 돌면서 dp를 초기화해주면 된다. 
처음에 coins = coins.filter(x=> x<=amount)
이렇게 쓴 이유는, amount보다 작은 코인만 필터하여 최적화한다. 

이 문제 풀이 소요시간이 1시간이 넘었는데, 
그 이유가, i-coin이 아니라, i+coin을 기준을 삼았었다. 
그러다보니 그러다 보니 각 금액 `i`의 최솟값을 찾기 위해 `dp[i]`를 `dp[i-coin]` 기반으로 갱신해야 한다는 핵심적인 아이디어를 적용하기 어려웠다.
`dp[i+coin]` 방식으로 접근하면, `dp[i]` 자체가 아직 최적의 상태가 아닌데도 그 값을 기반으로 미래의 `dp[i+coin]`을 업데이트하려 하기 때문에, 정확한 최적해를 찾아내기 어려웠다.
현재 금액 `i`를 만들기 위한 가장 효율적인 방법을 과거의 `dp[i-coin]`에서 찾는 '바텀업(Bottom-Up)' 방식이 이 문제에 훨씬 적합하다는 것을 깨닫는 데 시간이 걸렸다.



시간복잡도:  O(n * m)
공간 복잡도 : O(n)
 */