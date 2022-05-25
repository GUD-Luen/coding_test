def solution(nums):
    answer = 0
    prime_numbers = [2]
    nums.sort()
    nums.reverse()
    max_num = nums[0] + nums[1] + nums[2]
    i = 3
    while i ** 2 <= max_num:
        is_prime = True
        for prime_number in prime_numbers:
            if i % prime_number == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(i)
        i += 1

    print(prime_numbers)

    hap_list = []
    for a in range(len(nums) - 2):
        for b in range(a + 1, len(nums) - 1):
            for c in range(b + 1, len(nums)):
                hap_list.append(nums[a]+nums[b]+nums[c])

    for hap in hap_list:
        is_prime = True
        for prime_number in prime_numbers:
            if prime_number ** 2 > hap:
                break
            if hap % prime_number == 0:
                is_prime = False
                break
        if is_prime:
            answer += 1

    return answer