// 시간복잡도: O(1)
// 공간복잡도: O(1)

package main

func reverseBits(num uint32) uint32 {
  stack := []uint32{}

  for i := 0; i < 32; i++ {
    stack = append(stack, num&1)
    num >>= 1
  }

  result := uint32(0)

  for i := 0; i < 32; i++ {
    result <<= 1
    result |= stack[i]
  }

  return result
}
