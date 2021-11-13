
scene bg_map_day
with dis
label gakuen_friend_castle:
$ gakuen_friend_castle_seen = True
$ clockanim()


scene bg20_gd_day
with dis

play music gallery_front_day_p_wam

scene bg_par15_rg_ros_day with Dissolve(1.2)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その日、私は赤薔薇寮を訪れていた。"
if place_of_stay == "Hatter":
    jump gakuen_friend_castle1b
if place_of_stay == "Amuse":
    jump gakuen_friend_castle1c
if place_of_stay == "Tower":
    jump gakuen_friend_castle1d
label gakuen_friend_castle1b:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドに頼まれ、書類を届けに来たのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は不良生徒の一員になるつもりはないが、全員が素行不良というわけでもない。\n
しかし、帽子屋寮に住む者として、寮長の頼みを聞くべきだろう。"

jump gakuen_friend_castle2
label gakuen_friend_castle1c:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドに頼まれ、書類を届けに来たのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "担任ということもあってか、用事を言付かることも多い。"

jump gakuen_friend_castle2
label gakuen_friend_castle1d:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスに頼まれ、書類を届けに来たのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "別に保健委員や風紀委員になったわけでも、塔の中で何か役職についているわけでもないのだが、寮生として手伝うことも多い。"

jump gakuen_friend_castle2
label gakuen_friend_castle2:

scene bg25_rr_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなわけで、今回、書類の配達を引き受けた。\n
届け先は、自治会室だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（久しぶりだわ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最初に、自治会員になるために訪れて以来だ。普段あまり足を踏み入れることのない他寮というのは、入学してからしばらく経った今でも目新しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自寮という比較対象を得た分、前よりも赤薔薇寮らしさというのがよく分かる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「確か、ここ……、よね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "誰に確かめるでもなく呟いて、私は自治会室の扉をノックした。"

play sound se_0302

play music drawingroom_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0400
Peter "「……開いていますよ。\n
誰ですか？」"

if place_of_stay == "Hatter":
    jump gakuen_friend_castle3b
if place_of_stay == "Amuse":
    jump gakuen_friend_castle3c
if place_of_stay == "Tower":
    jump gakuen_friend_castle3d
label gakuen_friend_castle3b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「私、[firstname]＝[familyname]よ。\n
ブラッドに頼まれて書類を届けにきたの」"

jump gakuen_friend_castle4
label gakuen_friend_castle3c:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「私、[firstname]＝[familyname]よ。\n
ゴーランドに頼まれて書類を届けにきたの」"

jump gakuen_friend_castle4
label gakuen_friend_castle3d:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「私、[firstname]＝[familyname]よ。\n
ユリウスに頼まれて書類を届けにきたの」"

jump gakuen_friend_castle4
label gakuen_friend_castle4:
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
Peter "「！！！！！」"

play sound se_0285

scene bg_par16_rs_ros_day
with dis

show per_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice pet_g0401
Peter "「[firstname]！！！\n
ああ、やっと赤薔薇寮に来てくださる気になったんですね！！？」"

play sound se_0051
hide per_m_02_5
show per_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice pet_g0402
Peter "「嬉しいですよ、さあ、さっそくあなたの新しいお部屋へご案内致します！\n
荷物は、エース君にでも取ってきてもらいましょう！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「ねえ、ペーター。\n
……あなた、私の話を聞いていた？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "聞いちゃあいないんだろうな、と、分かりつつ……。"
if place_of_stay == "Hatter":
    jump gakuen_friend_castle5b
if place_of_stay == "Amuse":
    jump gakuen_friend_castle5c
if place_of_stay == "Tower":
    jump gakuen_friend_castle5d

label gakuen_friend_castle5b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_10")
T "「私、書類を届けにきたって言わなかったかしら。\n
ブラッドから預かってきたの」"

jump gakuen_friend_castle6
label gakuen_friend_castle5c:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_10")
T "「私、書類を届けにきたって言わなかったかしら。\n
ゴーランドから預かってきたの」"

