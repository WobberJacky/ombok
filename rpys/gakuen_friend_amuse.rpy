
scene bg_map_day
with dis
label gakuen_friend_amuse:
$ gakuen_friend_amuse_seen = True
$ clockanim()


scene bg20_gd_day
with dis

play music gallery_front_day_p_wam

scene bg_par15_rg_amu_day with Dissolve(1.2)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その日、私は遊園地寮を訪れていた。"
if place_of_stay == "Castle":
    jump gakuen_friend_amuse1a
if place_of_stay == "Hatter":
    jump gakuen_friend_amuse1b
if place_of_stay == "Tower":
    jump gakuen_friend_amuse1d
label gakuen_friend_amuse1a:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ビバルディに頼まれ、書類を届けに来たのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は自治会の役員になったわけではないのだが、それでも赤薔薇寮に住む者として、そして自治会員として無理のない範囲で手伝おうとは思っている。"

jump gakuen_friend_amuse2
label gakuen_friend_amuse1b:
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
帽子屋寮に住む者として、寮長の頼みを聞くべきだろう。"

jump gakuen_friend_amuse2
label gakuen_friend_amuse1d:
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

jump gakuen_friend_amuse2
label gakuen_friend_amuse2:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなわけで、今回、書類の配達を引き受けた。\n
届け先は、遊園地寮の代表者だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（久しぶりだわ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "前に一度表を通りかかったときには、ゴーランドの恐ろしい音波攻撃が流れており、慌てて逃げ出した。\n
おかげで、中は観察し損ねている。"


play music pierce_t_ali

show pia_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0270
Pierce "「あれ？君、どうしたの？どうしたのかな？\n
迷子？迷子なの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "勝手に入ってもいいものかと躊躇しているところで、背後から声がした。\n
よく知る声だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「ああ、よかったわ、ピアス。\n
悪いんだけど、ゴーランドかボリスのいるところまで案内してくれないかしら」"

hide pia_m_03_10
show pia_m_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice pie_g0271
Pierce "「ぴ？ボリスかゴーランド先生？\n
どっちでもいいの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「ええ、どちらでも」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "遊園地寮の代表者に渡してくれと頼まれているのだから、ボリスでもゴーランドでも構わないはずだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスは遊園地寮の寮長だし、ゴーランドは遊園地寮に住む教職員だ。"

hide pia_m_03_1
show pia_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0272
Pierce "「いいよ、いいよ！\n
俺が案内してあげるよ！」"

hide pia_m_01_6
show pia_m_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0273
Pierce "「君、迷子ってことは落し物だよね？\n
俺が案内するってことは拾ったのと同じだから、君は俺のもの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「……違うわよ。\n
ほら、さっさと歩く」"

play sound se_0776

play music corridor_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私には……、というよりも一般人には理解しかねる理屈をこねるピアスをせっついて、遊園地寮の中へと足を踏み入れる。"


scene bg25_rr_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "遊園地寮、という名前に相応しくとても色鮮やかで、楽しげな場所だ。\n
比べる対象として自寮があるからか、余計に新鮮に見える。"

hide pia_m_03_1
show pia_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0274
Pierce "「えっとね、えっとね、ボリスならレクリエーション室にいると思うんだ！\n
ボリスがいっぱい改造したから、すごいんだよ！」"

hide pia_m_01_11
show pia_m_03_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0275
Pierce "「他の寮とは全然違うんだから！\n
特別にすごいんだ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「そうなの？\n
そういえば私、自寮のレクリエーション室もよく知らないかも」"

play sound se_0776
hide pia_m_03_5

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな話をしながら、ピアスに導かれて廊下を歩く。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "歩く。"

play sound se_0776
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "歩く。\n
歩く。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "歩き続ける。"

play sound se_0776
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_11")
T "（……こんなに遠いものだっけ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は自寮の内部しか知らないが、男女共同区域というのはこんなにも広い場所だっただろうか。歩いても歩いても、目的地に着く気配がない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「ねえ、ピアス、ここで本当にあっているの？\n
……ごめんなさい、大丈夫よね」"


show pia_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice pie_g0276
Pierce "「うん、大丈夫！\n
俺、ちゃんと君を案内できるよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（そうよね……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ピアスは少々抜けているように見えても、遊園地寮にもう長く住んでいるはずなのだ。私のような新入生と違って、迷子になったりはしないだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_7")
T "（馬鹿は私だわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふるふると頭を横に振って、疑惑を振り払う。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（ピアスを信じよう）"

