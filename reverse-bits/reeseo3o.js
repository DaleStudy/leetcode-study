// Time Complexity: O(1)
// Space Complexity: O(1)

const reverseBits = (n) => {
    let result = 0;
  
    // 32비트 고정 - 정확히 32번
    for (let i = 0; i < 32; i++) {
      // 1. n의 마지막 비트만 뽑기 (0 또는 1)
      const bit = n & 1;
  
      // 2. result를 한 칸 왼쪽으로 밀고, 거기에 bit를 붙이기
      result = (result << 1) | bit;
  
      // 3. n은 오른쪽으로 한 칸 밀어서 다음 비트 준비
      n >>>= 1;
    }
  
    // 항상 32비트 unsigned로 보이게 하기 위해 마지막에 한 번 더 >>> 0
    return result >>> 0;
  };
  