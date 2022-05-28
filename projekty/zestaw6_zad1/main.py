import random_digraph
import save_graph
import page_rank
import write_methods

def main() -> None:
  n = input('Podaj liczbę węzłów (od 2 do 32)\n')

  try: 
    n = int(n)
  except ValueError:
    print(f'{n} to nie liczba całkowita - wyjście z programu')
    return
  
  if n < 2 or n > 32:
    print('Niewłaściwa wartość liczby węzłów')
    return

  adj_list = {}

  adj_list = random_digraph.generate_adjacency_list(n)
  
  print(f'Tworzenie grafu o liczbie węzłów n = {n}')
  G = random_digraph.generate_random_digraph(adj_list)
  save_graph.save_graph_to_file(G)
  print('Gotowe - graf zapisano do pliku graph.png')

  d = 0.15
  N_a = 1000000 # liczba iteracji dla błądzenia przypadkowego
  N_b = 100 # liczba iteracji dla metody potęgowej

  with open(f'result.txt', 'w', encoding='utf-8') as outfile:
    outfile.write("Lista sąsiedztwa:\n")
    write_methods.save_adj_list_to_file(adj_list, outfile)

    print(f'Obliczanie Page Rank - metoda błądzenia przypadkowego... (N = {N_a})')

    outfile.write(f'Algorytm PageRank - błądzenie przypadkowe (N = {N_a}):\n')
    random_walk_probabilities = page_rank.random_walk(G, d, N_a)
    write_methods.save_page_rank(random_walk_probabilities, outfile)

    print('Gotowe')
    print(f'Obliczanie Page Rank - metoda potęgowa... (N = {N_b})')

    outfile.write(f'Algorytm PageRank - metoda potęgowa (N = {N_b}):\n')
    power_method_probabilities = page_rank.power_method(G, d, N_b)
    write_methods.save_page_rank(power_method_probabilities, outfile)
    print('Gotowe')

  print(f'Program zakończył działanie - wyniki zapisano do pliku result.txt')


if __name__ == '__main__':
  main()
