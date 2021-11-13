
scene bg_map_day
with dis
label gakuen_friend_hatter:
$ clockanim()


scene bg20_gd_day
with dis

play music gallery_front_day_p_wam

scene bg_par15_rg_hat_day with Dissolve(1.2)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その日、私は帽子屋寮に訪れていた。"
if place_of_stay == "Castle":
    jump gakuen_friend_hatter1a
if place_of_stay == "Amuse":
    jump gakuen_friend_hatter1c
if place_of_stay == "Tower":
    jump gakuen_friend_hatter1d
label gakuen_friend_hatter1a:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ビバルディに頼まれ、書類を届けにきたのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は自治会の役員になったわけではないのだが、それでも赤薔薇寮に住む者として、そして自治会員として、無理のない範囲で手伝おうとは思っている。"

jump gakuen_friend_hatter2
label gakuen_friend_hatter1c:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドに頼まれ、書類を届けにきたのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "担任ということもあってか、用事を言付かることも多い。"

jump gakuen_friend_hatter2
label gakuen_friend_hatter1d:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスに頼まれ、書類を届けにきたのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "別に保健委員や風紀委員になったわけでも、塔の中で何か役職についているわけでもないのだが、寮生として手伝うことも多い。"

jump gakuen_friend_hatter2
label gakuen_friend_hatter2:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなわけで、今回、書類の配達を引き受けた。\n
届け先は、帽子屋寮だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（久しぶりだわ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "入学してからしばらく経った今でも新鮮だ。\n
門の辺りに差し掛かると、警備担当だという双子の姿が目に入った。"


show dee_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0509
Dee "「あ、お姉さんだ！\n
どうしたのお姉さん、お引越し？」"
if place_of_stay == "Castle":
    jump gakuen_friend_hatter3a
if place_of_stay == "Amuse":
    jump gakuen_friend_hatter3c
if place_of_stay == "Tower":
    jump gakuen_friend_hatter3d
label gakuen_friend_hatter3a:
hide dee_m_01_2
show dee_m_01_2 at left
with dis

show dam_m_01_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0510
Dam "「きっとお姉さんはあの我侭な女王様に嫌気が差したんだよ、兄弟。\n
お姉さんも辛かったよね……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「こらこらこら。\n
勝手に話を捏造しないでちょうだい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「ビバルディに頼まれて書類を届けにきただけよ。\n
ブラッドのところまで案内してくれない？」"

hide dee_m_01_2
show dee_m_01_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice dad_g0511
Dee "「……あの女王様が、ボスに何の用だろ。\n
嫌な予感しかしないよ」"

jump gakuen_friend_hatter4
label gakuen_friend_hatter3c:
hide dee_m_01_4
show dee_m_01_2 at left
with dis
hide dam_m_01_2
show dam_m_01_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0512
Dam "「きっとお姉さんはあのやかましい遊園地の騒音に嫌気が差したんだよ、兄弟。\n
お姉さんも辛かったよね……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「こらこらこら。\n
勝手に話を捏造しないでちょうだい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「ゴーランドに頼まれて書類を届けにきただけよ。\n
ブラッドのところまで案内してくれない？」"

hide dee_m_01_2
show dee_m_01_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice dad_g0513
Dee "「……あの音痴が、ボスに何の用だろ。\n
嫌な予感しかしないよ」"

jump gakuen_friend_hatter4
label gakuen_friend_hatter3d:
hide dee_m_01_4
show dee_m_01_2 at left
with dis
hide dam_m_01_2
show dam_m_01_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0514
Dam "「きっとお姉さんは陰気な塔に嫌気が差したんだよ、兄弟。\n
お姉さんも辛かったよね……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「こらこらこら。\n
勝手に話を捏造しないでちょうだい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「ユリウスに頼まれて書類を届けにきただけよ。\n
ブラッドのところまで案内してくれない？」"

