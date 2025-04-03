// MARK: 리뷰를 받고 시도해본 다른 풀이 (time: O(n), space O(n)
class Solution {
    func topKFrequent(_ nums: [Int], _ k: Int) -> [Int] {
        // 빈도수 별로 Dictionary에 저장
        var dict = [Int: Int]()
        for num in nums {
            dict[num, default: 0] += 1
        }
        // Bucket sort 사용, 크기는 nums 만큼, 빈도수가 nums 공간보다 클수는 없으니까
        var bucket = Array(repeating: [Int](), count: nums.count + 1)
        for (key, value) in dict {
            // 빈도수를 인덱스로 key == num 을 저장함
            // 배열로 한 이유는 빈도수가 같은게 있을 수 있으니까!
            bucket[value].append(key)
        }

        // 결과 출력
        var answer = [Int]()
        // bucket의 뒤에서부터 탐색
        for index in stride(from: nums.count, to: 0, by: -1) {
            // 없으면 무시
            guard !bucket[index].isEmpty else { continue }
            // 버켓의 현재 인덱스에 nil이 아니면 하나씩 결과에 추가해줌.
            for item in bucket[index] {
                answer.append(item)
                // k개 만큼 가져왔다면 바로 리턴
                if answer.count == k { return answer }
            }
        }

        return answer
    }
}
// MARK: time: O(nlogn), space: O(n)
// n+nlogn+n
class Solution {
    func topKFrequent(_ nums: [Int], _ k: Int) -> [Int] {
        var dict = [Int: Int]()
        for num in nums {
            dict[num, default: 0] += 1
        }
        return [Int](dict.sorted{$0.value > $1.value}.map{$0.key}[..<k])
    }
}