play sound se_0776
hide pia_m_01_6

with dis
$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME

play music corridor_day_p_wam
play sound se_0776
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "廊下を歩き始めて数十分が過ぎた。\n
さすがにクラスメイトに対しての信頼も揺らぎ始めてくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「ごめんね、ピアス。\n
こんなこと聞くべきじゃないって分かっているんだけど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_16")
T "「……大丈夫？」"


show pia_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_16")
voice pie_g0277
Pierce "「大丈夫だよ！\n
これね、無限廊下っていう魔法なんだけど、実際には無限じゃないんだ！」"

hide pia_m_01_10
show pia_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_16")
voice pie_g0278
Pierce "「ちゃんと夕食の時間が近くなったら出してくれるよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_9")
T "{size=+20}（ピアスを信じた私が馬鹿だった）{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "逆にいうと、夕食時間近くまで抜け出せないということか。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_14")
T "「ちょっとピアス！？\n
無限廊下ってなに！！？」"

play sound se_0051
camera at hpunch
camera at vpunch
hide pia_m_01_6
show pia_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_14")
Pierce "「！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はピアスの肩をがしっと捕まえると、揺さぶりながら問い詰める。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "さっさとボリスかゴーランドのどちらかにこの封筒を渡して、自寮に帰って寛ぎたい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_9")
T "（夕食時間まで歩き続けないといけないなんてごめんだわ！）"

hide pia_m_01_3
show pia_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_9")
voice pie_g0279
Pierce "「わわ！？無限廊下っていうのは、無限に続いている廊下だよ？\n
でもこれは無限じゃないから、本当は無限じゃないんだよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「そんなことはどうでもいいのよっ！\n
私は、ボリスかゴーランドに会いたいの！！」"

hide pia_m_03_3
show pia_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_12")
voice pie_g0280
Pierce "「ここでずっと彷徨っていると、いつもゴーランド先生が助けに来てくれるよ？\n
それまで待てば……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_13")
T "「待たないわよっ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ピアスは当てにならない。\n
自力でなんとかしなければ、この廊下から脱出することは出来ないようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_2")
T "「なんらかの魔法がかかっている……、のよね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうして寮の廊下に、こんなふざけた仕掛けがほどこされているのかは謎だ。\n
誰かの悪戯だろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_13")
T "「誰かー？\n
誰かいないー？」"

play sound se_0776
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は声をあげながら無限（ではないらしいが）廊下を歩く。"

hide pia_m_03_11
show pia_m_03_11 at left
with dis

show boy_e1_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0038
Seito "「……？\n
あれ？どうしたんだ、こんなところで」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ひょこりと廊下の角から、一人の男子生徒が顔を出した。\n
その角に辿り着けず、延々と歩いていた私たちにとってはまるで救世主だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「ごめんなさい、この廊下から出られなくなっちゃって……。\n
出方を教えてくれる？」"

hide boy_e1_9
show boy_e1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice oni_g0039
Seito "「いいよ、お安い御用だ。\n
……あんた、他寮の人？」"

play sound se_0776
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼はすたすたと私達のもとへと歩み寄ってくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私達がいくら歩いても、その角に辿り着けなかったというのに彼が私達の元へ来るのはあっという間だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「ええ、そうよ。\n
ゴーランドかボリスのどちらかに渡さないといけないものがあって、それを届けに来たの」"

hide boy_e1_3
show boy_e1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_13")
voice oni_g0040
Seito "「ああ、そうなのか。\n
無限廊下の罠なんて、うちの寮生じゃもう誰も引っかからないからさ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_16")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "無言で、隣のピアスを見る。\n
彼は間違いなく、ここの寮生だ。"

hide pia_m_03_11
show pia_m_01_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0281
Pierce "「ぴい……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の無言の訴えを察したのか、彼はふいっと視線をそらした。"

hide boy_e1_2
show boy_e1_8 at center
with dis
hide pia_m_01_8

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0041
Seito "「はは、ピアスはほら……、素直すぎるから。\n
……ちょっと痛いぜ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……え？」"

