from data_structures_and_algorithms.challenges.depth_first.depth_first import Graph


def to_adjacency_list(self,matrix):
    graph=dict()
    for i,row in enumerate(matrix):
        if i==0:
            continue
        key=matrix[0][i-1]
        graph[key]=[]
        for x,one in enumerate(row):
            if one == 1:
                # print(row[])
               graph[key].append(matrix[0][x])
                # print(row(x)) 
            # print(one ==1)

    return(graph)

Graph.matrix_represent=to_adjacency_list

#  | a b c d e 
# a| 0 1 0 0 1 
# b| 1 0 1 1 0
# c| 0 1 0 1 0 
# d| 0 1 1 0 1 
# e| 1 0 0 1 0
if __name__ == "__main__":
    
    matrix=[
    ['a','b','c','d','e'],
    [0, 1, 0, 0, 1 ],
    [1, 0, 1, 1, 0 ],
    [0, 1, 0, 1, 0 ],
    [0, 1, 1 ,0, 1 ],
    [1, 0 ,0 ,1, 0 ],

    ]
    # print(matrix)
    print(Graph().matrix_represent(matrix))
    # print(dir(Graph))