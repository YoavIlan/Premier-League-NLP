from py2neo import Graph, Node, Relationship
import os

graph = Graph("bolt://localhost:7687", auth=("neo4j", "NLP2"))

def add_relationship(entity1, entity2, relation):
    if relation == "is":
        a = Node("Player", name=entity1)
        b = Node("Nationality", name=entity2)
        rel = Relationship.type(relation)
        graph.merge(rel(a,b), "Player", "name")
    elif relation == "plays_for":
        a = Node("Player", name=entity1)
        b = Node("Team", name=entity2)
        rel = Relationship.type(relation)
        graph.merge(rel(a,b), "Player", "name")

pwd = os.getcwd() + '/Stanford_OpenIE_Python/relations'

for f in os.listdir(pwd):
    print('Processing', f+ '...')
    with open('Stanford_OpenIE_Python/relations/'+f) as relations:
    # with open(f) as relations:
        for relation in relations:
            triple = relation.split(' | ')
            add_relationship(triple[0], triple[2], triple[1])