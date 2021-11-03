class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)

        intervals.sort()

        def overlap(interval1, interval2):
            return not (interval2[1] < interval1[0] or interval1[1] < interval2[0])

        ans = []
        for interval in intervals:
            if not ans or not overlap(ans[-1], interval):
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])

        return ans
        