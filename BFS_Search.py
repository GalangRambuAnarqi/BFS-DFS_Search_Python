#Project Uninformed Search
#BFS Algorithm
#Yolo Squad

peta = {'A': {'B','C','D'},
         'B': {'A', 'C','E','F', 'G'},
         'C': {'A', 'B','D'},
         'D': {'A', 'C', 'H', 'I'},
         'E': {'B','L'},
         'F': {'B', 'G', 'L'},
         'G': {'B','F', 'J','H'},
         'H': {'D', 'G', 'J'},
         'I': {'D', 'J'},
         'J': {'I', 'G','H', 'K', 'M'},
         'K': {'L', 'J', 'M'},
         'L': {'E', 'F','M', 'K'},
         'M': {'L', 'K', 'J'}}


def rute_bfs(peta, mulai, tujuan):
    stack = [(mulai, [mulai])]

    while stack:

        (node, edge) = stack.pop(0)

        for next in peta[node].difference(edge):

            if next == tujuan:
                yield edge + [next]

            else:
                stack.append((next, edge + [next]))


print("---------Hasil Program-------")

list_jalur = list(rute_bfs(peta, 'E', 'G'))
cek = len(list_jalur)

if cek == 0:
    print("Tidak Ketemu")

else:
    print("Jalur yang mungkin -> ", list_jalur)
    print("jalur BFS = ", list_jalur[0])