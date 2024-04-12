class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
# 
        answer = [0] * n 

        for booking in bookings:
            answer[booking[0] - 1] += booking[2]
            if booking[1] < n:
                answer[booking[1]] -= booking[2]
        
        acc = 0
        for index, value in enumerate(answer):
            acc += value
            answer[index] = acc
        
        return answer
        
#         seats = [0]*n
    
#         for booking in bookings:
#             first, last, seatsCount = booking
#             i = first - 1
#             while  i < last:
#                 seats[i] += seatsCount
#                 i+=1
    

    
#         return seats
