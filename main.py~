# -*- coding: utf-8 -*-

import test

if __name__ == '__main__':
    count = 0
    emp = 0

    while True:
        s = []
        s.append(raw_input('Please input fruit >> '))
        s.append(raw_input('Please input name >> '))
        s.append(raw_input('Please input final_particle >> '))

#        if s[0] == 'apple':
#            s[0] = 0
#        elif s[0] == 'orange':
#            s[0] = 1
#        elif s[0] == 'banana':
#            s[0] = 2

#        if s[1] == 'apple':
#            s[1] = 0
#        elif s[1] == 'orange':
#            s[1] = 1
#        elif s[1] == 'banana':
#            s[1] = 2

#        if s[2] == 'dayo':
#            s[2] = 0
#        elif s[2] == 'dane':
#            s[2] = 1
#        elif s[2] == 'desuka':
#            s[2] = 2

        x = test.Train(s[0], s[1], s[2])
        count += 1

        x.check()　#入力された単語が既知のものかどうかを確認、新規語ならリストに追加
        x.select()

        if x.inner_mode != 0:
            action_mode = x.comparison()
        else:
            x.reco_name = x.subscript_name
            action_mode = 10

        if x.mental_mode == 0:
            emp += 1
        else:
            emp -= 1

        print action_mode, x.mental_mode, emp

#        print x.image_subscript
#        for i in x.name_subscript:
#            print i,
#        print ''
#        print x.memory

        while True:
            r = raw_input('Please reward >> ')
            if r == 'g':
                reward = 1
                break
            elif r == 'b':
                reward = -1
                break
            else:
                print 'Error: Unexcepted reward'
                continue

        x.learn(reward)
        del x
