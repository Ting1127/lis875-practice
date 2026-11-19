# LIS 875 定義表

> 我的程式小白字典。每學一個新指令或新語法，就補進對應的表格裡。
> 「週」欄位記錄第一次學到的週次，方便回頭找課程頁面。

最後更新：Week 11

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
| `touch 資料夾/檔名` | touch | 直接在某個資料夾裡建立新檔案，不用先 cd 進去 | `touch practice-w11/study.py` | W11 |

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
| `git add 資料夾` | 把整個資料夾裡的修改一次放進這次的紀錄 | 整箱一起裝進紙箱 | W11 |
| 綠格子（contribution） | 那天有 commit 並 push 到 GitHub，個人頁面就會亮一格 | 每日打卡 | W11 |

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
| `"文字" * 數字` | 把文字重複幾次（像複製貼上），不是乘法 | `"3" * 2` → `"33"` | W9 |
| `len(東西)` | length：算有幾個（清單有幾項、白板有幾格） | `len(vocab)` | W9 |
| `float()` | 把文字轉成有小數點的數字（float = 浮點數） | `float("3.5")` → `3.5` | W10 |
| `str()` | string：把數字轉成文字 | `str(20)` → `"20"` | W10 |

**`=` 的讀法：** 把 `=` 想成往左的箭頭 `←`。Python 一定先算右邊，再把結果放進左邊。`count = count * 2` 就是「先取出 count 乘 2，再放回 count」。

---

## 四、看開頭判斷「我在哪裡」

| 看到的開頭 | 代表 | 可以打什麼 |
|---|---|---|
| `yuting@Jennie-z 資料夾 %` | 在終端機，等待指令 | `cd`、`ls`、`python3 ...`、`git ...` |
| `~` | 家目錄 | |
| `>>>` | 在 Python 互動模式裡 | `print(...)`、`2 + 3` |
| 一個問題，如 `Name of a place:` | 程式還在跑，等你回答 | 直接打答案 |
| 一堆紅字，最後一行像 `TypeError: ...` | 程式出錯停下來了；`~~~^^^` 是在畫線標出問題位置 | 先看最後一行找原因，修好、存檔（Command + S），再按 ↑ 重新執行 |
| 紅字裡的 `File "test.py", line 2` | 錯在 test.py 的第 2 行 | 打開檔案，直接跳到那一行看 |

**看錯誤訊息（Traceback）兩步驟：** ① 先看最後一行：錯誤種類和原因（例如 `TypeError: can only concatenate str (not "int") to str` = 文字不能直接接數字）② 再往上找 `line 幾`：知道是哪一行。找 bug 不用自己盯著看，讓 Python 跑一次，它會告訴你在哪裡。

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
| 使用者打 3，`n * 2` 會得到 6 | `n` 是文字 `"3"`，`"3" * 2` 會得到 `"33"`（重複兩次）；要先 `int(n) * 2` 才是 6 |
| 盒子後面也可以加 `()`：`amount(category)`、`category(input(...))` | 只有作法卡（函式）後面才能加 `()`；盒子後面加 `()` 會出現 `TypeError: 'str' object is not callable`。要找白板的格子用 `[]` |
| loop 跑完後，`amount` 就是全部的總和 | `amount` 每一輪都被新的金額蓋掉，最後只剩最後一筆；要總和就喊 `total()` |
| 函式裡只寫 `print`，外面 `total = 函式()` 也能拿到結果 | `print` 只是印給人看；沒有 `return`，`total` 拿到的是 `None`（空的） |
| 看到函式就猜結果是 `None` | 只有函式裡「沒寫 `return`」才會是 `None`；先看函式裡有沒有 `return` |
| 加總時，同一格第二次會被新的金額蓋掉（food 只剩 120） | `spending[category] + amount` 是原本的加上新的：120 + 80 = 200 |
| `scores["Ben"] = scores["Ben"] + 10`：左邊是取出、右邊是放進去 | 剛好相反：先算右邊（取出來加 10），再放進左邊那格 |

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

---

## 七、函式（def）

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
| `None` | 「什麼都沒有」：函式裡沒寫 `return` 時，交回來的就是它（櫃台上空空的） | `y = b(5)` → `y` 是 `None` | W10 |

**一句話記：** def 是貼卡片，喊名字才會做；卡片上的空格名字要前後一致；return 是放櫃台，print 才是廣播。

**return vs print：** `return` 把結果交給程式，可以放進盒子、拿去計算；`print` 只是印給人看，程式拿不到。判斷結果時，先看函式裡有沒有 `return`。

**盒子 vs 作法卡：** 盒子（`amount`、`category`、`spending`）是放東西的，後面不能加 `()`；作法卡（`print`、`input`、`int`、`range`、`total`）是會做事的，加 `()` 就是喊它做事。白板找格子用 `[]`：`spending["food"]`。

---

## 八、List 與 Dictionary

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
| `字典[格子] = 字典[格子] + 金額` | 加總：跟計數一樣，只是每次加的不是 1，而是這一筆的數字 | `spending[category] = spending[category] + amount` | W9 |

**計數口訣：** 先準備白板（每格 0）→ 從一疊票裡一次抽一張 → 抽到哪個就在那格畫一筆。
**看不懂計數時：** 每一輪都把 `a` 換成這一輪抽到的字，再一輪一輪寫下白板的樣子。

**`[]` 的三種用法：** ① 單獨出現 `["a", "b"]` = 建立清單 ② 在 `=` 右邊或 `print` 裡 `spending["food"]` = 取出 ③ 在 `=` 左邊 `spending["food"] = 200` = 放進去／更新。

---

## 九、讀寫檔案

寫在 .py 檔裡。

| 語法 | 意思 | 範例 | 週 |
|---|---|---|---|
| `with open("檔名", "r", encoding="utf-8") as f:` | 打開檔案，取名叫 `f`；縮排的幾行可以用它，縮排結束就自動關檔。`with` 不是迴圈，只跑一次 | `with open("todo.txt", "r", encoding="utf-8") as f:` | W9 |
| `"r"` | read：只讀、不改 | | W9 |
| `"w"` | write：寫入；檔案原本的內容會被整個蓋掉 | `open("summary.txt", "w", encoding="utf-8")` | W9 |
| `encoding="utf-8"` | 用 utf-8 這本「號碼 ↔ 字」名單來讀寫；電腦只存號碼，名單拿錯就會變亂碼。照抄就好，有中文、日文一定要寫 | | W9 |
| `for line in f:` | 從檔案一次拿一行，拿到的那行叫 `line`（跟 `for x in 清單:` 一樣） | `for line in f:` | W9 |
| `.strip()` | 剪掉頭尾的空白和每行最後藏著的 Enter | `line = line.strip()` | W9 |
| `.split("記號")` | 遇到記號就剪一刀，剪完變成清單 | `"たべる = 吃".split(" = ")` → `["たべる", "吃"]` | W9 |
| `"字" in 文字` | 問左邊的字有沒有出現在右邊裡面 | `"lis" in line.lower()` | W9 |
| `print(..., file=out)` | 把字寫進檔案，不印在畫面上 | `print(line, file=out)` | W9 |

**VS Code 小提示：** 視窗最下面那條的右邊寫著 `UTF-8`，代表這個檔案是用 utf-8 存的。
