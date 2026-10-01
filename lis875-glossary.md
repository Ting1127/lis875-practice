# LIS 875 定義表

> 我的程式小白字典。每學一個新指令或新語法，就補進對應的表格裡。
> 「週」欄位記錄第一次學到的週次，方便回頭找課程頁面。

最後更新：Week 3

---

## 一、終端機指令

在 `%` 後面輸入。

| 指令 | 完整英文 | 意思 | 範例 | 週 |
|---|---|---|---|---|
| `pwd` | print working directory | 印出我現在所在的資料夾 | `pwd` | W0 |
| `ls` | list | 列出這個資料夾裡有哪些東西 | `ls` | W0 |
| `cd 資料夾` | change directory | 走進某個資料夾 | `cd Desktop` | W0 |
| `cd ..` | | 回到上一層資料夾 | `cd ..` | W0 |
| `cd` | | 直接回家目錄（~） | `cd` | W0 |
| `cd A/B` | | 一次走進兩層資料夾 | `cd Desktop/lis875` | W0 |
| `mkdir 名稱` | make directory | 建立新資料夾 | `mkdir lis875` | W0 |
| `python3` | | 進入 Python 互動模式（出現 `>>>`） | `python3` | W0 |
| `python3 檔名.py` | | 執行一支 Python 程式 | `python3 hello.py` | W0 |
| `quit()` | | 離開 Python 互動模式，回到 `%` | `quit()` | W0 |
| Control + C | | 強制停止正在跑的程式 | | W0 |
| Tab 鍵 | | 自動補完檔名或資料夾名稱 | `cd Dow` + Tab | W0 |
| ↑ 方向鍵 | | 叫出上一個打過的指令 | | W0 |

---

## 二、Git / GitHub

| 指令／名詞 | 意思 | 比喻 | 週 |
|---|---|---|---|
| repository（repo） | 一包專案檔案 | 一個專案資料夾 | W1 |
| Fork（網頁按鈕） | 把別人的 repo 複製一份到自己的 GitHub 帳號 | Google Docs 的「建立副本」 | W1 |
| `git clone 網址` | 把 repo 下載到電腦，並保持連線 | 下載 + 建立連線 | W1 |
| `git status` | 查看哪些檔案改過、哪些已經 add | 看一眼桌上的狀況 | W1 |
| `git add 檔名` | 把修改放進這次的紀錄 | 把東西放進紙箱 | W1 |
| `git commit -m "說明"` | 在電腦上建立一個版本 | 封箱、貼標籤 | W1 |
| `git push` | 電腦 → GitHub | 把紙箱寄出去 | W1 |
| `git pull` | GitHub → 電腦 | 收回別人寄來的紙箱 | W1 |
| access token | push 時用的專用密碼（`ghp_` 開頭） | 終端機專用鑰匙 | W1 |

**標準流程：** 改檔案 → `git status` → `git add` → `git commit -m "..."` → `git push`
**開始工作前：** 先 `git pull`

---

## 三、Python 語法

寫在 .py 檔裡。

| 語法 | 意思 | 範例 | 週 |
|---|---|---|---|
| `print()` | 印出一行 | `print("Hello")` | W0 |
| `# ...` | 註解，寫給人看，Python 會跳過 | `# Fill in some words` | W0 |
| `"文字"` | 字串：有引號就照字面印出 | `"head"` | W0 |
| `名字 = 內容` | 建立變數：把內容放進盒子 | `action = "catch"` | W0 |
| 沒有引號的名字 | 去盒子裡拿內容出來用 | `print(action)` | W0 |
| `input("問題")` | 問使用者，並等他打字 | `place = input("Name of a place: ")` | W0 |
| `int()` | 把文字轉成數字 | `int("5")` → 5 | W0 |
| `,`（print 裡） | 串接時自動加空格 | `print("my", body_part)` | W0 |
| `+`（print 裡） | 串接時不加空格 | `"my " + body_part` | W0 |
| `=` | 放進盒子 | `count = 2` | W0 |
| `==` | 比較兩邊是否相等 | `person == "Thor"` | W0 |
| `if` | 如果…… | `if drink == "tea":` | W0 |
| `elif` | 不然，如果……（可以有很多個） | `elif drink == "juice":` | W0 |
| `else` | 以上都不是（放最後，不寫條件） | `else:` | W0 |
| `or` | 其中一個成立就可以 | `(p == "cap") or (p == "Cap")` | W0 |
| `:` + 縮排 | 冒號之後縮排的幾行，屬於這一段 | | W0 |
| `for x in range(n):` | 重複執行 n 次 | `for i in range(20):` | W0 |
| `range(5)` | 產生 0、1、2、3、4（從 0 開始，不含 5） | | W0 |
| `.lower()` | 把文字轉成全小寫 | `input(...).lower()` | W0 |
| `count = count - 1` | 拿出目前的數字減 1，再放回去 | | W1 |

