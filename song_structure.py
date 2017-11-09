from random import choice, randint, random, shuffle

def keyboard_walk():

    lengths = range(randint(3, 4))
    repeat_lengths = [1, 1] + range(randint(2, 3))
    result = ' '
    for stance in choice([lengths]):
        for line in choice([repeat_lengths]):
            result = ' '.join([result, choice(combo)])
            result = result + c
        print result


# for i in range(20):
#     print keyboard_walk()

top_row = list('qwrtyp')
mid_row = list('sdfghjkl')
btm_row = list('zxcvbnm')
row_list = [top_row, mid_row, btm_row]
aa, bb,cc,ab ,ac, bc, ba ,ca, cb = ([] for i in range(9))

pair_list = [aa, bb,cc,ab ,ac, bc, ba ,ca, cb]
pair_sequence_list = [ab ,ac, bc]
pair_reverse_list = [ba ,ca, cb]
same_list = [aa, bb,cc]


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


def pair():
    #### TODO: optimize
    # aa, ab, ac = iterate(top_row, mid_row, btm_row)
    # bb, bc, ba = iterate(mid_row, btm_row, top_row)
    # cc, ca, cb = iterate(btm_row, top_row, mid_row)
    for index_a, a in enumerate(top_row):
        aa.append(a+a)
        if index_a + 1 < len(top_row):
            aa.append(a+top_row[index_a+1])  ## grabs neighbor
        else:
            aa.append(a+top_row[0])
        for b in mid_row:
            ab.append(a+b)
        for c in btm_row:
            ac.append(a+c)

    for index_b, b in enumerate(mid_row):
        bb.append(b+b)
        if index_b +1 < len(mid_row):
            bb.append(b+mid_row[index_b+1])
        else:
            bb.append(b+btm_row[0])
        for c in btm_row:
            bc.append(b+c)
        for a in top_row:
            ba.append(b+a)

    for index_c, b in enumerate(btm_row):
        cc.append(c+c)
        if index_c +1 < len(btm_row):
            cc.append(c+btm_row[index_c+1])
        else:
            cc.append(c+btm_row[0])
        for a in top_row:
            ca.append(a+c)
        for b in mid_row:
            cb.append(c+b)

pair()

print pair_list

def tripplet():
    ### this is a 2d list of list
    triples = []
    for index, pair in enumerate(pair_sequence_list):
        result = ' '
        lengths = range(randint(3, 8))
        for n in choice([lengths]):
            ab = choice(pair)
            bc = choice(pair)
            # print("ab ---- ", ab )
            abba = ab + ab[::-1]
            abb = ab+ ab[-1]
            aab = ab+ab[0]
            bccb = bc+bc[::-1]
            bbc = bc + bc[-1]
            bcc = bc + bc[0]
            combo = [ab, abb, aab, bccb, bbc, bcc]

            result = result + ' '.join([choice(combo), choice(combo), choice(combo)*2]) + ' \n'
        result = result + choice(combo)
        triples.append(result)

    print '\n'.join(triples)


tripplet()

    # aa = a+a
    # bb = b+b
    # cc = c+c
    # c = choice([choice(top_row), choice(btm_row)])
    # combo = [a+b , b+a, b+b+a, a+a, b+b+a, b+a+b]

# blob = " rgr rgg pffpff tdt tdt pjjpjj qg rkkr qggqgg wlw wll rsrs rjj tjt rjrrjr tll tlt tlltll pff pffp phhphh pfp txx tzz tzttzt tnt tnnt yzyz wvv wv wvvwvv qzzq qv qzzqzz yxx yx qnqqnq yx kvk kvk gmgm knnk knnk hnnhnn dzd dzz jnjjnj fbbf db dbdb svvs svs fzfz hxx hxx hxxhxx kz kzk gvvggvvg jbj dxd dxdx dxd"
# ssblob = blob.split(' ')
# shuffle(ssblob)
#
# print ' '.join(ssblob)
