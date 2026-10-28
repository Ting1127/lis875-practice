# LIS 875 定義表

> 我的程式小白字典。每學一個新指令或新語法，就補進對應的表格裡。
> 「週」欄位記錄第一次學到的週次，方便回頭找課程頁面。

最後更新：Week 7

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
| `touch 檔名` | touch | 建立一個空白的新檔案 | `touch feature_votes.py` | W7 |
| `open -a "App" 檔名` | open with application | 用指定的 App 打開檔案 | `open -a "Visual Studio Code" feature_votes.py` | W7 |

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
| 一堆紅字，最後一行像 `TypeError: ...` | 程式出錯停下來了；`~~~^^^` 是在畫線標出問題位置 | 先看最後一行找原因，修好、存檔（Command + S），再按 ↑ 重新執行 |

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
| 使用者打 5，`input()` 拿到的就是數字 5 | `input()` 拿到的永遠是文字 `"5"`；`"5" + 1` 會出錯，要先用 `int()` 轉成數字 |
| `range(3)` 會印出 0、1、2、3 | 只有 0、1、2；括號裡的數字是「總共幾個」，最後一個永遠少 1 |
| `int(input(...))` 會出錯 | 不會；Python 從最裡面的括號做起：先收到文字，再轉成數字，才放進盒子 |
| 只寫 `def`、沒呼叫，程式會出錯 | 不會出錯，只是什麼都不執行（卡片貼了，沒人喊） |
| 有 `def` 的程式就不會印東西 | 沒縮排的 `名字()` 就是呼叫，喊幾次就做幾次 |
| 參數取的名字和下面用的名字不同也沒關係 | 要一致；括號寫 `person`，下面就要用 `person`，不然 Python 找不到盒子會出錯 |
| `return` 會把結果顯示在畫面上 | `return` 只是把結果交回來，要 `print()` 才看得到 |
| `.append()` 會把東西加在最前面 | 一定加在清單的最後面 |
| for 計數時，同一個 key 只會加一次 | 清單裡出現幾次就加幾次；一輪一輪追蹤 `v` 輪到誰 |
| 名字少一個 s 沒關係（`vote`、`answer`） | 要跟當初建立的名字一模一樣（`votes`、`answers`），不然 Python 找不到 |
| 呼叫函式時可以把整疊清單塞進去：`add_vote(answers)` | 要填這一輪手上的那一個：`add_vote(a)`；整個 list 不能當 dictionary 的格子名稱 |
| `input(...).lower()` 會出錯 | 不會；先收到文字，再轉成小寫，才放進盒子 |
| `"Admin" == "admin"` 成立 | `==` 很嚴格，大小寫不同就不相等；要先 `.lower()` 再比較 |
| 看不懂的程式就猜它會出錯 | 目前真的會報錯的只有：名字找不到、文字 + 數字、冒號後面空著、把 list 當 dictionary 格子 |

---

## 六、函式（def）

寫在 .py 檔裡。

| 語法 | 意思 | 範例 | 週 |
|---|---|---|---|
| `def 名字():` | define（定義）函式：寫一張作法卡貼到牆上，還不會執行 | `def ship():` | W4 |
| `名字()` | 呼叫函式：店長喊名字，才照卡片做一次（前面沒有 `def`、沒有縮排） | `ship()` | W4 |
| `def 名字(參數):` | 參數：卡片上的填空欄位，名字自己取，下面要用同一個名字 | `def welcome(person):` | W6 |
| `名字(值)` | 呼叫時把值填進參數那格；換不同的值就能重複使用 | `welcome("Jennie")` | W6 |
| `return 結果` | 把結果交回來（放在櫃台），畫面上不會顯示 | `return seats + 1` | W6 |
| `盒子 = 名字(值)` | 把 return 交回的結果放進盒子，之後再用 | `total = add_seat(4)` | W6 |
| `print(名字(值))` | 把 return 交回的結果廣播出來，畫面才看得到 | `print(total_price(10))` | W6 |

**一句話記：** def 是貼卡片，喊名字才會做；卡片上的空格名字要前後一致；return 是放櫃台，print 才是廣播。

---

## 七、List 與 Dictionary

寫在 .py 檔裡。

| 語法 | 意思 | 範例 | 週 |
|---|---|---|---|
| `[A, B, C]` | list（清單）：一排照順序放的東西，像待辦清單 | `features = ["login", "search"]` | W2 |
| `清單[0]` | 拿清單裡的第幾個；從 0 開始數，`[1]` 是第二個 | `features[1]` → `"search"` | W2 |
| `.append(東西)` | 把東西加到清單最後面 | `features.append("cart")` | W2 |
| `for x in 清單:` | 從清單裡一次抽一個出來，抽到的那個叫 `x` | `for item in backlog:` | W2 |
| `import random` | 把「隨機」工具箱拿出來用 | `import random` | W2 |
| `random.choice(清單)` | 從清單裡隨機抽一個，每次可能不一樣 | `random.choice(colors)` | W2 |
| `{"名稱": 值}` | dictionary（字典）：一塊有標籤的白板，每格有名稱和內容 | `plan = {"name": "Pro", "price": 300}` | W5 |
| `字典["名稱"]` | 拿某一格的內容出來 | `plan["price"]` → `300` | W5 |
| `字典["名稱"] = 字典["名稱"] + 1` | 計數：那一格原本的數字加 1，再放回去（開票畫一筆） | `votes[feature] = votes[feature] + 1` | W7 |

**計數口訣：** 先準備白板（每格 0）→ 從一疊票裡一次抽一張 → 抽到哪個就在那格畫一筆。
