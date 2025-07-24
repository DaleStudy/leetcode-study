//1.dfs로 풀기 : 시간초과 남


/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    /*
    arr: 현재 고정 배열을 뜻함. dfs가 돌때마다 변경됨.
    start: 끝난 index. arr와 마찬가지로 이것은 for문안에서 변경될 예정. 
    dep: dep은 현재 dfs의 dep+1을 해주면 됨. 
    */
    const numsLength = nums.length
    if(numsLength ==3 && nums.reduce((a,b)=>a+b,0) == 0) return [nums]

   const ret = []
   const seen = new Set();
    nums.sort((a, b) => a - b);
    function dfs(arr,start,dep){
    if(dep == 3) {
    if(arr.length !==3) return
    const arrTotal = arr.reduce((a,b)=>a+b,0);
    if(arrTotal == 0){
        const string = [...arr].sort((a,b)=>a-b).join(',')
        if(!seen.has(string)){
            seen.add(string)
            ret.push(arr)
        }
    }
        return 
    }
    //만약 start가 0이 되면, i를 감소시켜야하고, 새로운 배열을 추가해야한다. 기존의 배열에 넣어주는게 아니다. 

    //끝점을 증가시키면서 진행해야함. 현재 고정 arr에 끝점 그 앞의 idx부터 진행해서 0까지 감소시키면서 dfs를 돌리면 된다. 
    //idx가 i-1부터이므로, i는 최소 1이어야 가능하다.
    for(let idx = start; idx<numsLength; idx++){
        // currArr.push([...arr,nums[idx]])
        //현재 i에 대한 현재 currArr를 만들어준다. 
        //만들어준 각 Arr에 대해서, 다시 dfs로 들어가서, 각 배열의 내부의 합이 0인지 확인하고, 
        //현재 배열에 대한 set에 대해서 중복이 되는 것은 없는지 확인하면서 넣어준다.
        dfs([...arr,nums[idx]],idx+1,dep+1)
    }}
    dfs([],0,0)
    //마지막에 set으로 triples의 중복을 제거해줘야한다. 

    return ret
};

/*
시간복잡도: 
nums.sort((a, b) => a - b): 배열 정렬에 O(NlogN)

N개 숫자 중 3개 선택하는 조합 수 N(N−1)(N−2)/6
정확히 알 수는 없지만, 

N^3 이상으로 보임.

공간복잡도 : O(N^3) => seen 때문.

*/

//2. 투포인터로 풀기