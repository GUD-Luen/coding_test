def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        z = bin(arr1[i] | arr2[i])
        z = z.replace('0b', '')
        for j in range(n - len(z)):
            z = '0' + z
        z = z.replace('1', '#')
        z = z.replace('0', ' ')
        answer.append(z)
    return answer