jump gakuen_friend_castle6
label gakuen_friend_castle5d:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_10")
T "「私、書類を届けにきたって言わなかったかしら。\n
ユリウスから預かってきたの」"

jump gakuen_friend_castle6
label gakuen_friend_castle6:
hide per_m_03_4
show per_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_10")
voice pet_g0403
Peter "「ええ、ですから転寮届けでしょう？\n
そんなの受理に決まっていますよ！ねえ、会長！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "相変わらず、私の幼馴染には言葉が通じない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "助けを求めるように、ちらりと視線を流せばビバルディは頭痛を覚えたようにぐりぐりとこめかみをもみしだいていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースは笑顔だ。\n
こちらも、以前会ったときと変わらず、無駄に爽やか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "好印象を演出しそうなものなのに、どこか空々しさを覚えるのも一緒だ。"


show viv_m_03_11 at center
with dis
hide per_m_02_1

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_g0285
Vivaldi "「そこのホワイトは放っておけ。\n
相手にすると頭がおかしくなるよ、と言いたいところじゃが……」"

hide viv_m_03_11
show viv_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_g0286
Vivaldi "「おまえの転寮届けであったなら、と、わらわも思うよ。\n
どうだ、越してくる気はないか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「もう、ビバルディまで……。\n
ここが嫌だから移動してこないわけじゃないのよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「ただ、一度決めたことを簡単に覆してしまうことが嫌なの。\n
今の寮にも慣れてきたし……、分かってくれるでしょう？」"

hide viv_m_01_2
show viv_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice viv_g0287
Vivaldi "「頑固な子じゃ。\n
どれ、およこし」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "赤く塗られた爪先を翻して、ビバルディが私へと手を差し出す。"

play sound se_0472
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「はい、確かに渡したわ」"

hide viv_m_01_4
if place_of_stay == "Hatter":
    jump gakuen_friend_castle7b
if place_of_stay == "Amuse":
    jump gakuen_friend_castle7c
if place_of_stay == "Tower":
    jump gakuen_friend_castle7d
label gakuen_friend_castle7b:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "封を押されている面を上にして、ブラッドから預かってきた封筒を渡した。\n
封印にはブラッドが好んで使う、帽子を象った紋章が押されている。"

jump gakuen_friend_castle8
label gakuen_friend_castle7c:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "封を押されている面を上にして、ゴーランドから預かってきた封筒を渡した。\n
封印にはゴーランドらしく音符をあしらった紋章で印がしっかりと押されている。"

jump gakuen_friend_castle8
label gakuen_friend_castle7d:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "封を押されている面を上にして、ユリウスから預かってきた封筒を渡した。\n
封印にはクローバーをモチーフにした印がしっかりと押されている。"

jump gakuen_friend_castle8
label gakuen_friend_castle8:
play sound se_0740

show white with Dissolve(.1)
hide white

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ビバルディの赤い爪先がその紋章に触れた瞬間、紋章はうっすらと光を放ちながら消えていった。\n
彼女はさっそく、中を改める。"
if place_of_stay == "Hatter":
    jump gakuen_friend_castle9b
if place_of_stay == "Amuse":
    jump gakuen_friend_castle9c
if place_of_stay == "Tower":
    jump gakuen_friend_castle9d
label gakuen_friend_castle9b:

show viv_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_g0288
Vivaldi "「……ふむ。\n
新たな催しものの提案……、じゃな」"

hide viv_m_01_4
show viv_m_01_4 at left
with dis

show ace_m_01_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0492
Ace "「ああ、また帽子屋寮の人達と遊ぶんですか？\n
それは楽しみだなあ」"

jump gakuen_friend_castle10
label gakuen_friend_castle9c:
hide viv_m_01_4
show viv_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_g0288
Vivaldi "「……ふむ。\n
新たな催しものの提案……、じゃな」"

hide viv_m_01_4
show viv_m_01_4 at left
with dis
hide ace_m_01_4
show ace_m_01_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0494
Ace "「ああ、今度は遊園地寮の人達と遊ぶんですか？\n
それは楽しみだなあ」"

