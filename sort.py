from random import randint
def a_sort(a_list):
    if len(a_list) == 0 or len(a_list)== 1:
        return a_list
    middle = a_list.pop()
    smaller = []
    larger = []
    for num in a_list:
        if num <= middle:
            smaller.append(num)
        else:
            larger.append(num)
    return a_sort(smaller) + [middle] + a_sort(larger)
if __name__ == '__main__':
    b_list = [randint(1,100) for i in range(10)]
    print a_sort(b_list)
