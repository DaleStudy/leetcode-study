// Time Complexity: O(1)
// Space Complexity: O(1)
func reverseBits(num uint32) uint32 {
	reversedBits := bits.Reverse32(num)
	return reversedBits
}
