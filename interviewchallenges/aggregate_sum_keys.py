def reg_dig_sum(n):
    convert_to_int = [int(i) for i in str(n)]
    total = sum(convert_to_int)
    if total < 10:
        return total
    else:
        return reg_dig_sum(total)


print(reg_dig_sum(12345))


def distr_of_rec_digit_sums(low=0, high=1500):
    sum_dict = {}
    for x in range(low, high + 1):
        if reg_dig_sum(x) not in sum_dict:
            sum_dict[reg_dig_sum(x)] = 1
        else:
            sum_dict[reg_dig_sum(x)] += 1
    return sum_dict