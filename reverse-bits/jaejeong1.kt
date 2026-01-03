fun reverseBits(n: Int): Int {
	var x = n
	var result = 0
	//시간복잡도: O(N) 공간복잡도: O(1)
	repeat(32) {
		// result를 왼쪽으로 1비트 밀어서 빈자리를 만듬
		result = (result shl 1)
		// x의 맨 오른쪽 1자리를 result의 맨 오른쪽에 할당
		result = result or (x and 1)
		// x 를 오른쪽으로 1비트 민다
		x = (x ushr 1)
	}
}
