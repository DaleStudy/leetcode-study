function reverseBits(n: number): number {
    const binaryStr = n.toString(2).padStart(32, '0')
    const reverseNum = binaryStr.split('').reverse().join('')
    return parseInt(reverseNum, 2)
};
