from collections import deque

def DFS_Visit(a):
        #G ist acyclic also DFS generiert keine back edges (u,v),denn ansonsten
        #ware (u,v) ein "kreis schliesser".

        #red node:
        #every edge leaving node has been explored .
        #if an edge reaches a red node, there is no need to continue search through this path.

        if G[a]=="red":
            return
        
        successors=G[a]
        
        if type(successors)==list and  successors!= []:
            for nodes in successors: #explore edges
                DFS_Visit(nodes)
                
            
        #after exploring every edge leaving a, paint 'a' red! 
        G[a]="red"
        #add from left all red painted verteces to the list. first in: successors. last in: ancestors.
        liste.appendleft(a) 
        return liste
    
def DFS(G):
        global liste
        
        liste=deque()
        #adjacency list: G={a:[b,c], b:[c,d],c:[], d:[]}
        for elem in (G): #each vertex in G
            if type(G[elem]) is list:
    
                a=DFS_Visit(elem)

        return list(liste)

"""
Korrektheit:
Sei A=[V1,..., Vn] die knoten sortierung (Ausgabe vom Algorithmus)
Sei (vi, vj) eine kante in G. G ist acyclic also DFS generiert keine back edges (u,v), ansonsten
ware (u,v) ein "Kreis Schliesser". Sei a einen knoten von G, erst wenn alle kanten die a verlassen
mit depth search unterucht sind faengt den Algorithmus an diese knoten ruckwarts hinzufugen, falls es noch nicht-rote
knoten bleiben mussen diese ancestors von a sein. Fur diese konten wiederholt sich den Algorithmus, da elemente von links
hingefugen werden, gilt i<j fur alle Knoten Vi, Vj mit (Vi, Vj) in E.

Laufzeit: Die kleine veranderungen vom Tiefensuche-Algorithmus
die hier implementiert sind andern die laufzeit nicht, denn die knoten hinzufugung kostet konstante Zeit O(1).
Die Laufzeit ist die gleiche wie bei der Tiefensuche also O(V+E).

"""

G={'a':['b','c'], 'b':['c','d'],'c':['d'], 'd':[], 'l':['a']}

