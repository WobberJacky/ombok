label gakuen_julius3:
scene bg_map_day
with dis
$ clockanim()

jump gakuen_dream_other
label gakuen_julius3_3:

$ time_effect()##PLEASE MANUALLY ADJUST ME

play sound se_0497

play music corridor_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ざわざわと、やっぱりどことなく騒がしい空気の中、ホームルームが終了した。\n
これで今日の授業は終わりだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（そういえば……、今日はユリウスがいる日だっけ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最近は、事前に風紀委員の仕事に関わる予定を教えてもらえるようになっていた。\n
カフェテリアで過ごす放課後も悪くはないが……。"

menu:
    "物足りない。":
        jump gakuen_julius3_4a
    "カフェテリアで充分。":
        jump gakuen_julius3_4b
label gakuen_julius3_4a:
$ lovechara_julius_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（物足りない……、なあ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あの静かな作業室に行けないと思うと、寂しさを感じる。\n
特に構ってもらえるわけでもなく、話が弾むわけでもないのに。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それなのに、あの時間を共有できないことを物足りなく感じてしまう。\n
今日のように、いると分かっている日には向かいたくなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（私、そんなにあの部屋のことが気に入っているのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "とにかく、今日はユリウスが作業室にいる日だ。\n
さっそく、訪ねるとしよう。"

jump gakuen_julius3_5
label gakuen_julius3_4b:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（ま、カフェテリアも悪くないわよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "作業室に比べると賑やかだが、無関心な賑やかさは程よい距離感だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それに作業室だと専ら珈琲になるが、カフェテリアならばもっと幅広い飲み物を楽しむことが出来る。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが……、と、彼の淹れた珈琲を思い浮かべる。\n
今日はせっかくユリウスが作業室にいるというのだから、そちらに行くとしよう。"

jump gakuen_julius3_5
label gakuen_julius3_5:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（その前にカフェテリアに寄って、何か差し入れでも持っていこうかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなことを思いながら、教室から出ようとして……。"


show bor_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0545
Boris "「[firstname]……！\n
危ないよ！」"

play sound se_0051
camera at hpunch
camera at vpunch
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぐっと、後ろから腕を掴んで引かれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一歩を踏み出そうと前のめりになりかけていた重心を無理矢理に後ろに戻されたせいで、呼び止めたボリスの腕の中へとよろける。"

play sound se_0127
pause .4
play sound se_0127
pause .4
play sound se_0127
pause 1
hide bor_m_01_2


scene bg27_rk_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その眼前、すれすれのところをとんでもない勢いで、箒に跨った生徒が通り過ぎていった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_8")
T "（び、びっくりした……！！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "心臓が跳ねた。\n
あのまま前に出ていたら、危うく彼らに轢かれるところだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「ありがとう、ボリス。\n
助かったわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「今の……、何？\n
双子じゃなかったわよね……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "廊下における、箒の高速レースは双子とボリスの得意技だ。\n
だが、ボリスはこうして私と一緒にいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "双子かとも思ったのだが、どうもちょっと雰囲気が違っていた。"


show bor_m_03_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0546
Boris "「ディーとダムじゃないよ。\n
……最近さ、増えているんだよね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「増えているって……、廊下で箒レースの参加者？\n
……そのわりに嬉しくなさそうね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつも楽しげに悪さをしているボリスなのだが、今はなんだかばつの悪そうな顔をしている。"

hide bor_m_03_6
show bor_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0547
Boris "「委員長さんの言いつけだとか校則破って悪さしている、俺の言えたことじゃないんだけどさ。あいつら、ちょっとルール違反が酷いんだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「ルール？\n
箒レースにそんなのがあったの？」"

hide bor_m_03_9
show bor_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice bor_g0548
Boris "「あるんだよ、一応。\n
たとえば、俺達が箒レースをやるときはコースが決まっているんだ」"

hide bor_m_01_11
show bor_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice bor_g0549
Boris "「どこからどこまで、どんなふうに飛ぶかっていう、ルールがあるんだよ。\n
……まあ、たまにそこから外れることもあるけど」"

