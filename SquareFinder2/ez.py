
def main():
    arr = [
        [1, 1, 1, 1, 0 ,0 ,0, 0 ,2 ,2],
        [1 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,2 ,2],
        [2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,3 ,3],
        [2 ,2 ,2 ,2 ,4 ,4 ,4 ,4 ,3 ,3],
        [2 ,2 ,2 ,2 ,4 ,4 ,3 ,3 ,3 ,3],
        [2 ,2 ,2 ,2 ,2 ,4 ,4 ,4 ,4 ,4],
        [2 ,1 ,1 ,2 ,2 ,2 ,4 ,4 ,4 ,4],
        [2 ,1 ,1 ,2 ,2 ,6 ,6 ,6 ,5 ,5],
        [2 ,1 ,1 ,2 ,2 ,6 ,6 ,0 ,0 ,5],
        [2 ,1 ,1 ,2 ,2 ,6 ,6 ,0 ,0 ,5],
      ]
    
    for i in arr:
        for j in i:
            if j == 1:
                print("1")
            elif j == 2:
                print("2")
            elif j == 3:
                print("3")
            elif j == 4:
                print("3")
            elif j == 5:
                print("3")
            elif j == 6:
                print("3")
        print()
if __name__ == '__main__':
    main()