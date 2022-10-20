class Solution:

    # Function to find maximum
    # product subarray
    def maxProduct(self,arr, n):
        cur_max=arr[0]
        cur_min=arr[0]
        prev_max=arr[0]
        prev_min=arr[0]
        res=arr[0]
        for i in range(1,len(arr)):
            cur_max=max(arr[i],arr[i]*prev_max,arr[i]*prev_min)
            cur_min=min(arr[i],arr[i]*prev_max,arr[i]*prev_min)
            res=max(res,cur_max)
            prev_max=cur_max
            prev_min=cur_min
        return res
