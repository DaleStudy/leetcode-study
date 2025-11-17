const cache: number[] = [];

function climbStairs(n: number): number {
    if(n === 1) return 1
    if(n === 2) return 2;

    // cache 값 있을 때
    if(cache[n]) return cache[n]

    // cache 값 없을 때
    cache[n] = climbStairs(n - 1) + climbStairs(n - 2);
    return cache[n]
};
