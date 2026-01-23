# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.


def maxArea(height):
        start = 0
        end = len(height)-1
        max_water = 0
        while start < end:

            min_height = min(height[start],height[end])
            water = min_height * (end - start)
            max_water = max(max_water,water)

            if height[start] < height[end]:
                start += 1

            else:
                end -= 1

        return max_water

h = [1,2,4,3]

print(maxArea(h))