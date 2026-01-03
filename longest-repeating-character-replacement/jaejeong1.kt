import kotlin.math.max

fun characterReplacement(s: String, k: Int): Int {
	// 시간복잡도: O(N) 공간복잡도: O(1)

	val frequencyMap = mutableMapOf<Char, Int>()
	var left = 0
	var maxFreq = 0
	var result = 0
	// 처음부터 끝까지 right 순회
	for (right in s.indices) {
		// right 위치 문자에 빈도를 증가시키고 map 저장
		val rightChar = s[right]
		frequencyMap[rightChar] = frequencyMap.getOrDefault(rightChar, 0) + 1
		maxFreq = max(maxFreq, frequencyMap[rightChar]!!)

		val windowSize = right - left + 1
		val downSizeNeeded = windowSize - maxFreq

		if (downSizeNeeded > k) {
			val leftChar = s[left]
			frequencyMap[leftChar] = frequencyMap[leftChar]!! - 1
			left++
		}
		result = max(result, right - left + 1)
	}
}