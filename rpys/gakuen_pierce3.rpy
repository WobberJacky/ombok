label gakuen_pierce3:
scene bg_map_day
with dis
$ clockanim()

jump gakuen_dream_other
label gakuen_pierce3_2:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（……最近は、みていなかったのに）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうして、いまさらになって夢に見たのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_12")
T "（ピアス相手に、先生の真似事をしているせいかしら……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_3")
T "（……先生）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "忘れっぽいのも問題だが、覚えすぎているのも同様に問題がある。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「……ピアスのこと、笑えないわね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "愚かなことに変わりはない。\n
むしろ、忘れ方を教わりたい。"

jump gakuen_cafeteria_notjoker
label gakuen_pierce3_3:
with dis
$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME
pause 1
play sound se_0229

play music classroom_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どことなくそわそわとした空気の中、放課後のホームルームが終わった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "顔を上げると、ピアスが身支度を整えてからこちらに来ようとしているのが目に入る。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この光景にも慣れたもの。\n
最近放課後は毎日のように、一緒に勉強をしているからだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "少し考え、今日の勉強会は中止にすることに決めた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「ピアス、今日は休みにするわ。\n
最近毎日勉強会をしていたもの、たまには休みましょう」"


show pia_m_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice pie_g0107
Pierce "「え？\n
君、今日は忙しいの？」"

hide pia_m_03_1
show pia_m_03_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice pie_g0108
Pierce "「それとも俺と遊んでくれるの？\n
俺も君と遊びたいな！遊びたいよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「違うわよ。\n
ゴーランドと話があるの」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……ゴーランド」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "会話のついでのように、ホームルームを終えて教室から去りかけていたゴーランドを呼び止める。"

hide pia_m_03_6
show pia_m_01_11 at left
with dis

show go_m_03_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0287
Gowland "「お？俺か？\n
今日が何の日なのかだとか、そういうのは俺も言えねえぜ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「そっちも気になるけど、そうじゃなくって。\n
ちょっと、付き合ってほしいのよ」"

hide go_m_03_9
show go_m_01_11 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice gor_g0288
Gowland "「ん？俺とか？\n
ピアス抜きで？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_13")
T "「そう、あなたに用があるの。\n
だから、今日は補習は休みにしようと思うの……」"

hide pia_m_01_11
show pia_m_01_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_13")
Pierce "「…………」"

hide pia_m_01_1
show pia_m_01_9 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_13")
voice pie_g0109
Pierce "「お……、俺も一緒にお話するよ！\n
いいでしょう！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_1")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（……困る）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、ピアスのことについてを、ゴーランドに相談するつもりだったのだ。\n
その場にピアスがいては、会話がかえって混乱する。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普段ならば、諦め混じりに、それでも構わないと承諾するところ。\n
けれど……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（……夢、が）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "明け方懐かしい夢を見てしまったせいで、変に意識してしまいそうになる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドに頼まれたからという理由以上に、ピアスに肩入れしてしまいそうになっている自分。\n
当人である彼には見られたくない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "意識していると、知られたくない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（……かなり分かりやすくても、気付くかどうか怪しいところだけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どう誤魔化そうか口ごもった私の躊躇を、ゴーランドは見透かしたようだった。"

play sound se_0448
hide go_m_01_11
show go_m_03_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0289
Gowland "「ピアス、悪いな。\n
ちょっと人には聞かれたくない話なんだ」"

hide go_m_03_2
show go_m_02_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0290
Gowland "「なあに、明日には補習再開だ。\n
……だよな？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「ええ、そうよ。\n
明日からはまた再開するから……、今日はお休みにしてもいいかしら」"

hide pia_m_01_9
show pia_m_03_9 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
Pierce "「…………」"

hide go_m_02_8
show go_m_02_8 at center
with dis
hide pia_m_03_9

play sound se_0417
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ピアスは不満そうだ。\n
不満そうに私とゴーランドを見比べると、何を言うでもなく無言でふいっと教室から出て行ってしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……仲間はずれにしちゃったかしら）"

menu:
    "子供っぽいんだから。":
        jump gakuen_pierce3_4a
    "悪いことしたな……。":
        jump gakuen_pierce3_4b
label gakuen_pierce3_4a:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（……子供っぽいんだから）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分の分からない話題に拗ねる子供のようだ。\n
去っていくピアスの背を見送りながら、私は考えを変えることにした。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（意識なんて、していない）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やはりあの夢は、先生の真似事をしているから見たものなのだ。\n
ピアスに特別な思い入れを感じ始めているなんて理由からではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「……変に気にして損したわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こんなことなら、ピアスがいたままでも構わなかった。\n
変にむくれさせてしまった。"

jump gakuen_pierce3_5
label gakuen_pierce3_4b:
$ lovechara_pierce_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（悪い事したな……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しょんぼりと肩を下げた背中は、とても寂しげに見えた。ピアスのことだから、私やゴーランドに嫌われたと勘違いしてしまったかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（今からでも、追いかけたほうがいいかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こうして後悔するぐらいなら、最初からピアスを遠ざけたりしなければよかった。"

