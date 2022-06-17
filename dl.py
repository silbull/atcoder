import tkinter as tk
import youtube_dl
from PIL import Image, ImageTk

# ダウンロードが完了したことをお知らせするポップアップ
def popup_finish():
    # 画面の基本設定
    root_popup_finish = tk.Toplevel() # GUI画面を最前面に生成
    root_popup_finish.geometry("300x100") # 画面の大きさを設定。真ん中の×印は小文字のエックス
    root_popup_finish.title("完了") # 画面のタイトルを設定

    # アイコンを設定
    root_popup_finish.iconphoto(True, tk.PhotoImage(file='./icon_youtube_downloader.png')) # Falseにするとアイコン画像が現在の特定のウィンドウにのみ適用となってしまう。アイコン画像はicon_youtube_downloader.png。

    # ラベルを設定
    l_popup_finish = tk.Label(
        root_popup_finish,
        font=("", 12), # フォントはデフォルト("")、フォント大きさは12
        text = "ダウンロードが完了しました"
    )
    l_popup_finish.place(x=1, y=1) # ラベルの表示座標

    root_popup_finish.mainloop() # 画面を表示


# ダウンロードが完了出来なかったことをお知らせするポップアップ
def popup_not_finish(sentence):
    # 画面の基本設定
    root_popup_not_finish = tk.Toplevel() # GUI画面を最前面に生成
    root_popup_not_finish.geometry("300x100") # 画面の大きさを設定。真ん中の×印は小文字のエックス
    root_popup_not_finish.title("エラー") # 画面のタイトルを設定

    # アイコンを設定
    root_popup_not_finish.iconphoto(True, tk.PhotoImage(file='./icon_youtube_downloader.png')) # Falseにするとアイコン画像が現在の特定のウィンドウにのみ適用となってしまう。アイコン画像はicon_youtube_downloader.png。

    # ラベルを追加
    l_popup_not_finish = tk.Label(
        root_popup_not_finish,
        font=("", 12),
        text = str(sentence)
    )
    l_popup_not_finish.place(x=1, y=1)

    root_popup_not_finish.mainloop() # 画面を表示


# youtubeから動画をダウンロードする関数
def youtube_download(url_movie):
    try:
        ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url_movie])
        popup_finish()
    except:
        popup_not_finish("ダウンロードできませんでした")      
    

# ツールを起動する関数
def start_tool():
    # 画面の基本設定
    root = tk.Tk() # GUI画面を生成
    root.geometry("700x500") # 画面の大きさを設定。真ん中の×印は小文字のエックス
    root.configure(bg='white') # 背景を白にする
    root.title("YouTube Douwnloader") # 画面のタイトルを設定

    # アイコンを設定
    root.iconphoto(True, tk.PhotoImage(file='./icon_youtube_downloader.png')) # Falseにするとアイコン画像が現在の特定のウィンドウにのみ適用となってしまう。アイコン画像はicon_youtube_downloader.png。

    # タイトル画像表示
    canvas = tk.Canvas(root, bg="white", height=200, width=440, highlightthickness=0) # 画像を載せるためのキャンバスを画面に設定。highlightthickness=0で枠を消す
    canvas.place(x=130, y=60) # キャンバスの設置位置
    img = Image.open('title.png') # 画像読込
    img = img.resize((440, 200)) # 画像をキャンバスと同じ大きさにリサイズ
    img = ImageTk.PhotoImage(img) # 画像読込
    canvas.create_image(0, 0, image=img, anchor=tk.NW) # キャンバス上のx座標=0,y座標=0の位置に表示。
    # Tk.CENTER、Tk.W (左よせ）、Tk.E （右よせ）、Tk.N （上よせ）、Tk.S （下よせ）、 Tk.NW （左上）、Tk.SW （左下）、Tk.NE （右上）、Tk.SE （右下）

    # ラベルを設定
    l1 = tk.Label(
        root,
        font=("", 12), # 文字フォントは""で指定しない。フォントの大きさは12。
        bg="white", #背景を白にする(デフォルトはグレー)
        text="ダウンロードしたいYouTube動画のURLを入力してDownloadボタンを押してください" # ラベルとして表示するテキスト
    )
    l1.place(x=30, y=270) # ラベルの位置を指定

    l2 = tk.Label(
        root,
        font=("", 12),
        bg="white",
        text = "URL"
    )
    l2.place(x=30, y=300)

    # エントリーを設定(YouTube動画のURLを入れるところ)
    E = tk.Entry(
        root,
        font=("", 12),
        bg="lightgrey",
        width = 74
    )
    E.place(x=50, y=320 )

    # downloadボタンを設定
    B = tk.Button(
        root,
        text="Download", # ボタンに表示するテキスト
        fg="white", # テキストの色を指定
        bg="dimgrey", # ボタン背景の色を指定
        font=("", 20, "bold"), # フォントサイズを指定。フォント自体は""で指定しない。
        command=lambda:youtube_download(E.get()) # ボタンを押したときに実行される関数、#lambda型で書かないとなぜか上手く動かない。.get()でEntry内に入力された内容を取得
    ) 
    B.place(x=270, y=380) # ボタン位置調整

    root.mainloop() # 画面を表示する

if __name__ == '__main__':
    start_tool()