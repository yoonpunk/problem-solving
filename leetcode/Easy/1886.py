# 1886. Determine Whether Matrix Can Be Obtained By Rotation
class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        # 일치하면 True
        if self.check(mat, target):
            return True

        # 반시계방향 회전 후 일치하면 True
        current_mat = mat
        for i in range(3):
            rotated_mat = self.rotate(current_mat)
            check_result = self.check(target, rotated_mat)
            if check_result:
                return True
            current_mat = rotated_mat
        
        # 아무것도 일치하지 않으면 False
        return False

    # 반시계방향으로 회전
    def rotate(self, mat: list[list[int]]):
        n = len(mat)
        rotated_mat = []
        for i in range(n):
            line = []
            for j in range(n):
                line.append(0)
            rotated_mat.append(line)
        
        for i in range(n):
            for j in range(n):
                # x->y, y->x 변환 후 x축 대칭하면 반시계방향 회전
                rotated_mat[n-1-j][i] = mat[i][j]

        return rotated_mat
    
    # 매트릭스 일치 여부 체크
    def check(self, mat: list[list[int]], target):
        n = len(mat)
        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[i][j]:
                    return False

        return True