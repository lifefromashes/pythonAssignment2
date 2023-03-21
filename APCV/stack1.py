stack = [] # all functions share it

def push(obj):
    global stack # use 'global' to indicate stack's scope
    stack.append(obj)

def pop():
    global stack
    if len(stack)==0 : #is the stack []?
        print('stack underflow')
        return None
    return stack.pop() # use list's pop() to remove the last element

def top():
    if len(stack)==0: # if it is empty
        print('stack is empty')
        return None
    return stack[len(stack)-1]

def empty(): return not stack # is the stack []?
def member(obj): return obj in stack # item in stack?
def size(): return len(stack) # number entries
def dump(): print('<Stack:%s>' % stack)