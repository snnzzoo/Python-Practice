# 가로와 세로의 길이를 각각 a, b로 받아
# 사각형 넓이와 둘레를 함께 반환
# 함수 rectangle을 정의하시요.
# 사각형이 가로가 20, 세로가 30

def rectangle(a, b):
    area = a * b
    perimeter = 2 * (a+b)
    return area, perimeter
print(rectangle(20, 30))
