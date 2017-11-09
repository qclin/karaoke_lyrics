# intro combo, repeat, interate, mix
# k v k v kv kv vk vk vkv kkv vvk kv


# short sounds  tk nm
# long sounds shhh

from random import choice, randint, random, shuffle

top_row = list('qwrtyp')
mid_row = list('sdfghjkl')
btm_row = list('zxcvbnm')

helper_row = list('hflrs')


def find_pair():
    print choice(mid_row), choice(helper_row)*2
    print choice(mid_row), choice(top_row)
    print choice(mid_row), choice(btm_row)

find_pair()


def iterate(currentRow, siblingRow1, siblingRow2):
    cur_cur, cur_prev, cur_next = ([] for i in range(3))

    for index, item in enumerate(currentRow):
        cur_cur.append(item+item)
        if (index + 1) < len(currentRow):
            cur_cur.append(item+currentRow[index+1])  ## grabs neighbor
        else:
            cur_cur.append(item+currentRow[0])
        for sib1 in siblingRow1:
            cur_prev.append(item+sib1)
        for sib2 in siblingRow2:
            cur_next.append(item+sib2)
    return cur_cur, cur_prev, cur_next

bb, ba, bc = iterate(mid_row, top_row, btm_row)


print bb
print ba
print bc