jump gakuen_pierce3_5
label gakuen_pierce3_5:
hide go_m_02_8
show go_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0291
Gowland "「で、俺に何の用だ？\n
何が聞きたいって？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「召喚魔法のことで、質問があるの」"

hide go_m_03_9
show go_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice gor_g0292
Gowland "「……ははあ。\n
ピアスのことか」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドは、すぐに得心がいったらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（それもそうよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "わざわざピアスを追い払ってから聞いているのだ。\n
彼が関係している話題だと見当をつけるのはたやすい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それに、ピアスのお友達召喚は有名だ。\n
ネズミばかりだが、立派な召喚術といえる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「ピアスの召喚って、あれはどういう特性のものなの？\n
確か、召喚って二種類あったわよね？」"

hide go_m_01_3
show go_m_01_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice gor_g0293
Gowland "「お、さすが優等生だな。\n
よく予習してある」"

hide go_m_01_5
show go_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice gor_g0294
Gowland "「召喚は、俺の次の授業あたりで扱おうと思っていたところだ。\n
だが……、あんたは待てそうにないし、説明してやるよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「ありがとう。\n
特別授業みたいね、ずるかしら」"

hide go_m_03_4
show go_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice gor_g0295
Gowland "「いいだろ、それくらいは。\n
ピアスの補習はそもそも俺が頼んだことだしな」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドは頷いて、説明を引き受けてくれた。\n
生徒のいなくなった放課後の教室で、特別講座だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（これ……、いつもは私が教える側なのよね。\n
我ながら、よく出来るなあ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "人を教えるのは難しいし、慣れていないと緊張もする。"

hide go_m_02_12

show m_pia3_1and3_4 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0296
Gowland "「あんたが言ったみたいに、召喚には二種類存在する。\n
第一種が、モンスターと契約を交わしてこちらに呼び出すタイプのものだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドが、教壇の上にすっと指を滑らせる。\n
迷いもなく書き上げるのは、複雑な魔法陣だ。"

play sound se_0496
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Gowland "「…………」"

play sound se_0375
$ flash_color("dark_red",.1)
$ flash_color("dark_red",.1)
hide m_pia3_1and3_4
show m_pia3_2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼の呪文が完成すると同時に、机の上に描かれた魔法陣がぼうっと燃え上がる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、その炎は机に延焼しようとはしない。\n
じりじりと魔法陣だけを熱く燃やしている。"

play sound se_0138
$ flash_color("dark_red",.1)
hide m_pia3_2
show m_pia3_3 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "中央に、めらりと炎が踊り、やがて緋色のトカゲへと変わった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「……サラマンダー？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "有名だが、それだけにかなり高位なモンスターだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "火噴きトカゲなんて愛称で呼ばれたりもしているが、気位が高く、ゴツゴツとした鱗に覆われた姿はトカゲというよりも小型のドラゴンのようにも見える。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_7")
T "（本物は初めて見たわ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なかなか見られるものではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0297
Gowland "「ああ、サラマンダーだ。\n
これが、第一種の召喚だな」"

play sound se_0468
play sound se_0735
hide m_pia3_3
show m_pia3_1and3_4 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「消えた……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice gor_g0298
Gowland "「はは、そりゃな。\n
召喚しといて、帰せなきゃ大変だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は簡単に言う。\n
出すのも引っ込めるのも自在だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_7")
T "（……さすが、シンフォニアの教師だわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "サラマンダークラスのモンスターを、ただ召喚の例に呼び出してみせるなんて普通では考えられない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "意味もなく呼ばれたモンスターが機嫌を損ね、マスターのいう事を聞かずに暴れるなんていうのも、よく聞く話だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0299
Gowland "「で、召喚の第二種が……」"

hide m_pia3_1and3_4
show m_pia3_5 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "つっと、ゴーランドが指先で新たな魔法陣を描く。\n
先ほどよりも簡単な、あっさりとした形状だ。"

play sound se_0496
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Gowland "「…………」"

play sound se_0138
hide m_pia3_5
show white onlayer master
with dis
hide white
show m_pia3_6 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「……っ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "息を飲んでしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "光の灯った魔法陣の中心。\n
そこに浮かび上がったのは「私」だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いかにも妖精といったふんわりとしたドレスを身にまとっているが、どこからどう見ても「私」。\n
[firstname]＝[familyname]だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女はふわふわと燐粉の零れる羽を羽ばたかせ、ひらひらくるくると私達の目の前を舞う。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（す、素直に感動していいのかどうか……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "可愛いし綺麗だとは思うのだけれども、相手はミニチュアサイズとはいえ、「私」と同じ姿をしている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「ご、ゴーランド！？\n
これ、どういうこと！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_5")
voice gor_g0300
Gowland "「はは、これが第二種の召喚だ。\n
己の魔力自体に、姿を与えて使役する」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（……ってことは）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「あなたが、わざとこういう姿にしたってこと？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_3")
voice gor_g0301
Gowland "「おう。\n
そのほうがピンとくるかと思ってよ」"

