
class DisjointSetForest:

    def __init__(self, n):
        self.dsf = [-1] * n

    def is_index_valid(self, index):
        return 0 <= index <= len(self.dsf)

    def create_dsf(n, k):
        dsf = [-1] * (n * k)
        tmp = 0
        for i in range(len(dsf)):
            if (i % k) == 0:
                tmp = i
                continue
            dsf[i] = tmp
        return dsf

    def find(self, a):
        if not self.is_index_valid(a):
            return -1

        if self.dsf[a] < 0:
            return a
        return self.find(self.dsf[a])

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        self.dsf[rb] = ra

    def is_single(self, k):
        if self.dsf[k] >= 0:
            return False

        for num in self.dsf:
            if num == k:
                return False

        return True

    def get_num_sets(self):
        count = 0

        for num in self.dsf:
            if num < 0:
                count += 1

        return count

    def is_compressed(self):
        for num in self.dsf:
            if self.dsf[num] != -1:
                return False

        return True