hide bor_m_01_10
show bor_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice bor_g0550
Boris "「必ず始める前にイベントとして告知する。\n
守れる範囲でのルールは保たれているってわけ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（そういえば……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一番最初、私が双子の暴走に行き当たったときも、私以外の生徒達は皆見物としてわざわざ廊下を空けて声援を飛ばしていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ああやってイベントにしてしまうことで、逆にある程度の安全を確保していたということなのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「でも、彼らはそうじゃないのね？」"

hide bor_m_03_10
show bor_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice bor_g0551
Boris "「あいつらはレースっつーよりも、鬼ごっこなんだよね。\n
だから、ルートも決まってない」"

hide bor_m_03_9
show bor_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice bor_g0552
Boris "「それに何より俺が気に食わないのはさ。\n
あいつら、顔を隠しているんだよな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_10")
T "「……え？」"

hide bor_m_03_3
show bor_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_10")
voice bor_g0553
Boris "「俺や双子は、堂々と悪さして、楽しんだ後は委員長さんに怒られたりだとかしているわけなんだけど。あいつら、覆面被って鬼ごっこしているんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「えええええ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "廊下を高速で飛びまわっているだけでも充分危ないというのに、そこでさらに覆面をしているとは危険極まりない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普通に考えて、そんなものを被っていては視界が狭くなるだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（……卑怯でもあるけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分達が怒られないように、自分達は責任に問われないようにしながら、校内で危険なことをしている。"

hide bor_m_01_8
show bor_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0554
Boris "「……それでも普段なら、一応もっと人が少なくなった時間からやり始めるんだけどな」"

hide bor_m_02_10
show bor_m_02_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0554_5
Boris "「今日は、テンション上がっちゃっているのかもね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「例のアレで？」"

hide bor_m_02_13
show bor_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice bor_g0555
Boris "「そ、例のアレで」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私達新入生には教えてくれない例のイベントだ。\n
今からこんな騒ぎを起こしていては、夜になったらどうなってしまうのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（イベントは楽しみだけど……。\n
それ以上に不安が……）"

hide bor_m_02_3

with dis
$ hi_mes()

scene bg27_rk_day with Dissolve(.8)

scene bg10_sb_day
with stripe_l_medium

scene bg_map_day
with stripe_l_medium

scene bg_par15_rg_tow_day
with stripe_l_medium

scene bg_par23_jr_k
with stripe_l_long

play music quiet_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "カフェテリアまで寄って、差し入れを用意してから作業室へと向かった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつまでも紙コップというのも切ないので、私の手にしたお盆の上には二人分の珈琲カップとクッキーの盛られた皿が載っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "カフェテリアの珈琲なんて聞いたらユリウスは顔をしかめそうだが、カップを手に入れるためだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それに普段淹れてもらうばかりというのも、なんだか悪い。\n
たまには、私のほうから休憩を申し出てもいいだろう。"

play sound se_0217
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "辿り着いた先、片手で盆を支えてノックをする。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0631
Hatena "「……おや。\n
誰か来たぞ、委員長」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（……あら？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "部屋の中から、ユリウスではない声がする。\n
誰か、客でも来ているのだろうか。"

play sound se_0199

show bra_m_02_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Blood "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ドアを開けてくれた人物と、見詰め合ってしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "つい先日カリスマ性が何だのと噂になっていた人物、帽子屋寮寮長のブラッド＝デュプレだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "お互い呆気に取られて見詰め合っていたのだが、先に我に返ったのはブラッドのほうだった。"

hide bra_m_02_6
show bra_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0632
Blood "「……ふ。\n
委員長、君が先ほどからさっさと帰れと繰り返していたのは、こういうわけだったのか」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0175
Julius "「……うるさい。\n
余計なことを喋っていないで、さっさと自寮に帰れ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0176
Julius "「仕事の話はすんだだろう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……仕事？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "想定外の取り合わせだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスはシンフォニア学生の風紀を取り締まる風紀委員長。\n
ブラッド＝デュプレといえば、アウトローの代表格だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな二人が、こんな私的な空間で会っているなんて誰が想像しただろう。\n
寮長同士の話し合いといったふうでもない。"

