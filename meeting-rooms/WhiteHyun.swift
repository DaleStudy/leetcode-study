//  
//  252. Meeting Rooms
//  https://leetcode.com/problems/meeting-rooms/description/
//  Dale-Study
//  
//  Created by WhiteHyun on 2024/05/12.
//  


/*
Definition of Interval:
class Interval {
    var start: Int
    var end: Int
    init() { start = 0; end = 0; }
    init(_ a: Int, _ b: Int) { start = a; end = b }
}
 */
final class Solution {
  func canAttendMeetings(_ intervals: [Interval]) -> Bool {
    let sortedIntervals = intervals.sorted { lhs, rhs in
      lhs.start < rhs.start
    }

    for i in sortedIntervals.indices.dropFirst() where sortedIntervals[i - 1].end > sortedIntervals[i].start {
      return false
    }

    return true
  }
}
