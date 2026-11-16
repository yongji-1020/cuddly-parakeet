Web VPython 3.2
# ================= 판 ,선 ==================
box(size = vec (130,130,1),color = color.white) # 판
box(size = vec (3.5,130,2),color = color.black , pos = vec(23.5, 0,0)) # 선
box(size = vec (3.5,130,2),color = color.black , pos = vec(-25,0,0)) # 선
box(size = vec (130,2,2),color = color.black , pos = vec(0,-25,0)) # 선
box(size = vec (130,2,2),color = color.black , pos = vec(0,25,0)) # 선
# =============================================================================================================================================================================

# ===================================================================================== 도형 1 ================================================================================

while True :
    rate(100)
    k = keysdown()
    if '1' in k : 
       box(pos = vec(-45, 45, 1), size = vec(25, 25, 1),(texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlSSweKCceCbF-9zvGjl9enQ_EF56uck-pjxeyQVRCXg&s=10"))
    if '2' in k : 
       box(pos = vec(0, 45, 1), size = vec(25, 25, 1),(texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlSSweKCceCbF-9zvGjl9enQ_EF56uck-pjxeyQVRCXg&s=10"))
    if '3' in k : 
       box(pos = vec(45, 45, 1), size = vec(25, 25, 1),(texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlSSweKCceCbF-9zvGjl9enQ_EF56uck-pjxeyQVRCXg&s=10"))
    if '4' in k : 
       box(pos = vec(-45, 0, 1), size = vec(25, 25, 1),(texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlSSweKCceCbF-9zvGjl9enQ_EF56uck-pjxeyQVRCXg&s=10"))
    if '5' in k : 
       box(pos = vec(0, 0, 1), size = vec(25, 25, 1),(texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlSSweKCceCbF-9zvGjl9enQ_EF56uck-pjxeyQVRCXg&s=10"))
    if '6' in k : 
       box(pos = vec(45, 0, 1), size = vec(25, 25, 1),(texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlSSweKCceCbF-9zvGjl9enQ_EF56uck-pjxeyQVRCXg&s=10"))
    if '7' in k : 
       box(pos = vec(-45,-45, 1), size = vec(25, 25, 1),(texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlSSweKCceCbF-9zvGjl9enQ_EF56uck-pjxeyQVRCXg&s=10"))
    if '8' in k : 
       box(pos = vec(0,-45, 1), size = vec(25, 25, 1),(texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlSSweKCceCbF-9zvGjl9enQ_EF56uck-pjxeyQVRCXg&s=10"))
    if '9' in k : 
       box(pos = vec(45,-45, 1), size = vec(25, 25, 1),(texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlSSweKCceCbF-9zvGjl9enQ_EF56uck-pjxeyQVRCXg&s=10"))
# ============================================================================================================================================================================

# ================================================================================= 도형 2 ===================================================================================
    if 'q' in k : 
        box(pos = vec(-45, 45, 1), size = vec(25, 25, 1),(texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdXcMPwTrtz9ibpGvbAnymtegwjd37leD-E8iSeYPoJA&s"))
    if 'w' in k : 
        box(pos = vec(0, 45, 1), size = vec(25, 25, 1),(texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdXcMPwTrtz9ibpGvbAnymtegwjd37leD-E8iSeYPoJA&s"))
    if 'e' in k : 
        box(pos = vec(45, 45, 1), size = vec(25, 25, 1),(texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdXcMPwTrtz9ibpGvbAnymtegwjd37leD-E8iSeYPoJA&s"))
    if 'r' in k : 
        box(pos = vec(-45, 0, 1), size = vec(25, 25, 1),(texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdXcMPwTrtz9ibpGvbAnymtegwjd37leD-E8iSeYPoJA&s"))
    if 't' in k : 
        box(pos = vec(0, 0, 1), size = vec(25, 25, 1),(texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdXcMPwTrtz9ibpGvbAnymtegwjd37leD-E8iSeYPoJA&s"))
    if 'y' in k : 
        box(pos = vec(45, 0, 1), size = vec(25, 25, 1),(texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdXcMPwTrtz9ibpGvbAnymtegwjd37leD-E8iSeYPoJA&s"))
    if 'u' in k : 
        box(pos = vec(-45, -45, 1), size = vec(25, 25, 1),(texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdXcMPwTrtz9ibpGvbAnymtegwjd37leD-E8iSeYPoJA&s"))
    if 'i' in k : 
        box(pos = vec(-0, -45, 1), size = vec(25, 25, 1),(texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdXcMPwTrtz9ibpGvbAnymtegwjd37leD-E8iSeYPoJA&s"))
    if 'o' in k : 
        box(pos = vec(45,-45, 1), size = vec(25, 25, 1),(texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdXcMPwTrtz9ibpGvbAnymtegwjd37leD-E8iSeYPoJA&s"))
        
# ============================================================================================================================================================================
