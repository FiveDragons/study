# 리스트 : [대괄호] / 튜플 : (소괄호)
# 리스트 같은경우 append같은 함수를 사용하여 추가하거나 빼거나 유동적으로 가능하지만
# 튜플 같은 경우엔 자물쇠가 잠겨있는 것 처럼 변경, 수정할 수 없다.
# 즉 튜플은 변하면 안되는 값을 쓸 때 사용한다.


# [튜플에서 안되는 것]
'''
t1 = (1,2,'a','b') 
del t1[0]           # 튜플이기에 삭제가 되지 않는다.
t1[0] = 'c'         # 교체도 되지않는다.
'''


# [튜플에서 되는 것]

# slicing
t1 = (1,2,'a','b') 
print(t1[0:2])

# 더하기, 곱하기
t1 = (1,2,'a','b') 
t2 = (3,4)
print(t1 + t2) # t1과 t2를 더한 새로운 튜플을 만든 것이지 t1, t2가 변한게 아니다.
print(t1 * 3) # t1의 값과 t2의 값이 변동된게 아니기에 더하기,곱하기가 가능하다.