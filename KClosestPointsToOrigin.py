class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = list()
        for point in points:
            distance.append([point[0] * point[0] + point[1] * point[1], point[0], point[1]])
        distance.sort(key=lambda l:l[0])
        result = list()
        for i in range(k):
            result.append(distance[i][1:3])
        return result
