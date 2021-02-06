nemo = ['nemo']
everyone = ['dory', 'nemo']


def find_nemo(array):
    for i in range(len(array)):
        if array[i] == 'nemo':
            print(array[i])


if __name__ == '__main__':
    find_nemo(nemo) # O(n) -> Linear Time

