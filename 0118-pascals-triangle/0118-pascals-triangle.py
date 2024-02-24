def generate_row(row):
    ans = 1
    ans_row = [1]

    for col in range(1, row):
        ans = ans * (row - col)
        ans = ans // (col)
        ans_row.append(ans)

    return ans_row
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(1, numRows+1):
            temp = generate_row(i)
            ans.append(temp)
        return ans
        