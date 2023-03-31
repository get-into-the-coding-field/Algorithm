'''
프로그래머스 Lv2. 과제 진행하기
https://school.programmers.co.kr/learn/courses/30/lessons/176962
'''

def solution(plans):
    
    '''
    plans를 반복문으로 돌면서 plan을 뺀다. 
    plan의 playtime을 합산해서 다음 plan보다 작다면 
    남은 시간과 해당 plan을 멈춤 stack에 넣어놓는다.
    다음 plan이 더 크다면 과제를 완료 처리하고
    멈춤 스택에 있는 plan을 빼서 남은 시간만큼 처리한다.
    다 처리못하면 남은 스택만큼 다시 계산해서 넣어놓는다.
    이것을 반복하고 플랜을 다 처리한 후 남은 stack에서 빼면서 완료 처리한다.
    '''
    
    
    plans.sort(key=lambda x: (x[1], x[2]))
    
    print(plans)
    stopped = []
    answer = []
    def convert_time_to_int_min(time):
        hour, min = map(int, time.split(":"))
        return hour * 60 + min
    
    
    
    for i in range(len(plans)):
        
        if i == len(plans) - 1:
            answer.append(plans[i][0])
            break
        
        task, start_time, play_time = plans[i]
        next_task, next_start_time, next_play_time = plans[i+1]
        
        
        # 다음 플랜 안에 과제를 끝낼 수 있다면 과제를 완료 처리한다.
        end_time = convert_time_to_int_min(start_time) + int(play_time)
        next_task_start_time = convert_time_to_int_min(next_start_time)
        remain_time = abs(next_task_start_time - end_time)
        
        if end_time <= next_task_start_time:
            print(f"{task}를 시간 안에 처리할 수 있습니다! 과제 완료!!!")
            answer.append(task)            
            # 멈춤 스택에 있는 과제를 처리한다.
            
            print(f'remain_time: {remain_time}')
            if remain_time > 0:    
                
                while stopped and remain_time > 0:
                    stopped_task, stopped_task_remain_time = stopped.pop()
                    print(f"다음 과제까지 {remain_time}분 남아있습니다. 밀린 과제인 {stopped_task}를 처리합니다!")
                    if stopped_task_remain_time <= remain_time:
                        answer.append(stopped_task)
                        print(f'처리 완료!')
                        remain_time -= stopped_task_remain_time
                    else:
                        print(f'아직 남은 시간 {stopped_task_remain_time-remain_time} 분을 저장합니다.!!')
                        stopped.append((stopped_task, stopped_task_remain_time-remain_time))
                        remain_time = 0
                    
        else:
            # 다음 플랜보다 작다면 멈춤
            print(f'{task}는 다음 과제인 {next_task} 시작 시간 안에 끝내질 못하기 때문에 남은 시간{remain_time}를 같이 저장합니다.')
            stopped.append((task, remain_time))
    
    while stopped:
        answer.append(stopped.pop()[0])
    return answer

print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]))
print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))
print(solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]))
