#树的深度遍历
import TreeLayerTraversal as LS


def DeepSearch_middle(head):
    if(head.left != None):
        DeepSearch_middle(head.left)
    if(head.value != None):
        print head.value
    if(head.right != None):
        DeepSearch_middle(head.right)

def DeepSearch_preorder(head):
    if(head.value != None):
        print head.value
    if(head.left != None):
        DeepSearch_preorder(head.left)
    if(head.right != None):
        DeepSearch_preorder(head.right)

def DeepSearch_postorder(head):
    
    if(head.left != None):
        DeepSearch_postorder(head.left)
    if(head.right != None):
        DeepSearch_postorder(head.right)
    if(head.value != None):
        print head.value

if __name__ == "__main__":
    head = LS.tree_node(None)
    LS.create_tree(head)
    print("Middle traversal is:")
    DeepSearch_middle(head)
    print("Preorder traversal is:")
    DeepSearch_preorder(head)
    print("Postorder traversal is:")
    DeepSearch_postorder(head)
