class Node:
    def __init__(self, l, d):
        self.letter = l
        self.depth = d
        self.childs = []
        self.cnt = 0

root = Node('', 0)

def make_tree(word):
    cur = root
    for i in range(len(word)):
        # cur의 childs에 word[i]가 있을때,
        for c in cur.childs:
            if c.letter == word[i]:
                cur = c
                cur.cnt += 1
                break
        # 없을때,
        else:
            temp_node = Node(word[i], cur.depth + 1)
            temp_node.cnt += 1
            cur.childs.append(temp_node)
            cur = cur.childs[-1]

def search_tree(word):
    cur = root
    for i in range(len(word)):
        if cur.cnt == 1:
            return cur.depth
        else:
            for c in cur.childs:
                if c.letter == word[i]:
                    cur = c
    return len(word)


def solution(words):
    answer = 0
    for w in words:
        make_tree(w)
    for w in words:
        answer += search_tree(w)
        
    return answer
