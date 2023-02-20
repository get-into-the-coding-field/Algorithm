def solution(expression):
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = []
    for op in operations:
        a = op[0]
        b = op[1]
        temp_list = []
        
        print(f'a: {a}, b: {b}')
        for e in expression.split(a):
            temp = [f"({i})" for i in e.split(b)]
            temp_list.append(f'({b.join(temp)})')
            print(f'e: {e}, temp: {temp},  temp_list: {temp_list}')
            print(f'a.join:::: {a.join(temp_list)}')
        answer.append(abs(eval(a.join(temp_list))))
    return max(answer)
print(solution("100-200*300-500+20"))
# print(solution('50*6-3*2'))
# print(solution('2*2*2*2*2-2*2*2'))

