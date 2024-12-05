from collections import defaultdict


def read_data(file_name):
  with open(file_name, 'r') as file:
    for line in file.readlines():
      yield line


def read_edges():
  for line in read_data("day5.graph.input"):
    yield [int(i) for i in line.split('|')]


def read_queries():
  for line in read_data("day5.query.input"):
    yield [int(i) for i in line.split(',')]


def main():
  correct_count = 0
  wrong_count = 0
  for query in read_queries():
    # build graph
    in_degree = defaultdict(int)
    out_degree = defaultdict(list)
    for u, v in read_edges():
      if u in query and v in query:
        in_degree[v] += 1
        out_degree[u].append(v)

    copy_in_degree = in_degree.copy()

    # checkValidity
    for num in query:
      if in_degree[num] != 0:
        break
      for _node in out_degree[num]:
        in_degree[_node] -= 1

    # check for invalid case
    if any(in_degree[i] for i in in_degree):
      # invalid case
      in_degree = copy_in_degree
      process_order = []

      queue = []
      for num in query:
        if in_degree[num] == 0:
          queue.append(num)

      while queue:
        num = queue.pop(0)
        process_order.append(num)

        for i in out_degree[num]:
          in_degree[i] -= 1
          if in_degree[i] == 0:
            queue.append(i)

      wrong_count += process_order[len(process_order) // 2]
    else:
      # valid case
      correct_count += query[len(query) // 2]
  print("correct_count", correct_count)
  print("wrong_count", wrong_count)


if __name__ == '__main__':
  main()