hide dee_m_01_2
show dee_m_01_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice dad_g0515
Dee "「……陰気の塊みたいな委員長が、ボスに何の用だろ。\n
嫌な予感しかしないよ」"

jump gakuen_friend_hatter4
label gakuen_friend_hatter4:
hide dam_m_01_2
show dam_m_01_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice dad_g0516
Dam "「そうだね、兄弟。\n
その封筒をここで燃やしたほうが、幸せになれる気がするよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_6")
T "「駄目駄目。\n
ほら、早く案内してよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_17")
T "「そうじゃないと勝手に入っちゃうわよ？\n
いいの？」"

hide dee_m_01_4
show dee_m_01_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_17")
voice dad_g0517
Dee "「だ、駄目だよお姉さん！\n
お客さんを案内してあげなきゃ、僕らがボスに怒られちゃうからね！」"

hide dam_m_01_4
show dam_m_01_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_17")
voice dad_g0518
Dam "「お姉さん、案内してあげるよ！\n
ボスがいるのは、共同区域のテラスだよね、兄弟」"

play sound se_0361
pause .5
play sound se_0361
hide dee_m_01_5

hide dam_m_01_2

play sound se_0624
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人にそれぞれ手をとられ、導かれるままに帽子屋寮の敷地内へと足を踏み入れる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "前回は、門の前までしか訪ねなかった。\n
こうして中に入るのはこれが初めてだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自寮という比べる対象を知ってしまったせいか、前に外から眺めたときよりも帽子屋寮という建物が新鮮に見える。"


scene bg_par12_hct_day
with dis

play music high_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうして、双子に案内されて私が連れていかれたのは、帽子屋寮の男女共同区域にあるテラスだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "フェンスには蔓薔薇が絡みつき、ところどころ赤い花をつけている。\n
優雅な白のティーテーブルでは、二つの人影が今まさにお茶会の真っ最中だった。"


show eri_m_02_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0337
Elliot "「んん？\n
ガキ共、おまえら、またサボって……、んん？」"

hide eri_m_02_6
show eri_m_01_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0338
Elliot "「[firstname]、あんた、どうしたんだ？\n
こんなところまで、何か用か？」"
if place_of_stay == "Castle":
    jump gakuen_friend_hatter5a
if place_of_stay == "Amuse":
    jump gakuen_friend_hatter5c
if place_of_stay == "Tower":
    jump gakuen_friend_hatter5d
label gakuen_friend_hatter5a:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「ビバルディから封筒を預かってきたのよ。\n
ブラッドに渡してほしいんですって」"


show bra_m_03_18 at center
with dis
hide eri_m_01_5

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
Blood "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "紅茶のカップを持ち上げかけていたブラッドの手が、止まった。\n
訝しげに片眉がひくりと跳ね上がる。"

hide bra_m_03_18
show bra_m_03_14 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0662
Blood "「私に？\n
はてさて、あの女王様からラブレターを貰うような心当たりはないんだがな……」"

jump gakuen_friend_hatter6
label gakuen_friend_hatter5c:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「ゴーランドから封筒を預かってきたのよ。\n
ブラッドに渡してほしいんですって」"

hide bra_m_03_14
show bra_m_03_18 at center
with dis


with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
Blood "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "紅茶のカップを持ち上げかけていたブラッドの手が、止まった。\n
訝しげに片眉がひくりと跳ね上がる。"

hide bra_m_03_18
show bra_m_03_14 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0663
Blood "「私に？\n
はてさて、あの歩く騒音公害からラブレターを貰うような心当たりはないんだがな……」"

jump gakuen_friend_hatter6
label gakuen_friend_hatter5d:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「ユリウスから封筒を預かってきたのよ。\n
ブラッドに渡してほしいんですって」"

hide bra_m_03_14
show bra_m_03_18 at center
with dis


