def main():
  sections = getSections()

def getSections():
  lines = []
  with open('input.txt', 'r') as f:
    for l in f.readlines():
      intervals = []
      l = l.replace("\n", "")
      split = l.split(" ")
      
      current = split[0]
      x_from = 0
      x_to = 1
      for i in range(1, len(split)):
        if current == split[i]:
          x_to+=1
          continue
        
        intervals.append(Interval(current, x_from, x_to, x_to+1-x_from))
        current = split[i]
        x_from = x_to
      
      lines.append(intervals)
  
  print(a)
  
  return lines

class Interval:
  def __init__(self, character, x_from, x_to, length):
    self.character = character
    self.x_from = x_from
    self.x_to = x_to
    self.length = length

if __name__ == '__main__':
  main()
