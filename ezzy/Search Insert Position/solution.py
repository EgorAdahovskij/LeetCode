class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        sorted_list = nums
        low = None
        max_num = target - 1
        if target < min(sorted_list):
            return 0
        elif target > max(sorted_list):
            return len(sorted_list)
        if target in sorted_list:
            return sorted_list.index(target)
        else:
        
            while True:
                if max_num in sorted_list:
                    low = max_num
                    break
                else:
                    max_num -=1
            return sorted_list.index(max_num)+1
