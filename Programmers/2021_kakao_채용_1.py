import string
import re

def solution(new_id):
    
    # 1
    new_id = new_id.lower()
    
    # 2
    alphabet = string.ascii_lowercase + '-_.' + string.digits
    new_id = ''.join( x for x in new_id if x in alphabet)
    
    # 3
    new_id = re.sub("\.{2,}", '.', new_id)
    
    # 4
    if len(new_id) != 0 and new_id[-1] == '.':
        new_id = new_id[:-1]
    if len(new_id) != 0 and new_id[0] == '.':
        new_id = new_id[1:]
    
    # 5
    if len(new_id) == 0:
        new_id += 'a'
        
    # 6
    if len(new_id) >= 16 :
        new_id = new_id[:15]
    if len(new_id) != 0 and new_id[-1] == '.':
        new_id = new_id[:-1]
        
    # 7
    if len(new_id) <= 2 :
        last = new_id[-1]
        while len(new_id) != 3:
            new_id += last

    
    return new_id
