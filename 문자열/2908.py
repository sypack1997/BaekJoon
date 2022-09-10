a,b = input().split()

a_change = int(a[2] + a[1] + a[0])
b_change = int(b[2] + b[1] + b[0])

if a_change > b_change:
    print(a_change)
else:
    print(b_change)



# other code
''' 
a, b = input().split()
print(max("".join(reversed(a)), "", join(reversed(b))))
'''
# join 함수 : 매개변수로 들어온 리스트에 있는 요소 하나하나를 합쳐서 하나의 문자열로 바꾸어 반환하는 함수. ''.join(리스트)