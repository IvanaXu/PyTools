# -*-coding:utf-8-*-
# @auth ivan
# @time 2019-09-02 11:26:03
# @goal leetcode rotate-image
"""
matrix1 =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

matrix2 =
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
"""
matrix = \
[
      [1,2,3],
      [4,5,6],
      [7,8,9]
]


class Solution1:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, r = len(matrix), []
        if n:
            for i in range(0, n):
                r1 = []
                for j in range(0, n):
                    k = n-j-1
                    r1.append(matrix[k][i])
                r.append(r1)
        return r

class Solution2:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = map(list, zip(*matrix[::-1]))
        return matrix

print(Solution1().rotate(matrix), Solution1().rotate(matrix))



