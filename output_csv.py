import pandas as pd
import os
from tkinter import filedialog
import tkinter as tk
import subprocess

class output:

    def __init__(self,name):
        self.name = name

    def output_csv(self):

        url = 'https://finance.yahoo.co.jp/stocks/ranking/up?market=all&term=daily'
        dfs = pd.read_html(url)

        df = dfs[0]

        # print(df['取引値'].dtype)  #データ型確認
        # print(df['取引値'])
        # print(df['前日比'][0].replace('+',' '))

        #  前日比の＋を削除しながら、dfの前日にセット
        #  以下のLoopの場合と同じ挙動
        df['前日比'] = [datum.replace('+',' ') for datum in df['前日比'].tolist()]
        # print(df.tail)

        df = df.astype(
        {'順位':int
        })

        # # Loopの場合
        # data = []
        # for datum in df['前日比'].tolist():
        #     data.append(datum.replace('+',' '))
        #
        # df['前日比'] = data


        print(df)

        output.save_csv(df)

    @staticmethod
    def save_csv(df):

        #tkinterのウィンドウを非表示へ
        root = tk.Tk()
        root.withdraw()

        # ダイアログ表示
        fname = filedialog.asksaveasfilename(
            title = "名前を付けて保存",
            filetypes = [("csvファイル", ".csv")], # ファイルフィルタ
            initialdir = "./", # 自分自身のディレクトリ
            defaultextension = "csv"
            )

        # CSVに出力
        if fname:
            df.to_csv(fname)

        # キャンセルが選択された場合
        else:
            return            

        # #カレントディレクトリを取得
        # path = os.getcwd()
        #
        # #ファイル出力場所を指定(フォルダーダイアログでフォルダーを選択)
        # path = filedialog.askdirectory(initialdir = path)


        # #csvファイル（フルパス）
        # file_name = path + '/test.csv'

        print(fname)

        #サクラエディタでoutfile.csvを開く
        exe = r'C:/Program Files/sakura/sakura.exe'
        subprocess.Popen([exe, fname])


if __name__ == '__main__':
    ot = output('name')
    ot.output_csv()
