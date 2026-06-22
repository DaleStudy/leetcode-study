// TC: O(log n)
// SC: O(1)
function hammingWeight(n: number): number {
    const binary = n.toString(2);
    let bits = 0;
    for(let i = 0; i < binary.length; i++) {
        if(binary[i] === '1') {
            bits++;
        }
    }

    return bits;
};
