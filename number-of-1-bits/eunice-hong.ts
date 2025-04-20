function hammingWeight(n: number): number {
  // 1. convert the number to a binary string
  const binaryString = n.toString(2);

  // 2. count the number of 1s in the binary string
  return binaryString.split("").filter((char) => char === "1").length;
}
