def solution(files):
    answer = []
    
    # 파일을 3분류로 분리
    newFiles = []
    
    for i in files:
        head = ''
        number = ''
        tail = ''
        onTail = False
        for j in i:
            if j.isdigit() and len(number) < 5 and not onTail:
                    number += j
            elif len(number) > 0:
                onTail = True
                tail += j
            else:
                head += j

        newFiles.append([head, number, tail]) if tail != "" else newFiles.append([head, number])
    print(newFiles)
    answer = [ "".join(i[0]+i[1]+i[2]) if len(i) > 2  else "".join(i[0]+i[1]) for i in sorted(newFiles, key = lambda x: (x[0].lower(), int(x[1]))) ]
    return answer

# print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
# print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
print(solution(["O00321", "O49qcGPHuRLR5FEfoO00321"]))

# HEAD는 숫자가 아닌 문자로 이루어져 있으며, 최소한 한 글자 이상이다.
# NUMBER는 한 글자에서 최대 다섯 글자 사이의 연속된 숫자로 이루어져 있으며, 앞쪽에 0이 올 수 있다. 0부터 99999 사이의 숫자로, 00000이나 0101 등도 가능하다.
# TAIL은 그 나머지 부분으로, 여기에는 숫자가 다시 나타날 수도 있으며, 아무 글자도 없을 수 있다.