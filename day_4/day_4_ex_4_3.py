row_1 = ['0', '0', '0']
row_2 = ['0', '0', '0']
row_3 = ['0', '0', '0']


my_map = [row_1,
          row_2,
          row_3]

for row in my_map:
    print(row)
    

def get_coords(msg) -> tuple:
    while 1:
        try:
            coords = int(input(msg))
            x, y = coords // 10, coords % 10
            if 0 <= x <= 3 and 0 <= y <= 3:
                return(x, y)
            else:
                print('Coordinates are out of range!')
        except ValueError:
            print('Use integers')
            
def add_treasure(mmap:list=my_map, treasure:str='X') -> None:
    x, y = get_coords('Type in your coords (e.g. 32 is row=3, col=2): ')
    mmap[x-1][y-1] = treasure
    print(* mmap, sep='\n')
    
add_treasure()