jump gakuen_friend_castle10
label gakuen_friend_castle9d:
hide viv_m_01_4
show viv_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_g0289
Vivaldi "「……ふむ。\n
以前提出した、決闘状……、もとい、催しものの申請にようやく許可が下りたようじゃな」"

hide viv_m_01_3
show viv_m_01_3 at left
with dis
hide ace_m_01_4
show ace_m_01_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0493
Ace "「ああ、今度は塔の人達と遊ぶんですか？\n
それは楽しみだなあ、トカゲさんとやりあうのが楽しみだぜ！」"

jump gakuen_friend_castle10
label gakuen_friend_castle10:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「催しもの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何かイベントだろうか。\n
特に校内で行事があるというような話は聞いていない。"


show per_m_02_8 at center
with dis
hide viv_m_01_3

hide ace_m_01_4

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0404
Peter "「ああ、違いますよ、[firstname]。\n
勘違いしないでくださいね？」"

hide per_m_02_8
show per_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0405
Peter "「学校行事として何かがあるわけじゃないんです。\n
この人たちが、勝手気ままに寮対抗でトラブルを起こそうってだけなんですよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_10")
T "「ト、トラブル？\n
嫌よ、私そんなことの片棒を担がされるのは」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この書類をビバルディへと届けたのは私だ。\n
それが原因でトラブルが起きるというのは困る。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私に彼女を止めることが出来るかといったらそれは不可能な気がしてならないわけだが、だからといって見過ごすわけにはいかない。"


show viv_m_01_4 at center
with dis
hide per_m_01_4

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_g0290
Vivaldi "「……ふむ。\n
今回はチェスでもしようかと思っておったのだが、おまえは反対するか？」"
if place_of_stay == "Hatter":
    jump gakuen_friend_castle11b
if place_of_stay == "Amuse":
    jump gakuen_friend_castle11c
if place_of_stay == "Tower":
    jump gakuen_friend_castle11d
label gakuen_friend_castle11b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「チェス？\n
ブラッドとチェスをするの？」"

jump gakuen_friend_castle12
label gakuen_friend_castle11c:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「チェス？\n
ゴーランドとチェスをするの？」"

jump gakuen_friend_castle12
label gakuen_friend_castle11d:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「チェス？\n
ユリウスとチェスをするの？」"

jump gakuen_friend_castle12
label gakuen_friend_castle12:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "チェスとは、拍子抜け。\n
もちろん、止める必要性も感じない。"

hide viv_m_01_4
show viv_m_02_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_g0291
Vivaldi "「ああ、チェスだ。\n
……おいで、わらわのお気に入りのチェスボードを見せてあげよう」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_15")
T "「本当に？\n
嬉しいわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "チェスというボードゲームの道具には、遊戯道具という意味以上に美術品の価値が付加されていることが多々ある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "象牙を削って作られた駒や、螺鈿のはられたボードというようなものは美術館などで展示されているのを見かけるぐらいだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_14")
T "（ビバルディのお気に入りのボードだなんて、一体どんなものなのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "きっと彼女に似合う華やかなものだろう。"

hide viv_m_02_9
show viv_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_g0292
Vivaldi "「おまえも、チェスはやるのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「そんなに強いわけじゃないけれど、ルールぐらいは知っているわ。\n
家族で対戦する程度」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_14")
T "（なかなか勝てなくて……。\n
それが悔しくて、何度もねだったっけ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "チェスというのは純粋な頭脳戦だ。\n
互いの知恵を比べあい、いかに相手のキングを追い詰めるかを考えるゲームだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "母や姉に比べたら私はまだまだ子供で、その年齢差だけで私が勝てない理由は充分だった。それでも負けず嫌いな私は、何度も挑んだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_1")
T "（久しぶりに、してみたいな）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今ならば、昔よりももっとまともな手が打てるだろうか。\n
そんなことを考えていた私を、ビバルディが手招いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その先は、窓際だ。"

play sound se_0776
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……？？？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "チェスボードを見せてくれるのではなかったのだろうか。\n
窓の外を見下ろすビバルディの横に並ぶ。"


