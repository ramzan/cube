import numpy as np
import matplotlib.pyplot as plt


class Cube:

    def __init__(self, dim: int):
        if dim < 0:
            print("Invalid entry")
            exit()
        elif dim == 0:
            self.verts = [['', [0, 0, 0]]]
        elif dim == 1:
            self.verts = [['0', [0, 0, 0]], ['1', [1, 0, 0]]]
        elif dim == 2:
            self.verts = [['00', [0, 0, 0]], ['01', [0, 1, 0]],
                          ['11', [1, 1, 0]], ['10', [1, 0, 0]]]
        else:
            self.verts = get_coords(dim)
        print(len(self.verts))

    def plot_graph(self):
        x = [v[1][0] for v in self.verts]
        y = [v[1][1] for v in self.verts]
        z = [v[1][2] for v in self.verts]

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        ax.scatter(x, y, z)

        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_zticklabels([])

        for i in range(len(self.verts)):
            for j in range(i, len(self.verts)):
                if distance(self.verts[i][0], self.verts[j][0]) == 1:
                    ax.plot([x[i], x[j]], [y[i], y[j]], [z[i], z[j]],
                            color='g')

        plt.show()


def codes(r: int):
    """
    Return list of all binary strings of length r.
    """
    if r == 0:
        return ['']
    small = codes(r-1)
    lst = []
    for item in small:
        lst.append(item + '0')
        lst.append(item + '1')
    return lst


def get_coords(n: int):
    """
    Return list of lists containing a binary string and coordinates
    for each vertex in the hypercube.
    """
    lst = codes(n)
    lst = [[y, [int(x) for x in y]] for y in lst]
    for i in range(len(lst)):
        for j in range(len(lst[i][1])):
            if lst[i][1][j] == 0:
                lst[i][1][j] = -1
    arr = []
    start = 0
    end = 8
    for i in range(n - 2):
        if i > 0:
            start = end
            end += 2**(i+2)
        temp = lst[start][1][3:]
        scale = ((sum([(r+1) for r in range(len(temp)) if temp[r] == 1])
                  * i) + 1) * (1 - 1/n)
        for j in range(start, end):
            arr.append([lst[j][0], np.array(lst[j][1][:3]) * scale])

    seen = {}
    for i in range(len(arr)):
        while tuple(arr[i][1]) in seen:
            arr[i][1] *= 2
        seen[tuple(arr[i][1])] = None
    return arr


def distance(s1, s2):
    """
    Return Hamming distance of two binary
    strings s1 and s2.
    """
    distance = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            distance += 1
    return distance


if __name__ == "__main__":
    c = Cube(int(input("Enter a dimension (non-negative integer):")))
    c.plot_graph()
