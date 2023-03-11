import csv
import sys
import random

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node, neighbours):
        self.nodes[node] = neighbours
    
    def get_path(self, start, end):
        self.paths = [[start]]
        self.visited = set()

        while end not in self.visited:
            old_len = len(self.paths)
            for path in self.paths:
                self.next_depth(path)
            if len(self.paths) == old_len:
                break
            
        for path in self.paths:
            if end in path:
                return path
        return None
            
    def next_depth(self, path):
        for neighbour in filter(lambda x: x not in self.visited, self.nodes[path[-1]]):
            self.paths.append(path + [neighbour])
            self.visited.add(neighbour)

def random_word_generator():
    with open('words_big.csv') as file:
        keys = [i[0] for i in csv.reader(file)]
        return random.choice(keys)

    
def main():
    graph = Graph()
    with open('words_big.csv') as file:
        csv_file = [x for x in csv.reader(file)]
        keys = set([i[0] for i in csv_file])
        for line in csv_file:
            # print(line[0], list(filter(lambda x: x in keys, line[1:])))
            graph.add_node(line[0], list(filter(lambda x: x in keys, line[1:])))
        
            
    print(f'Graph created, size: {len(graph.nodes)}')
    try:
        start = sys.argv[1]
    except IndexError:
        start = random_word_generator()
    try:
        end = sys.argv[2]
    except IndexError:
        end = random_word_generator()
    print(f'Searching for {start} to {end}')
    print(f'{" -> ".join(graph.get_path(start, end))}')

if __name__ == '__main__':
    main()