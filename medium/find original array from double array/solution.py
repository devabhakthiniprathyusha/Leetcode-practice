def findOriginalArray(self, changed: List[int]) -> List[int]:
    if len(changed) % 2:
        return []

    dic = Counter(changed)
    print(dic)
    changed.sort()
    output = []

    for n in changed:
        if n == 0 and dic[n] >= 2:
            output.append(n)
            dic[n] -= 2
        elif n > 0 and dic[n] and dic[n * 2]:
            output.append(n)
            dic[n] -= 1
            dic[n * 2] -= 1

    if len(output) == len(changed) // 2:
        return output
    else:
        return []