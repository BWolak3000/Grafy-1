def print_adjacency_list(adj_list):
  for node, neigbors in adj_list.items():
    print(f'{node}: {neigbors}')

def print_page_rank(page_rank_results):
  for node, result in page_rank_results.items():
    print(f'{node} ==> PageRank: {result}')