---

## 四、看開頭判斷「我在哪裡」

| 看到的開頭 | 代表 | 可以打什麼 |
|---|---|---|
| `yuting@Jennie-z 資料夾 %` | 在終端機，等待指令 | `cd`、`ls`、`python3 ...`、`git ...` |
| `~` | 家目錄 | |
| `>>>` | 在 Python 互動模式裡 | `print(...)`、`2 + 3` |
| 一個問題，如 `Name of a place:` | 程式還在跑，等你回答 | 直接打答案 |

---

## 五、我踩過的坑

| 我以為 | 其實 |
|---|---|
| `pwd` 是 password | 是 print working directory，印出目前位置 |
| 在 `%` 後面可以打 `print(...)` | 程式碼要寫在 .py 檔裡，終端機只負責執行 |
| 要把答案寫進 `input("...")` 的括號裡 | 括號裡是問題；答案是執行時才在終端機打 |
| 程式在問問題時，可以打新的指令 | 程式還在跑時，打的字都會被當成答案；按 Control + C 可中斷 |
| `cd clone` | 下載 repo 是 `git clone`，第一個字是 git |
| `git clone` 是打開網址 | 是把整個 repo 下載到電腦，並保持連線 |
| `Download` | 資料夾名稱是 `Downloads`，差一個字母就找不到（用 Tab 補完） |
| 下載的檔案叫 eliza.py | 重複下載會變成 `Eliza (1).py`，要改回全小寫、無空格 |
| `done()` 可以放在中間 | Python 走到 `done()` 就停住，後面的都不會畫；`done()` 永遠放最後一行 |
| `pendown()`、`done()` 括號裡要放數字 | 這兩個括號裡不放東西，空著就好 |
| 畫框框往上走用 `right(90)` | 臉朝右時，`right(90)` 是轉向下；要往上要用 `left(90)` |
| `forward(50)` 可以換到下一行 | `forward` 是往臉的方向畫一條線；要往下移得先抬筆、轉向下、走、轉回來、放筆 |
| Exercise 6 的 second name 是「姓氏」 | 是「第二個人的名字」 |
| 只打 `python3` 就能執行程式 | 只打 `python3` 會進入 `>>>` 互動模式；要加檔名：`python3 stars.py` |

---

## 六、Turtle 畫圖

檔案第一行先寫 `from turtle import *`，下面的指令才能用。

| 語法 | 意思 | 範例 | 週 |
|---|---|---|---|
| `from turtle import *` | 把 turtle 的所有畫圖指令拿進來用（放在第一行） | `from turtle import *` | W3 |
| `forward(n)` | 往臉朝的方向走 n 步，筆放下時會畫出線 | `forward(100)` | W3 |
| `back(n)` | 往後退 n 步（臉的方向不變） | `back(50)` | W3 |
| `left(角度)` | 原地往左轉幾度 | `left(90)` | W3 |
| `right(角度)` | 原地往右轉幾度 | `right(144)` | W3 |
| `penup()` | 把筆抬起來：之後移動不會畫線（括號裡不放東西） | `penup()` | W3 |
| `pendown()` | 把筆放下：之後移動會畫線（括號裡不放東西） | `pendown()` | W3 |
| `write("文字")` | 在 turtle 站的地方寫字；有引號照字面寫，沒引號去盒子拿 | `write(name)` | W3 |
| `font=("字型", 大小, "粗細")` | 放在 `write()` 裡，設定字的樣子 | `write(name, font=("Arial", 20, "normal"))` | W3 |
| `textinput("標題", "問題")` | 跳出小視窗問使用者，答案放進盒子（turtle 版的 `input()`） | `name = textinput("Name", "Please enter your name")` | W3 |
| `color("顏色")` | 設定筆和填色的顏色 | `color("red")` | W3 |
| `begin_fill()` | 開始記錄「要塗滿的形狀」 | `begin_fill()` | W3 |
| `end_fill()` | 形狀畫完，把剛剛圍起來的地方塗滿 | `end_fill()` | W3 |
| `done()` | 畫完了，讓視窗停著等人關掉（永遠放最後一行） | `done()` | W3 |
| `["red", "blue"]` | 清單（list）：一個盒子裡放好幾樣東西，用來讓每顆星星換顏色 | `colors = ["red", "blue", "yellow"]` | W3 |
| 迴圈裡再放迴圈 | 外面的迴圈每跑一次，裡面的迴圈就整個跑完一輪 | 一排五顆星：外圈 5 次、內圈畫一顆星 | W3 |

**往下移一行、不畫線的固定組合：** `penup()` → `right(90)` → `forward(40)` → `left(90)` → `pendown()`
**畫一顆星星（3 行）：** `for i in range(5):` → `forward(100)` → `right(144)`
