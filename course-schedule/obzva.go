/*
풀이
- 각 course를 node로 생각하고, prerequisite 관계에 있는 node를 간선으로 이어주면 단방향 간선으로 연결된 node 집합의 graph를 떠올릴 수 있습니다
- 이 문제는 위에서 설명한 graph에 loop가 있냐 없느냐를 판단하는 문제입니다
- 함수의 재귀호출 및 백트래킹을 이용해서 풀이할 수 있습니다

Big O
- N: 과목 수 (node의 개수)
- M: 배열 prerequisites의 길이 (간선의 개수)
- Time compleixty: O(N + M)
  - prereqMap을 초기화 -> O(M)
  - 함수의 재귀호출을 통해 우리는 각 node를 최대 한번씩 조회합니다 -> O(N)
- Space complexity: O(N + M)
  - prereqMap -> O(M)
  - checkingSet, checkedSet -> O(N)
*/

func canFinish(numCourses int, prerequisites [][]int) bool {
	// 주어진 prerequisites 배열로 `a_i: b_0, b_1, ...` 형태의 맵을 짭니다
	prereqMap := make(map[int][]int, numCourses)
	for _, pair := range prerequisites {
		prereqMap[pair[0]] = append(prereqMap[pair[0]], pair[1])
	}

	// checkingSet으로 현재 탐색하고 있는 구간에 loop가 생겼는지 여부를 판단하고, checkedSet으로 이미 탐색한 node인지를 판단합니다
	checkingSet, checkedSet := make(map[int]bool, 0), make(map[int]bool, 0)

	// 특정 과목 c를 듣기 위한 선행 과목들을 탐색했을 때 loop가 생기는지 여부를 판단하는 함수입니다
	// (Go 언어 특성상 L:20-21 처럼 함수를 선언합니다 (함수 내부에서 함수를 선언할 땐 익명 함수를 사용 + 해당 함수를 재귀호출하기 위해서 선언과 초기화를 분리))
	var checkLoop func(int) bool // loop가 있다면 true
	checkLoop = func(c int) bool {
		// 과목 c가 현재 탐색하고 있는 구간에 존재한다면 loop가 있다고 판단 내릴 수 있습니다
		_, checkingOk := checkingSet[c]
		if checkingOk {
			return true
		}
		// 과목 c가 이미 탐색이 완료된 과목이라면 과목 c를 지나는 하위 구간에는 loop가 없다고 판단할 수 있습니다
		_, checkedOk := checkedSet[c]
		if checkedOk {
			return false
		}
		// 과목 c를 checkingSet에 추가합니다
		// 만약 하위 구간에서 과목 c를 다시 만난다면 loop가 있다고 판단할 수 있습니다
		checkingSet[c] = true
		// 각 선행과목 별로 하위구간을 만들어 탐색을 진행합니다
		// 하위구간 중 하나라도 loop가 발생하면 현재 구간에는 loop가 있다고 판단할 수 있습니다
		for _, prereq := range prereqMap[c] {
			if checkLoop(prereq) {
				return true
			}
		}
		// 만약 loop가 발견되지 않았다면 checkedSet에 과목 c를 추가함으로써 과목 c를 지나는 구간이 안전하다고 표시합니다
		checkedSet[c] = true
		// checkingSet에서 과목 c를 지워줍니다
		delete(checkingSet, c)
		return false
	}

	for i := 0; i < numCourses; i++ {
		if checkLoop(i) {
			return false
		}
	}
	return true
}