with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
Blood "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "紅茶のカップを持ち上げかけていたブラッドの手が、止まった。\n
訝しげに片眉がひくりと跳ね上がる。"

hide bra_m_03_18
show bra_m_03_14 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0664
Blood "「私に？\n
はてさて、あの堅物の委員長殿からラブレターを貰うような心当たりはないんだがな……」"

jump gakuen_friend_hatter6
label gakuen_friend_hatter6:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「怖いこと言わないでよ」"

hide bra_m_03_14
show bra_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
voice blo_g0665
Blood "「何かしらの熱情はこもっていそうだがな……。\n
まあ、せっかく来たんだ、お嬢さんも茶につきあえ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "座りなさい、と目で命じられる。\n
どのみち封筒を渡す必要があるので、私は示されるままに席についた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その両傍らを、双子がかためる。\n
お向かいには帽子屋寮寮長と副寮長。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "贅沢なのか、危険なのかがいまいち分からなくなるフォーメーションだ。"

hide bra_m_02_3
show bra_m_02_18 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0666
Blood "「ではいただこうか。\n
私宛なんだろう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「ええ、あなたに渡すようにと言付かっているわ。\n
これで、確かに渡せたわね」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（だから、さっさとこの閉じ込めるような雰囲気をどうにかしてちょうだい……）"

play sound se_0472
hide bra_m_02_18

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "きちんと封のされている面を表にしてブラッドへと差し出す。\n
それを受け取ると、ブラッドはすっと指先をその封へと滑らせた。"

play sound se_0740

show white with Dissolve(.1)
hide white
if place_of_stay == "Castle":
    jump gakuen_friend_hatter7a
if place_of_stay == "Amuse":
    jump gakuen_friend_hatter7c
if place_of_stay == "Tower":
    jump gakuen_friend_hatter7d
label gakuen_friend_hatter7a:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ビバルディその人を象徴するような薔薇の紋章が一度淡く光り、その後うっすらと消えていった。"

jump gakuen_friend_hatter8
label gakuen_friend_hatter7c:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドを象徴するような音符の紋章が一度淡く光り、その後うっすらと消えていった。"

jump gakuen_friend_hatter8
label gakuen_friend_hatter7d:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "塔を象徴するクローバーの紋章が一度淡く光り、その後うっすらと消えていった。"

jump gakuen_friend_hatter8
label gakuen_friend_hatter8:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドは、さっそくその中身を改める。"

play sound se_0470

show bra_m_01_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Blood "「…………」"

play sound se_0697 volume .8
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その眉間に、深く皺が寄った。\n
ひゅぅうううううっと周囲の気温が急速に冷えていくような錯覚を覚える。"

hide bra_m_01_13
show bra_m_01_13 at left
with dis

show eri_m_01_12 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0339
Elliot "「ブラッド？\n
どうしたんだ、そんな険しい顔して……」"

hide eri_m_01_12
show eri_m_01_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0340
Elliot "「あいつらが、何か無茶でも言ってきたのか？\n
大丈夫だ、俺がついてる！あんたのためだったらなんでもしてやるからな！」"

hide bra_m_01_13
show bra_m_03_14 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0667
Blood "「……結構だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "俯いたまま顔を上げようとしないブラッド。対して、相変わらずに盲信っぷりを見せ付けながらエリオットが励ましの言葉を口にする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、一言で切り捨てられた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_7")
T "（う、薄ら寒い……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "見ているだけで、エリオットが地雷原を歩いているのが分かってしまう。\n
隣の双子も、同じく「うわあ」という顔をしているため、気付いているのだろう。"


show dee_m_02_7 at center
with dis
hide bra_m_03_14

hide eri_m_01_1

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0521
Dee "「ひ、ひよこウサギってこういうところ強いよね。\n
見習いたくないけど見習いたいよね」"

hide dee_m_02_7
show dee_m_02_7 at left
with dis

