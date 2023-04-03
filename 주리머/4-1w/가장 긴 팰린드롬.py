'''
프로그래머스 lv3. 가장 긴 팰린드롬
https://school.programmers.co.kr/learn/courses/30/lessons/12904
'''
def solution(s):
    answer = 1
    # 큰 팰린드롬부터 찾아서 return
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if is_palindrome(s[i:j]):
                answer = max(answer, j-i)
    return answer
def is_palindrome(s):
    return s == s[::-1]

print(solution("abcdcba"))
print(solution("abacde"))