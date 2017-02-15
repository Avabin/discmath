def ExEuclid(u,v):
    if v == 0:
        p = (u, 1, 0)
        return p
    temp = u%v
    temp1 = u//v
    print("|\t", u,"\t|\t", v, "\t|\t", temp, "\t|\t", temp1,"\t|")
    p = ExEuclid(v, temp)
    p = (p[0], p[2], p[1] - p[2] * temp1)
    print("p[0] = ", p[0],
          "\np[1] = ", p[1],
          "\np[2] = ", p[2])
    print(p)
    return p

def MLES(a, k, d):
    a = a%d
    k = k%d
    print("a = ", a,
          "\nk = ", k,
          "\nd = ", d,
          "\n|\tu\t|\tv\t|\tt0\t|\tt1\t|")
    e = ExEuclid(d, a)
    print(e)
    if k%e[0] != 0:
        print("Brak rozwiązania")
        return
    x0 = (e[2] * (k // e[0])) % d
    for t in range(e[0]):
        print('x', t, ' = ', (x0 + t * (d // e[0])) % d)

MLES(-5, 1, 29)

MLES(-52, 4, 29)