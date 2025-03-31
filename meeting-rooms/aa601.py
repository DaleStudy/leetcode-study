'''
TC: O(nlogn) 
SC: O(1)
풀이 방법: 구간 중 첫번째 인자에 대해 정렬한 뒤, 이웃한 인자에 대해서만 겹치는지 확인한다
	시간 복잡도는 정렬에 드는 nlogn만큼 필요하다
'''

from typing import (
	List,
)
from lintcode import (
	Interval,
)
"""
Definition of Interval:
class Interval(object):
	def __init__(self, start, end):
		self.start = start
		self.end = end
"""

class Solution:
	"""
	@param intervals: an array of meeting time intervals
	@return: if a person could attend all meetings
	"""
	def can_attend_meetings(self, intervals: List[Interval]) -> bool:
		intervals.sort(key=lambda x: x.start)
		for i in range(1, len(intervals)):
			if intervals[i - 1].end > intervals[i].start:
				return False
		return True
