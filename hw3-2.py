import sys
sys.setrecursionlimit(200000)
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    integers = list(map(int, input_data))
    if len(integers) % 2 != 0:
        return
        
    n = len(integers) // 2
    preorder = integers[:n]
    inorder = integers[n:]
    
    inorder_map = {val: i for i, val in enumerate(inorder)}
    
    pre_iter = iter(preorder)
    
    def build_tree(in_start, in_end):
        if in_start > in_end:
            return 0
            
        root_val = next(pre_iter)
        root_idx = inorder_map[root_val]
        
        left_size = root_idx - in_start
        
        
        left_height = build_tree(in_start, root_idx - 1)
        right_height = build_tree(root_idx + 1, in_end)
        
        return max(left_height, right_height) + 1

    height = build_tree(0, n - 1)
    print(height)

if __name__ == '__main__':
    solve()
