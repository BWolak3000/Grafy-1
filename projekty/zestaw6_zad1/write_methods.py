def save_adj_list_to_file(adj_list, file):
  for node, neigbors in adj_list.items():
    file.write(f'{node}: {neigbors}\n')
  file.write('\n')

def save_page_rank(page_rank_results, file):
  for node, result in page_rank_results.items():
    file.write(f'{node} ==> PageRank: {round(result, 6)}\n')
  file.write('\n')
