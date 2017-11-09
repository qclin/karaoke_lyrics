from random import choice, randint, random, shuffle

blends = ["bl", "br", "cl", "cr", "dr", "fr", "pr", "tr", "fl", "gl",  "gr", "pl", "pr", "sl", "sm", "sp", "st", "tr", "wr"]
triagraphs = ["scr", "shr", "spl", "spr", "str", "thr", ""]
diagraphs =["sh", "ck", "ch", "th", "wh", "gh", "ng", "ph", "ng","sc", "sk", "sl", "sn", "sw", "tw"]

pair_sequence_list = [blends, triagraphs, diagraphs]



all_phone = ["bl", "br", "cl", "cr", "dr", "fr", "pr", "tr", "fl", "gl",  "gr", "pl", "pr", "sl", "sm", "sp", "st", "tr", "wr", "scr", "shr", "spl", "spr", "str", "thr", "sh", "ck", "ch", "th", "wh", "gh", "ng", "ph", "ng","sc", "sk", "sl", "sn", "sw", "tw"]


pair_ultimate = [['qq', 'qw', 'ww', 'wr', 'rr', 'rt', 'tt', 'ty', 'yy', 'yp', 'pp', 'pq'], ['ss', 'sd', 'dd', 'df', 'ff', 'fg', 'gg', 'gh', 'hh', 'hj', 'jj', 'jk', 'kk', 'kl', 'll', 'lz'], ['mm', 'mx', 'mm', 'mc', 'mm', 'mv', 'mm', 'mb', 'mm', 'mn', 'mm', 'mm', 'mm', 'mz'], ['qs', 'qd', 'qf', 'qg', 'qh', 'qj', 'qk', 'ql', 'ws', 'wd', 'wf', 'wg', 'wh', 'wj', 'wk', 'wl', 'rs', 'rd', 'rf', 'rg', 'rh', 'rj', 'rk', 'rl', 'ts', 'td', 'tf', 'tg', 'th', 'tj', 'tk', 'tl', 'ys', 'yd', 'yf', 'yg', 'yh', 'yj', 'yk', 'yl', 'ps', 'pd', 'pf', 'pg', 'ph', 'pj', 'pk', 'pl'], ['qz', 'qx', 'qc', 'qv', 'qb', 'qn', 'qm', 'wz', 'wx', 'wc', 'wv', 'wb', 'wn', 'wm', 'rz', 'rx', 'rc', 'rv', 'rb', 'rn', 'rm', 'tz', 'tx', 'tc', 'tv', 'tb', 'tn', 'tm', 'yz', 'yx', 'yc', 'yv', 'yb', 'yn', 'ym', 'pz', 'px', 'pc', 'pv', 'pb', 'pn', 'pm'], ['sz', 'sx', 'sc', 'sv', 'sb', 'sn', 'sm', 'dz', 'dx', 'dc', 'dv', 'db', 'dn', 'dm', 'fz', 'fx', 'fc', 'fv', 'fb', 'fn', 'fm', 'gz', 'gx', 'gc', 'gv', 'gb', 'gn', 'gm', 'hz', 'hx', 'hc', 'hv', 'hb', 'hn', 'hm', 'jz', 'jx', 'jc', 'jv', 'jb', 'jn', 'jm', 'kz', 'kx', 'kc', 'kv', 'kb', 'kn', 'km', 'lz', 'lx', 'lc', 'lv', 'lb', 'ln', 'lm'], ['sq', 'sw', 'sr', 'st', 'sy', 'sp', 'dq', 'dw', 'dr', 'dt', 'dy', 'dp', 'fq', 'fw', 'fr', 'ft', 'fy', 'fp', 'gq', 'gw', 'gr', 'gt', 'gy', 'gp', 'hq', 'hw', 'hr', 'ht', 'hy', 'hp', 'jq', 'jw', 'jr', 'jt', 'jy', 'jp', 'kq', 'kw', 'kr', 'kt', 'ky', 'kp', 'lq', 'lw', 'lr', 'lt', 'ly', 'lp'], ['qm', 'wm', 'rm', 'tm', 'ym', 'pm', 'qm', 'wm', 'rm', 'tm', 'ym', 'pm', 'qm', 'wm', 'rm', 'tm', 'ym', 'pm', 'qm', 'wm', 'rm', 'tm', 'ym', 'pm', 'qm', 'wm', 'rm', 'tm', 'ym', 'pm', 'qm', 'wm', 'rm', 'tm', 'ym', 'pm', 'qm', 'wm', 'rm', 'tm', 'ym', 'pm'], ['ms', 'md', 'mf', 'mg', 'mh', 'mj', 'mk', 'ml', 'ms', 'md', 'mf', 'mg', 'mh', 'mj', 'mk', 'ml', 'ms', 'md', 'mf', 'mg', 'mh', 'mj', 'mk', 'ml', 'ms', 'md', 'mf', 'mg', 'mh', 'mj', 'mk', 'ml', 'ms', 'md', 'mf', 'mg', 'mh', 'mj', 'mk', 'ml', 'ms', 'md', 'mf', 'mg', 'mh', 'mj', 'mk', 'ml', 'ms', 'md', 'mf', 'mg', 'mh', 'mj', 'mk', 'ml']]



