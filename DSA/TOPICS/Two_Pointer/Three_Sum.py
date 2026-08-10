# def three_sum(arr):
#     res = set()
#     n = len(arr)
#
#     for i in range(n):
#         for j in range(i+1, n):
#             for k in range(j+1, n):
#                 if arr[i] + arr[j] + arr[k] == 0:
#                     # res.add((arr[i], arr[j], arr[k]))
#                     triples = [arr[i], arr[j], arr[k]]
#                     res.add(tuple(sorted(triples)))
#
#     return [list(t) for t in res]

# class Solution:
#     def three_sum(self, nums):
#         n = len(nums)
#         seen = set()
#         for i in range(n):
#             mp = set()
#             for j in range(i+1, n):
#                 c = - nums[i] - nums[j]
#                 if c in mp:
#                     seen.add(tuple(sorted((nums[i], nums[j], c))))
#                 mp.add(nums[j])
#         return [list(t) for t in seen]

class Solution:
    def three_sum(self, nums):
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, n - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif total < 0:
                    l += 1
                else:
                    r -= 1

        return res



# # ans = Solution()
# nums = [-1,0,1,2,-1,-4]
# ans1 = three_sum(nums)
# print(f"Three sum triples are{ans1}"

nums = [-1,0,1,2,-1,-4]
ans = Solution()
print(f"Three sum triples are{ans.three_sum(nums)}")


