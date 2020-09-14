# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 13:04:32 2020

@author: Minoru Otsuka
"""

import random
import tkinter
from tkinter import ttk
from tkinter import messagebox

def main():
    global txt, combo
    
    w = tkinter.Tk()
    w.title("DQWガチャシミュレータ")

    f = ttk.Frame(w, padding=10) 
    f.pack()
    
    combo = ttk.Combobox(f, state="readonly")
    combo["value"] = ("伝説の勇者装備",
                     "メタスラ装備",
                     "聖盾騎士装備",
                     "聖女装備",
                     "黒嵐装備",
                     "あぶない水着装備",
                     "蒼竜装備",
                     "魔狼装備",
                     "世界樹の導き装備")
    combo.current(8)
    combo.grid(row=0, column=0, sticky=tkinter.W)
    
    b_start = ttk.Button(f,text="ガチャ開始",command=gacha_start,)
    b_start.grid(row=0, column=1, sticky=tkinter.W)

    txt = tkinter.Text(f, height=20, width=80)
    txt.grid(row=1, columnspan=2)
    
    f.mainloop()

def gacha_start():
    global combo
    global item

    if(combo.current() == 0):
        item = ["王者の剣","ひかりのかぶと","ひかりのよろい上","ひかりのよろい下","勇者の盾","☆☆5☆☆","☆4","ゴミ"]
        odds1 = [0.5, 0.5, 0.5, 0.5, 0.5, 4.5, 23.0, 70.0]
        odds2 = [7.14285, 7.14285, 7.14285, 7.14285, 7.14285, 64.28575, 0, 0]
        odds3 = [20.0, 20.0, 20.0, 20.0, 20.0, 0, 0, 0] 
    elif(combo.current() == 1):
        item = ["メタスラのオノ","メタルウィング","メタスラの剣","メタスラのやり","メタスラの盾","☆☆5☆☆","☆4","ゴミ"]
        odds1 = [0.5, 0.5, 0.5, 0.5, 0.5, 4.5, 23.0, 70.0]
        odds2 = [7.14285, 7.14285, 7.14285, 7.14285, 7.14285, 64.28575, 0, 0]
        odds3 = [20.0, 20.0, 20.0, 20.0, 20.0, 0, 0, 0]   
    elif(combo.current() == 2):
        item = ["聖盾騎士のオノ","聖盾騎士のかぶと","聖盾騎士のよろい上","聖盾騎士のよろい下","聖盾騎士の大盾","☆☆5☆☆","☆4","ゴミ"]
        odds1 = [0.5, 0.5, 0.5, 0.5, 0.5, 4.5, 23.0, 70.0]
        odds2 = [7.14285, 7.14285, 7.14285, 7.14285, 7.14285, 64.28575, 0, 0]
        odds3 = [20.0, 20.0, 20.0, 20.0, 20.0, 0, 0, 0]    
    elif(combo.current() == 3):
        item = ["聖女のこん","聖女のティアラ","聖女のころも上","聖女のころも下","☆☆5☆☆","☆4","ゴミ"]
        odds1 = [0.5, 0.5, 0.5, 0.5, 5.0, 23.0, 70.0]
        odds2 = [7.14285, 7.14285, 7.14285, 7.14285, 71.4286, 0, 0]
        odds3 = [25.0, 25.0, 25.0, 25.0, 0, 0, 0]
    elif(combo.current() == 4):
        item = ["黒嵐のツメ","黒嵐のフード","黒嵐のローブ上","黒嵐のローブ下","☆☆5☆☆","☆4","ゴミ"]
        odds1 = [0.5, 0.5, 0.5, 0.5, 5.0, 23.0, 70.0]
        odds2 = [7.14285, 7.14285, 7.14285, 7.14285, 71.4286, 0, 0]
        odds3 = [25.0, 25.0, 25.0, 25.0, 0, 0, 0]
    elif(combo.current() == 5):
        item = ["オーシャンウィップ","あぶない髪飾り","あぶない水着上","あぶない水着下","☆☆5☆☆","☆4","ゴミ"]
        odds1 = [0.5, 0.5, 0.5, 0.5, 5.0, 23.0, 70.0]
        odds2 = [7.14285, 7.14285, 7.14285, 7.14285, 71.4286, 0, 0]
        odds3 = [25.0, 25.0, 25.0, 25.0, 0, 0, 0]
    elif(combo.current() == 6):
        item = ["蒼竜のやり","蒼竜のヘルム","蒼竜のよろい上","蒼竜のよろい下","☆☆5☆☆","☆4","ゴミ"]
        odds1 = [0.5, 0.5, 0.5, 0.5, 5.0, 23.0, 70.0]
        odds2 = [7.14285, 7.14285, 7.14285, 7.14285, 71.4286, 0, 0]
        odds3 = [25.0, 25.0, 25.0, 25.0, 0, 0, 0]
    elif(combo.current() == 7):
        item = ["魔狼牙","魔狼のマスク","魔狼の鎧上","魔狼の鎧下","魔狼の盾","☆☆5☆☆","☆4","ゴミ"]
        odds1 = [0.5, 0.5, 0.5, 0.5, 0.5, 4.5, 23.0, 70.0]
        odds2 = [7.14285, 7.14285, 7.14285, 7.14285, 7.14285, 64.28575, 0, 0]
        odds3 = [20.0, 20.0, 20.0, 20.0, 20.0, 0, 0, 0]    
    elif(combo.current() == 8):
        item = ["世界樹のつるぎ","世界樹の宝冠","世界樹の鎧上","世界樹の鎧下","みちびきの盾","☆☆5☆☆","☆4","ゴミ"]
        odds1 = [0.5, 0.5, 0.5, 0.5, 0.5, 4.5, 23.0, 70.0]
        odds2 = [7.14285, 7.14285, 7.14285, 7.14285, 7.14285, 64.28575, 0, 0]
        odds3 = [20.0, 20.0, 20.0, 20.0, 20.0, 0, 0, 0]    
        
    gacha10x10(item,odds1,odds2,odds3)

def gacha10x10(item,odds1,odds2,odds3):
    global gacha_result, txt
    global res
    
    gacha_result = [0] * len(item)
    txt.delete("1.0","end")
    
    for i in range(1,6):
        print(str(i)+"回目")
        txt.insert("end", str(i)+"回目\n")
        res = ""
        gacha(10,item,odds1)
        print("")
        txt.insert("end", res+"\n")
        
    for i in range(6,7):
        print(str(i)+"回目(1枠☆5確定)")
        txt.insert("end", str(i)+"回目(1枠☆5確定)\n")
        res = ""
        gacha(1,item,odds2)
        gacha(9,item,odds1)
        print("")
        txt.insert("end", res+"\n")
    
    for i in range(7,10):
        print(str(i)+"回目")
        txt.insert("end", str(i)+"回目\n")
        res = ""
        gacha(10,item,odds1)
        print("")
        txt.insert("end", res+"\n")

    for i in range(10,11):
        print(str(i)+"回目(1枠ピックアップ確定)")
        txt.insert("end", str(i)+"回目(1枠ピックアップ確定)\n")
        res = ""
        gacha(1,item,odds3)
        gacha(9,item,odds1)
        print("")
        txt.insert("end", res+"\n")

    print_result()
        
def gacha(num,item,odds):
    global gacha_result
    global res
    
    for i in range(num):
        dice = random.random()*100
        
        for name in item:
            if dice < odds[item.index(name)]:
                print(name,end=" ")
                res += name + " "
                gacha_result[item.index(name)] += 1
                break
            else:
                dice = dice - odds[item.index(name)]

def print_result():
    global item
    global gacha_result

    mes = ""
    for i in range(len(item)):
        mes += item[i] + " "
        mes += str(gacha_result[i])
        mes += "個\n"
    print(mes)
    messagebox.showinfo("100連ガチャ 入手結果",mes)    
     
#メイン関数実行
main()
