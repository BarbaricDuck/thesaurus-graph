from main import *

def main():
    graph = Graph()
    with open(THESAURUS) as file:
        csv_file = [x for x in csv.reader(file)]
        keys = set([i[0] for i in csv_file])
        for line in csv_file:
            graph.add_node(line[0], list(filter(lambda x: x in keys, line[1:])))
            
    print(f'Graph created, size: {len(graph.nodes)}')
    
    with open("connections.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        for start in graph.nodes:
            for end in graph.nodes:
                print(f'{str((list(graph.nodes.keys()).index(end) / len(graph.nodes)) * 100)[:5]}% of {str((list(graph.nodes.keys()).index(start) / len(graph.nodes)) * 100)[:5]}%')
                if (path:=graph.get_path(start, end)) != ["Not Connected"]:
                    writer.writerow(path)

if __name__ == '__main__':
    main()