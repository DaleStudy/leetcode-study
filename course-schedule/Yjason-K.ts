
/**
 * 선수 과목과 이수 과목 관계를 확인하여 모든 과목을 이수할 수 있는지 여부 확인.
 * @param {number} numCourses - 전체 과목 수
 * @param {number[][]} prerequisites - 선수 과목과 이수 과목 관계 정보
 * @returns {boolean} - 모든 과목을 수강할 수 있는지 여부
 * 
 * 시간 복잡도: O(V + E)
 *  - 그래프를 생성하는 과정에서 O(E),
 *  - bfs O(V + E),
 * 
 * 공간 복잡도: O(V + E)
 *  - 각 과목에 대한 선수 과목 저장에 O(V + E),
 *  - prereqCount 저장에 O(V),
 *  - 큐(queue) 저장에 O(V),
 */
function canFinish(numCourses: number, prerequisites: number[][]): boolean {
    // 각 과목의 선수 과목 정보를 저장하는 리스트
    const graph: number[][] = Array.from({ length: numCourses }, () => []);
    // 각 과목의 선수 과목 수 를 저장하는 배열
    const prereqCount: number[] = new Array(numCourses).fill(0);
    
    // 그래프 및 선수 과목 개수 초기화
    for (const [course, prereq] of prerequisites) {
        graph[prereq].push(course); // 선수 과목을 들어야 수강 가능한 과목 추가
        prereqCount[course]++; // 해당 과목의 선수 과목 개수 증가
    }
    
    // 선수 과목이 없는 과목들을 저장할 큐
    const queue: number[] = [];
    
    // 선수 과목이 없는 과목들을 큐에 추가 (진입 차수가 0인 노드)
    for (let i = 0; i < numCourses; i++) {
        if (prereqCount[i] === 0) {
            queue.push(i);
        }
    }
    
    // 수강한 과목 수
    let completedCourses = 0;
    
    // 선수 과목이 없는 과목을 사용해서 다음 과목을 수강
    while (queue.length > 0) {
        const current = queue.shift()!;
        completedCourses++; // 과목 수강 완료
        
        // 현재 과목을 선수 과목으로 하는 다른 과목들의 선수 과목 개수 감소
        for (const nextCourse of graph[current]) {
            prereqCount[nextCourse]--;
            
            // 선수 과목 개수가 0이 되면 큐에 추가 (더 이상 기다릴 필요 없음)
            if (prereqCount[nextCourse] === 0) {
                queue.push(nextCourse);
            }
        }
    }
    
    // 모든 과목을 수강 수 있는지 확인
    return completedCourses === numCourses;
}