hide bra_m_03_3
show bra_m_03_15 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0633
Blood "「そんなところに立ち尽くしていないで、入ったらどうだ、お嬢さん。\n
ああ……、だがその香りは耐え難いな」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドは半身引いて私を招きいれようとするものの、ほかほかと湯気を放つ珈琲二つには露骨に顔をしかめた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "紅茶派で有名な彼には、珈琲の芳香も悪臭に等しいらしい。\n
すっと持ち上がる右手に握られていたステッキが、コンっと軽く盆に触れる。"

play sound se_0174
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……っわ！？」"

play sound se_0731
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなに強い衝撃ではなかったとはいえ、ぐらりとカップの中身が揺れて……。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「……ええ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "小さくちゃぷっと水のはねる音がしたかと思った次の瞬間には、カップの中身の色が変わっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "深い黒色から、澄んだ琥珀色への変化に合わせて、周囲に漂う香りまでが変わっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、ついでに、カップの数までも。"

hide bra_m_03_15
show bra_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0634
Blood "「ふう。\n
やはり紅茶の香りはいい……、安らぐな」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Julius "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドはとことんマイペースだ。\n
三人分に増えたティーカップのうちの一つを、さっそく手にとっている。"

hide bra_m_02_5


scene bg_par06_jr with stripe_l_medlong

play music tower_room1_p_ali
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつまでも立ち尽くしていても仕方がないので、私も部屋の中へと足を踏み入れた。"

play sound se_0546
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスの作業机の上に盆を下ろして、紅茶のカップを手にとる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（……いい匂い）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は紅茶も珈琲も、ココアだろうがホットミルクだろうが、何でも美味しくいただけるわけなのだが……、ユリウスはどうなのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドが珈琲を受け付けないように、彼にも拒否反応があるのだろうか。"


show yuri_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Julius "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスは無言で、ティーカップを手に取った。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（珈琲が好きだけど、紅茶も駄目ってわけではないのね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いいことを知った。\n
紅茶なら、私もそれなりに美味しく淹れることが出来る。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「ねえ、なんでここにブラッドがいるの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一口、紅茶を味わってから切り出す。"

hide yuri_m_01_11
show yuri_m_01_11 at left
with dis

show bra_m_02_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0635
Blood "「おや、私がここにいては困るのか？\n
はは、逢引の邪魔をするつもりはなかったんだがね」"

hide yuri_m_01_11
show yuri_m_03_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0177
Julius "「……っ！！」"

hide yuri_m_03_3
show yuri_m_03_7 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0178
Julius "「逢引なわけがあるか。\n
こいつが勝手に私の部屋に押しかけてくるだけだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（……む）"

hide bra_m_02_2
show bra_m_02_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice blo_g0636
Blood "「おやおや、そうなのかお嬢さん？\n
どうだ、こんな唐変木の部屋などやめて、私の部屋にこないか？」"

hide bra_m_02_1
show bra_m_03_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice blo_g0637
Blood "「きっとお嬢さんを満足させて……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「何の話よ。\n
それよりも……、あなた達、仲よかったの？」"

hide yuri_m_03_7
show yuri_m_02_7 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice jul_g0179
Julius "「……っぐ」"

hide bra_m_03_4
show bra_m_02_17 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice blo_g0638
Blood "「……っぐ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の素朴な疑問に、二人して咽かけたのか、同時に嫌そうな声をあげた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（仲良し……、じゃなさそうね。\n
少なくとも、それを認め合う間柄ではなさそう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……いや、私も「仲がいい」という言葉がこれほど違和感があるとは思っていなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "第三者の口から聞いていたら、きっと同じ反応をしていただろう。"

hide yuri_m_02_7
show yuri_m_02_11 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0180
Julius "「……この男と仲がいいなんてことがあるわけないだろう。\n
たまたま今回は利害が一致しただけだ」"

