import math


class Node():
    def __init__(self, val="", parent=None, leftChild=None, rightChild=None):
        self.val=val
        self.parent = parent
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.children = [x for x in [leftChild, rightChild] if x != None]
    
    def traverse(self):
        returnList = []
        if self.leftChild != None:
            returnList.append(self.leftChild.traverse())
        returnList.append(self.val)
        if self.rightChild != None:
            returnList.append(self.rightChild.traverse())
        
        return returnList
    
    def __repr__(self):
        return self.val

    def __str__(self):
        return self.val
            
           
def initTree(treeHeight):
    topParent = Node()
    children = tree(treeHeight, [topParent])
    print(topParent.leftChild, topParent.parent, topParent.rightChild)
    
    return topParent, children
    
def tree(treeHeight, parents:list[Node]= None):
    if treeHeight == 0: return parents
    children = []
    for x in parents:
        x.leftChild = Node(parent=x)
        children.append(x.leftChild)
        x.rightChild = Node(parent=x)
        children.append(x.rightChild)
    return tree(treeHeight-1, children)

def singleElimination(teamlist:list):
    numTeams = len(teamlist)
    if numTeams == 0:
        return False, "Invalid Teams"
    treeHeight = int(math.log2(numTeams))
    
    parent, children = initTree(treeHeight)
    
    for n in range(len(children)):
        children[n].val = teamlist[n]
    
    unassigned = teamlist[len(children):]
    
    for u in range(len(unassigned)):
        gamenode = children[u]
        gamenode.leftChild = Node(gamenode.val, parent = gamenode)
        gamenode.val = ''
        gamenode.rightChild = Node(unassigned[u], parent = gamenode)
        
        children.pop(u)
        children += [gamenode.leftChild, gamenode.rightChild]
        
    children.sort(key=lambda x: x.val)
    
    print(children)
    
    # TODO: number the tree by game order
    
    return parent.traverse()

print(singleElimination(list("abcde")))
    