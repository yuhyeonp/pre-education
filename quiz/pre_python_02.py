""""2.if문을 이용해 첫번째와 두번 수, 연산기호를 입력하게 하여 계산값이 나오는 계산기를 만드시오


예시
<입력>
첫 번째 수를 입력하세요 : 10
두 번째 수를 입력하세요 : 15
어떤 연산을 하실 건가요? : *

<출력>
150
"""

first_num = int(input("첫 번째 수를 입력하세요 : "))
second_num = int(input("두 번째 수를 입력하세요 : "))
op = input("어떤 연산을 하실 건가요? : ")

if op == '+':
    print(first_num + second_num)

elif op == '-':
    print(first_num - second_num)

elif op == '*':
    print(first_num * second_num)

elif op == '**':
    print(first_num ** second_num)

elif op == '/':
    print(first_num / second_num)

elif op == '//':
    print(first_num // second_num)

elif op == '%':
    print(first_num % second_num)