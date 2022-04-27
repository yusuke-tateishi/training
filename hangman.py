import random

def hangman(word):
    wrong=0
    stages=["",
            "__________          ",
            "|                   ",
            "|        |          ",
            "|        O          ",
            "|       /|＼        ",
            "|       / ＼        ",
            "|                   "
            ]
    rletters=list(word)
    board=["_"]*len(word)
    win=False
    print("""ハングマンへようこそ！\n
          このゲームは英単語当てクイズになっています\n
          1文字ずつ予想してアルファベットを入力し単語を完成させてください\n
          ハングマン（首吊り）の絵が完成してしまうとあなたの負けです\n
          それではゲームスタート！！""")
    while wrong<len(stages)-1:
        print("\n")
        msg="１文字を予想してね："
        char=input(msg)
        if char in rletters:
            print("正解！！")
            cind=rletters.index(char)
            board[cind]=char
            rletters[cind]='$'
        else:
            print("残念！！")
            wrong+=1
        print(" ".join(board))
        e=wrong+1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win=True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は {}.".format(word))

hangman_list=["cat","dog","bat","bull","fox"]
i=random.randint(0,len(hangman_list))
hangman(hangman_list[i])