long_long_list = ['qq', 'qw', 'ww', 'wr', 'rr', 'rt', 'tt', 'ty', 'yy', 'yp', 'pp', 'pq', 'ss', 'sd', 'dd', 'df', 'ff', 'fg', 'gg', 'gh', 'hh', 'hj', 'jj', 'jk', 'kk', 'kl', 'll', 'lz', 'mm', 'mx', 'mm', 'mc', 'mm', 'mv', 'mm', 'mb', 'mm', 'mn', 'mm', 'mm', 'mm', 'mz', 'qs', 'qd', 'qf', 'qg', 'qh', 'qj', 'qk', 'ql', 'ws', 'wd', 'wf', 'wg', 'wh', 'wj', 'wk', 'wl', 'rs', 'rd', 'rf', 'rg', 'rh', 'rj', 'rk', 'rl', 'ts', 'td', 'tf', 'tg', 'th', 'tj', 'tk', 'tl', 'ys', 'yd', 'yf', 'yg', 'yh', 'yj', 'yk', 'yl', 'ps', 'pd', 'pf', 'pg', 'ph', 'pj', 'pk', 'pl', 'qz', 'qx', 'qc', 'qv', 'qb', 'qn', 'qm', 'wz', 'wx', 'wc', 'wv', 'wb', 'wn', 'wm', 'rz', 'rx', 'rc', 'rv', 'rb', 'rn', 'rm', 'tz', 'tx', 'tc', 'tv', 'tb', 'tn', 'tm', 'yz', 'yx', 'yc', 'yv', 'yb', 'yn', 'ym', 'pz', 'px', 'pc', 'pv', 'pb', 'pn', 'pm', 'sz', 'sx', 'sc', 'sv', 'sb', 'sn', 'sm', 'dz', 'dx', 'dc', 'dv', 'db', 'dn', 'dm', 'fz', 'fx', 'fc', 'fv', 'fb', 'fn', 'fm', 'gz', 'gx', 'gc', 'gv', 'gb', 'gn', 'gm', 'hz', 'hx', 'hc', 'hv', 'hb', 'hn', 'hm', 'jz', 'jx', 'jc', 'jv', 'jb', 'jn', 'jm', 'kz', 'kx', 'kc', 'kv', 'kb', 'kn', 'km', 'lz', 'lx', 'lc', 'lv', 'lb', 'ln', 'lm', 'sq', 'sw', 'sr', 'st', 'sy', 'sp', 'dq', 'dw', 'dr', 'dt', 'dy', 'dp', 'fq', 'fw', 'fr', 'ft', 'fy', 'fp', 'gq', 'gw', 'gr', 'gt', 'gy', 'gp', 'hq', 'hw', 'hr', 'ht', 'hy', 'hp', 'jq', 'jw', 'jr', 'jt', 'jy', 'jp', 'kq', 'kw', 'kr', 'kt', 'ky', 'kp', 'lq', 'lw', 'lr', 'lt', 'ly', 'lp', 'qm', 'wm', 'rm', 'tm', 'ym', 'pm', 'qm', 'wm', 'rm', 'tm', 'ym', 'pm', 'qm', 'wm', 'rm', 'tm', 'ym', 'pm', 'qm', 'wm', 'rm', 'tm', 'ym', 'pm', 'qm', 'wm', 'rm', 'tm', 'ym', 'pm', 'qm', 'wm', 'rm', 'tm', 'ym', 'pm', 'qm', 'wm', 'rm', 'tm', 'ym', 'pm', 'ms', 'md', 'mf', 'mg', 'mh', 'mj', 'mk', 'ml', 'ms', 'md', 'mf', 'mg', 'mh', 'mj', 'mk', 'ml', 'ms', 'md', 'mf', 'mg', 'mh', 'mj', 'mk', 'ml', 'ms', 'md', 'mf', 'mg', 'mh', 'mj', 'mk', 'ml', 'ms', 'md', 'mf', 'mg', 'mh', 'mj', 'mk', 'ml', 'ms', 'md', 'mf', 'mg', 'mh', 'mj', 'mk', 'ml', 'ms', 'md', 'mf', 'mg', 'mh', 'mj', 'mk', 'ml']

