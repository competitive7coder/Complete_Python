def mergearray(nums1, nums2, m, n):
        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            if i >= 0 and nums2[j] > nums1[i]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                i >= 0
                nums1[k] = nums1[i]
                i -= 1
            k -= 1
        return nums1


nums1 = [1]
nums2 = []
m =1
n = 0
ans  = mergearray(nums1, nums2,m ,n)
print(ans)