hide viv_m_02_10


scene bg_par15_rg_ros_day
with dis

play music view_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "眼下に広がるのは薔薇の生垣が迷路のように並ぶ中庭だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_g0293
Vivaldi "「よく見ておれ。\n
これがわらわのお気に入りのボードじゃ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女が手にしていた豪奢な杖をすっと持ち上げる。"

play sound se_0707
camera at hpunch
camera at vpunch
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_6")
T "「……っ、な……！？」"

play sound se_0051



scene bg_par16_rs_ros_day
with dis

show per_m_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_6")
voice pet_g0406
Peter "「大丈夫ですよ、[firstname]。\n
あなたには指一本触れさせませんからね！」"

hide per_m_03_1
show per_m_03_1 at left
with dis

show ace_m_03_10 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_6")
voice ace_g0495
Ace "「はは、何さりげなく彼女の肩を抱いているんだよ、ペーターさん。\n
指一本どころか触りまくっているじゃないか」"

hide per_m_03_1
show per_m_01_9 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_6")
voice pet_g0407
Peter "「僕はいいんです！」"

hide ace_m_03_10
show ace_m_03_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_6")
voice ace_g0496
Ace "「いやいや。\n
よくないだろ」"

play sound se_0016
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつのまにか背後にいたペーターが私の肩を抱き、その手を同じくいつのまにか背後にやってきていたエースが朗らかに笑いながらひっぺがす。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この二人は何かと争いたがる。\n
間に立つというより、攻防に巻き込まれるようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、それを気にしていられないだけの光景が私の眼下では繰り広げられていた。"

hide per_m_01_9

hide ace_m_03_3


scene m_cut_siro_friend
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まるで生き物のように身をくねらせて、薔薇の生垣が中庭を逃げ惑う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やがて障害物のなくなった中庭の中央に、巨大なリングめいた石版が浮かび上がった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_7")
T "「まさか……、これチェスボードなの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "信じられないくらい巨大なサイズだが、升目の数からしてチェスボードだろう。"

with dis
$ hi_mes()

scene m_cut_siro_friend_u
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_g0294
Vivaldi "「ふふ、見事だろう？\n
どれ、駒も配置してやろう」"

play sound se_0712
pause .5
play sound se_0578
camera at hpunch
camera at vpunch
pause .5
play sound se_0578
camera at hpunch
camera at vpunch
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ビバルディの杖が唸りをあげると同時に、ずーんずーんっと腹に響く低い音が木霊した。そして、石版のフィールド内に、同じく石造りの駒が出現した。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "駒といっても、等身大ほどの大きさのある石像だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_g0295
Vivaldi "「知っておったか？\n
もともとチェスというのは、戦争を模したゲームなのじゃ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ビバルディの声は酷く楽しげだ。\n
わくわくと弾む様は無邪気ともいえる。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_g0296
Vivaldi "「エース、ホワイト。\n
この子に見せておやり」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0497
Ace "「おおせのままに。\n
[firstname]、見ていてくれよな」"

play sound se_0277
pause .2
play sound se_0125
pause .3

show ace_m_03_10 at center
with dis
play sound se_0073
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0408
Peter "「エース君だけにいいところを見させるわけにはいきません！\n
僕も行きますよ！」"

play sound se_0277
pause .2
play sound se_0125
pause .3
hide ace_m_03_10
show ace_m_03_10 at left
with dis

show per_m_02_10 at right
with dis
play sound se_0073
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ビバルディがすいっと身を引くのと同時に、指名された二人が窓を開け放つ。\n
そして、そのままそこから中庭へと飛び降りていった。"

hide ace_m_03_10

hide per_m_02_10


scene m_cut_siro_friend
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_7")
T "（……まさか）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "大体予想がつくような気がする。\n
実物大の、巨大なチェスボード。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "戦争を模したのだというこのゲーム。"

play sound se_0651
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "馬のいななく声がして、はっとする。\n
そちらへと目をやれば、エースが黒毛の馬に跨ったところだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "さきほどまでは実物大の胸像に過ぎなかった馬が、エースという騎手を得て息づいている。"

