from backend.contracts.contracts import Node, Edge, Graph, calculate_path_metrics, euclidean_heuristic

def test_shared_contracts():
    g = Graph({'A': Node('A','intersection','A',0,0), 'B': Node('B','client','B',3,4)}, [Edge('A','B',5,8)])
    assert calculate_path_metrics(g,['A','B']) == {'distance_km':5.0,'time_min':8.0,'hops':1}
    assert euclidean_heuristic(g,'A','B') == 5.0
