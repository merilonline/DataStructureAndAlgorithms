
array = ['a','b','c','d','e']

def print_all_pairs(array):
    for i in range(len(array)):
        for j in range(len(array)):
            print(array[i],array[j])


if __name__ == '__main__':
    print_all_pairs(array)  # O(n^2)
