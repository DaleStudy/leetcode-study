function countBits(n: number): number[] {
    let base = 1;
    let result = [0];

    while (base <= n) {
        const numberOfBits = Array.from(base.toString(2)).filter(num => num === "1").length;
        result.push(numberOfBits);
        base += 1;
    }
    
    return result;
};
