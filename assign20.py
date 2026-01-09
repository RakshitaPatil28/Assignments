#dictionary
graph={
   ' A':1,
    'B':2,
    'C':3}
print(graph)
print(graph['B'])

#methods
print(graph.keys())
print(graph.values())
print(len(graph))

#modification
graph['D']=4
print(graph)
graph['B']=5
graph['C']=1
print(graph)

#deletion
#graph.pop('D')
#print(graph)

#graph.clear()
#print(graph)

