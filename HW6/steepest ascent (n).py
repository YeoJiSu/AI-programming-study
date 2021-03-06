from problem import Problem
# Problem만 받아와도 동작이 되어야 함 

def main():
    p = Problem()
    p.setVariables() 
    steepestAscent(p)
    
    
    # p = createProblem() 
    # solution, minimum = steepestAscent(p)
    # describeProblem(p)
    # displaySetting()
    # displayResult(solution, minimum)
    
def steepestAscent(p):
    current = p.randonInit()
    #current = randomInit(p) # 'current' is a list of values
    # valueC = evaluate(current, p)
    # while True:
    #     neighbors = mutants(current, p)
    #     successor, valueS = bestOf(neighbors, p)
    #     if valueS >= valueC:
    #         break
    #     else:
    #         current = successor
    #         valueC = valueS
    # #p.storeResult(solution, value)
    # return current, valueC


    # 빈 배열  neighbors  생성
    neighbors = []
    # i 가 0 부터  current의 길이 -1 까지 반복문을 돌림.
    for i in range(0,len(current)):
        # 전체 i에 대해 DELTA 일 때 -DELTA일 때 모두 mutate 하여 neighbor list에 추가합니다.
        neighbors.append(mutate(current, i, DELTA,p))
        neighbors.append(mutate(current, i, -DELTA,p))
    # 생성한 list를 return 합니다.
    return neighbors

def bestOf(neighbors, p):
    # 빈 리스트 all을 생성합니다.
    all = []
    # i가 0부터 neighbors의 길이 -1 까지 반복문을 돌림.
    for i in range(0,len(neighbors)):
        # all list에 neighbors의 모든 경우에 대해 evaluate을 하여 붙여넣습니다. 
        all.append(evaluate(neighbors[i],p))
    # 만들어진 list의 원소값 중 최솟값을 bestValue에 저장합니다. 
    bestValue=min(all)
    # 만들어진 list의 원소값중 최솟값의 index를 찾아 해당 index의 neighbors값을 best 에 저장합니다.
    best = neighbors[all.index(min(all))]

    return best, bestValue

def displaySetting():
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")
    print()
    print("Mutation step size:", DELTA)

main()
