"""10. 팩토리얼을 구하는 함수를 작성하시오.
ex ) 5! = 5x4x3x2x1
  print(factoral(5)) -> 120 출력
  
예시
<입력>
print(factorial(5))

<출력>
120
  """

def factorial(num):
    result = 1
    for i in range(1, (num + 1)):
        result *= i
    return result

print(factorial(5))