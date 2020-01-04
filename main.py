class Mapper:
    def __init__(self,course):
        self.y = 1
        self.x = 2
        self.course = course
        self.past = [(1,1)]
        self.branch = []

    def next_from_here(self,direction):
        return self.next(self.y,self.x,direction)

    def next(self,y,x,direction):
        dy = None
        dx = None
        if(direction == 'n'):
            dx = x
            dy = y-1
        elif(direction == 'e'):
            dx = x+1
            dy = y
        elif(direction == 's'):
            dx = x
            dy = y+1
        else:
            dx = x-1
            dy = y
        return self.course[dy][dx],dy,dx

    def left_side(self,x,y,direction):
        dd = None
        if(direction == 'n'):
            dd = 'w'
        elif(direction == 'e'):
            dd = 'n'
        elif(direction == 's'):
            dd = 'e'
        else:
            dd = 's'
        
        return self.next(y,x,dd)

    def go(self,ny,nx):
        
        self.course[self.y][self.x] = '>'
        self.past.append( (self.y,self.x) )
        
        self.y = ny
        self.x = nx

    def has_reached(self,y,x):
        for p in self.past:
            if( p == (y,x) ):
                return True
        return False

    def branch_here(self):
        self.branch.append( (self.y,self.x) )

    def back(self):
        pos = self.branch.pop()
        self.y = pos[0]
        self.x = pos[1]

    def display(self):
        for r in self.course:
            print("".join(r))
            
    def output(self):
        with open('ans.txt','w') as f:
            for r in self.course:
                v = ''.join(r)
                f.write(v)

    def now_tile(self):
        return self.course[ self.y ][ self.x ]


direction = [ 'n' , 'e' , 'w' , 's' ] 

row = 0
course = []
with open('course.txt') as f:
    for line in f:
        course.append(list(line))

mapper = Mapper(course)
y = None
x = None
next_tile = None
end = False

while( not end ):

    mapper.output()    
    print(mapper.y , mapper.x , mapper.now_tile())

    no_arrive = []
    disables = 0
    for d in direction:
        tt,ty,tx = mapper.next_from_here(d)
        if(mapper.has_reached(ty,tx) or tt == '#'):
            disables = disables + 1
            continue
        no_arrive.append( (ty,tx) )

    if(len(no_arrive)>=2):
        mapper.branch_here()

    print(disables,no_arrive)

    #行き止まり
    if(disables == 4):
        mapper.back()
        continue

    for d in direction:
        next_tile,ny,nx = mapper.next_from_here(d)

        if(next_tile == 'G'):
            mapper.go(ny,nx)
            end = True
            break

        if( next_tile == ' ' ):
            mapper.go(ny,nx)
            break



mapper.display()

mapper.output()