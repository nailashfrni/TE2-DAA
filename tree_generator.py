import random

def addEdge(adj, x, y):
	adj[x-1].append(y)
	adj[y-1].append(x)

def generate_random_tree(size_dp, size_bnb): 
    # Prepare adjacency list
    adj_dp = [[] for i in range(size_dp)]
    adj_bnb = [[] for i in range(size_bnb)]

    # Generate vertices and randomize it
    vertices = [i for i in range(2, size_dp + 1)]
    random.shuffle(vertices)

    # Randomly choose parent for each vertex
    for v in vertices:
          parent = random.choice(range(1, v))
          addEdge(adj_dp, v, parent)
          # Add to dataset BnB too if the size still compatible
          if parent <= size_bnb and v <= size_bnb:
                addEdge(adj_bnb, v, parent)

    return adj_dp, adj_bnb


def adj_to_file(adj, filename):
      with open(f'dataset/{filename}', 'w') as f:
            # Write the number of vertices
            f.write(str(len(adj)) + '\n')

            # Write neighbors for each vertex in the graph
            for neighbors in adj:
                  f.write(' '.join([str(i) for i in neighbors]) + '\n')


def generate_dataset_file(size_dp, size_bnb, size_str):
      adj_dp, adj_bnb = generate_random_tree(size_dp, size_bnb)
      adj_to_file(adj_dp, f'dp/{size_str}.txt')
      adj_to_file(adj_bnb, f'bnb/{size_str}.txt') 


if __name__ == '__main__':
     sizes = ['small', 'medium', 'large']
     dp_sizes = [10**4, 10**5, 10**6]
     bnb_sizes = [60, 80, 100]
     
     for i in range(len(sizes)):
           generate_dataset_file(dp_sizes[i], bnb_sizes[i], sizes[i])