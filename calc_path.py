import pickle, copy_reg
import networkx as nx
import sys, os

curr = os.getcwd()

def calc_path_2_ORCIDs(path=curr,node1=None,node2=None):
    """
    Calculates shortest path between two nodes (ORCID IDs). Returns path + degrees.

    Answers "How many degrees are you from astronomy's Kevin Bacon (or whoever else)?"
    :param path: path to where the output graph file is stored
    :param node1: first node; defaults to most central node
    :param node2: second node; defaults to second most central node
    :return: shortest path + degrees (len(shortest path) - 1)
    """

    with open(path + '/' + 'ORCID_graph.pkl', 'rb') as f:
        G = pickle.load(f)

    if (node1 is None) or (node2 is None):
        with open(path + '/' + 'centrality.csv', 'rb') as f:
            centrality = csv.reader(f, delimiter='\t')
            rn = 0
            for row in centrality:
                if rn == 0:
                    tmp1 = row
                    rn += 1
                elif rn == 1:
                    tmp2 = row
                    rn += 1
                else:
                    break
        if node1 is None:
            node1 = tmp1[0]
        if node2 is None:
            node2 = tmp2[0]

    try:
        short_path = nx.algorithms.shortest_paths.generic.shortest_path(G, source=node1,target=node2)
    except:
        return []

    return short_path

if __name__ == '__main__':
    orcid1 = sys.argv[1]
    orcid2 = sys.argv[2]
    # TODO: if you run it from the command line, you want a nice string and the number of degrees
    print(calc_path_2_ORCIDs(node1=orcid1, node2=orcid2))