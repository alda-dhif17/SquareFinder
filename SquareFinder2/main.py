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
            if (self.x - x) % SPACING == 0:
                points.remove(find_point(points, x, self.y))
        
    def discover_y(self, a, d, points):
        for y in range(self.y+d, -1 if d < 0 else len(a), d):
            if a[y][self.x] != self.n:
                break
            self.xy[0 if d < 0 else 1] += 1
            if (self.y - y) % SPACING == 0:
                points.remove(find_point(points, self.x, y))
        
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

def main():
    a = []
    with open('input.txt', 'r') as f:
        a = [[int(c) for c in l.split(' ')] for l in f.read().replace('\r\n', '\n').split('\n')]

    points = gen_points(a)
    for p in points:
        p.discover(a, points)
        
    print([str(p) for p in points])

if __name__ == '__main__':
    main()