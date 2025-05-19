// time: O(n*amount) space: O(amount)
class Solution {
    func coinChange(_ coins: [Int], _ amount: Int) -> Int {
        var queue: [(count: Int, total: Int)] = [(0, 0)] // (동전 개수, 누적 금액)
        var visited = Set<Int>() // 중복 제거용
        var index = 0  // 큐의 head
        
        while index < queue.count {
            let (count, total) = queue[index]
            index += 1
            
            if total == amount {
                return count
            }
            if visited.contains(total) {
                continue
            }
            visited.insert(total)
            // BFS 방식
            for coin in coins { // 모든 코인을 현재 누적금액에 한 번씩 더해서 큐에 저장
                let newTotal = total + coin
                if newTotal <= amount {
                    queue.append((count + 1, newTotal))
                }
            }
        }
        return -1
    }
}
