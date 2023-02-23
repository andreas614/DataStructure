from BinarySearchTreeClass import BST



if __name__ == '__main__':
    BST1 = BST()
    print('printing', BST1)
    BST1.insert(2)
    BST1.insert(5)
    BST1.insert(3)
    BST1.insert_arr([4, 9, 0])
    print('printing', BST1)
    BST1.print_pretty()