show dam_m_01_12 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0522
Dam "「兄弟、それじゃあどっちか分からないよ。\n
でも……、同感だよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（……分かる気がする）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットの異常なまでの鈍感さは、ちょっと見習いたい域だ。"


show bra_m_03_10 at center
with dis
hide dee_m_02_7

hide dam_m_01_12

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0668
Blood "「……ふふふ、これがおまえ達にはなんに見える？\n
是非、聞かせてくれないか」"

play sound se_0529
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ばさりっとティーテーブルの上に封筒が投げ出され、その中身が封筒から滑り出た。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……請求書？\n
ああ、それと監督不行届始末書……？」"

hide bra_m_03_10


show eri_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
Elliot "「！！！！」"

hide eri_m_02_5
show eri_m_02_5 at left
with dis

show dee_m_02_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
Dee "「！！！！」"

hide eri_m_02_5
show eri_m_02_5 at left_center
hide dee_m_02_7
show dee_m_02_7 at center
with dis

show dam_m_02_7 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
Dam "「！！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ティーテーブルの上に広がった書類のタイトルを読み上げる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "と、同時に向かいのエリオットと、両脇の双子とがそれぞれびくりと身体を竦ませた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……心当たりがあるのね？）"

hide dam_m_02_7

hide dee_m_02_7

hide eri_m_02_5

play sound se_0184
camera at hpunch
camera at vpunch
play sound se_0313
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いきなりエリオットが椅子の上に立ちあがったと思ったら、ティーテーブルを飛び越えてこちらへとやってきた。"


show eri_m_03a_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0341
Elliot "「すまねえブラッド……！！\n
あんたに迷惑をかけるつもりはなかったんだ！！」"

hide eri_m_03a_3
show eri_m_03a_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0342
Elliot "「なかったんだが……っ！\n
こいつらとじゃれているうちに、ちょっとばかり夢中になっちまって……！！」"

hide eri_m_03a_4


show dee_m_02_13 at left
with dis

show dam_m_02_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0523
Dee "「夢中になってたのはひよこウサギだけだよ、ボス！！\n
僕達は被害者だよ！」"

hide dam_m_02_7
show dam_m_02_13 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0524
Dam "「そうだよ、ボス！\n
僕達もちょっとくらいは悪かったかもしれないけど、ほんのちょっと！ちょこっとだけ！」"


show eri_m_02_9 at center
with dis
hide dee_m_02_13

hide dam_m_02_13

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0343
Elliot "「うるせえ！おまえらのせいだろ！？\n
仕事サボったあげく俺のことをウサギ呼ばわりするから……！！」"

hide eri_m_02_9


show dee_m_02_3 at left
with dis

show dam_m_02_13 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0525
Dee "「ウサギにウサギって言って何が悪いんだよ！！\n
大体、仕事仕事って、僕達学生だよ！？」"

hide dam_m_02_13
show dam_m_02_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0526
Dam "「子供を働かせようなんて、酷い大人だよ！\n
大人って汚いよね！！」"


show eri_m_01_5 at center
with dis
hide dee_m_02_3

hide dam_m_02_3

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0344
Elliot "「ふざけんなっっ！！\n
おまえらがな……っ！！？」"

hide eri_m_01_5

play sound se_0394
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "双子とエリオットの言い争いに気を取られていたところで、やけに重々しい音が響いた。\n
そちらへと目をやって、息を飲む。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "優雅なティーテーブルに、繊細なティーカップと美味しそうな茶菓子。\n
そして……、そこに一丁のマシンガンが一緒に並んでいる。"


