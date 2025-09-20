object Solution {
    val _DRCS = Array(
        Array(-1, 0),
        Array(0, -1),
        Array(0, 1),
        Array(1, 0),
    )
    def pacificAtlantic(heights: Array[Array[Int]]): List[List[Int]] = {
        val visited = Array.fill[Array[Int]](heights.length)(
            Array.fill[Int](heights.head.length)(0)
        )
        for (i <- heights.indices) {
            dfs(heights, visited, i, 0, 1)
            dfs(heights, visited, i, heights.head.length - 1, 2)
        }
        for (i <- heights.head.indices) {
            dfs(heights, visited, 0, i, 1)
            dfs(heights, visited, heights.length - 1, i, 2)
        }
        (
            for {
                r <- visited.indices
                c <- visited.head.indices
                if visited(r)(c) == 3
            } yield List(r, c)
        ).toList
    }
    def dfs(heights: Array[Array[Int]], visited: Array[Array[Int]], r: Int, c: Int, v: Int): Unit = {
        visited(r)(c) |= v
        _DRCS.map { case Array(dr, dc) => (r + dr, c + dc) }
                .filter { case (nr, nc) => nr != -1 && nr != heights.length && nc != -1 && nc != heights.head.length }
                .filter { case (nr, nc) => (visited(nr)(nc) & v) == 0 && heights(r)(c) <= heights(nr)(nc) }
                .foreach { case (nr, nc) =>
                    dfs(heights, visited, nr, nc, v)
                }
    }
}