play sound se_0413
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "続いて響いたのは、金属を打ち鳴らす涼やかな音だった。先ほどまで白のビショップがいた位置に、巨大な錫杖を片手に携えたペーターが立っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_g0297
Vivaldi "「始めよ！」"


scene m_cut_siro_friend_u
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "凛、と響く声音でビバルディがそう宣言すると、戦争は始まった。石造りのポーンたちがそれぞれ前に出ては衝突し、互いに切り結んでは砕けていく。"

play sound se_0578
camera at hpunch
camera at vpunch
play sound se_0677
##special anime"kiseki01"loop="false"time="1000"]
play sound se_0413
$ flash(.2)
play sound se_0658
camera at hpunch
camera at vpunch
play sound se_0651
pause .5
play sound se_0652
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その最中を黒毛の馬の胸像に跨り駆け抜けるのはエースで、錫杖を片手に次々と敵のポーンを粉砕しながら突き進んでいくのがペーターだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その動きには、私の知るチェスの法則が申し訳程度には反映されている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースはあちこち飛び回り、ペーターは斜めに、盤上を縦横無尽に駆け回っては敵を打ち倒していく。"

play sound se_0657
camera at hpunch
camera at vpunch
play sound se_0578
camera at hpunch
camera at vpunch
play sound se_0677
##special anime"kiseki03"loop="false"time="1000"]
play sound se_0413
$ flash(.2)
$ flash(.2)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それはもはやチェスでなく、本物の戦争のようだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_g0498
Ace "「ペーターさんって、クイーンも似合いそうだよな！\n
ははは、ビショップなんて敬虔な柄じゃないだろ？」"

play sound se_0651
pause .5
play sound se_0652
pause .5
play sound se_0677
##special anime"kiseki02"loop="false"time="1000"]
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0409
Peter "「ふふふ、君こそ騎士なんて柄じゃないでしょうに。\n
馬上の騎士を気取ったところで、その性根が腐っていますからね！」"

play sound se_0413
$ flash(.2)
play sound se_0656
camera at hpunch
camera at vpunch
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ははは、ふふふ、と。\n
不気味に低い笑いをあげながら、二人は盤上でついには対峙する。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースは馬上で剣を構え、ペーターは長い錫杖を構えた。"


scene bg_par16_rs_ros_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……ねえ、ビバルディ。\n
チェスってこういうゲームだったかしら」"

play sound se_0657 volume .6
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本来なら、こんな力任せなゲームではなく、もっとプレイヤーが頭を使って駒を動かし、相手のキングを追い詰めていくゲームだったはずだ。"


show viv_m_01_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_g0298
Vivaldi "「仕方あるまい。\n
現在、このゲームにプレイヤーはおらぬ」"

play sound se_0658 volume .6
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……プレイヤーがいない？」"

hide viv_m_01_12
show viv_m_01_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice viv_g0299
Vivaldi "「誰も駒に命令を下さぬ。\n
王不在のゲームなど、この程度のもの」"
if place_of_stay == "Hatter":
    jump gakuen_friend_castle13b
if place_of_stay == "Amuse":
    jump gakuen_friend_castle13c
if place_of_stay == "Tower":
    jump gakuen_friend_castle13d
label gakuen_friend_castle13b:
hide viv_m_01_13
show viv_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice viv_g0300
Vivaldi "「帽子屋と遊ぶ折には、もちろんわらわがキングとして命令を下すよ。\n
ああ……、そうだな……」"

play sound se_0682 volume .6
hide viv_m_01_11
show viv_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice viv_g0301
Vivaldi "「[firstname]、おまえ、わらわのクイーンになる気はないか？\n
帽子屋のところと人数が合わぬ」"

jump gakuen_friend_castle14
label gakuen_friend_castle13c:
hide viv_m_01_4
show viv_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice viv_g0304
Vivaldi "「ゴーランドと遊ぶ折には、もちろんわらわがキングとして命令を下すよ。\n
ああ……、そうだな……」"

