// week2 goal
// not knowing how to express, I googled and referenced a bit
function climbStairs(n: number): number {
    let stairArray: number[] = [1,2]
    for(let i = 2;i<n; i++){
        stairArray.push(stairArray[i-1]+stairArray[i-2])
    }
    return stairArray[n-1]
};
