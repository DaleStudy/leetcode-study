/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */

/**
 * candidates를 여러번 사용해도 된다. 하지만 사용한 종류와 개수가 모두 같으면 안된다. 
 * 
 */
var combinationSum = function(candidates, target) {
    const candidatesLength = candidates.length
    // 시작 시점에서 array를 만들어서 넘겨줘야한다. 
    // candidates 중에 넣으면 target이 되면 답에 그 배열을 넣고 탈출한다. 
    // 만약 더했는데 target보다 크면 그냥 리턴한다. 
    // target보다 작은것에 대해서 넣는다.
    const ret = []
    function dp(total,newNum,currentArr){
        if(total + newNum > target){
            return
        }
        if(total + newNum == target && ){
            ret.push([...currentArr,newNum]);
            return
        }

        //두 가지 어느것에도 해당하지 않으면 재귀를 또 다시 돈다.
        for(let i = 0; i<candidatesLength; i++){
            dp(total+newNum , candidates[i],[...currentArr,candidates[i]])
        }
    }
    dp(0,0,[])
    return ret
};

//여기서 문제가 생겼다. 
// 중복이 생긴다는 것이다. 어떻게 중복을 제거하면 좋을까?
/**
 * 1. Set을 이용한다.
 * 2. 순서를 둔다. idx를 dfs에 넘겨주어서, 순서대로 작동하게 한다. 
 */

var combinationSum = function(candidates, target) {
    const candidatesLength = candidates.length
    const ret = []
    function dp(idx,total,currentArr){
        if(total > target){
            return
        }
        if(total == target){
            ret.push(currentArr);
            return
        }

        //idx를 넘겨받아서, 그 이후의 것에만(자기 자신 포함) 돌게 된다. 그러면 절반정도만 돈다고 볼 수 있다.
        for(let i = idx; i < candidatesLength; i++){
            dp(i,total+ candidates[i],[...currentArr,candidates[i]])
        }
    }
    dp(0,0,[])
    return ret
};



/**
 시간복잡도: O(N^(target/min)) : N개 후보 중 선택하는 경우의 수가 target/min 깊이만큼 반복
공간복잡도: O(target/min) : 재귀 스택의 최대 깊이가 target/min


 */


// 2. dp를 활용한 문제 해결방법
var combinationSum = function(candidates, target) {
    const dp = Array.from({length:target+1},()=>[])
    dp[0] = [[]];
    for(let candidate of candidates){
        //여기서 candidate에 대해서, 이후 타겟까지 더할 수있는 숫자에 대한 조합에, candidate를 각각 넣어준다.
        for(let i = candidate; i <= target; i++){
            for(let comb of dp[i-candidate]){ //각 조합에 넣어줌
                dp[i].push([...comb,candidate])
            }   
        }
    }
    return dp[target]
};
/**
시간복잡도: O(N × target × 2^target)
N개 후보를 순회하면서, 각 후보마다 target까지의 값들에 대해 기존 조합들을 복사해서 새 조합을 생성하는데, 조합 개수가 지수적으로 증가함
공간복잡도: O(target × 2^target)
dp 배열의 각 인덱스에 해당 값을 만드는 모든 조합들을 저장하며, 최악의 경우 조합 개수가 지수적으로 증가함
 */