play sound se_0682 volume .6
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice viv_g0303
Vivaldi "「[firstname]、おまえ、わらわのクイーンになる気はないか？\n
おまえも加わりたいだろう？」"

jump gakuen_friend_castle14
label gakuen_friend_castle13d:
hide viv_m_01_11
show viv_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice viv_g0302
Vivaldi "「風紀委員長と遊ぶ折には、もちろんわらわがキングとして命令を下すよ。\n
ああ……、そうだな……」"

play sound se_0682 volume .6
hide viv_m_01_11
show viv_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice viv_g0303
Vivaldi "「[firstname]、おまえ、わらわのクイーンになる気はないか？\n
おまえも加わりたいだろう？」"

jump gakuen_friend_castle14
label gakuen_friend_castle14:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_6")
T "「ええっ？」"

play sound se_0656 volume .6
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ビバルディがクイーンというのは、響きからしても合う。\n
私がクイーンとなると……、微妙だ。"

play sound se_0683 volume .6
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "危険そうなゲームだということもあり、参加するには躊躇ってしまう。\n
中庭からは、打ち合う剣と錫杖の鋭い音が響き渡っている。"
if place_of_stay == "Hatter":
    jump gakuen_friend_castle15b
if place_of_stay == "Amuse":
    jump gakuen_friend_castle15c
if place_of_stay == "Tower":
    jump gakuen_friend_castle15d
label gakuen_friend_castle15b:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "相手が帽子屋寮だとした場合、当然キングはブラッドだろう。"

play sound se_0683 volume .6
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "キャスティングとしては、ルークがエリオットで、双子がビショップのそれぞれといったところか。"

jump gakuen_friend_castle16
label gakuen_friend_castle15c:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "相手が遊園地寮だとした場合、当然キングはゴーランドだろう。"

play sound se_0683 volume .6
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "キャスティングとしては、ナイトがボリスで、ピアスがルークかビショップかのどちらかといったところか。"

jump gakuen_friend_castle16
label gakuen_friend_castle15d:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "相手が塔だとした場合、当然キングはナイトメアだろう。"

play sound se_0683 volume .6
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "キャスティングとしては、ナイトがグレイで、ユリウスがルークかビショップかのどちらかといったところか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……そもそもユリウスが参加するかどうかが危ういというのは置いておくとして。\n
申請の受理と、自分の参加は別の話だ、とか言って拒否しそうだ。"

jump gakuen_friend_castle16
label gakuen_friend_castle16:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……誰に当たったとしても、勝てる気がしない）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「無理。\n
即死するのが目に見えているわ」"

play sound se_0656 volume .6
hide viv_m_01_4
show viv_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice viv_g0305
Vivaldi "「ふふ、大丈夫。\n
わらわが守ってあげる」"

play sound se_0551
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "するりと肩口にビバルディの腕がまわる。\n
華やかな薔薇の香りがふわりと鼻先を掠めた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "甘い匂いだ。\n
そして、同じだけ声音も甘い。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「……でも、普通、逆でしょう？\n
クイーンがキングを守るものだわ」"

hide viv_m_03_2
show viv_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice viv_g0306
Vivaldi "「だが、わらわはおまえを守りたい。\n
ルールなど、変えてしまえばよいのだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_6")
T "「……それなら、最初から私がキングになればよくない？\n
ビバルディ、あなたにクイーンはきっとはまり役だわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "日頃から「赤薔薇の女王」の二つ名をほしいままにしている彼女だ。\n
きっとクイーンの役が似合うことだろう。"
if place_of_stay == "Hatter":
    jump gakuen_friend_castle17b
if place_of_stay == "Amuse":
    jump gakuen_friend_castle17c
if place_of_stay == "Tower":
    jump gakuen_friend_castle17d
label gakuen_friend_castle17b:
hide viv_m_03_10
show viv_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_g0307
Vivaldi "「おまえの命令ならば、聞いてやってもかまわぬが……。\n
相手は、あの性悪のブラッド＝デュプレだぞ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「……無理ね。\n
即死でなくても、無理」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "同寮だからこそ、ブラッド＝デュプレという男のことはそれなりに心得ている。\n
悪趣味で、気紛れな男ではあるが、たいそう頭のいい男でもあるのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（あの人と対峙するなんて、冗談じゃないわ）"

