/**
 * 가지고 있는 동전을 최대한 활용하여 최소의 조합으로 amount를 만드는 최소 동전 개수 구하는 함수
 * 
 * @param {number[]} coins  - 사용 가능한 동전 배열
 * @param {number} amount - 만들어야 하는 총합
 * @returns {number}
 * 
 * 시간 복잡도 O(n * m)
 *   - n은 동전 배열의 크기
 *   - m은 amount
 * 
 * 공간 복잡도 (n);
 *  - 큐에 최대 n개의 요소가 들어갈 수 있음
 */
function coinChange(coins: number[], amount: number): number {
    // 총합이 0인 경우 0 반환
    if (amount === 0) return 0;

    // 너비 우선 탐색을 활용한 풀이

    const queue: [number, number] [] = [[0, 0]]; // [현재 총합, 깊이]
    const visited = new Set<number>();

    while (queue.length > 0) {
        const [currentSum, depth] = queue.shift()!;

        // 동전을 하나씩 더해서 다음 깊이을 탐색
        for (const coin of coins) {
            const nextSum = currentSum + coin;
            
            // 목표 금액에 도달하면 현재 깊이를 반환
            if (nextSum === amount) return depth + 1;

            // 아직 총합에 도달하지 않았고, 중복되지 않아 탐색 가능한 경우
            if (nextSum < amount && !visited.has(nextSum)) {
                queue.push([nextSum, depth + 1]);
                visited.add(nextSum)
            }

        }
    }

    // 탐색 조건을 완료 해도 경우의 수를 찾지 못한 경우
    return -1;
}