hide bra_m_02_17
show bra_m_02_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0639
Blood "「言い換えれば……。\n
利害さえ一致したならば協力しあえる程度には仲良し、なのかもしれないな？」"

hide yuri_m_02_11
show yuri_m_02_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0181
Julius "「……言い換えるな。\n
余計に気分が悪くなる」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（……まあ、確かに）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（それにしても……、風紀委員長と不良のボスで一致する利害って何？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の頭の上にはクエスチョンマークがぐるぐると回っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それに気付いていながら、答える気がないのか黙って紅茶を啜るユリウスと、焦らす気満々という顔のブラッド。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "教える気がありそうなだけ、ブラッドのほうがマシだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「それで、利害って何なのよ？」"

hide yuri_m_02_8
show yuri_m_03_12 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice jul_g0182
Julius "「おまえには関係ない。\n
……帽子屋、おまえも用がすんだならさっさと帰れ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうも私には聞かれたくないのか、ユリウスはつっけんどんだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……いいじゃない、教えてくれたって。\n
いいわよ、ブラッドに聞くから」"

hide bra_m_02_2
show bra_m_03_15 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice blo_g0640
Blood "「そうだな、お嬢さん。\n
君がこの堅物ではなく私に付き合ってくれるというなら、睦言代わりに喜んで語ろう」"

play sound se_0551
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「……っわ！！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いきなりウェストに手がかかり、ぐいっと引き寄せられて焦る。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、身の危険を感じたというわけでなく、単純に手に持ったティーカップの中身を案じただけだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドの声には笑みが滲んでいるし、風紀委員長であるユリウスの目の前でそんな馬鹿なことをするわけもない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「ちょっとブラッド、悪ふざけは……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "苦情を言いながら、私の体を抱き寄せたブラッドを見上げて息を飲んだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（……先生に、似ている？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "目を瞠ってしまう。\n
彼の体から漂う紅茶の香りは、懐かしい家の匂いでもある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "柄にもなく、硬直してしまった。"

hide yuri_m_03_12
show yuri_m_03_7 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0183
Julius "「おい、[firstname]？\n
帽子屋、悪ふざけがすぎるぞ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の様子がおかしいのに気付いたのか、ユリウスがブラッドへと制止をかけた。\n
一方ブラッドのほうも、訝しげに眉根を寄せて私を見下ろす。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これぐらいの接触は彼にとって、遊びの範囲。\n
何度か接したときも、悪ふざけとしてからかわれたことがある。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（私だって、動揺しないのに。\n
……普段なら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は賢い男だ。\n
悪ふざけをするにも、ちゃんと相手を選ぶ。"

hide bra_m_03_15
show bra_m_02_6 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0641
Blood "「……お嬢さん？\n
どうしたんだ、そんなバケモノでも見た顔をして」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「……どうして、かしら。\n
あなたを見ていて、今朝見た悪夢を思い出したの」"

hide bra_m_02_6
show bra_m_02_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_3")
voice blo_g0642
Blood "{size=+20}「失礼だぞ、お嬢さん」{/size} "

hide yuri_m_03_7
show yuri_m_01_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_3")
voice jul_g0184
Julius "「ああ、さぞかし悪い夢見だったんだろうな。\n
……こいつの夢なんて」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「いやいや、別にブラッドの夢を見たわけじゃないのよ？\n
ただ、なんとなく思い出しただけ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドに、先生の面影を重ねてしまった。\n
よくよく見れば、そんなに似ているところなんてないというのに。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（夢見が悪かったせいよね、本当）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぱ、とブラッドが手を放して解放してくれた。\n
一息ついて、どうやら無事だった紅茶のカップを持ち上げる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "つい先刻までは美味だったその味が、今はなんだか物足りなく感じられた。"

hide yuri_m_01_3

hide bra_m_02_7
##[chara2 PAY ATTENTION="false"]
with dis
$ hi_mes()

scene bg_par15_rg_tow_day
with stripe_l_medium

scene bg_map_day
with stripe_l_long
##endmemory
jump gakuen_julius4