def get_variation(pair):
    pair_mirror = pair + pair[::-1]
    pair_n_last = pair + pair[-1]
    pair_n_first = pair + pair[0]
    return [pair_mirror, pair_n_last, pair_n_first]

def get_intro(ab, bc):
    intro = '\n'.join([ab, bc])
    intro_two = ' '.join([ab, bc])
    intro_repeat = ' '.join([ab, bc, ab, bc])
    return '\n'.join([intro, intro_two, intro_repeat])

def get_mutation(combo):
    first = choice(combo)
    second = choice(combo)
    third = choice(combo)

    a_verse = (first + second + '   ') * 2
    b_verse = ' '.join([(first+'  ')*2, third, second])
    verse = '\n'.join([a_verse, b_verse])
    return verse

def find_unique_pair(pairs):
    ab = choice(pairs)
    bc = choice(pairs)
    while ab == bc: # if we got the same pair
        ab = choice(pairs)
        bc = choice(pairs)
    return ab, bc

def tripplet():
    ### this is a 2d list of list
    triples = []
    for index, pair in enumerate(pair_ultimate):
        result = ' '
        lengths = range(randint(3, 8))
        for n in choice([lengths]):
            ab, bc = find_unique_pair(pair)
            ab_variation = get_variation(ab)
            bc_variation = get_variation(bc)

            combo = ab_variation + bc_variation
            intro = get_intro(ab, bc)
            mutation = get_mutation(combo)
            mutation_again = get_mutation(combo)
            result = result + ' '.join([intro, mutation, mutation_again]) + ' \n'
        triples.append(result)
    print '\n'.join(triples)

# tripplet()


def verse_a_b_mutation():
    verse_lines = []
    result = ' '
    for index, pair in enumerate(pair_sequence_list):
        first, second = find_unique_pair(pair)
        first_variation = get_variation(first)
        second_variation = get_variation(second)
        first_second_dbl = (first + ' ' + second)*2

        variation = choice([first_variation, second_variation])
        combo = first_variation + second_variation

        result = result + '   '.join([first_second_dbl, '\n ',get_mutation(combo), choice(variation)])
    verse_lines.append(result)
    return '\n'.join(verse_lines)


# verse_a_b_mutation()

def chorus():
    chorus_lines = []
    result = ' '
    varie_list = []
    for i in range(3):
        pair = choice(long_long_list)
        # print "par------ ", pair
        variations = get_variation(pair)
        varie_list.append(variations)
        # print varie_list
        for index,  vv in enumerate(varie_list):
            first_string_of_previous = varie_list[(index-1)%len(varie_list)][0]
            all_of_previous = varie_list[(index-1)%len(varie_list)]
            last_string_of_next = varie_list[(index+1)%len(varie_list)][-1]
            return ' '.join([vv[0], first_string_of_previous, ' '.join(vv[1:-1]),last_string_of_next, first_string_of_previous*2])

    # print varie_list

    #
    # result = result + ' '.join([get_mutation(combo), choice(variation)*3])
    # chorus_lines.append(result)
    # print '\n'.join(verse_lines)

def song_00():
    lyrics = []
    for i in range(3):
        verse_one = verse_a_b_mutation()
        verse_two = verse_a_b_mutation()
        chor_1 = chorus()
        chor_2 = chorus()
        chor_3 = chorus()
        # stance_str = [verse_one,verse_two, chor]
        # print stance_str
        lyrics.append(verse_one+'\n\n')
        lyrics.append(verse_two+'\n\n')
        lyrics.append(chor_1+'\n'+chor_2+'\n'+chor_3+'\n')
    return '\n'.join(lyrics)



print song_00()
# Vers
# dr tr dr tr drddrd   drddrd
# sl gr sl gr slsgrrg   slsgrrg
# cr tr cr tr crrctrt   crrctrt
