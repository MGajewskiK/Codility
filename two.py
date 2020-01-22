
def solution(string_binary):
    # remove leading zeros
    normalized = string_binary.lstrip('0')
    if len(normalized) == 0:
        return 0

    if normalized[-1] == '0':
        # division right bit shift
        return solution(normalized[:-1]) + 1

    else:
        # subtraction 0 at the last bit
        return solution(normalized[:-1] + '0') + 1


print(solution('011100'))
