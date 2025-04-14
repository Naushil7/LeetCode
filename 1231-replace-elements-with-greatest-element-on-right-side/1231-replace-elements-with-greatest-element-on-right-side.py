class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # start = 0
        # end = len(arr) - 1

        # while start < end:
        #     temp_1 = 0
        #     temp_2 = max(arr[start+1:]) 
        #     temp_1 = max(temp_1, temp_2)
        #     arr[start] = temp_1
        #     start += 1

        # if start == end:
        #     arr[end] = -1

        # return arr
        max_so_far = -1

        for i in range(len(arr)-1, -1, -1):
            current = arr[i]
            arr[i] = max_so_far
            max_so_far = max(max_so_far, current)

        return arr