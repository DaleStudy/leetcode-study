/*
dp 배열을 만들고 s를 순회하며 각 단계에서 이전 자리의 숫자를 채택하거나 버리는 경우를 더해 나간다
만약 현재 순번의 숫자가 0일 경우 : 이전 자리의 숫자를 채택, i-1 순번의 숫자가 0이거나 3 이상이면 즉시 0을 리턴. 아닐 경우 dp의 i-2번째값을 넣는다.
이전 순번의 숫자와 현재 숫자를 더한 값이 26보다 크거나 이전 순번의 숫자가 0일 경우 : 개별 자리의 숫자를 채택, 직전 dp값을 넣는다
위에 모두 해당하지 않을 경우 : 개별 자리의 숫자를 채택하거나 버리는 경우를 다 고려하여 직전 dp값과 2스텝 전 dp값을 더한다
맨 끝 순번에 도달했을 때의 값을 구한다

시간복잡도 : O(N) (N은 s의 길이)
*/

function numDecodings(s: string): number {
    if(s.startsWith("0")) return 0;
    const dp = [];

    dp.push(1);
    if(s.length<2) return dp[0]
    for(let i=1;i<s.length;i++){
        const numStr = s[i];
        if(numStr === "0") {
            if(s[i-1] === "0" || Number(s[i-1])>=3) return 0;
            dp.push(dp?.[i-2] ?? 1)
        }else if(Number(`${s[i-1]}${numStr}`) > 26 || s[i-1] === "0"){
            dp.push(dp[i-1])
        }else{
            dp.push(dp[i-1] + (dp?.[i-2] ?? 1))
        }
    }

    return dp[s.length-1];
};