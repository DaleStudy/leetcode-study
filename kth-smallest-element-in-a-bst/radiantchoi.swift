// Definition for a binary tree node.
public class TreeNode {
    public var val: Int
    public var left: TreeNode?
    public var right: TreeNode?
    public init() { self.val = 0; self.left = nil; self.right = nil; }
    public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
    public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
        self.val = val
        self.left = left
        self.right = right
    }
}

class Solution {
    // 자체 풀이 - heapq를 구현하고, 그에 따라 트리의 모든 원소를 꺼내서 넣은 다음, k에 도달할 때까지 뽑아내는 방식
    // 모든 종류의 이진 트리에 적용 가능
    func kthSmallest(_ root: TreeNode?, _ k: Int) -> Int {
        var heapq = HeapQ<Int>(criteria: <)
        extractElement(root, &heapq)

        var result: Int? = nil

        for _ in 0..<k {
            result = heapq.pop()
        }

        return result ?? 0
    }

    func extractElement(_ root: TreeNode?, _ heapq: inout HeapQ<Int>) {
        guard let root else { return }

        heapq.push(root.val)

        extractElement(root.left, &heapq)
        extractElement(root.right, &heapq)
    } 
}

struct HeapQ<Element> {
    var storage: [Element]
    var criteria: (Element, Element) -> Bool

    var isEmpty: Bool {
        storage.isEmpty
    }

    init(
        storage: [Element] = [],
        criteria: @escaping (Element, Element) -> Bool
    ) {
        self.storage = storage
        self.criteria = criteria
    }

    mutating func push(_ element: Element) {
        storage.append(element)
        siftUp(from: storage.endIndex - 1)
    }

    mutating func pop() -> Element? {
        guard !isEmpty else { return nil }

        storage.swapAt(0, storage.endIndex - 1)

        defer {
            if !isEmpty {
                siftDown(from: 0)
            }
        }

        return storage.removeLast()
    }

    private mutating func siftUp(from index: Int) {
        var parent = (index - 1) / 2
        var child = index

        while child > 0 && criteria(storage[child], storage[parent]) {
            storage.swapAt(parent, child)
            child = parent
            parent = (child - 1) / 2
        } 
    }

    private mutating func siftDown(from index: Int) {
        var parent = index

        while true {
            let left = 2 * parent + 1
            let right = 2 * parent + 2
            var candidate = parent

            if left < storage.count && criteria(storage[left], storage[candidate]) {
                candidate = left
            }

            if right < storage.count && criteria(storage[right], storage[candidate]) {
                candidate = right
            }

            if candidate == parent { return }

            storage.swapAt(parent, candidate)
            parent = candidate
        }
    }
    
    // AI와 논의한 풀이: BST의 성질을 이용해 중위 탐색을 수행
    // 원소를 일반 배열에 삽입함으로써, 삽입시마다 O(logN)의 시간복잡도를 갖지 않고 O(1)의 시간복잡도를 가짐
    // 중위 탐색: 왼쪽 서브트리 - 자기 자신 - 오른쪽 서브트리 순으로 탐색
    func kthSmallest2(_ root: TreeNode?, _ k: Int) -> Int {
        var values: [Int] = []
        traverse(root, &values, k)

        return values[k - 1]
    }

    func traverse(_ node: TreeNode?, _ values: inout [Int], _ threshold: Int) {
        guard let node, values.count < threshold else { return }
        traverse(node.left, &values, threshold)
        
        guard values.count < threshold else { return }
        values.append(node.val)
        
        traverse(node.right, &values, threshold)
    }
}
