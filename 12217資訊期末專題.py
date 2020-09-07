import time
import random

#遊戲主程式

def game():
        
    #設定棋盤大小
    
    print('輸入你要哪一個棋盤：')
    print('1:9*9')
    print('2:11*11')
    print('3:13*13')
    print('4:19*19')
    while 1:
        size=input()
        if size!='1' and size!='2' and size!='3' and size!='4':
            print('請正確輸入(1 or 2 or 3 or 4)')
        else:
            break
    if int(size)==1:
        c_size=9
    elif int(size)==2:
        c_size=11
    elif int(size)==3:
        c_size=13
    elif int(size)==4:
        c_size=19

    #初始設定棋盤大小和電腦下棋積分

    board=[[0]*(c_size*2-1) for i in range((c_size*2-1))]
    score=[[0]*(c_size) for i in range((c_size))]

    #決定下棋順序

    print('誰先?')
    print('1:玩家')
    print('2:電腦')
    while 1:
        first=input()
        if first!='1' and first!='2':
            print('請正確輸入(1 or 2)')
        else:
            break
    
    #定義遊戲結束

    def gameover():
        for i in range(100):
            print('')
        game()

    #定義棋盤打印內容
    
    def piece(a):
        if a==0:
            return ('---')
        elif a==1:
            return ('X')
        elif a==2:
            return ('O')
        elif a==3:
            return ('   ')
        elif a==4:
            return ('|')
        elif a==5:
            return ('·')

    #初始化棋盤
            
    def r_body():        
        for i in range(c_size*2-1):
            for j in range(c_size*2-1):
                if i%2==0 and j%2==0:
                    board[i][j]=5
                elif i==0 or i==8:
                    board[i][j]=0
                elif j==0 or j==8:
                    board[i][j]=4
                elif i%2==0:
                    board[i][j]=0
                elif j%2==0:
                    board[i][j]=4
                elif (i*j)%2==1:
                    board[i][j]=3
        if int(first)==2:
            a=random.randint(1,c_size)*2-2
            b=random.randint(1,c_size)*2-2
            board[a][b]=2
            print(a,b)

    #打印棋盤  
                                         
    def p_body():
        print('輸入X軸座標(1~',c_size,')，Enter完再輸入Y軸座標(1~',c_size,')')
        print('')
        print('  ',end='')
        for i in range(1,c_size+1):
            if i<=9:
                print(i,end='   ')
            else:
                print(i,end='  ')
        print('')    
        for i in range(c_size*2-1):
            if i%2==0:
                if i<=17:
                    print(int((i+2)/2),'',end='')
                else:
                    print(int((i+2)/2),end='')
            else:
                print('  ',end='')
            for j in range(c_size*2-1):
                print(piece(board[i][j]),end='')
            print('')

    #計算電腦下棋總積分和判斷勝利

    def output(n,m,a,b,c):
        tem=0
        if n==4:
            tem=1000
            if board[a*2][b*2]==c:
                print('Game Over!')
                print('You ',m)
                time.sleep(5)
                gameover()
        elif n==3:
            tem=400
        elif n==2:
            tem=55
        elif n==1:
            tem=20
        elif n==0:
            tem=0
        return tem

    #刷新頁面

    def loading():
        for i in range(100):
            print('')
            
    #計算雙方八方向連線棋子數目
            
    def ul_O(a,b):
        n=0
        c=a
        d=b 
        if a!=0 and b!=0:
            if board[a*2-2][b*2-2]==2:
                while c!=0 and d!=0 and board[c*2-2][d*2-2]==2:
                    n+=1
                    c-=1
                    d-=1           
        return n      

    def uc_O(a,b):
        n=0    
        c=a
        d=b
        if a!=0 :
            if board[a*2-2][b*2]==2:
                while c!=0 and board[c*2-2][d*2]==2:
                    n+=1
                    c-=1              
        return n
        
    def ur_O(a,b):
        n=0    
        c=a
        d=b
        if a!=0 and b!=(c_size-1):
            if board[a*2-2][b*2+2]==2:
                while c!=0 and d!=(c_size-1) and board[c*2-2][d*2+2]==2:
                    n+=1
                    c-=1
                    d+=1                 
        return n
        
    def cl_O(a,b):
        n=0    
        c=a
        d=b
        if b!=0:
            if board[a*2][b*2-2]==2:
                while d!=0 and board[c*2][d*2-2]==2:
                    n+=1
                    d-=1                   
        return n
        
    def cr_O(a,b):
        n=0
        c=a
        d=b
        if b!=(c_size-1):
            if board[a*2][b*2+2]==2:
                while d!=(c_size-1) and board[c*2][d*2+2]==2:
                    n+=1
                    d+=1            
        return n
        
    def dl_O(a,b):
        n=0    
        c=a
        d=b
        if a!=(c_size-1) and b!=0:
            if board[a*2+2][b*2-2]==2:
                while c!=(c_size-1) and d!=0 and board[c*2+2][d*2-2]==2:
                    n+=1
                    c+=1
                    d-=1            
        return n
        
    def dc_O(a,b):
        n=0    
        c=a
        d=b
        if a!=(c_size-1):
            if board[a*2+2][b*2]==2:
                while c!=(c_size-1) and board[c*2+2][d*2]==2:
                    n+=1
                    c+=1        
        return n
        
    def dr_O(a,b):
        n=0
        c=a
        d=b
        if a!=(c_size-1) and b!=(c_size-1):
            if board[a*2+2][b*2+2]==2:
                while c!=(c_size-1) and d!=(c_size-1) and board[c*2+2][d*2+2]==2:
                    n+=1
                    c+=1
                    d+=1                
        return n
        
    def ul_X(a,b):
        n=0
        c=a
        d=b        
        if a!=0 and b!=0:
            if board[a*2-2][b*2-2]==1:
                while c!=0 and d!=0 and board[c*2-2][d*2-2]==1:
                    n+=1
                    c-=1
                    d-=1      
        return n
        
    def uc_X(a,b):
        n=0    
        c=a
        d=b
        if a!=0 :
            if board[a*2-2][b*2]==1:
                while c!=0 and board[c*2-2][d*2]==1:
                    n+=1
                    c-=1            
        return n
        
    def ur_X(a,b):
        n=0    
        c=a
        d=b        
        if a!=0 and b!=(c_size-1):
            if board[a*2-2][b*2+2]==1:
                while c!=0 and d!=(c_size-1) and board[c*2-2][d*2+2]==1:
                    n+=1
                    c-=1
                    d+=1       
        return n
        
    def cl_X(a,b):
        n=0    
        c=a
        d=b
        if b!=0:
            if board[a*2][b*2-2]==1:
                while d!=0 and board[c*2][d*2-2]==1:
                    n+=1
                    d-=1                      
        return n
        
    def cr_X(a,b):
        n=0
        c=a
        d=b
        if b!=(c_size-1):
            if board[a*2][b*2+2]==1:
                while d!=(c_size-1) and board[c*2][d*2+2]==1:
                    n+=1
                    d+=1
        return n
    
    def dl_X(a,b):
        n=0    
        c=a
        d=b
        if a!=(c_size-1) and b!=0:
            if board[a*2+2][b*2-2]==1:
                while c!=(c_size-1) and d!=0 and board[c*2+2][d*2-2]==1:
                    n+=1
                    c+=1
                    d-=1            
        return n
        
    def dc_X(a,b):
        n=0    
        c=a
        d=b
        if a!=(c_size-1):
            if board[a*2+2][b*2]==1:
                while c!=(c_size-1) and board[c*2+2][d*2]==1:
                    n+=1
                    c+=1                        
        return n
        
    def dr_X(a,b):
        n=0
        c=a
        d=b
        if a!=(c_size-1) and b!=(c_size-1):
            if board[a*2+2][b*2+2]==1:
                while c!=(c_size-1) and d!=(c_size-1) and board[c*2+2][d*2+2]==1:
                    n+=1
                    c+=1
                    d+=1           
        return n
        
    #計算電腦攻防總積分

    def x(i,j):
        return output((ul_O(i,j)+dr_O(i,j)),'lose',i,j,2)+output((ul_X(i,j)+dr_X(i,j)),'win',i,j,1)
    
    def y(i,j):
        return output((uc_O(i,j)+dc_O(i,j)),'lose',i,j,2)+output((uc_X(i,j)+dc_X(i,j)),'win',i,j,1)
    
    def z(i,j):
        return output((ur_O(i,j)+dl_O(i,j)),'lose',i,j,2)+output((ur_X(i,j)+dl_X(i,j)),'win',i,j,1)
    
    def w(i,j):
        return output((cl_O(i,j)+cr_O(i,j)),'lose',i,j,2)+output((cl_X(i,j)+cr_X(i,j)),'win',i,j,1)

    #計算積分

    def point():
        for i in range(c_size):
            for j in range(c_size):
                score[i][j]=x(i,j)+y(i,j)+z(i,j)+w(i,j)

    #電腦下棋

    def ai():
        a=0
        b=0
        c=0
        for i in range(c_size):
            for j in range(c_size):
                if board[i*2][j*2]==5:
                    if score[i][j]>a:
                        a=score[i][j]
                        b=i
                        c=j
        board[b*2][c*2]=2
        return (c+1,b+1)

    #人下棋

    def person(a,b):
        while 1:
            if a.isdigit() and b.isdigit():
                c=int(a)
                d=int(b)
            if a.isdigit()==0 or b.isdigit()==0:
                print("請分兩次，依序輸入X座標、Y座標，請輸入數字")    
            elif (0<=c and c<=c_size and 0<=d and d<=c_size)==0:
                print('格式或範圍錯誤.輸入X軸座標(1~',c_size,')，Enter完再輸入Y軸座標(1~',c_size,')')
            elif board[(d)*2-2][(c)*2-2]!=5:
                print('請下在還沒有棋子的地方')
            else:
                board[(d)*2-2][(c)*2-2]=1
                break
            a=str(input())
            b=str(input())

    #開始

    def begin():
        r_body()
        loading()
        p_body()
        point()

    #判斷是否遊戲中

    def playing():
        global play
        play=1
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j]==5:
                    return 0
        play=0

    #遊戲程式

    def body():
        global play
        play=1
        person(str(input()),str(input()))
        time.sleep(1)
        loading()
        p_body()
        point()
        playing()
        if play==0:
            return play
        time.sleep(1)
        ai_xy=ai()
        loading()
        print('電腦下在',ai_xy)
        p_body()
        point()
        playing()
        if play==0:
            return play
        return 1
    
    #主程式
                                       
    begin()
    play=1
    while play!=0:
        play=body()        
    print('棋盤下滿了')
    time.sleep(5)
    gameover()

#開始遊戲

game()    

        
        










