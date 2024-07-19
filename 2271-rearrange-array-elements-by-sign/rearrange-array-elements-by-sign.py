class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negative= []
        positive= []

        for num in nums:
            if num < 0:
                negative.append(num)
            else:
                positive.append(num)
        final=list()
        for pos, neg in zip(positive, negative):
            final. append(pos)
            final.append(neg)

        return final