jump gakuen_friend_castle18
label gakuen_friend_castle17c:
hide viv_m_01_4
show viv_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_g0309
Vivaldi "「おまえの命令ならば、聞いてやってもかまわぬが……。\n
相手は腐ってもシンフォニアの教師、ゴーランドだぞ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「……全力で遠慮しておくわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "担任だからこそ、ゴーランドという男のことはそれなりに心得ている。\n
陽気で、気のいい男ではあるが、実力はあるのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それに傍らで補佐するであろうボリスの存在も馬鹿に出来ない。\n
寮長なのだから、絶対に参戦してくるはず。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（ただでさえ、お祭り好きなんだし……。\n
大変なことになりそう）"

jump gakuen_friend_castle18
label gakuen_friend_castle17d:
hide viv_m_01_4
show viv_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_g0308
Vivaldi "「おまえの命令ならば、聞いてやってもかまわぬが……。\n
まあ、あそこで指揮したがるのはナイトメアだからな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「……なんとなく勝てそうな気がするから、かえって困るわよね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアはそれなりに実力を持つシンフォニアの職員だ。\n
病弱で、貧弱……、だが実力はあるはず。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それに、傍らで補佐するであろうグレイやユリウスの存在は馬鹿に出来ない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（というか、倒したら倒したで大変そう。\n
寝込んだら、周囲のほうがいい迷惑だろうし……）"

jump gakuen_friend_castle18
label gakuen_friend_castle18:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "駒として戦うのも無理だが、そんな彼らを相手に頭脳戦を繰り広げられる気もしない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「私は、観客でいいわ。\n
あなた達の戦いを見届ける」"

hide viv_m_01_4


show ace_m_01_4 at center
with dis

scene bg_par15_rg_ros_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice ace_g0499
Ace "「それなら、君、賞品になっちゃうといい。\n
俺達が勝ったらさ、赤薔薇寮においでよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_6")
T "「！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "心臓に悪い。\n
抜き身の剣を片手にぶら下げて、エースが窓辺に戻ってきていた。"

hide ace_m_01_4


scene m_cut_siro_friend2_u
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "チェスもどきの戦争はどうなったのかと、中庭を覗いてみる。\n
そこには、打ち砕かれた石造の残骸だけが転がっていた。"


scene m_cut_siro_friend2
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_10")
T "（……無惨だわ）"


scene bg_par15_rg_ros_day
with dis

show ace_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_10")
voice ace_g0500
Ace "「はは、気付いたらお互いのキングが死んじゃってたんだよな。\n
馬がいきなり崩壊するから、何かと思ったぜ！」"

hide ace_m_02_4
show ace_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_10")
voice ace_g0501
Ace "「ペーターさんと遊ぶのが楽しくて、キングを守るの忘れていたのが致命的だよな！\n
遊びすぎはよくないね、ペーターさん！」"

hide ace_m_02_1
show ace_m_02_1 at left
with dis

show per_m_01_14 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_10")
voice pet_g0410
Peter "「違いますよ、僕はエース君のように無能じゃあありません。\n
守れなかったのではなく、最初から守る気がなかったんですよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_17")
T "「……そっちのほうが問題じゃない？」"

hide per_m_01_14
show per_m_03_4 at center
with dis
hide ace_m_02_1

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_17")
voice pet_g0411
Peter "「ですけど、[firstname]、あなたがキング、もしくはクイーンならば！\n
僕は命をかけてでもあなたを守り抜いて見せますよ……！！」"
if place_of_stay == "Hatter":
    jump gakuen_friend_castle19b
if place_of_stay == "Amuse":
    jump gakuen_friend_castle19c
if place_of_stay == "Tower":
    jump gakuen_friend_castle19d
label gakuen_friend_castle19b:
hide per_m_03_4
show per_m_02_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_17")
voice pet_g0412
Peter "「ああでも、あなたが賞品というのも捨てがたいです……！\n
あんなならず者どもの巣窟、あなたには不似合すぎる！」"

