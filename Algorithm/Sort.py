__author__ = 'sukhanna'

class Sort:
# swap values at index1 and index2
# swap only unsigned integer values

    @staticmethod
    def swap(input_list, index1, index2):
        if index1 == index2:
            return
        input_list[index1] = input_list[index1] ^ input_list[index2] # a = a ^ b
        input_list[index2] = input_list[index1] ^ input_list[index2] # b = a ^ b
        input_list[index1] = input_list[index1] ^ input_list[index2] # a = a ^ b


    # sort elements in an array in ascending order
    # o(n) nlog(n)
    @staticmethod
    def quick_sort1(unsorted_list, l, u, p):
        if l >= u:
            return
        pivot_value = unsorted_list[p]
        Sort.swap(unsorted_list, p, u)
        m = l
        for i in range(l+1, u):
            if unsorted_list[i] <= pivot_value:
                Sort.swap(unsorted_list, i, m)
                m += 1
        Sort.swap(unsorted_list, m, u)
        Sort.quick_sort1(unsorted_list, l, m-1, l)
        Sort.quick_sort1(unsorted_list, m+1, u, m+1)