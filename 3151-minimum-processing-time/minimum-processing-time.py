class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime*=4
        processorTime.sort()
        tasks.sort(reverse=True)
        return max(time+task for time,task in zip(processorTime,tasks))