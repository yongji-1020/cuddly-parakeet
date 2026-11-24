Web VPython 3.2
# ================= 판 ,선 ==================
box(size = vec (130,130,1),color = color.white) # 판
box(size = vec (3.5,130,2),color = color.black , pos = vec(23.5, 0,0)) # 선
box(size = vec (3.5,130,2),color = color.black , pos = vec(-25,0,0)) # 선
box(size = vec (130,2,2),color = color.black , pos = vec(0,-25,0)) # 선
box(size = vec (130,2,2),color = color.black , pos = vec(0,25,0)) # 선
# =============================================================================================================================================================================

# ===================================================================================== 리스트 ================================================================================
x = []
a = list()

board = [0, 0, 0, 0, 0, 0, 0, 0, 0]    
pos_x = [-45, 0, 45, -45, 0, 45, -45, 0, 45]
pos_y = [45, 45, 45, 0, 0, 0, -45, -45, -45]


wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

game_over = 0     
msg = label(pos = vec(0,-61,3), text = "1: 1~9 / 2: q~o 키로 칸을 선택", height = 18, box = False, color = color.white)

# ===================================================================================== 도형 1 ================================================================================

while game_over == 0 :
    rate(100)
    k = keysdown()
    if '1' in k : 
        if board[0] == 0 :
            board[0] = 1
            x.append(0)
            box(pos = vec(-45, 45, 1), size = vec(25, 25, 1), texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlSSweKCceCbF-9zvGjl9enQ_EF56uck-pjxeyQVRCXg&s=10")
    if '2' in k : 
        if board[1] == 0 :
            board[1] = 1
            x.append(1)
            box(pos = vec(0, 45, 1), size = vec(25, 25, 1), texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlSSweKCceCbF-9zvGjl9enQ_EF56uck-pjxeyQVRCXg&s=10")
    if '3' in k : 
        if board[2] == 0 :
            board[2] = 1
            x.append(2)
            box(pos = vec(45, 45, 1), size = vec(25, 25, 1), texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlSSweKCceCbF-9zvGjl9enQ_EF56uck-pjxeyQVRCXg&s=10")
    if '4' in k : 
        if board[3] == 0 :
            board[3] = 1
            x.append(3)
            box(pos = vec(-45, 0, 1), size = vec(25, 25, 1), texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlSSweKCceCbF-9zvGjl9enQ_EF56uck-pjxeyQVRCXg&s=10")
    if '5' in k : 
        if board[4] == 0 :
            board[4] = 1
            x.append(4)
            box(pos = vec(0, 0, 1), size = vec(25, 25, 1), texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlSSweKCceCbF-9zvGjl9enQ_EF56uck-pjxeyQVRCXg&s=10")
    if '6' in k : 
        if board[5] == 0 :
            board[5] = 1
            x.append(5)
            box(pos = vec(45, 0, 1), size = vec(25, 25, 1), texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlSSweKCceCbF-9zvGjl9enQ_EF56uck-pjxeyQVRCXg&s=10")
    if '7' in k : 
        if board[6] == 0 :
            board[6] = 1
            x.append(6)
            box(pos = vec(-45,-45, 1), size = vec(25, 25, 1), texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlSSweKCceCbF-9zvGjl9enQ_EF56uck-pjxeyQVRCXg&s=10")
    if '8' in k : 
        if board[7] == 0 :
            board[7] = 1
            x.append(7)
            box(pos = vec(0,-45, 1), size = vec(25, 25, 1), texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlSSweKCceCbF-9zvGjl9enQ_EF56uck-pjxeyQVRCXg&s=10")
    if '9' in k : 
        if board[8] == 0 :
            board[8] = 1
            x.append(8)
            box(pos = vec(45,-45, 1), size = vec(25, 25, 1), texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlSSweKCceCbF-9zvGjl9enQ_EF56uck-pjxeyQVRCXg&s=10")
# ============================================================================================================================================================================
                                                                             
# ================================================================================= 도형 2 ===================================================================================
    if 'q' in k : 
        if board[0] == 0 :
            board[0] = 2
            x.append(0)
            box(pos = vec(-45, 45, 1), size = vec(25, 25, 1), texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdXcMPwTrtz9ibpGvbAnymtegwjd37leD-E8iSeYPoJA&s")
    if 'w' in k : 
        if board[1] == 0 :
            board[1] = 2
            x.append(1)
            box(pos = vec(0, 45, 1), size = vec(25, 25, 1), texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdXcMPwTrtz9ibpGvbAnymtegwjd37leD-E8iSeYPoJA&s")
    if 'e' in k : 
        if board[2] == 0 :
            board[2] = 2
            x.append(2)
            box(pos = vec(45, 45, 1), size = vec(25, 25, 1), texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdXcMPwTrtz9ibpGvbAnymtegwjd37leD-E8iSeYPoJA&s")
    if 'r' in k : 
        if board[3] == 0 :
            board[3] = 2
            x.append(3)
            box(pos = vec(-45, 0, 1), size = vec(25, 25, 1), texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdXcMPwTrtz9ibpGvbAnymtegwjd37leD-E8iSeYPoJA&s")
    if 't' in k : 
        if board[4] == 0 :
            board[4] = 2
            x.append(4)
            box(pos = vec(0, 0, 1), size = vec(25, 25, 1), texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdXcMPwTrtz9ibpGvbAnymtegwjd37leD-E8iSeYPoJA&s")
    if 'y' in k : 
        if board[5] == 0 :
            board[5] = 2
            x.append(5)
            box(pos = vec(45, 0, 1), size = vec(25, 25, 1), texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdXcMPwTrtz9ibpGvbAnymtegwjd37leD-E8iSeYPoJA&s")
    if 'u' in k : 
        if board[6] == 0 :
            board[6] = 2
            x.append(6)
            box(pos = vec(-45, -45, 1), size = vec(25, 25, 1), texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdXcMPwTrtz9ibpGvbAnymtegwjd37leD-E8iSeYPoJA&s")
    if 'i' in k : 
        if board[7] == 0 :
            board[7] = 2
            x.append(7)
            box(pos = vec(-0, -45, 1), size = vec(25, 25, 1), texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdXcMPwTrtz9ibpGvbAnymtegwjd37leD-E8iSeYPoJA&s")
    if 'o' in k : 
        if board[8] == 0 :
            board[8] = 2
            x.append(8)
            box(pos = vec(45,-45, 1), size = vec(25, 25, 1), texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdXcMPwTrtz9ibpGvbAnymtegwjd37leD-E8iSeYPoJA&s")
# ============================================================================================================================================================================

# ================================================================================= 빙고 확인 ================================================================================
    for w in wins :
        c = board[w[0]]
        if c == board[w[1]] :
            if c == board[w[2]] :
                if c == 1 :
                    x1 = pos_x[w[0]]
                    y1 = pos_y[w[0]]
                    x2 = pos_x[w[2]]
                    y2 = pos_y[w[2]]
                    cylinder(pos = vec(x1, y1, 3), axis = vec(x2 - x1, y2 - y1, 0), radius = 2, color = color.red)
                    msg.text = "도형 1 승리"
                    a.append(1)
                    game_over = 1
                elif c == 2 :
                    x1 = pos_x[w[0]]
                    y1 = pos_y[w[0]]
                    x2 = pos_x[w[2]]
                    y2 = pos_y[w[2]]
                    cylinder(pos = vec(x1, y1, 3), axis = vec(x2 - x1, y2 - y1, 0), radius = 2, color = color.red)
                    msg.text = "도형 2 승리"
                    a.append(2)
                    game_over = 1
# ============================================================================================================================================================================

# ================================================================================= 무승부 확인 ===============================================================================
    if game_over == 0 :
        empty = 0
        for b in board :
            if b == 0 :
                empty = empty + 1
        if empty == 0 :
            msg.text = "무승부"
            game_over = 1
# ============================================================================================================================================================================
