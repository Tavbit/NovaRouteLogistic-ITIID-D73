from __future__ import annotations
from dataclasses import dataclass, field, asdict
from typing import Literal, Optional
NodeType=Literal['distribution_center','intersection','client']; CostMetric=Literal['distance_km','time_min']
@dataclass(frozen=True)
class Node: id:str; type:NodeType; name:str; x:float; y:float
@dataclass(frozen=True)
class Edge:
    from_node:str; to_node:str; distance_km:float; time_min:float
    def __post_init__(self):
        if self.distance_km<=0 or self.time_min<=0: raise ValueError('Edge distance and time must be > 0')
@dataclass(frozen=True)
class Delivery: delivery_id:str; destination_id:str; package_type:str; weight_kg:float; priority:str='normal'; status:str='pending'
@dataclass(frozen=True)
class OptimizationWeights:
    distance_weight:float=.5; time_weight:float=.5
    def __post_init__(self):
        if abs(self.distance_weight+self.time_weight-1.0)>1e-9: raise ValueError('Optimization weights must sum to 1.0')
@dataclass(frozen=True)
class Vehicle: vehicle_id:str; name:str; capacity_kg:float; active:bool=True
@dataclass(frozen=True)
class Journey:
    journey_id:str; date:str; vehicle_id:str; start_node:str; delivery_ids:list[str]; optimization:OptimizationWeights=field(default_factory=OptimizationWeights); return_to_start:bool=True; status:str='planned'
@dataclass
class AlgorithmResult:
    algorithm:str; start_node:str; goal_node:str; cost_metric:str; path:list[str]=field(default_factory=list); distance_km:float=0.; time_min:float=0.; explored_nodes:int=0; execution_ms:float=0.; success:bool=False; message:str='No route found'
    def to_dict(self): return asdict(self)
@dataclass
class GeneticResult:
    start_node:str; destinations:list[str]; visit_order:list[str]=field(default_factory=list); full_path:list[str]=field(default_factory=list); distance_km:float=0.; time_min:float=0.; fitness:float=0.; generations:int=0; population_size:int=0; execution_ms:float=0.; success:bool=False; message:str='No solution found'; algorithm:str='genetic'
    def to_dict(self): return asdict(self)
@dataclass
class Graph:
    nodes:dict[str,Node]; edges:list[Edge]; directed:bool=False
    def has_node(self,node_id): return node_id in self.nodes
def validate_search_request(graph,start,goal):
    if not graph.has_node(start): raise ValueError(f'Unknown start node: {start}')
    if not graph.has_node(goal): raise ValueError(f'Unknown goal node: {goal}')
def validate_cost_metric(metric):
    if metric not in {'distance_km','time_min'}: raise ValueError(f'Unsupported cost_metric: {metric}')
def calculate_path_metrics(graph,path):
    if len(path)<2:return {'distance_km':0.,'time_min':0.,'hops':0}
    d=t=0.
    for a,b in zip(path,path[1:]):
        edge=next((e for e in graph.edges if (e.from_node==a and e.to_node==b) or (not graph.directed and e.from_node==b and e.to_node==a)),None)
        if edge is None: raise ValueError(f'No edge between {a} and {b}')
        d+=edge.distance_km;t+=edge.time_min
    return {'distance_km':round(d,3),'time_min':round(t,3),'hops':len(path)-1}
def euclidean_heuristic(graph,current,goal):
    validate_search_request(graph,current,goal);a=graph.nodes[current];b=graph.nodes[goal];return ((b.x-a.x)**2+(b.y-a.y)**2)**.5
# API stubs: implementation lives in dedicated modules.
def bfs(graph,start,goal)->AlgorithmResult: raise NotImplementedError
def dfs(graph,start,goal)->AlgorithmResult: raise NotImplementedError
def ucs(graph,start,goal,cost_metric:CostMetric='distance_km')->AlgorithmResult: raise NotImplementedError
def astar(graph,start,goal,cost_metric:CostMetric='distance_km',heuristic='euclidean')->AlgorithmResult: raise NotImplementedError
def hill_climbing(graph,start,goal,heuristic='euclidean')->AlgorithmResult: raise NotImplementedError
def genetic_algorithm(graph,start,destinations,distance_weight=.5,time_weight=.5,population_size=100,generations=200,mutation_rate=.05,seed:Optional[int]=None)->GeneticResult: raise NotImplementedError
