object Solution {
    def topKFrequent(nums: Array[Int], k: Int): Array[Int] = {
        return nums.groupBy(identity)
                .view.mapValues(_.size)
                .toSeq
                .sortBy(- _._2)
                .take(k)
                .map(_._1)
                .toArray
    }
}
