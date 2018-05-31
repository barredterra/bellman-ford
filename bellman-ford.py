"""
Computes shortest paths from a single source vertex to all of the other vertices 
in a weighted digraph.

Copyright (c) 2018 Raffael Meyer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import csv

def bellman_ford(E, D):
    """
    Fuer alle Knoten v setze D[v] = unendlich
    D[s] = 0
    Von i = 1 bis n-1
      Fuer alle Kanten (u,v)
        Falls D[u] + g(u,v) < D[v] dann
          D[v] = D[u] + g(u,v)
    """
    log = []
    n = len(D)
    for i in range(1, n-1):
        for e in E:
            if(D[e[0]] + e[2] < D[e[1]]):
                D[e[1]] = D[e[0]] + e[2]
            log.append(get_state(e, D))
        if (i==2):
            return D, log

def get_state(edge, distances):
    """
    create one row for the log
    ['v1-v2', dist, dist, ...]
    """
    edge_s = ['(' + edge[0] + '-' + edge[1] + ')']
    distances_l = [distances[i] for i in sorted(distances.keys())]
    state = edge_s + distances_l
    return state

def save_csv(logs, vertecies):
    """
    produce a CSV-file containing the logs
    """
    with open('bf.csv', 'w') as csvfile:
        logwriter = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        logwriter.writerow(['edge'] + vertecies) # header
        for l in logs:
            logwriter.writerow(l)
        print('\nlog saved as ' + csvfile.name)

def print_log(log):
    print('Log:\n')
    for l in log:
        print(l)

def main():
    # Edges [(vertex1, vertex2, weight)]
    E = [('a', 'b', 4), ('a', 'c', 1), ('a', 'f', 9), ('b', 'd', 1), ('c', 'b', 2), 
         ('c', 'e', 3), ('d', 'e', 1), ('d', 'f', 4), ('e', 'b', -2), ('e', 'f', 1)]
    # Distances {'vertex': distance_from_a}
    D = {'a': 0, 'b': 999, 'c': 999, 'd': 999, 'e': 999, 'f': 999}
    
    result, log = bellman_ford(E, D)
    print_log(log)

    V = [i for i in D.keys()]
    save_csv(log, V)

if __name__ == '__main__':
    main()