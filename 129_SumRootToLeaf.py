#basically, the question is asking you to use dfs to find every path
#from root to leaf and add them together
#for example, binary tree [1,2,3] has 2 paths, 1->2 and 1->3
#in this case, we add 12 and 13 together to return 25

#class that represents a node in the tree
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#solution class
class Solution():
    def dfsHelper(self, root, tempRes, sumArr):
        if root is None:
            return
        tempRes = tempRes * 10 + root.val
        if root.left is None and root.right is None:
            sumArr[0] += tempRes
            return
        self.dfsHelper(root.left, tempRes, sumArr)
        self.dfsHelper(root.right, tempRes, sumArr)
    def sumNumbers(self, root):
        sumArr = [0]
        tempRes = 0
        self.dfsHelper(root, tempRes, sumArr)
        return sumArr[0]

def test_solution():
    solution = Solution()
    
    # Test case 1: [1,2,3]
    # Paths: 1->2 (12) and 1->3 (13). Sum = 25
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    print(f"Test 1: {solution.sumNumbers(root1)}")  # Expected: 25
    
    # Test case 2: [4,9,0,5,1]
    # Paths: 4->9->5 (495) and 4->9->1 (491) and 4->0 (40). Sum = 1026
    root2 = TreeNode(4)
    root2.left = TreeNode(9)
    root2.right = TreeNode(0)
    root2.left.left = TreeNode(5)
    root2.left.right = TreeNode(1)
    print(f"Test 2: {solution.sumNumbers(root2)}")  # Expected: 1026
    
    # Test case 3: Empty tree
    print(f"Test 3: {solution.sumNumbers(None)}")  # Expected: 0
    
    # Test case 4: Single node
    root4 = TreeNode(5)
    print(f"Test 4: {solution.sumNumbers(root4)}")  # Expected: 5

if __name__ == "__main__":
    test_solution()