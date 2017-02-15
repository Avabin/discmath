
A = {1:{2, 3, 9}, 2:{1, 3, 9}, 3:{1, 2, 4, 8, 9}, 4:{3, 5, 6, 7, 8}, 5:{4, 6}, 6:{4, 5, 7, 8}, 7:{4, 6, 8}, 8:{3, 4, 6, 7}, 9:{1, 2, 3}}
V = set(A.keys())
Q = []


def Expand(Cand, Fini):
    if Cand | Fini == set():
        print(Q)
    elif Cand != set():
        s = Select(Cand, Fini)
        for q in Cand - A[s]:
            Cand.remove(q)
            Q.append(q)
            Expand(Cand & A[q], Fini & A[q])
            Fini.add(q)
            Q.pop()



def Select(Cand, Fini):
    Ax = {x: A[x] & Cand for x in Cand | Fini}
    Dx = [len(Ax[x]) for x in Cand | Fini]
    Dx.sort()
    Bx = [x for x in Cand|Fini if len(Ax[x]) == Dx[len(Dx)-1]]
    return Bx[0]
Expand(V, set())