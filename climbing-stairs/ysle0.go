package climbing_stairs

/**
 * 풀이: 이전 스텝을 계산하여 고정 한후 다음 조건을 확인하는 것에서 dp유형의 문제라는 생각이 들었지만
 * dp가 뭔지몰라 무서워 패턴은 못찾았습니다! (감정적)
 * 그래서 힌트 보고 피보나치 수열인 것을 파악 후 재귀하지않는 방식으로 풀었습니다.
 * 풀면서 피보나치도 dp의 방식으로 풀 수 있다는 걸 명확하게 알았네요. (memoization)
 */
func climbStairs(n int) int {
	return fibo(n)
}

func fibo(n int) int {
	ret := []int{0, 1}
	for i := 2; i <= n; i++ {
		ret = append(ret, ret[i-1]+ret[i-2])
	}
	ret = ret[len(ret)-2:]

	sum := 0
	for _, n := range ret {
		sum += n
	}
	return sum
}
