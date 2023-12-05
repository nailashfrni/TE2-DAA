import time
import tracemalloc
from DP import *
from BnB import *

# FUNCTION FOR PARSING INPUT FILES
def parse(datafile, adj):
	with open(datafile) as f:
		num_vertices = int(f.readline().strip())
		for i in range(num_vertices):
			neighbors = list(map(int, f.readline().split()))
			adj.append(neighbors)
	return adj, num_vertices


def compute_time_space(adj_dp, graph_bnb, size_dp, size_bnb, size_str):
	print('--- ' + size_str.upper() + ' ---')
	
    # Init tracer time and space
	tracemalloc.start()
	start = time.time()
	
    # DP algo
	mvc_dp = min_vertex_cover_dp(adj_dp, size_dp)
	
    # End tracer
	end = time.time()
	memory_usage = tracemalloc.get_traced_memory()[1] / 1000000
	tracemalloc.stop()
	print(f'=================================== DP {size_dp} vertices ===================================')
	print('Output MVC:', mvc_dp, 'vertices')
	print('Memory usage:', memory_usage, 'MB')
	print('Running time:', (end-start) * 1000, 'ms')
	
	# Init tracer time and space
	tracemalloc.start()
	start = time.time()
	
    # BnB algo
	mvc_bnb = BnB(graph_bnb)
	
    # End tracer
	end = time.time()
	memory_usage = tracemalloc.get_traced_memory()[1] / 1000000
	tracemalloc.stop()
	print(f'================================= BnB {size_bnb} vertices ===================================')
	print('Output MVC:', len(mvc_bnb), 'vertices')
	print('Memory usage:', memory_usage, 'MB')
	print('Running time:', (end-start) * 1000, 'ms\n')
	

if __name__ == '__main__':
	sizes = ['small', 'medium', 'large']
     
	for i in range(len(sizes)):
		adj_dp = [[]]
		adj_bnb = []
		
		adj_dp, dp_size = parse(f'dataset/dp/{sizes[i]}.txt', adj_dp)
		adj_bnb, bnb_size = parse(f'dataset/bnb/{sizes[i]}.txt', adj_bnb)
		
		graph_bnb = create_graph(adj_bnb)
		compute_time_space(adj_dp, graph_bnb, dp_size, bnb_size, sizes[i])
    