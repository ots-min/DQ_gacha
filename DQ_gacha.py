# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 13:04:32 2020

@author: Minoru Otsuka
"""

import random

def main():
    seijo_10x10()

def seijo_10x10():
    item = ["聖女のこん","聖女のティアラ","聖女のころも上","聖女のころも下","☆☆5☆☆","☆4","ゴミ"]
    odds1 = [0.5, 0.5, 0.5, 0.5, 5.0, 23.0, 70.0]
    odds2 = [7.14285, 7.14285, 7.14285, 7.14285, 71.4286, 0, 0]
    odds3 = [25.0, 25.0, 25.0, 25.0, 0, 0, 0]
    
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