show bra_m_03_9 at center with Dissolve(1.5)
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そろりとマシンガンから視線を持ち上げて見やった先、ブラッドはやっぱり笑顔だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その背に、ドス黒い何かを背負っていたとしても、やはり笑顔だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_10")
T "（……{size=+20}怖っ！！{/size}）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "帽子屋寮というのはならず者の集まりで、皆好き勝手にやっているのだとばかり思っていたが、実はそうでもないのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_9")
T "（自分が巻き込まれるのは嫌なのね？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちらりと見えた、監督不行届始末書というのはおそらく、この三人がやらかしたことについてブラッドにまで及んだ咎なのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドは寮長であり、ボスだ。\n
その寮生であり、部下である彼らのしたことにまで責任を持たなくてはいけない。"

hide bra_m_03_9
show bra_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0669
Blood "「……で、何があったんだ？\n
いや……、何をした？」"

hide bra_m_01_10


show eri_m_03a_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0345
Elliot "「た、たいしたことじゃないんだぜ……！？\n
ちょっと、ちょっとだよ！な！？」"

hide eri_m_03a_4
show eri_m_03a_4 at left
with dis

show dee_m_01_11 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0527
Dee "「うん、そうだよ！ちょこっと！！\n
ひよこウサギの言うとおりだよボス！！」"

hide eri_m_03a_4
show eri_m_03a_4 at left_center
hide dee_m_01_11
show dee_m_01_11 at center
with dis

show dam_m_02_7 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0528
Dam "「そうだよ、ボス！\n
本当にちょっとだけなんだよ！！」"


show bra_m_01_7 at center
with dis
hide dee_m_01_11

hide dam_m_02_7

hide eri_m_03a_4

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Blood "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドの笑みがますます深くなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "背後に渦巻くどす黒い何かさえ見えなければ、慈愛に満ちているようにも見えたかも……。いや見えないだろう、どちらにしても怖い。"

play sound se_0055
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "無意識なのか、私の背後にいるエリオットがまるで私を盾にするかのよう私の肩に手を置いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_10")
T "（わ、私を巻き込むのはやめてよ\n
ね！？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はあくまで頼まれた封筒を届けにきただけだ。\n
ブラッドに恨まれるようなことは何ひとつしていない。"

hide bra_m_01_7


show eri_m_03b_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Elliot "「…………」"

hide eri_m_03b_11
show eri_m_03b_11 at left
with dis

show dee_m_02_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Dee "「…………」"

hide eri_m_03b_11
show eri_m_03b_11 at left_center
hide dee_m_02_8
show dee_m_02_8 at center
with dis

show dam_m_02_8 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Dam "「…………」"

hide dee_m_02_8

hide dam_m_02_8

hide eri_m_03b_11

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "笑顔での威圧に負けたように、三人が沈黙する。"
if place_of_stay == "Castle":
    jump gakuen_friend_hatter9a
if place_of_stay == "Amuse":
    jump gakuen_friend_hatter9c
if place_of_stay == "Tower":
    jump gakuen_friend_hatter9d
label gakuen_friend_hatter9a:

show eri_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0346
Elliot "「す、すまねえ……。\n
赤薔薇寮の外壁、ぶっ壊しちまった……」"

hide eri_m_01_10
show eri_m_01_10 at left
with dis

show dee_m_01_11 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0529
Dee "「ご、ごめんなさい、ボス。\n
どこかよく分からない部屋の壁、ぶち抜いちゃった……」"

hide eri_m_01_10
show eri_m_01_10 at left_center
hide dee_m_01_11
show dee_m_01_11 at center
with dis

show dam_m_01_11 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0530
Dam "「ごめんなさい、ボス。\n
誰のものか分かんないけど、たくさんのぬいぐるみを焼き払っちゃった……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「！！！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "三人の自白した内容に、私まで愕然としてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……{size=+20}つまり、破壊の限りを尽くしたってことね？{/size}）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言われてみれば、私にこの封筒を託した際のビバルディは、なんだか目がすわっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "魔法で破壊されたものは、魔法によって修復できるというのが定説だが、さすがに焼き払われて灰になってしまったら難しいだろう。"

