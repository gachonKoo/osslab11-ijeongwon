import geo.utils as utils

# pythagoras 테스트
a, b = 3, 4
# 빈칸 채우기 → pythagoras 함수 호출
c = utils.pythagoras(a, b)
print("c =", c)

# circle 테스트
r = 10
# 빈칸 채우기 → circle 함수 호출
area = utils.circle(r)
print("area =", area)
