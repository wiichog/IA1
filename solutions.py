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
                    path = remove_choiseDFS(frontier)
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
    lenPath = [len(node) for node in frontier]
    for node in frontier:
        frontier.remove(node)
        return node

def remove_choiseDFS(frontier):
    for node in frontier:
        return min(frontier)

def remove_choiseAStart(frontier):
    pass
    
    