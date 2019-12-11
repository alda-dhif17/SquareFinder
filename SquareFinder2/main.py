import sys
from threading import Thread

SPACING = 5

class Point(object):
    def __init__(self, x, y, n):
        self.x = x
        self.y = y
        self.n = n
        
        self.xx = [0, 0]
        self.xy = [0, 0]
            
    def discover_x(self, a, d, points):
        for x in range(self.x+d, -1 if d < 0 else len(a[self.y]), d):
            if a[self.y][x] != self.n:
                break
            self.xx[0 if d < 0 else 1] += 1
        
    def discover_y(self, a, d, points):
        for y in range(self.y+d, -1 if d < 0 else len(a), d):
            if a[y][self.x] != self.n:
                break
            self.xy[0 if d < 0 else 1] += 1
        
    def discover(self, a, points):
        t = []
        for i in [-1,1]:
            s = Thread(target=self.discover_x, args=(a, i, points,))
            s.start()
            t.append(s)
            
            s = Thread(target=self.discover_y, args=(a, i, points,))
            s.start()
            t.append(s)
            
        for s in t:
            s.join()
            
    def __str__(self):
        return 'Point({:d}, {:d}, {:d}: [{}], [{}])'.format(self.x, self.y, self.n, 
                                                      ','.join([str(n) for n in self.xx]), 
                                                      ','.join([str(n) for n in self.xy]))
        
def gen_points(a):
    ps = []
    for y in range(0, len(a), SPACING):
        for x in range(0, len(a[y]), SPACING):
            ps.append(Point(x, y, a[y][x]))
    return ps

def find_point(ps, x, y):
    return list(filter(lambda p: p.x == x and p.y == y, ps))[0]

def step(a, x, y, ox, oy, n):
    x -= 1
    y -= 1
    
    for tx in range(ox, x+1):
        if a[oy][tx] != n or a[y][tx] != n:
            return False
        # print('(%d, %d) | (%d, %d)' % (tx, oy, tx, y))
    # print('='*32)
    for ty in range(oy, y+1):
        if a[ty][ox] != n or a[ty][x] != n:
            return False
        # print('(%d, %d) | (%d, %d)' % (ox, ty, x, ty))
    return True

def find_square(a, ox, oy):
    x, y = ox, oy
    n = a[y][x]
    l = 0
    while a[y][x] == n:
        x += 1
        y += 1
        l += 1

    print(ox, oy, l)
    print('='*32)
    
    while l > 0 and not step(a, x, y, ox, oy, l):
        print(x, y, l)
        x -= 1
        y -= 1
        l -= 1
    
    return l

def build_square(a, p):
    return find_square(a, p.x, p.y)

def evolve_square(a, x, y, s):
    maxi = dict(x=x, y=y, s=s)
    visited_points = []
    t = []
    
    def move_x(x, y, td):
        x += td
        if (x, y) in visited_points:
            return
        s = find_square(a, x, y)
        if s >= maxi['s']:
            maxi['x'] = x
            maxi['y'] = y
            maxi['s'] = s
        else:
            return

        visited_points.append((x, y))
        tt = []
            
        for td in (-1, 1):
            s = Thread(target=move_x, args=(x, y, td,))
            s.start()
            tt.append(s)

            s = Thread(target=move_y, args=(x, y, td,))
            s.start()
            tt.append(s)

        for s in tt:
            s.join()
    
    def move_y(x, y, d):
        y += d
        if (x, y) in visited_points:
            return
        s = find_square(a, x, y)
        if s >= maxi['s']:
            maxi['x'] = x
            maxi['y'] = y
            maxi['s'] = s
        else:
            return
            
        visited_points.append((x,y))
        tt = []
            
        for d in (-1, 1):
            s = Thread(target=move_x, args=(x, y, d,))
            s.start()
            tt.append(s)

            s = Thread(target=move_y, args=(x, y, d,))
            s.start()
            tt.append(s)

        for s in tt:
            s.join()
    
    for d in (-1, 1):
        s = Thread(target=move_x, args=(x, y, d,))
        s.start()
        t.append(s)
        
        s = Thread(target=move_y, args=(x, y, d,))
        s.start()
        t.append(s)
    
    for s in t:
        s.join()
        
    return maxi['x'], maxi['y'], maxi['s']
            
def main(): 
    a = []
    with open('input.txt', 'r') as f:
        a = [[int(c) for c in l.split(' ')] for l in f.read().replace('\r\n', '\n').split('\n')]

    points = gen_points(a)
    for p in points:
        p.discover(a, points)
        
    points.sort(key=lambda p: min(sum(p.xx), sum(p.xy)), reverse=True)
    s = build_square(a, points[0])
    print('Base-square: P(%d, %d) - Side: %d' % (points[0].x, points[0].y, s))
    
    # x, y, s = evolve_square(a, points[0].x, points[0].y, s)
    # print('Biggest-square: P(%d, %d) - Side: %d' % (x, y, s))
    
if __name__ == '__main__':
    main()