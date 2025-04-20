function hammingWeight(n: number): number {
  const binary: string = getBinary(n, "");
  return binary.replaceAll("0", "").length;
}

function getBinary(n: number, s: string): string {
  if (n <= 1) return n + s;
  return getBinary(Math.trunc(n / 2), (n % 2) + s);
}
