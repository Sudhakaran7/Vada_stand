class Validate:
    def Vada_stand(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            k = (right + left) // 2
            curr = k * (k + 1) // 2
            if curr == n:
                return k
            if n < curr:
                right = k - 1
            else:
                left = k + 1
        return right

vall = Validate()
vada=int(input())
print(vall.Vada_stand(vada))
