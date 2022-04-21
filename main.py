from nose.tools import assert_true, assert_false

MATRIX = [ list("SRGD"), list("OFAE"), list("NUBL"), list("TSPE") ]


def start():
    """ Generaturfunktion für alle Startpunkte """
    for rows in range(0, len(MATRIX[0])):
        for cols in range(0, len(MATRIX)):
            yield (rows, cols)


def neighbors(p):
    """ Generatorfunktion für alle Nachbarn von p """
    for i in range(-1, 2):
        for k in range(-1, 2):
            o = (p[0] + i, p[1] + k)

            if 0 <= o[0] < 4 and 0 <= o[1] < 4 and o != p:
                yield o


def search(word):
    """ Suche Wort im Buchstabenrätsel """

    if len(word) >= 16:
        return False

    for i, k in start():
        if MATRIX[i][k] == word[0]:
            visited = []
            next = (i, k)
            visited.append(next)
            for c in word[1::]:

                foundNeighbor = False
                for ii, kk in neighbors(next):
                    if MATRIX[ii][kk] == c:
                        if MATRIX[ii][kk] not in visited:
                            visited.append(MATRIX[ii][kk])
                            next = (ii, kk)
                            foundNeighbor = True
                            break
                if foundNeighbor is False:
                    break

            if len(visited) == len(word):
                return True
    return False


def find_word_hits(file):
    hits = []

    with open(file, "r") as input:
        for line in input.readlines():
            line = line.replace("\n", "")
            line = line.upper()

            if line not in hits:
                if search(line):
                    hits.append(line)

    return hits

hits = find_word_hits("german.lst")

print(len(hits))

assert_true(search("ORGELBAU"))
assert_true(search("PLAGE"))
assert_true(search("STUBE"))
assert_false(search("SONATE"))
assert_false(search("HAUSAUFGABE"))
assert_false(search("MAUS"))

"""
SRGD
OFAE
NUBL
TSPE

"""