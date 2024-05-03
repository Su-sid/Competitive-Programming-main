class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        # store=[]
        # prev= -inf

        # # print(prev)

        # if firstList== None or secondList==None:
        #     return []
        # else:

        #     for i in range(len(secondList)):
        #         # print(i)
        #         if prev==firstList[i][0]:

        #             store.append([prev, prev])
        #         prev=secondList[i][1]
        #         store.append([secondList[i][0],firstList[i][1]])
        #     # print(store)

        # return store

        l = 0
        r = 0
        store = []

        while l < len(firstList) and r < len(secondList):
            mini = max(firstList[l][0], secondList[r][0])
            maxi = min(firstList[l][1], secondList[r][1])
            if maxi >= mini:
                store.append([mini, maxi])
            if firstList[l][1] <= secondList[r][1]:
                l += 1
            else:
                r += 1
        return store
