#キーボードから数字を入力して、
#その高さの三角形を*で出力してください

"""
例)5 と入力すると
*
**
***
****
*****
と出力する
"""
h = int (input('高さを入力してください'))

for x in range(1,h+1):
    print(x * '*')
print()


"""for horizontal in  range(h):
    for vertical in range(horizontal):
        print('*' , end=' ')
    print()
        """

for horizontal in range(h + 1):
    for vertical in range(horizontal):
        if vertical == 0 or vertical == horizontal - 1 or horizontal == h:
            print ('*' , end =' ')
        else:
            print('+' , end = ' ')
    print()