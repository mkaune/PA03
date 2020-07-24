from collections import deque

def DFS_Visit(a):
        global top_sortierung
        if a.color=="red":
            #red node:
            #every edge leaving node has been explored .
            #if an edge reaches a red node, there is no need to continue search through this path.
            return
        
        if a.color=="black":
            #black node: back edge/ancestor 
            #an edge that reaches a black vertex has reached an ancestor this indicates a cycle, thus no TS
            top_sortierung=False
            return
        
        a.color="black"
        #every explored node ist now ancestor
        
        if a.successors!=[]:
            
            #if a white?
            for nodes in a.successors: #explore edge
                
                DFS_Visit(nodes)
                #nodes.__dict__["color"]="red"

        #after exploring every edge leaving a, paint 'a' red!   
        a.color="red"
        
        #print(liste)
        liste.appendleft(a.name) 
        #liste.appendleft(a) 
        return liste
        #liste.append(a)
    
def top_order(G):
        global liste
        global top_sortierung
        top_sortierung=True
        liste=deque()
        #G=[a,b,c,d]
        for elem in G:
            
            if elem.color=="white" and top_sortierung:
                #print(elem.__dict__["name"])
                #liste.appendleft(elem.__dict__["name"]) 
                a=DFS_Visit(elem)
                    
        if top_sortierung==False:
            #print("p")
            return [-1]
        
        return list(liste)

"""a=node()
b=node()
c=node()
d=node()
e=node()
f=node()
a.name="a"
b.name="b"
c.name="c"
d.name="d"
e.name="e"
f.name='f'
a.color=b.color=c.color=d.color="white"
a.succesors=[b,c,e]
b.succesors=[c,f]
c.succesors=[]
d.succesors=[b,c]
e.succesors=[d]
f.succesors=[c]
G=[a,b,c,d,e,f]
#G=[]
print(top_order(G))"""
