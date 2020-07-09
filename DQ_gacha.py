# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 13:04:32 2020

@author: Minoru Otsuka
"""

import random

def main():
    mizugi_10x10()
    #kuroarashi_10x10()
    #seijo_10x10()
    #seitate_10x10()
    #metal_10x10()
    #densetsu_10x10()

def mizugi_10x10():
    item = ["オーシャンウィップ","あぶない髪飾り","あぶない水着上","あぶない水着下","☆☆5☆☆","☆4","ゴミ"]
    odds1 = [0.5, 0.5, 0.5, 0.5, 5.0, 23.0, 70.0]
    odds2 = [7.14285, 7.14285, 7.14285, 7.14285, 71.4286, 0, 0]
    odds3 = [25.0, 25.0, 25.0, 25.0, 0, 0, 0]
    
    gacha10x10(item,odds1,odds2,odds3)
    
def kuroarashi_10x10():
    item = ["黒嵐のツメ","黒嵐のフード","黒嵐のローブ上","黒嵐のローブ下","☆☆5☆☆","☆4","ゴミ"]
    odds1 = [0.5, 0.5, 0.5, 0.5, 5.0, 23.0, 70.0]
    odds2 = [7.14285, 7.14285, 7.14285, 7.14285, 71.4286, 0, 0]
    odds3 = [25.0, 25.0, 25.0, 25.0, 0, 0, 0]
    
    gacha10x10(item,odds1,odds2,odds3)
        
def seijo_10x10():
    item = ["聖女のこん","聖女のティアラ","聖女のころも上","聖女のころも下","☆☆5☆☆","☆4","ゴミ"]
    odds1 = [0.5, 0.5, 0.5, 0.5, 5.0, 23.0, 70.0]
    odds2 = [7.14285, 7.14285, 7.14285, 7.14285, 71.4286, 0, 0]
    odds3 = [25.0, 25.0, 25.0, 25.0, 0, 0, 0]

    gacha10x10(item,odds1,odds2,odds3)

def seitate_10x10():
    item = ["聖盾騎士のオノ","聖盾騎士のかぶと","聖盾騎士のよろい上","聖盾騎士のよろい下","聖盾騎士の大盾","☆☆5☆☆","☆4","ゴミ"]
    odds1 = [0.5, 0.5, 0.5, 0.5, 0.5, 4.5, 23.0, 70.0]
    odds2 = [7.14285, 7.14285, 7.14285, 7.14285, 7.14285, 64.28575, 0, 0]
    odds3 = [20.0, 20.0, 20.0, 20.0, 20.0, 0, 0, 0]    
 
    gacha10x10(item,odds1,odds2,odds3)
    
def metal_10x10():
    item = ["メタスラのオノ","メタルウィング","メタスラの剣","メタスラのやり","メタスラの盾","☆☆5☆☆","☆4","ゴミ"]
    odds1 = [0.5, 0.5, 0.5, 0.5, 0.5, 4.5, 23.0, 70.0]
    odds2 = [7.14285, 7.14285, 7.14285, 7.14285, 7.14285, 64.28575, 0, 0]
    odds3 = [20.0, 20.0, 20.0, 20.0, 20.0, 0, 0, 0]    
 
    gacha10x10(item,odds1,odds2,odds3)

def densetsu_10x10():
    item = ["王者の剣","ひかりのかぶと","ひかりのよろい上","ひかりのよろい下","勇者の盾","☆☆5☆☆","☆4","ゴミ"]
    odds1 = [0.5, 0.5, 0.5, 0.5, 0.5, 4.5, 23.0, 70.0]
    odds2 = [7.14285, 7.14285, 7.14285, 7.14285, 7.14285, 64.28575, 0, 0]
    odds3 = [20.0, 20.0, 20.0, 20.0, 20.0, 0, 0, 0]    
 
    gacha10x10(item,odds1,odds2,odds3)


def gacha10x10(item,odds1,odds2,odds3):
    for i in range(1,6):
        print(str(i)+"回目")
        gacha(10,item,odds1)
        print("")
        
    for i in range(6,7):
        print(str(i)+"回目(1枠☆5確定)")
        gacha(1,item,odds2)
        gacha(9,item,odds1)
        print("")
    
    for i in range(7,10):
        print(str(i)+"回目")
        gacha(10,item,odds1)
        print("")

    for i in range(10,11):
        print(str(i)+"回目(1枠ピックアップ確定)")
        gacha(1,item,odds3)
        gacha(9,item,odds1)
        print("")
        
def gacha(num,item,odds):
    
    for i in range(num):
        dice = random.random()*100
        
        for name in item:
            if dice < odds[item.index(name)]:
                print(name,end=" ")
                break
            else:
                dice = dice - odds[item.index(name)]
     
#メイン関数実行
main()