jump gakuen_friend_castle20
label gakuen_friend_castle19c:
hide per_m_02_13
show per_m_02_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_17")
voice pet_g0414
Peter "「ああでも、あなたが賞品というのも捨てがたいです……！\n
あんなやかましいだけの不衛生な場所、あなたには不似合いです！」"

jump gakuen_friend_castle20
label gakuen_friend_castle19d:
hide per_m_02_13
show per_m_02_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_17")
voice pet_g0413
Peter "「ああでも、あなたが賞品というのも捨てがたいです……！\n
あんなしめっぽくって不衛生な場所、あなたには不似合いです！」"

jump gakuen_friend_castle20
label gakuen_friend_castle20:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "同じく窓辺に戻ってきたペーターが、熱っぽく力説する。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "賞品にしろ、クイーンもしくはキングにしろ、私が巻き込まれるのは決定しているらしいのがなんとも不穏だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「言っておくけれど……。\n
私は、参加もしないし賞品になるつもりもないわよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「言ったでしょう？\n
住む場所は決めたんだから、そう簡単には引っ越したりしないわ」"

hide per_m_02_13


show viv_m_01_7 at center
with dis

scene bg_par16_rs_ros_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice viv_g0310
Vivaldi "「……むぅ。\n
おまえは頑固だのう」"
if place_of_stay == "Hatter":
    jump gakuen_friend_castle21b
if place_of_stay == "Amuse":
    jump gakuen_friend_castle21c
if place_of_stay == "Tower":
    jump gakuen_friend_castle21d
label gakuen_friend_castle21b:
hide viv_m_01_7
show viv_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice viv_g0311
Vivaldi "「まあいい、おまえがこの遊びを好かぬというのならまた別のを考えよう。\n
帽子屋と遊ぶ約束なぞ、いつになったとして構わぬ」"

jump gakuen_friend_castle22
label gakuen_friend_castle21c:
hide viv_m_01_4
show viv_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice viv_g0313
Vivaldi "「まあいい、おまえがこの遊びを好かぬというのならまた別のを考えよう。\n
まあ、あの男のリサイタル以外なら何でもいいのじゃ」"

jump gakuen_friend_castle22
label gakuen_friend_castle21d:
hide viv_m_01_4
show viv_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice viv_g0312
Vivaldi "「まあいい、おまえがこの遊びを好かぬというのならまた別のを考えよう。\n
せっかく風紀委員長より許可を得たわけだが、構わぬ」"

jump gakuen_friend_castle22
label gakuen_friend_castle22:
play sound se_0125
pause .3
play sound se_0707
hide viv_m_01_4


scene m_cut_siro_friend2_u
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "飽きた、というように彼女が手にしている杖をひらめかせる。"


scene bg_par15_rg_ros_day with Dissolve(1.5)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "外から再び地響きの音がした。\n
チェスボードが消え、赤薔薇の生垣が中庭に戻っていく。"


scene bg_par16_rs_ros_day with dis ##PAY ATTENTION="true"]

show viv_m_03_10 at center
with dis

play music drawingroom_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_g0314
Vivaldi "「さあ、[firstname]。\n
わらわと遊んでくれぬというのなら、せめて茶会に付き合っておくれ」"

hide viv_m_03_10
show viv_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_g0315
Vivaldi "「美味しい茶菓子も用意しよう。\n
まだ、帰らぬだろう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_2")
T "「……ええ。\n
まだ帰らないわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_7")
T "（大掛かりなゲームなんかなくても……、いいえ、ないほうが寛げるもの）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "甘えるようなビバルディの言葉に、今度は頷いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "お茶会にならいくらでも付き合おう。\n
争いよりもよほどいい。"

hide viv_m_01_3
##[chara2 PAY ATTENTION="false"]
with dis
$ hi_mes()

scene bg_par15_rg_ros_day
with stripe_l_medium

scene bg_map_day
with stripe_l_long
jump gakuen_friend_end
