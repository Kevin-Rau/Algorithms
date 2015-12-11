#LastName: Rau   
#FirstName: Kevin
#Email: Kevin.Rau@colorado.edu   
#Comments: None, srry. 

from __future__ import print_function
import sys
import functools 

# We will use a class called my trie node
class MyTrieNode:
    # Initialize some fields 
  
    def __init__(self, isRootNode):
        #The initialization below is just a suggestion.
        #Change it as you will.
        # But do not change the signature of the constructor.
        self.isRoot = isRootNode
        self.isWordEnd = False # is this node a word ending node
        self.isRoot = False # is this a root node
        self.count = 0 # frequency count
        self.next = {} # Dictionary mappng each character from a-z to the child node

    def addWord(self, w): 
        assert(len(w) > 0)
        
        for char in w:
            if char not in self.next:
                self.next[char] = MyTrieNode(True)
            self = self.next[char]
        self.isWordEnd = True
        self.count += 1

    def lookupWord(self,w):
        
        for char in w:
            if char not in self.next:
                return 0
            else:
                self = self.next[char]
 
        return self.count
        
    def iterateChar(self,w,results=[]):
        for i in self.next:
            if(self.next[i].isWordEnd):
                results.append((w+i,self.next[i].count))
            self.next[i].iterateChar(w+i,results)
            
        return results
    
    def autoComplete(self,w):
        results = []
        for char in w:
            if char not in self.next:
                return []
            self = self.next[char]
        
        if self.isWordEnd:
                results.append((w, self.count)) 
        return list(self.iterateChar(w,results))
    
if (__name__ == '__main__'):
    t= MyTrieNode(True)
    lst1=['test','testament','testing','ping','pin','pink','pine','pint','testing','pinetree']

    for w in lst1:
        t.addWord(w)
    
    j = t.lookupWord('testy') # should return 0
    j2 = t.lookupWord('telltale') # should return 0
    j3 = t.lookupWord ('testing') # should return 2
    lst3 = t.autoComplete('pi')
    print('Completions for \"pi\" are : ')
    print(lst3)
    
    lst4 = t.autoComplete('tes')
    print('Completions for \"tes\" are : ')
    print(lst4)