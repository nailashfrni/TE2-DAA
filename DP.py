from node import Node

def v_cover_dp(root):
    if not root:
        return 0
    
    if not root.left and not root.right:
        return 0
    
    # compute size when root is included
    size_incl = (1 + v_cover_dp(root.left)
                 + v_cover_dp(root.right))
    

    # compute size when root is excluded
    size_excl = 0
    if root.left:
        size_excl += (1 + v_cover_dp(root.left.left)
                      + v_cover_dp(root.left.right))
        
    if root.right:
        size_excl += (1 + v_cover_dp(root.right.left)
                      + v_cover_dp(root.right.right))
        
    return min(size_incl, size_excl)

if __name__ == '__main__':
    root  = Node(20)
    root.left = Node(8)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    root.right  = Node(22)
    root.right.right = Node(25)
 
    print("Size of the smallest vertex cover is", v_cover_dp(root))