play sound se_0423
$ flash(.1)
camera at hpunch
camera at vpunch
play sound se_0423
$ flash(.1)
camera at hpunch
camera at vpunch
#special anime hit center
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "聞き返すより先に、背中を思いっきり叩かれていた。"


show pia_m_02_6 at center
with dis
hide boy_e1_8

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0282
Pierce "「ぴ！！？\n
痛い！痛いよ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_8")
T "「……っつう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "じんと痺れるような痛みに、呻く。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "といっても、ちゃんと手加減はしてくれたのか、その痛みは一過性のものだ。\n
すぐにそんな痛みはなくなっていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「……あれ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "痛みが引くのと一緒に、視界がクリアになったような気がした。\n
ぱち、と何度か瞬く。"


show boy_e1_3 at center
with dis
hide pia_m_02_6

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0042
Seito "「廊下って、ほとんど景色変わらないだろ？\n
こういう単調な場所って、案外暗示にかかりやすいんだよな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_7")
T "「……暗示、だったの？」"

hide boy_e1_3
show boy_e1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_7")
voice oni_g0043
Seito "「そうそう。\n
あんた、歩いているつもりだったと思うけど、実際にはそこにぼーっと突っ立ってたんだぜ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_6")
T "「え！？」"

play sound se_0313
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "振り返って確認してみる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（……本当だわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ずいぶん長く廊下を歩いてきたと思っていたのに、実際には私達は廊下に入ってすぐのところに立ち尽くしていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちっとも、進んでいない。\n
長く歩き続けた割には、足も痛くなかった。"

hide boy_e1_3
show boy_e1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0044
Seito "「背中を叩いたりだとか、そういう軽いショックで解ける程度の弱い暗示なんだけどな。暗示って気付かないと、なかなか出られないんだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_17")
T "「……一つ聞いていいかしら」"

hide boy_e1_2
show boy_e1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_17")
voice oni_g0045
Seito "「ん？\n
なに？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_14")
T "「……{size=+20}なんで、寮の中にこんな暗示の罠が潜んでいるのよ！？{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "侵入者用の罠や、警備のためといった感じのものではない。\n
おふざけ用のトラップだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（悪戯っていうなら分かるけど、それが放置されているだなんて……）"

hide boy_e1_3
show boy_e1_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice oni_g0046
Seito "「あー……、それはまあ。\n
ここが遊園地寮だからじゃないかな！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「……どういうこと？」"

hide boy_e1_5
show boy_e1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_12")
voice oni_g0047
Seito "「楽しいものは置いておけってこと。\n
そこまで害もないしね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼はまるで当たり前のように言う。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_9")
T "「～～～っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_9")
T "（……慣れない人には害になるわよ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、慣れない者が引っかかることも含めて「楽しいもの」なのだろう。\n
ここは本当に、名前だけでなくその中身まで遊園地のようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「……他にも何か、知っておいたほうがいい仕掛けってあるかしら？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ピアスはどうにも当てにならない。"

hide boy_e1_3
show boy_e1_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0048
Seito "「そうだなあ。\n
階段上がったところに、甲冑が飾ってあるんだけどさ」"

hide boy_e1_9
show boy_e1_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0049
Seito "「それ、目が合ったら追いかけてくるんだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「こ、怖……。\n
どうすればいいの？」"

hide boy_e1_9
show boy_e1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice oni_g0050
Seito "「それを解除するためには……、にっこり笑顔だ」"

##special anime"kirakira_center"loop="false"time="1000"]
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……へ？」"

hide boy_e1_2
show boy_e1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice oni_g0051
Seito "「にっこり笑いかけると、停止するから。\n
普通に逃げていると、どこまでも追いかけてくるぜ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「……あ、悪趣味すぎない？」"

hide boy_e1_3
show boy_e1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
voice oni_g0052
Seito "「斬り掛かってくるわけじゃないから」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「そうは言っても……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普通、追われれば逃げるのに必死になる。\n
そんな中、笑顔など作る余裕が果たしてあるだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（……解除方法を知っていなければ、延々と追いかけっこよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "追いかける甲冑が、そういったジョークアイテムだとはタネを知らなければ気付かない。"

