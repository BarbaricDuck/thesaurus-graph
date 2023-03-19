"""
Usage:
py main.py {start} {end}
OR
py main.py (creates 2 random words)
"""

THESAURUS = 'generated.csv'

import csv
import sys
import random

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node, neighbours):
        self.nodes[node] = neighbours
    
    def get_path(self, start, end):
        if start == end:
            return [start]
        
        self.paths = [[[start]]]
        self.visited = set()
        

        while end not in self.visited:
            # print(f'Depth: {len(self.paths)} Synonyms Checked: {len(self.paths[-1])}')
            old_len = len(self.paths[-1])
            self.paths.append([])
            for path in self.paths[-2]:
                self.next_depth(path)
            if len(self.paths[-1]) == old_len:
                break
            
        for path in self.paths[-1]:
            if end in path:
                return path
        return ["Not Connected"]
            
    def next_depth(self, path):
        for neighbour in filter(lambda x: x not in self.visited, self.nodes[path[-1]]):
            self.paths[-1].append(path + [neighbour])
            self.visited.add(neighbour)

def random_word_generator():
    with open(THESAURUS) as file:
        keys = [i[0] for i in csv.reader(file)]
        return random.choice(keys)
    
def main():
    graph = Graph()
    with open(THESAURUS) as file:
        csv_file = [x for x in csv.reader(file)]
        keys = set([i[0] for i in csv_file])
        for line in csv_file:
            graph.add_node(line[0], list(filter(lambda x: x in keys, line[1:])))
            
    print(f'Graph created, size: {len(graph.nodes)}')
    try:
        if (arg_1:=sys.argv[1]) in graph.nodes:
            start = arg_1
        else:
            print(f'{arg_1} not in word list')
            start = random_word_generator() 
    except IndexError:
        start = random_word_generator()

    try:
        if (arg_2:=sys.argv[2]) in graph.nodes:
            end = arg_2
        else:
            print(f'{arg_2} not in word list')
            end = random_word_generator() 
    except IndexError:
        end = random_word_generator()

    print(f'Searching for "{start}" to "{end}"')
    print(f'{" -> ".join(graph.get_path(start, end))}')

if __name__ == '__main__':
    main()