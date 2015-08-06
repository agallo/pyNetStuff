#!/usr/bin/python

import networkx as nx

# create Directed Graph called DG
DG = nx.DiGraph()

# create a list of ASNs
ASpath1=[11039, 174, 14743, 13546]

# add edges to directed graph from a list
# new nodes will be created as needed (ie, if they don't exist in DG, they'll be created, existing nodes
# will not be duplicated)
DG.add_path(ASpath1)

print 'Nodes so far: ' + str((DG.nodes()))
print 'Edges so far: ' + str((DG.edges()))

# add second path
secondpath = [11039, 174, 16657, 5061, 13546]
DG.add_path(secondpath)

print 
print 'added a second path:'
print 'Nodes so far: ' + str((DG.nodes()))
print 'Edges so far: ' + str((DG.edges()))


# add a bunch of ASpaths manually
DG.add_path([11039, 174, 3356, 13546])
DG.add_path([11039, 4901, 11164, 29791, 12182, 14743, 13546])
DG.add_path([11039, 4901, 11164, 4323, 5061, 13546])
DG.add_path([11039, 6461, 12182, 12182, 12182, 12182, 12182, 12182, 12182, 12182, 12182, 12182, 12182, 14743, 13546])
DG.add_path([11039, 6461, 174, 14743, 13546])
DG.add_path([11039, 6461, 3356, 13546])
DG.add_path([11039, 6461, 4323, 5061, 13546])
DG.add_path([11039, 11557, 4436, 3257, 12182, 12182, 12182, 14743, 13546])
DG.add_path([11039, 11557, 4436, 3257, 14743, 13546])
DG.add_path([11039, 11557, 4436, 3257, 3356, 13546])
DG.add_path([11039, 11557, 4436, 3257, 3356, 16657, 5061, 13546])


print
print 'Nodes and degrees: ' + str(nx.degree(DG))