hide boy_e1_3
show boy_e1_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0053
Seito "「まあ、そういうのがほら、遊園地寮らしさなんだよ。\n
皆、一度は通る道なんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "遊園地寮というのは、私が想像していた以上にとんでもない場所だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_7")
T "（楽しければオーケー、か……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「……ありがとう、助かったわ。\n
これでなんとかレクリエーション室まで辿り着けると思う」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_13")
T "「ほら、ピアス、行くわよ」"


show pia_m_01_6 at center
with dis
hide boy_e1_5

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_13")
voice pie_g0283
Pierce "「うん！\n
俺行くよ！！」"

play sound se_0776
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は彼に礼を行って別れると、再び廊下を歩き出す……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_16")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "振り返った。\n
ピアスは、ぼんやりとその場に立ちつくしている。"

hide pia_m_01_6
show pia_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0284
Pierce "「君、すごいね、歩くの早いね！\n
俺、追いつけないよ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_9")
T "「～～～……っ！\n
言われたそばから、どうしてまた……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "力いっぱいに腕をふり上げ、その背中へと打ち下ろした。"

play sound se_0124
camera at hpunch
camera at vpunch
#special anime hit center
hide pia_m_03_3
##[chara1 PAY ATTENTION="false"]
with dis
$ hi_mes()

scene bg_par02_ct_amu_eve
with stripe_l_long

play music dining_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ようやくボリスとゴーランドに出会えたのは、遊園地寮のレクリエーション室ではなくカフェテリアだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……結局、私とピアスは、レクリエーション室には辿り着けなかったのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「……無駄に疲れた」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "後悔するのは、何故あそこでピアスに声をかけてしまったのか、だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "正直、ピアスがいなければ、もっと早く、もっと楽に目的を達成できていた気がする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "せっかく私が解除方法を聞いておいた甲冑にも、見事ピアスは追いかけまわされ……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "笑顔笑顔と私が言い続けているにも関わらず、ずっと泣きながら逃げ惑っていたのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最初は走り回るピアスを追いかけ、声をかけ続けていた私だったのだけれども、途中で諦めた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "階段に腰掛け、ピアスが甲冑に追いかけまわされてぐるぐると回る様を傍観する。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（……何を言っても無駄）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "悟りを開いた気分だ。\n
そうして私がたそがれているところを、レクリエーション室帰りのボリスに見つけてもらって今に至る。"


show bor_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0556
Boris "「あははは、あんたも物好きだよな～。\n
ただでさえ仕掛けの多い遊園地寮に、ピアスと一緒に入るなんてさ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「……ピアスだって遊園地寮の生徒でしょう？\n
だから、大丈夫かと思ったのよ」"

hide bor_m_02_3
show bor_m_02_3 at left
##[rchara1 PAY ATTENTION="false"]
show pia_m_01_6 at right
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
voice pie_g0285
Pierce "「俺、大丈夫だよ！！」"


show go_m_03_12 at center
hide bor_m_02_3

hide pia_m_01_6

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
voice gor_g0342
Gowland "「おうおう、そうだよな。\n
おまえはいつでも大丈夫だよな……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドの疲れた声は正しい。\n
ピアスはいつだって、一人で「大丈夫」なのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "廊下の暗示に引っかかろうと、甲冑に追いかけまわされようと、それはピアスの中では「大丈夫」の中に分類されることなのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_17")
T "（……付き合わされるこっちが馬鹿をみる）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "深い深い溜息がこみ上げた。"

hide go_m_03_12
show go_m_02_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0343
Gowland "「で、あんたはどうしてここに？\n
別に、遊園地寮の実態を楽しみにきたってわけじゃないんだろ？」"

hide go_m_02_13
show go_m_02_13 at left
with dis

show bor_m_03_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0557
Boris "「それなら俺が、もっとすごい仕掛けのところに案内してやるぜ？\n
どうする？」"

if place_of_stay == "Castle":
    jump gakuen_friend_amuse3a
if place_of_stay == "Hatter":
    jump gakuen_friend_amuse3b
if place_of_stay == "Tower":
    jump gakuen_friend_amuse3d
label gakuen_friend_amuse3a:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「……遠慮するわ。\n
これ、ビバルディから預かってきたの」"

jump gakuen_friend_amuse4
label gakuen_friend_amuse3b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「……遠慮するわ。\n
これ、ブラッドから預かってきたの」"

jump gakuen_friend_amuse4
label gakuen_friend_amuse3d:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「……遠慮するわ。\n
これ、ユリウスから預かってきたの」"