play sound se_0138
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちょいとゴーランドが差し出した手指の上。\n
文鳥のように妖精が留まる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "見れば見るほどに、私にそっくりだ。\n
静止しているとよく分かる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「……なんだか、気色悪いわ。\n
自分のミニチュアなんて」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice gor_g0302
Gowland "「そう言うなって。\n
分かりやすく説明しようと思って、わざわざあんたの形を再現してみたんだからさ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_8")
T "「これって、術者の頭でイメージを組み立てるんでしょう？\n
……よくここまで忠実に描けたわね」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_8")
voice gor_g0303
Gowland "「ああ、任せろ。\n
スリーサイズの比率まで一致させている自信が……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_9")
T "「…………」"

play sound se_0107
camera at hpunch
camera at vpunch
hide m_pia3_6 ##instant

show go_m_02_4 at center with dis
#special anime hit center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_9")
voice gor_g0304
Gowland "「あだああっ！！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "見直したのが間違いだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……セクハラ教師」"

hide go_m_02_4
show go_m_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice gor_g0305
Gowland "「な、何も殴ることねえだろうによー。\n
なあ、おまえもそう思うだろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
Yousei "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "妖精の形をしたものが、ゴーランドに相槌を打つようにこくこくと顎を引く。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（高度な技術を使った、お人形遊びね……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "思考は私と一致しない。\n
冷たい私の視線に、ゴーランドは苦笑しながら、もう一度呪文を唱えた。"

play sound se_0496
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「…………」"

play sound se_0138
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふわりと溢れた光の中、妖精スタイルの私がうっすらと光の粒子に飲まれ、消えていく。"

hide go_m_03_1
show go_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0306
Gowland "「で、あんたが俺に聞きたいのは……。\n
ピアスの奴の召喚がどっちの分類か、ってことか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "再び、優秀なシンフォニアの教師の顔に戻られてしまった。\n
こうなると、素直になるしかない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……そうよ。\n
あのネズミ達って、ピアスの影から溢れ出てくるでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どこに収納できているのか、というほど大量のネズミをピアスは召喚してみせる。\n
それがずっと不思議だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "大量のネズミと契約を交わしているのか、それとも魔力をネズミの形にして使役しているのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "召喚には二種類あると本で読んで以来、気になっていたのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その種類さえ分かれば、ピアスの能力をアップさせることや応用することも可能かもしれない。"

hide go_m_02_12
show go_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0307
Gowland "「あれはおそらく……、第二種だな。\n
普通のネズミに、契約できるだけの知能があるとは思えねえ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「……でも、ピアスはネズミの言葉を解するのよ？\n
それで、なんとかなるのかもしれないわ」"

hide go_m_03_2
show go_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice gor_g0308
Gowland "「ネズミの言葉が分かるんじゃない。\n
ピアスはネズミの意思……、感情を読んでいるだけだ」"

hide go_m_01_11
show go_m_03_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice gor_g0309
Gowland "「ネズミには、それだけ高度なやりとりをするだけの頭はねえよ」"

hide go_m_03_12
show go_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice gor_g0309_5
Gowland "「ピアスの出すアレは、ネズミ好きのネズミ男が作り上げた、ネズミの形をした魔力塊だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_10")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "改めてそう言われると、ピアスもすごい。\n
そして、私のミニチュア同様に不気味でもある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あれほど多くのネズミを魔力で形作り、その小さな一つ一つを本物そっくりに動かし、操るなんて。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「優秀なのね、ピアスって……」"

hide go_m_01_10
show go_m_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice gor_g0310
Gowland "「シンフォニアに入れるくらいだ。\n
そもそも、馬鹿なわけがないんだよ」"

hide go_m_03_1
show go_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice gor_g0311
Gowland "「……あんたも分かってんだろ？\n
味方してるみたいだしな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_13")
T "「ああ、知っていたの。\n
だって、悔しいし、もったいないんだもの」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_2")
T "「力があるのに馬鹿にされるままで。\n
ピアスは、それでいいのかしら」"

hide go_m_03_4
show go_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_2")
voice gor_g0312
Gowland "「あいつ自身は召喚がどういうことなのかも、理解してねえ。\n
呼んだら来てくれる心強いお友達、っていった程度の認識だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……そう」"

hide go_m_01_6
show go_m_03_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice gor_g0313
Gowland "「そこまで、無欲だから召喚しやすいのかもしれないけどな。\n
召喚師……、特に動物の使役は、純粋な奴のほうがいいらしいから」"

hide go_m_03_12
show go_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice gor_g0314
Gowland "「第二種で、実際の生き物じゃなくても、そういうのは影響するらしい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「なるほど。\n
無邪気なほうが心を通わせやすそうだものね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふむふむと頷きながら、私は顎先を撫でた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「それじゃあ、イベントに乗じて……」"

hide go_m_02_10
show go_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
voice gor_g0315
Gowland "「？\n
……あんた、何を企んでいるんだ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、今日一日周囲に言われてきた言葉を、仕返しのようにゴーランドに向けて言い返した。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_2")
T "「内緒、よ」"

hide go_m_03_11
##[chara1 PAY ATTENTION="false"]
with dis
$ hi_mes()

scene bg10_sb_day
with stripe_l_medium

scene bg_map_day
with stripe_l_long
##endmemory
jump gakuen_pierce4