jump gakuen_friend_hatter10
label gakuen_friend_hatter9c:
hide eri_m_01_10
show eri_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0347
Elliot "「す、すまねえ……。\n
遊園地寮の外壁、ぶっ壊しちまった……」"

hide eri_m_01_10
show eri_m_01_10 at left
with dis
hide dee_m_01_11
show dee_m_01_11 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0529
Dee "「ご、ごめんなさい、ボス。\n
どこかよく分からない部屋の壁、ぶち抜いちゃった……」"

hide eri_m_01_10
show eri_m_01_10 at left_center
hide dee_m_01_11
show dee_m_01_11 at center
with dis
hide dam_m_01_11
show dam_m_01_11 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0531
Dam "「ごめんなさい、ボス。\n
ゴーランド先生の楽器を焼き払っちゃった……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「！！！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "三人の自白した内容に、私まで愕然としてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言われてみれば、私にこの封筒を託した際のゴーランドは、なんだか目がすわっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "魔法で破壊されたものは、魔法によって修復できるというのが定説だが、さすがに焼き払われて灰になってしまったら難しいだろう。"

jump gakuen_friend_hatter10
label gakuen_friend_hatter9d:
hide eri_m_01_10
show eri_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0348
Elliot "「す、すまねえ……。\n
塔の外壁、ぶっ壊しちまった……」"

hide eri_m_01_10
show eri_m_01_10 at left
with dis
hide dee_m_01_11
show dee_m_01_11 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0532
Dee "「ご、ごめんなさい、ボス。\n
委員長の作業室の薬品棚、吹っ飛ばしちゃった……」"

hide eri_m_01_10
show eri_m_01_10 at left_center
hide dee_m_01_11
show dee_m_01_11 at center
with dis
hide dam_m_01_11
show dam_m_01_11 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0533
Dam "「ごめんなさい、ボス。\n
委員長のレポートを焼き払っちゃった……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「！！！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "三人の自白した内容に、私まで愕然としてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それは酷い。\n
酷すぎる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言われてみれば、私にこの封筒を託した際のユリウスは、なんだか目がすわっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "魔法で破壊されたものは、魔法によって修復できるというのが定説だが、高価な薬品を駄目にされたり、レポートを焼き払ってしまったのなら難しいだろう。"

jump gakuen_friend_hatter10
label gakuen_friend_hatter10:

show bra_m_01_10 at center
with dis
hide dam_m_01_11

hide dee_m_01_11

hide eri_m_01_10

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0670
Blood "「ふ、そうか……。\n
ふふふ、それはさぞや気分がよかったことだろう」"

hide bra_m_01_10
show bra_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0671
Blood "「……だが、私の気分はあまりよくないな。自分ではその爽快感を味わえず、尻拭いだけをさせられるというのは……、実に不愉快だ」"

play sound se_0516
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドがついには声に出して笑い出した。\n
じゃきりっとマシンガンを傍らに構える。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "怒りの掃射準備は万端といった感じだ。"

hide bra_m_01_3
show bra_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0672
Blood "「……さっさと逃げたまえ、お嬢さん。\n
巻き込まれることになるぞ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_10")
T "「……！！」"

play sound se_0184
camera at hpunch
camera at vpunch
play sound se_0454
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は跳ねるように立ち上がると、慌てて双子やエリオットの傍から離れた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まさか、本物のマシンガンではないだろう。しかし、マジックアイテムといえ、その威力を自身の身でもって試したいとは思わない。"

hide bra_m_01_2
show bra_m_01_3 at left
with dis

show eri_m_02_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0349
Elliot "「わ、悪かったよブラッド！\n
な、落ち着けって！！！」"

hide bra_m_01_3
show bra_m_02_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0673
Blood "「これが落ち着いていられるか。\n
どうして私が始末書などを書かねばならないんだ？」"

hide bra_m_02_3
show bra_m_03_10 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0674
Blood "「なあ、エリオット、子供達。\n
私に教えてくれないか」"