jump gakuen_friend_amuse4
label gakuen_friend_amuse4:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「遊園地寮の代表者に渡してくれ、って言っていたわ」"

hide bor_m_03_4
show bor_m_01_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice bor_g0558
Boris "「それじゃあ、おっさん。\n
おっさんに任せるよ」"

hide go_m_02_13
show go_m_02_4 at center
with dis
hide bor_m_01_3

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice gor_g0344
Gowland "「ボリス～、おまえ一応寮長だろうが。\n
まあ、いいけどよ」"

hide go_m_02_4

play sound se_0472
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドの差し出した手の上に、よれよれになってしまった封筒を乗せる。\n
よれてしまってはいるが、封印は無事だ。"
if place_of_stay == "Castle":
    jump gakuen_friend_amuse5a
if place_of_stay == "Hatter":
    jump gakuen_friend_amuse5b
if place_of_stay == "Tower":
    jump gakuen_friend_amuse5d
label gakuen_friend_amuse5a:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "きちんと赤薔薇の紋章で封が押されている。"

jump gakuen_friend_amuse6
label gakuen_friend_amuse5b:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "きちんと帽子をあしらった紋章で封が押されている。"

jump gakuen_friend_amuse6
label gakuen_friend_amuse5d:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "きちんとクローバーをあしらった紋章で封が押されている。"

jump gakuen_friend_amuse6
label gakuen_friend_amuse6:
play sound se_0740
show white with Dissolve(.1)
hide white

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドがその紋章に指で触れると、紋章は一瞬淡く光を放ち、そしてうっすらと消えていった。\n
さっそく、彼はその中身を確認する。"


show go_m_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0345
Gowland "「ああ、この件か……」"

if place_of_stay == "Castle":
    jump gakuen_friend_amuse7a
if place_of_stay == "Hatter":
    jump gakuen_friend_amuse7b
if place_of_stay == "Tower":
    jump gakuen_friend_amuse7d
label gakuen_friend_amuse7a:
hide go_m_03_9
show go_m_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0346
Gowland "「そっちの女王さんに、ちゃんと受け取ったって伝えてくれ。\n
……で、せっかくだからあんた、飯でも食っていかねえか？」"

jump gakuen_friend_amuse8
label gakuen_friend_amuse7b:
hide go_m_02_12
show go_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0347
Gowland "「そっちのボスに、ちゃんと受け取ったって伝えてくれ。\n
……で、せっかくだからあんた、飯でも食っていかねえか？」"

jump gakuen_friend_amuse8
label gakuen_friend_amuse7d:
hide go_m_02_12
show go_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0348
Gowland "「委員長さんに、ちゃんと受け取ったって伝えてくれ。\n
……で、せっかくだからあんた、飯でも食っていかねえか？」"

jump gakuen_friend_amuse8
label gakuen_friend_amuse8:
hide go_m_02_12
show go_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0349
Gowland "「礼にならないかもしれないが、特別メニューを出してやるぜ？」"

hide go_m_02_8
show go_m_02_8 at left
with dis

show bor_m_02_6 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0559
Boris "「ああ、そうしなよ。\n
疲れているみたいだしさ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「ありがとう。\n
それなら、せっかくだし……」"

hide go_m_02_8

hide bor_m_02_6
show bor_m_02_6 at left
with dis

show pia_m_01_6 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice pie_g0286
Pierce "「一緒にチーズ食べようよ！\n
ここのチーズは美味しいんだよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……いや、それはいい」"

play sound se_0184

show go_m_01_2 at center
with dis
hide bor_m_02_6

hide pia_m_01_6

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice gor_g0350
Gowland "「よおし、せっかくの客人だ！\n
食事と共に、一曲……」"

hide go_m_01_2
show go_m_01_2 at left
with dis

show bor_m_03_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice bor_g0560
Boris "「やめろ！\n
おっさん……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_9")
T "「……それも、遠慮します」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "チーズと、音楽。\n
そして、トラップももうこりごり。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_1")
T "（でも……、たしかに楽しい寮よね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "噂に違わず、遊園地寮は底抜けに賑やかだ。"

hide bor_m_03_3

hide go_m_01_2
with dis
$ hi_mes()

scene bg_par15_rg_amu_eve
with stripe_l_medium
jump gakuen_friend_end
