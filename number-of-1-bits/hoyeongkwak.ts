/* 
    time complexity : O(log n)
    space complexity : O(1)
*/
function hammingWeight(n: number): number {   
    let count = 0
    while ( n != 0) {
        count += n & 1
        n >>>= 1
    }
    return count

    /* 
    time complexity : O(log n)
    space complexity : O(log n)
    */
    // const twoBits = n.toString(2)
    // const bitCount = twoBits.split('').filter((s) => s === '1').length
    // return bitCount
};