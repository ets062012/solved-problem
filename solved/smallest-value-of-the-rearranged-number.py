class Solution:
    def smallestNumber(self, num: int) -> int:
        newnum = str(num)
        arr = list(newnum)

        if newnum[0] != "-":
            arr.sort()
            if arr[0] == "0":
                for i in range(1, len(arr)):
                    if arr[i] != "0":
                        arr[0], arr[i] = arr[i], arr[0]
                        break

            return int("".join(arr))
        else:
            newarr = sorted(arr[1:], reverse=True)
            newarr.insert(0, "-")

            return int("".join(newarr))
