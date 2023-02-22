def solution(order):
    answer = 0
    aux_container = []
    order_queue = []
    
    for i in range(len(order)):
        aux_container.append([order[i] ,i+1])
        order_queue.append(order[i])
        
        while order_queue and order_queue[0] == aux_container[-1][1]:
            order_queue.pop(0)
            aux_container.pop()
            answer += 1
    return answer