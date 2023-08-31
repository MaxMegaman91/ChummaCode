import math, copy
import random

class Node():
    def __init__(self, val="", parent=None, leftChild=None, rightChild=None):
        self.val=val
        self.parent = parent
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.children = [x for x in [leftChild, rightChild] if x is not None]
    
    def traverse(self):
        returnList = []
        if self.leftChild:
            returnList.append(self.leftChild.traverse())
        returnList.append(self.val)
        if self.rightChild:
            returnList.append(self.rightChild.traverse())
        
        
        return returnList
    
    def __repr__(self):
        return self.val

    def __str__(self):
        return ", ".join(self.val)

def tree(children:list[Node], gamenums:list[int], games:list[Node]=[]) -> tuple[Node, list[Node]]:
    if len(children) == 1: return children[0], games
    for x in range(0, len(children) // 2):
        lc = x
        rc = lc + 1
        
        children[lc].parent = Node(["Match", gamenums.pop(0)], None, children[lc], children[rc])
        children[rc].parent = children[lc].parent
        
        child = children.pop(lc)
        children.pop(lc)
        
        children = [child.parent] + children
            
        games.append(child.parent)
    
    return tree(children, gamenums, games)

def singleElimination(teams:list, seeded:bool=True) -> tuple[list[Node], list[Node], Node]:
    if not seeded: random.shuffle(teams)
    
    teamnodes = []
    for team in teams:
        teamnodes.append(Node(["Team", team]))
    
    parent, games = tree(teamnodes, list(range(1, len(teams))))

    return teamnodes, games, parent


def humanize(games:list[Node]):
    for game in games:
        _, num = game.val
        
        leftChild = game.leftChild
        rightChild = game.rightChild
        
        if leftChild.val[0] == "Match":
            leftText = f"winner of match {leftChild.val[1]}"
        elif leftChild.val[0] == "Team":
            leftText = leftChild.val[1]
        
        if rightChild.val[0] == "Match":
            if rightChild.val[1] > leftChild.val[1]:
                rightText = f"winner of match {rightChild.val[1]}"
            else: 
                rightText = leftText
                leftText = f"winner of match {rightChild.val[1]}"
            
        elif rightChild.val[0] == "Team":
            rightText = rightChild.val[1]
            
        print(f"Match {num}: between {leftText} and {rightText}")

def unvaltree(initchildren=[], children:list[Node]=[], games:list[Node]=[]) -> tuple[Node, list[Node]]:
    if len(children) == 1: return children[0], games
    for x in range(0, len(children) // 2):
        lc = x
        rc = lc + 1
        
        children[lc].parent = Node("", None, children[lc], children[rc])
        children[rc].parent = children[lc].parent
        
        child = children.pop(lc)
        children.pop(lc)
        
        children = [child.parent] + children
            
        games.append(child.parent)
    
    return unvaltree(children, games)

def doubleElimination(teams:list):
    teamnodes = []
    dupe = []
    for team in teams:
        teamnodes.append(Node(["Team", team]))
        dupe.append(Node(["Team", team]))
    
    wparent, wgames = unvaltree(teamnodes)
    lparent, lgames = unvaltree()
    
    for x in dupe:
        par = x.parent
        par.leftChild = None
        par.rightChild = None
        x.parent = None
        
    parent = Node("final", None, wparent, lparent)
    
    return parent.traverse()
    
    
"""results = singleElimination(list("abcdef"))
humanize(results[1])
print(results[2].traverse())"""

print(doubleElimination(list("abcd")))