play sound se_0187
hide bra_m_03_10

hide eri_m_02_5
show eri_m_02_5 at left
with dis

show dee_m_01_12 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Dee "「……～～！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドの指先が引き金にかかる。\n
あと少し、あと少しでも力を加えたら、マシンガンが火を噴くことになるだろう。"

hide eri_m_02_5
show eri_m_02_9 at center
with dis
hide dee_m_01_12

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0350
Elliot "「分かった！あんたに俺なりの詫びを入れさせてくれ！\n
償いのチャンスをくれねえか！？」"


show bra_m_01_9 at center
with dis
hide eri_m_02_9

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0675
Blood "「詫びだと？\n
私の貴重な時間を奪おうとしていることに対して、どんな謝罪が有効だと思っているんだ、おまえは」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "書かなければならない始末書やら、払わねばならない請求金額などに思いを馳せているのか、ブラッドの声音は低く冷たい。"


show eri_m_01_6 at center
with dis
hide bra_m_01_9

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0351
Elliot "「俺の誠意だ！\n
受け取ってくれ！！」"

hide eri_m_01_6

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_8")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "（……嫌な予感が）"

play sound se_0496

show magic_r onlayer master with Dissolve(1.5)

show eri_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_5")
Elliot "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が止めるよりも先に、エリオットの呪文が完成していた。"

hide eri_m_01_11


play music overslept_wam
hide magic_r
$ flash_color("orange",.2)
play sound se_0722

show m_bousi_friend1 onlayer master
with dis
$ flash_color("orange", .3)
play sound se_0733
hide m_bousi_friend1
show m_bousi_friend2 onlayer master
with dis
$ flash_color("orange", .4)
play sound se_0346
hide m_bousi_friend2
$ flash_color("orange", .5)

show eri_m_03a_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0352
Elliot "「ど、どうだ……！？\n
俺の一か月分の食料とおやつだ！！」"

hide eri_m_03a_4
show eri_m_03a_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0353
Elliot "「なかなか手に入らねえ、珍しいにんじん料理も入っている！\n
俺のとっておき！貴重な品々だが、遠慮はいらねえぜ！！」"

hide eri_m_03a_7
show eri_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0354
Elliot "「俺の気持ちだ、受け取ってくれブラッド！！！！\n
ああ、まだまだあるぜ！！？」"

hide eri_m_01_8
##[chara3 PAY ATTENTION="false"]
play sound se_0733
$ flash_color("orange", .3)

show m_bousi_friend3 onlayer master
with dis
play sound se_0346
$ flash_color("orange", .5)
hide m_bousi_friend3
show m_bousi_friend4 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_10")
T "「…………」"

play sound se_0454
hide m_bousi_friend4

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんだか、展開が読めてしまう。\n
私は、そーっと、そーっとテラスを後にするべく後ずさった。"


show bra_m_01_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Blood "「…………」"
$ flash_color("orange", .5)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "オレンジ色に埋まりつつ。"

hide bra_m_01_13
show bra_m_01_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0676
Blood "「……死ね」"

hide bra_m_01_9
##[chara4 PAY ATTENTION="false"]
play sound se_0347
$ flash(.1)
$ flash(.1)
$ flash(.1)
$ flash(.1)
$ flash(.1)

show white onlayer master with Dissolve(.2)

scene bg_par15_rg_hat_day ##instantPAY ATTENTION="true"]
hide white with Dissolve(.5)
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドの短い呪詛めいた声が響くのと、マシンガンが火を噴くのは、私がテラスを脱出するのとほぼ同時だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……帽子屋寮が、物騒で賑やかだという噂に嘘はなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（……追加するなら、オレンジ色に染まっているってことかしら）"

##[rchara4 PAY ATTENTION="false"]
##[chara4 PAY ATTENTION="false"]
$ hi_mes()

scene bg_map_eve
with stripe_l_long
jump gakuen_friend_end
