#树的深度遍历
import TreeLayerTraversal as LS


def DeepSearch_middle(head):
    if(head.left != None):
        DeepSearch_middle(head.left)
    if(head.value != None):
        print head.value
    if(head.right != None):
        DeepSearch_middle(head.right)



if __name__ == "__main__":
    head = LS.tree_node(None)
    LS.create_tree(head)
    DeepSearch_middle(head)
