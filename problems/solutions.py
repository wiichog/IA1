
functions = {
    "BDS":(lambda pathLens: pathLens.index(min(pathLens))),
    "DFS":(lambda pathLens: pathLens.index(max(pathLens)))
}

def graph_search(problem):
        frontier = [[problem.initial]]
        explored = []
        while(True):
            if len(frontier):
                path = remove_choise(frontier,problem)
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
            
def remove_choise(frontier,problem):
    if(problem.type==1):
        index = functions.get("BDS")([len(node) for node in frontier])
    elif(problem.type==2):
        index = functions.get("DFS")([len(node) for node in frontier])
    elif(problem.type ==3):
        index = functions.get("BDS")([euclideanHeuristics(node,problem) for node in frontier])
    elif(problem.type ==4):
        index = functions.get("BDS")([manhattanHeuristics(node,problem) for node in frontier])
    print(frontier)
    node = frontier[index]
    frontier.remove(node)
    return node

def euclideanHeuristics(node,problem):
    return min([problem.pathCost(node) + (abs(  (node[-1].x-i.x)**2 + (node[-1].y-i.y)**2  ))**0.5 for i in problem.goal])

def manhattanHeuristics(node,problem):
    return min([ problem.pathCost(node) + (abs(node[-1].x-i.x) + abs(node[-1].y-i.y)) for i in problem.goal])
    
    