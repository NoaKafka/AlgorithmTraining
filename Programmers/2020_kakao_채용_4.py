class Node :
    def __init__(self, val, leaf = False):
        self.val = val
        self.child = {}
        self.depth = 0
        self.leaf = leaf
        
class Trie:
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, string):
        cur =  self.head
        for c in string:
            if c not in cur.child:
                cur.child[c] = Node(c)
            cur.depth += 1
            #print(cur.val, ' 를 지나가는건 ', cur.depth, ' 개')
            cur = cur.child[c]
        cur.depth += 1
        #print(cur.val, ' 를 지나가는건 ', cur.depth, ' 개')
    
    def search(self, prefix):
        cur = self.head
        for c in prefix:
            if c in cur.child:
                cur = cur.child[c]
            else:
                return 0
        return cur.depth
    
def solution(words, queries):
    answer = []
    dic = {}
    
    for i in range(len(words)):
        num = str(len(words[i]))
        if not num in dic:
            dic.update({num : [Trie(), Trie()]}) #[Trie / reverseed Trie]
        dic[num][0].insert(words[i])
        dic[num][1].insert(words[i][::-1])
            
    for que in queries:
        le = len(que) #문자열 길이 ---> to find dic[le]
        #print(le)
        if not str(le) in dic:
            answer.append(0)
            continue

        
        if que[0] == '?' and que[len(que)-1] == '?':
            answer.append(dic[str(le)][0].cnt)
            continue
        elif que[0] == '?':
            #print(2)
            s = que[::-1]
            end = 0
            #print(s)
            for k in range(len(s)):
                if s[k] == '?':
                    end = k 
                    break
            #print(end)
            answer.append(dic[str(le)][1].search(s[:end]))
        elif que[len(que)-1] == '?':
            #print(2)
            end = 0
            for k in range(len(que)):
                if que[k] == '?':
                    end = k 
                    break
            answer.append(dic[str(le)][0].search(que[:end]))
        else :
            answer.append(0)
    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))
