def container(height):
    n = len(height)
    max_area = 0

    for i in range(n):
        for j in range(i + 1, n):
            h = min(height[i], height[j])
            w = j - i
            area = h * w
            if area > max_area:
                max_area = area

    return max_area


print(container([1,8,6,2,5,4,8,3,7]))
print(container([1,1]))
# OPTIMAL
# i, j = 0, len(height) - 1
#         max_area = 0
#         while i < j:
#             h = min(height[i], height[j])
#             w = j - i
#             area = h * w
#             if area > max_area:
#                     max_area = area
#             if height[i] < height[j]:
#                 i+= 1
#             else:
#                 j-= 1
#
#         return max_area