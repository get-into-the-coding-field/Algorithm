def solution(cards1, cards2, goal):
    
    for _ in range(len(goal)):
        if len(cards1) > 0and goal[0] == cards1[0]:
            cards1.pop(0)
            goal.pop(0)
        elif len(cards2) > 0 and goal[0] == cards2[0]:
            cards2.pop(0)
            goal.pop(0)
        
    return "No" if len(goal) > 0 else "Yes"
    
print(solution(["i", "drink", "water"],["want", "to"],["i", "want", "to", "drink", "water"]))
print(solution(["i", "water", "drink"],["want", "to"],["i", "want", "to", "drink", "water"]))