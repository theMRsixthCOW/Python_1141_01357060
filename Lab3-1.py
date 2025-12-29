import sys

def solve():
    # Read all input from stdin
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        
        # Read n integers for user A
        a_friends = set()
        for _ in range(n):
            a_friends.add(int(next(iterator)))
            
        # Read m integers for user B
        b_friends = set()
        for _ in range(m):
            b_friends.add(int(next(iterator)))
            
        # Find common friends
        common = a_friends.intersection(b_friends)
        
        # Output count
        print(len(common))
        
        # Output sorted common friends if any
        if common:
            sorted_common = sorted(common)
            print(*(sorted_common))
            
    except StopIteration:
        pass

if __name__ == '__main__':
    solve()