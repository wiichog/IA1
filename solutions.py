def graph_search(problem):
        frontier = [[problem.initial]]
        explored = []
        while(True):
            if len(frontier):
                if(problem.type==1):
                    path = remove_choiseBFS(frontier)
                elif(problem.type==2):
                    path = remove_choiseDFS(frontier)
                elif(problem.type ==3):
                    path = remove_choiseAStart(frontier,problem)
                elif(problem.type ==4):
                    path = remove_choiseAStart(frontier,problem)
                s = path[-1]
                explored.append(s)
                if(problem.goalTest(s)):
                    return path
                for a in problem.actions(s):
                    result = problem.result(s,a)
                    if result[0] not in explored:
                        new_path = []
                        new_path.extend(path)
                        new_path.extend(problem.result(s,a))
                        frontier.append(new_path)
            else:
                return False    
            
def remove_choiseBFS(frontier):
    pathLens = [len(node) for node in frontier]
    index = pathLens.index(min(pathLens))
    node = frontier[index]
    frontier.remove(node)
    return node

def remove_choiseDFS(frontier):
    pathLens = [len(node) for node in frontier]
    index = pathLens.index(max(pathLens))
    node = frontier[index]
    frontier.remove(node)
    return node

def remove_choiseAStart(frontier,problem):
    if(problem.type ==3):#euclidean
        heuristics = [euclideanHeuristics(node,problem) for node in frontier]
        index = heuristics.index(min(heuristics))
        print(min(heuristics))
        node = frontier[index]
        frontier.remove(node)
        return node
    elif(problem.type ==4):#manhattan
        heuristics = [manhattanHeuristics(node,problem) for node in frontier]
        index = heuristics.index(min(heuristics))
        print(min(heuristics))
        node = frontier[index]
        frontier.remove(node)
        return node
    pass

def euclideanHeuristics(node,problem):
    return min( [ problem.pathCost(node) + (abs(  (node[-1].x-i.x) + (node[-1].y-i.y)  ))**0.5 for i in problem.goal])

def manhattanHeuristics(node,problem):
    return min([ problem.pathCost(node) + ((node[-1].x-i.x) + (node[-1].y-i.y)) for i in problem.goal])
    
    