import re
text="""キリンは大昔から __複数名詞__の興味の対象でした。キ
リンは __複数名詞__ の中で一番背が高いですが、科学者たちはそのよ
うな長い __体の一部__ をどうやって獲得したのか説明できません。キ
リンの身長は __数値__ __単位__ 近くあり、その高さのほとんどは脚
と __体の一部__ によるものです。
"""

def mad_libs(mls):
    """
    :param mls: 文字列で、ユーザーに入力してもらいたい単語(=
ヒント)の部分は後を2つのアンダースコアで挟んで下さい。ヒントの単
語にはアンダースコアを含めないで下さい。__hint_hint__ はだめで
す。__hint__ はOKです。
　　"""

    hints=re.findall("__.*?__",mls)
    if hints is not None:
        for word in hints:
            q="{} を入力:".format(word)
            new=input(q)
            mls=mls.replace(word,new,1)
        print("\n")
        mls=mls.replace("\n","")
        print(mls)

    else:
        print("引数mlsが無効です")

mad_libs(text)
