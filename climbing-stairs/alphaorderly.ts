/**
 * 시간 복잡도: O(n)
 * 공간 복잡도: O(1)
 */
function climbStairs(n: number): number {
    if(n <= 2) {
        return n
    }


    let a = 1;
    let b = 2;

    for(let i = 1; i < n; i++) {
        let temp = a;
        a = b;
        b = a + temp;
    }

    return a;
};
