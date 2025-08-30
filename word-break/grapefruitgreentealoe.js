
//1. 백트레킹

/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */

function findIndexAfter(arr, startIndex, callback) {
  for (let i = startIndex + 1; i < arr.length; i++) {
    if (callback(arr[i], i, arr)) {
      return i;
    }
  }
  return -1; // 못 찾으면 -1
}

var wordBreak = function(s, wordDict) {
    let current = '';
    const dp = new Array(s.length).fill('');
    for(let i=0;i<s.length;i++){
        const isSegment = wordDict.find((e) => e == current+s[i] )
        if(isSegment) {
            dp[i] = current + s[i]
            current = ''
        }else{
            current += s[i]
        }

        if(current.length == s.length && i == s.length-1){
            return dp[i] ? true:false
        }

        // 문자열이 저장이 되어있는 위치에 다시 돌아간다.
        // 그 위치에 빈 문자열을 넣어준 후 다음 index로 돌아가게끔 한다.
        if(i == s.length-1 && dp[s.length-1] == ''){
            i = dp.findLastIndex(e => e!=='')
            current = dp[i]
            dp[i] = '';
        }
    }
    return dp[s.length-1] ? true:false

};


// 가장 초기값으로 들어가게 되면, 또 같은일을 여러번 반복하게 되므로, 가장 큰 값으로 돌아가야하는게 맞다.
// 그런데 그만큼, 더 오래걸리는 경우가 발생한다. 

/*시간복잡도: O(n² * m) (n: 문자열 길이, m: wordDict 길이)
공간복잡도: O(n)
*/

//2. 실패난 지점을 메모이제이션 하기 : 시간리밋이 난 이유는, 이전에 실패난 지점에 대해서 다시 돌아간다는 문제가 있었기 때문에, word의 시작기점으로 잡으면 무조건 실패가 나는 index를 메모이제이션 한다.

/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
var wordBreak = function(s, wordDict) {
    const wordSet = new Set(wordDict); //중복이 되지 않게 만든다.
    const failed = new Set(); //실패한 인덱스를 기록한다.

    function dfs(start){
        if(start === s.length) return true; // 성공
        if(failed.has(start)) return false; //여길 기점으로 하면 실패한다는 것을 기록. 

        for(let end = start+1; end<=s.length; end++){
            const word = s.slice(start,end); 
            if(wordSet.has(word) && dfs(end)){ // 여기서 잘랐을 때 가능한지.
                return true;
            }
        }
        failed.add(start);
        return false;
    }
    return dfs(0);
};

/*
시간복잡도: O(n^2) + 메모이제이션으로 최적화
공간복잡도 : O(n) : 재귀스택, failed set
*/

//3. dp를 활용하여, 이중 포문으로 j,i 사이에 가능한 부분이 있는지 확인한다. 

var wordBreak = function(s, wordDict) {
    const wordSet = new Set(wordDict);
    const dp = new Array(s.length + 1).fill(false);
    dp[0] = true; // 빈 문자열은 항상 가능

    for (let i = 1; i <= s.length; i++) {
        for (let j = 0; j < i; j++) {
            if (dp[j] && wordSet.has(s.slice(j, i))) {
                dp[i] = true;
                break; // 더 이상 검사 안 해도 됨
            }
        }
    }

    return dp[s.length];
};

/*
시간복잡도: O(n^2)
공간복잡도 : O(n)
*/
