// 8비트로 쪼갠 방법
function reverseBits(n: number): number {
  const TOTAL_BITS = 32;
  const BITS_IN_BYTE = 8;
  const BYTES_IN_INTEGER = TOTAL_BITS / BITS_IN_BYTE;
  const BYTE_MASK = 0xff;

  let result = 0;

  const reversedByteCache: number[] = Array.from({ length: 2 ** BITS_IN_BYTE }, (_, n) => {
    let reversedNum = 0;

    for (let i = 0; i < BITS_IN_BYTE; i++) {
      const bit = (n >>> i) & 1;
      reversedNum |= bit << (BITS_IN_BYTE - 1 - i);
    }

    return reversedNum;
  });

  for (let i = 0; i < BYTES_IN_INTEGER; i++) {
    const byte = (n >>> (i * BITS_IN_BYTE)) & BYTE_MASK;

    const reversed = reversedByteCache[byte];
    result |= reversed << (TOTAL_BITS - (i + 1) * BITS_IN_BYTE);
  }

  return result >>> 0;
}

// 32번 연산 방법
function reverseBits(n: number): number {
  const BITS_LEN = 32;

  let reversed = 0;

  for (let i = 0; i < BITS_LEN; i++) {
    const bit = (n >>> i) & 1;

    const reversedPosition = 31 - i;
    reversed |= bit << reversedPosition;
  }

  return reversed >>> 0;
}
