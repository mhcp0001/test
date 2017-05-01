# -*- coding: utf-8 -*-

import sys
import datetime
import math
import random

class Train:
    #obj_max = 6
    action_value = [[0 for i in range(2)] for j in range(3)] #行動選択Q値
    respond = [[0 for i in range(2)] for j in range(3)] #共感選択Q値
    memory = [[0 for i in range(3)] for j in range(3)] #物体記憶Q値
    #memory = [[0 for i in range(obj_max)] for j in range(obj_max)]
    inner = [0.0, 0.0] #行動選択時の確率保持
    mental = [0.0, 0.0] #共感選択時の確率保持　
    name_subscript = ['ぼーる', 'たまご', 'ぶどう'] #記憶リストの列
    image_subscript = ['ball', 'egg', 'grape'] #記憶リストの行
    inner_mode = 0
    mental_mode = 0
    subscript_name = 0 #発話認識された列番号
    subscript_image = 0 #物体認識された行番号
    reco_name = 0 #想起された列番号
    alpha = 0.1
    tau = 0.16

    def __init__(self, image, noun, final):
#        if image == 0:
#            self.image = 'apple'
#        elif image == 1:
#            self.image = 'orange'
#        else:
#            self.image = 'banana'

#        if noun == 0:
#            self.noun = 'りんご'
#        elif noun == 1:
#            self.noun = 'みかん'
#        else:
#            self.noun = 'ばなな'
        self.image = image
        self.noun = noun
        if final == 'だよ':
            self.final = 0
        elif final == 'だね':
            self.final = 1
        elif final == 'ですか':
            self.final = 2
        #self.final = int(final)

    def check(self): #認識された列と行の切り替え・追加
        for self.subscript_name in range(len(self.name_subscript)):　　#単語リストに入力された単語があるかを検索
            f = 0
            if self.name_subscript[self.subscript_name] == self.noun:
                f = 1
                break

        if f == 0:
            self.name_subscript.append(self.noun) #名詞リストに新規語を追加
            self.subscript_name += 1
            for i in range(len(self.image_subscript)):
                self.memory[i].append(0)

        for self.subscript_image in range(len(self.image_subscript)):　#イメージリストの検索
            f = 0
            if self.image_subscript[self.subscript_image] == self.image:
                f = 1
                break

        if f == 0: #イメージリストに追加
            self.image_subscript.append(self.image)
            self.subscript_image += 1
            self.memory.append([0 for i in range(len(self.name_subscript))])

    def select(self): #ソフトマックス選択
        inner_rnd = random.random()　#動作(記憶or想比)を決めるときに使う変数
        mental_rnd = random.random()
        self.inner[0] = math.exp(self.action_value[self.final][0] / self.tau)
        self.inner[1] = self.inner[0] + math.exp(self.action_value[self.final][1] / self.tau)

        self.mental[0] = math.exp(self.respond[self.final][0] / self.tau)
        self.mental[1] = self.inner[0] + math.exp(self.respond[self.final][1] / self.tau)

        for self.inner_mode in range(2):
            if inner_rnd <= self.inner[self.inner_mode] / self.inner[1]:
                break

        for self.mental_mode in range(2):
            if mental_rnd <= self.mental[self.mental_mode] / self.mental[1]:
                break


    def comparison(self): #想起・比較
        num = len(self.name_subscript)
        total = [0.0 for i in range(num)]
        rnd = random.random()

        for j in range(num):　#ソフトマックス法の前段階
            if j == 0:
                total[j] = math.exp(self.memory[self.subscript_image][j] / self.tau)
            else:
                total[j] = total[j - 1] + math.exp(self.memory[self.subscript_image][j] / self.tau)

        for self.reco_name in range(num):　#ソフトマックスの比較段階
            if rnd <= total[self.reco_name] / total[num - 1]:
                break


        if self.subscript_name == self.reco_name:
            return 0
        else:
            return 1

    def learn(self, reward): #学習更新
        self.action_value[self.final][self.inner_mode] = self.action_value[self.final][self.inner_mode] + self.alpha * (reward - self.action_value[self.final][self.inner_mode])

        self.respond[self.final][self.mental_mode] = self.respond[self.final][self.mental_mode] + self.alpha * (reward - self.respond[self.final][self.mental_mode])

        self.memory[self.subscript_image][self.reco_name] = self.memory[self.subscript_image][self.reco_name] + self.alpha * (reward - self.memory[self.subscript_image][self.reco_name])

