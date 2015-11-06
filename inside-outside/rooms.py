'''
Created on Nov 5, 2015

@author: clayt
'''



class RoomArranger():
    def __init__(self, n):
        self.n = n
        self.folks = [False] * n
        self.moves = []
        
    def arrange(self):
        self.moves.append(list(self.folks))
        self._solve_it(self.n)
    
    def _solve_it(self, n):
        if n==1:
            self.flip(n)
        else:
            self._solve_it(n-1)
            self.flip(n)
            self._solve_it(n-1)
            
    def flip(self, n):
        self.folks[n-1] = not self.folks[n-1]
        self.moves.append(list(self.folks))

    def __str__(self):
        s = str([[int(person) for person in move] for move in self.moves])
        return s.replace('], [', ']\n[')
        
        
if __name__ == '__main__':
    ra = RoomArranger(10)
    ra.arrange()
    print (ra)
    