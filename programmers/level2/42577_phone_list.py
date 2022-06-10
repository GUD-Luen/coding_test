import time


def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if len(phone_book[i]) < len(phone_book[i+1]):
            if phone_book[i + 1].startswith(phone_book[i]):
                return False
    return True


test_case_list = [
    ["119", "97674223", "1195524421"],
    ["123", "456", "789"],
    ["12", "123", "1235", "567", "88"],
]

start_time = time.time()

for test_case in test_case_list:
    print(solution(test_case))

print(round((time.time() - start_time) * 1000, 6), 'ms')
