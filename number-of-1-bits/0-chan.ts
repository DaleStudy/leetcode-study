/**
 * time complexity : O(logn)
 * space complexity : O(logn)
 */
function hammingWeight(n: number): number {
    const MAX_NUM = 2147483648 - 1;
    
    const  bitwiseOperated = (n & MAX_NUM).toString(2);
    return  bitwiseOperated.replaceAll('0', '').length;
};
