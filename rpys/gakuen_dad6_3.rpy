label gakuen_dad6_3:
if lovechara_deedam_points == 9:
    jump gakuen_dad6_3a
jump gakuen_dad6_3b
label gakuen_dad6_3a:
menu:
    "（ここまで来たら、勝っても負けても……）":
        jump gakuen_dad6_3b
    "（いやいや、やっぱり勝ちたい……！）":
        jump gakuen_dad6_3c
label gakuen_dad6_3b:
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0040
Servant "「捕まえたぞ……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0035
Maid "「子供のときのツインズには、まだ負けませんよ！」"

play sound se_0403


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぎりぎりのところで逃げ切れず、使用人達の手が私達へと届いた。\n
同時に空気が抜けるような音がして、私達の魔法が一斉に解除されてしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_9")
T "「……！！」"


play music night_garden_p_ali

scene bg20_gd_nig with Dissolve(1.6)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "逃走中ということもあり、勢いのついていた体は前方へと投げ出される……。\n
と、身構えたのだが、そんなことにはならなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すぐさま別の使用人が発動させた魔法により、静かにその場で停止させられる。\n
私にとっては初めての経験だったのだが、ディーとダムは慣れているようだ。"


show dee_m_01_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0360
Dee "「あ～あ……。\n
せっかくお姉さんと愛の逃避行だったのに、捕まっちゃうなんてついていないよ」"

hide dee_m_01_5
show dee_m_01_5 at left
with dis

show dam_m_01_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0361
Dam "「そうだね、兄弟。\n
やっぱり大人にならないと、いろいろ不便だね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「……どうして、大人にならなかったの？」"

hide dee_m_01_5
show dee_m_01_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice dad_g0362
Dee "「お姉さん、大人の僕達のこと、苦手でしょ？」"

hide dam_m_01_5
show dam_m_01_10 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice dad_g0363
Dam "「だからね、子供のままでも使用人達に勝てるって証明したかったんだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「二人とも……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "誤解だ。\n
私は別に二人の大人の姿を苦手だとは思っていない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いや……、ある意味苦手なのだろうか。\n
大人の格好で子供のときと同じように無邪気に接せられると、照れたりときめいてしまったりと、いろいろと大変なのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼らは外見だけが大人になっているだけなので、問題ないかもしれないが、私にとっては大問題。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だから、大人な彼らに対しての態度は、ちょっとぎこちなくなってしまっている部分がある。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_7")
T "（気にしてくれていたのね……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こんなふうに、気にかけてくれていたとは驚きだ。"

hide dee_m_01_1

hide dam_m_01_10


show maid_b_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0036
Maid "「ふふ。\n
勝てませんでしたね」"

hide maid_b_6
show maid_b_6 at left
with dis

show siyounin_a1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tan_g0030
Servant "「ブリーズなのにストームの真似ごとをするとは、大胆すぎですよ……。\n
負けて当然です」"


show dee_m_02_3 at center
with dis
hide siyounin_a1_2

hide maid_b_6

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0364
Dee "「ふん、だ！\n
次は勝つよ！！」"

hide dee_m_02_3
show dee_m_02_3 at left
with dis

show maid_b_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0037
Maid "「次、ですか……。\n
懲りない子達ですこと」"

hide maid_b_3
show maid_b_3 at left
with dis

show siyounin_a2_1 at right
with dis
hide dee_m_02_3

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tan_g0031
Servant "「それでは、ちょっとは懲りてもらえるよう、あなた方二人には三週間分のお掃除をお願いしましょう」"

hide siyounin_a2_1
show siyounin_a2_1 at left
with dis

show dee_m_02_7 at right
with dis
hide maid_b_3

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0365
Dee "「えええええ～！？\n
なにそれ！三週間！？子供相手に横暴だよ！？」"

hide siyounin_a2_1
show siyounin_a1_1 at left
with dis
hide dee_m_02_7
show dee_m_02_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tan_g0032
Servant "「残念。\n
大人というのは横暴なものなんです」"

hide dee_m_02_7
show dee_m_02_7 at left
with dis
hide siyounin_a1_1
show dam_m_02_6 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0366
Dam "「ブリーズの夜なんだから大目に見てよ～」"

hide dee_m_02_7
show maid_b_8 at center
with dis
hide dam_m_02_6

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0030
Maid "「大目に見られるのは、女子生徒だけですよ。\n
あなた達はお説教です」"

hide maid_b_8
show maid_b_8 at left
with dis

show siyounin_a1_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tan_g0033
Servant "「そうそう、今はストームじゃないんですからね。\n
ほら、男子寮へ戻って、戻って」"

hide maid_b_8
show maid_b_10 at center
with dis
hide siyounin_a1_7

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0031
Maid "「……あなたは、私と一緒に、一度女子寮に戻りましょうね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「は～い」"

hide maid_b_10
show siyounin_a2_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice tan_g0034
Servant "「ほら、行きますよ……」"

play sound se_0624
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "メイドさんに促されて私は女子寮へと、ディーとダムは使用人に促されて男子寮へと向かって歩き出す。"

hide siyounin_a2_5


scene bg06_sk_h_nig with Dissolve(1.6)
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（……これじゃあ、ブリーズの続きは無理ね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私へと課せられるのは、一度最初に戻る、ということだけだ。\n
ブリーズのルール通りで、罰にもならない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一度寮の自室に戻ってさえしまえば、再出発は別に禁止されてはいないのだ。\n
イベントごとの続きを楽しむことも出来る。"


scene bg20_gd_nig
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "けれど……、あの二人と会えないならば、男子寮に向かっても意味はない。\n
彼らはこれからお説教タイムだろうから続行は無理だ。"


show dam_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0367
Dam "「お姉さん！\n
また明日遊ぼうね！！」"


show dee_m_01_6 at left
with dis
hide dam_m_01_6
show dam_m_01_6 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0368
Dee "「また明日ー！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_9")
T "「……もう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今からお小言、明日以降には罰掃除が待っているというのに、二人はのんきなものだ。\n
どうせまた、逃げ出す気なのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私に向かって大きく手をふりふり、男子寮へと見えなくなっていった。"

with dis
$ hi_mes()
hide dee_m_01_6

hide dam_m_01_6
##[chara2 PAY ATTENTION="false"]

scene bg_par15_rg_hat_nig
with stripe_l_medium

scene bg_map_nig
with stripe_l_medium

scene bg_map_day
with stripe_l_medium

scene bg_par15_rg_hat_day
with stripe_l_medium

play music daytime_a_wam

scene bg20_gd_day
with stripe_l_long
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズやストームというのは、健全だとはいうものの大胆なイベントだ。\n
何せ、一時とはいえ男女が室内で二人っきりになることができる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それをきっかけに仲が進展することも多いはず。\n
後から聞くところによると、カップルが成立する率も低くないらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、カップルというにはちょっといろいろ特殊な事情がある私達はといえば、木陰で三人仲良く涼んでいた。"

play sound se_0464

show m_twi_goodend1 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0368_5
Dee "「お姉さん、次は絶対負けないからね！\n
そしたら……、僕達と付き合ってくれる？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "木の幹に背中を預けて座る私の、それぞれの足を枕に双子が芝生に転がる。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0369
Dam "「次は絶対に負けないから……！\n
僕達が勝ったら、僕達と付き合ってね！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_14")
T "（僕達、ね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ひとくくりになることも、今は違和感がないものの。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_3")
T "「……そうね、考えておくわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "結局、特に何かが変わることもなく、相変わらずの関係を続けている。\n
双子の私に対する想いが、何であるのかは今も明確ではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "同じく、私が、双子に対して抱いている気持ちの正体もよく分からない。\n
よく分からないままに、私達の関係は形を変えないままに続いている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（……形を変える機会がなかったのよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズの夜を一緒に過ごしていたのならば、もしかするともっと違った関係になっていたのかもしれないが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……なんて、終わってしまったことを考えても仕方がない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ディーとダムの二人も、すでに次のストームとブリーズへと目標を絞っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今のところ二人の目標は、大人への変身魔法を使うことなく、使用人達に勝つことだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_7")
T "（そして、私と付き合うこと）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "くすぐったいような気持ち。\n
これは、期待なのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "イベントとしても、方向性としても、間違っている。\n
私は年長者として、止めるべきなのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_17")
T "「……ま、いいわよね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "終わったばかりで、そんなに先のことを考えるほど計画的でも、大人でもない。\n
考える時間ならばたっぷりとある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "次のストームとブリーズまで、あと一年。\n
二人と一緒に成長していけばいい。"

scene m_twi_goodend1
hide frame_par_togaki
hide ali_m_06_16
with Dissolve(5)

stop music
##endmemory
jump gakuen_b
label gakuen_dad6_3c:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "諦めにも似た感情がよぎってしまったが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_9")
T "（いやいや、やっぱり勝ちたい……！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここまで来たら、やはり勝ち抜けたい。\n
そう、私が強く思った瞬間のことだった。"

play sound se_0504

play music denouement_a_ali
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "激しい銃声が連続して響く。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0041
Servant "「な……！！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0038
Maid "「これは……！！」"

play sound se_0505
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本物の銃ではないものの、威力は強い。\n
そして、実際の銃撃では有り得ないほど正確。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その魔法の弾幕は、私達と使用人達の間に正確に線を引くようにして撃ち込まれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "使用人達はそのラインを超えることが出来ず、たたらを踏んで停止する。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「！！」"

scene bg_par12_hct_nig ##instantPAY ATTENTION="true"]

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "視線を向けた先、帽子屋寮のテラス。"

##[rchara2 PAY ATTENTION="false"]
show eri_m_01_1 at left
with dis

show bra_m_01_11 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "マシンガンを片手にけだるそうにしている男と目が合った。\n
その傍らで、緩くこちらに向かって手を振っているのはエリオットだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0370
Dee "「うわ！？ボスが援護してくれるなんて……！\n
どういう風の吹き回し！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0371
Dam "「わ～、すごい気まぐれ……。\n
……高くつきそう」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_2")
T "「……なんにしても、感謝」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私達は、思いも寄らぬ援護のおかげでどうにか逃げ切り、男子寮の中に滑り込んだ。"

play sound se_0347
play sound se_0381
with dis
$ hi_mes()
hide bra_m_01_11

hide eri_m_01_1

pause .4

scene bg_par15_rg_hat_nig
with stripe_l_medium
pause .4

scene bg25_rr_nig
with stripe_l_long
pause .4

play music night_a_wam
play sound se_0001
pause .2
play sound se_0398

scene bg23_rd_nig
with stripe_l_long
play sound se_0399
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_6")
T "「……っ、はあ、はあ」"


show dee_m_02_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_6")
voice dad_g0372
Dee "「……っ、はは」"

hide dee_m_02_7
show dee_m_02_7 at left
with dis

show dam_m_02_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_6")
voice dad_g0373
Dam "「……、スリル、あったね、お姉さん……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ディーとダムの二人にそれぞれ手を引かれ、縺れ込むようにして辿り着いた先の部屋。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私達はドアを閉めると同時に、そのドアに背中を預けてずるずると座り込んでしまっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニアの生徒として恥ずかしくないだけの体力はあると思っていたのだが……、ここまでの運動は想像外だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（ここは一体何の学校なんだって思うわよね、本当に……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "魔法使いの学校のくせに、体力を必要としすぎだ。\n
さすがの双子も疲れたように、ドアに背中を預けている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（あれだけ魔法を使ったんだもの。\n
私よりもよっぽど疲れているはず……）"

hide dee_m_02_7
show dee_m_01_12 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_10")
Dee "「…………」"

hide dam_m_02_7
show dam_m_01_12 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_10")
Dam "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……ふう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "休憩を挟み、ばくばくと脈打っていた心音や、荒く弾んでいた吐息も徐々に落ち着きだした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "視線を上げ、改めて双子の部屋を観察してみることにした。"

hide dee_m_01_12

hide dam_m_01_12

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "日頃は、互いの寮の行き来は禁止されている。\n
こうして、二人の部屋を訪れるのは初めてのことだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「……広い、はずなのに。\n
そう見えないのが不思議よね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニアの学生寮は、基本的には一人一部屋を与えられる。そんな中、ディーとダムは特別に二人分の広さのある部屋に、二人で暮らしている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドが許可を与えたのだろうか。\n
彼なら、許しそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "帽子屋寮においては、重要なルール、規則については校則に則っているものの、瑣末な部分においては、ブラッド＝デュプレの趣味や主義が反映されている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "双子の部屋には、そんな寮長のアバウトさがよく反映されているように見えた。"


show dee_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0374
Dee "「最初はもっと広かったんだけどね。\n
僕や兄弟のコレクションが増えるにつれて、どんどん手狭になってきているんだ」"

hide dee_m_02_10
show dee_m_02_10 at left
with dis

show dam_m_02_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0375
Dam "「もっと広い部屋がほしいよ。\n
……あと一つぐらい壁を壊しても怒られないかな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「え？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二部屋分の広さのある部屋を、二人で使っているのだと思ったが……。\n
そういえば、基本一人一部屋なので、造りとして珍しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（女子寮にも、こんな部屋はないし……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_7")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「ま、まさか自力で……？」"

hide dee_m_02_10
show dee_m_02_11 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice dad_g0376
Dee "「うん、壁なんて邪魔なだけだからね。\n
僕と兄弟で壊しちゃったんだよ」"

hide dee_m_02_11
show dee_m_02_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice dad_g0378
Dee "「楽しいんだよ。\n
溶かしたり、割ったり、削ったり……」"

hide dam_m_02_8
show dam_m_02_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice dad_g0379
Dam "「いろんな攻撃魔法の効果を試せるんだ。\n
でも……、危うく上の階が崩壊しかけたのには驚いたね、兄弟」"

hide dee_m_02_2
show dee_m_02_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice dad_g0380
Dee "「そうだね、あれは驚いたよ、兄弟。\n
まさか僕達の住む帽子屋寮が、耐震偽装仕様だったなんてね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "建築家が怒り出すようなことを言う。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「……本来ないといけない壁を、無計画に取っ払ってしまえば、そりゃあ崩落も起きるわよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「あんた達、退寮する際に、莫大な修繕費用を求められても知らないからね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "部屋を借りて暮らす以上、その部屋に傷をつけることはせず、借りたときと同じ状態で返すことを求められるのは常識だ。\n
学生寮といえど、そこは同じだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だというのに、ここまで派手な大改造を施してしまったこの部屋を、この二人はどうやって学校側に返却するつもりなのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "魔法で壊されたものは、魔法で修復しやすいという特性があることにはあるが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それだって、あまり時間が経ちすぎてしまうと、希望するほどのアドバンテージを持たなくなってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_7")
T "（大雑把……）"

hide dee_m_02_5

hide dam_m_02_4

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "よいしょ、と私は立ち上がって部屋の中を見渡す。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（……男の子の部屋だなあ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "散らかっている、のとは違う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "物が多いせいか、雑然とした印象が強いだけで、実際にはきちんとそれぞれがそれぞれのあるべき場所に置かれていることが分かる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私や、姉さん、イーディスの部屋とはずいぶんとイメージが違う。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_10")
T "「ふふ」"


show dam_m_01_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_10")
voice dad_g0382
Dam "「何か気に入ったものがあった？\n
僕らの宝物だけど、お姉さんにだったらあげてもいいよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「いいえ、違うの。\n
ほら、いろんなものがあるけど……、どれもちゃんと二つずつあるんだなあと思って」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_10")
T "（双子らしい）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "色違いだったりもするが、大体部屋にあるものは対になって揃えられている。"

hide dam_m_01_7
show dee_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0383
Dee "「兄弟が好きなものは、だいたい僕も好きだからね。\n
双子だから、趣味がよく似ているんだよ」"

hide dee_m_01_6
show dee_m_01_6 at left
with dis

show dam_m_01_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0384
Dam "「だけど、一つだけだと喧嘩になっちゃうからね。\n
そうなると……、僕ら壊しちゃうんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "するりと二人が私の傍らへと歩み寄った。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "無邪気な色を浮べた、赤と青。\n
二つの瞳が私をじっと見上げる。"

hide dee_m_01_6
show dee_m_02_13 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0385
Dee "「兄弟に取られちゃうと、嫌だから」"

hide dam_m_01_3
show dam_m_02_11 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0385_5
Dam "「兄弟が独り占めするなんて、ずるいから」"

hide dee_m_02_13
show dee_m_03_10 at left
with dis
hide dam_m_02_11
show dam_m_03_12 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0386
Dam "「だから、壊すんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぞくりとした。\n
二人の声に、特に思い入れはない。\n
淡々と、響く。"

hide dee_m_03_10
show dee_m_03_9 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0387
Dee "「僕と兄弟を喧嘩させるなんて、悪い玩具だからね。\n
二人で仲良く、壊しちゃうんだ」"

hide dam_m_03_12
show dam_m_03_11 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0388
Dam "「そうすると、ほら。\n
僕と兄弟は仲のいい双子でいられる」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_11")
T "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それぞれ、右と左、彼らの腕が私の腕へと絡みつく。\n
ぎゅっと抱きしめられた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "抱きしめられた腕から伝わる、彼らの体温と、心音。\n
二つの……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_17")
T "（……心臓の音）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうしてか、不思議な気分になる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "不思議な……、泣きたいような気分だ。\n
彼らからは、二人分の心音がして、生きているのだと実感する。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（当たり前なのに……。\n
変なの）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "とても、特別なことに感じられる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「……私のことも、壊しちゃうの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人への問いかけは、穏やかだった。"

hide dee_m_03_9
show dee_m_02_7 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0389
Dee "「まさか……！\n
お姉さんは、玩具なんかと違って、代わりがきかないからね」"

hide dam_m_03_11
show dam_m_02_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0390
Dam "「お姉さんは、僕と兄弟の二人とも好きでいてくれるでしょう？\n
選んだり、しないよね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "縋るような目を向けられる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「選ぶのが悪いみたいに言うのね。\n
普通は、自分だけを見てほしがるものじゃないの？」"

hide dee_m_02_7
show dee_m_01_7 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice dad_g0391
Dee "「うん、お姉さんに選ばれたら、きっと幸せだと思うよ。\n
とっても嬉しい」"

hide dam_m_02_7
show dam_m_02_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice dad_g0392
Dam "「だよね、お姉さんに選んでもらえたら、幸せだよ。\n
他に何もいらない、って思うかもしれない」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……大袈裟ね」"

hide dee_m_01_7
show dee_m_01_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice dad_g0393
Dee "「大袈裟じゃないよ。\n
選ばれて一人だけになるって、すごいことだから」"

hide dam_m_02_4
show dam_m_01_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice dad_g0394
Dam "「でも、寂しいことでもあるんだよ。\n
一人ぼっちになる」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぎゅ、っと二人が私の腕に抱きつく力が強くなった。\n
振りほどこうとなどしていないのに、そうされることを恐れているかのようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「元々、あなた達は違う二人よ。\n
ディーはダムの代わりにはなれないし、ダムもディーの代わりにはなれないわ」"

hide dee_m_01_2
show dee_m_01_9 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_13")
voice dad_g0395
Dee "「そうかな、兄弟。\n
……どう思う？」"

hide dam_m_01_5
show dam_m_01_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_13")
voice dad_g0396
Dam "「ふふ、お姉さんは可愛いね。\n
気付いていないんだね」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……何に？）"


show m_twi6_5and7 onlayer master
with dis
hide dee_m_01_9

hide dam_m_01_7

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私を見上げる二人が、同じ表情で笑う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつもなら、同じ顔でも色の違いから別の人間だと認識できる二人。
しかし、途端に同一化してしまったような錯覚に襲われる。"

play sound se_0496
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Dee "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ディーが小さく呪文を唱えた。"

hide m_twi6_5and7
show m_twi6_6 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_6")
T "（目の、色が）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まったく同じ造作をした二人の顔を見分けるための、最大のヒントはその目の色だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その違いが分かりやすすぎて、他に注意がいかないほど。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ディーは青い色。\n
ダムは赤い色。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その二色がぼんやりと滲んで、その色を変えていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぱちり、と私が一度瞬きを挟んだ間に、二人はすっかりその立ち位置を変えてしまっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ディーだったはずの子の目が、今は赤く。\n
ダムだと思っていた子の目が、青い。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0397
Dee "「ねえ、お姉さん。\n
僕が誰か分かる？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0398
Dam "「お姉さん、僕は誰か当てられる？\n
……分かるかな？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_7")
T "（分からない。\n
分かるわけがない）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私でなくとも、この二人を見分けることなど誰にも出来ないだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ただ、この二人と親密な関係を築き、そして新しく一歩を踏み出そうと思っていた私にとっては、少なからずショックなことだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分の好きな相手の違いすら、見分けられないなんて。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（……代わりにはなれないなんて、偉そうなことを言っておいて）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「もしかして……。\n
今までも、入れ替わったりしていたの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice dad_g0399
Dee "「うん、そうだよ。\n
でも入れ替わるというよりも、好きな色を交換するだけだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice dad_g0400
Dam "「お姉さんだって、毎日同じ色だったら飽きるでしょう？\n
だから、交換してみるんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "遊び飽きた玩具を交換するのと同じ感覚で、彼らは互いの姿も入れ替えてしまう。"

play sound se_0496
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Dee "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "再び、双子の片割れが呪文を唱えた。\n
その目の色が薄くなっていき、ある一定のところまでいってするりと反転する。"

hide m_twi6_6
show m_twi6_5and7 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0401
Dee "「話し方も変えちゃえば完璧。\n
見抜ける奴なんかいないよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あっという間に、二人はもとの位置関係へと戻った。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0402
Dee "「ね？だからね、お姉さん。\n
もし片方を嫌いになっても、好きなほうになるから安心してね」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0403
Dam "「二人が嫌で一人がいいなら、うまく入れ替わるよ。\n
どっちか分からないように……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_8")
T "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人ともを好きなんて、悪いことのように思っていた。\n
少なくとも、常識からは外れている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、今はいいことのように思える。\n
二人に対して、こう言えるから。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「……私は、二人とも好きなの」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_7")
T "「見分けられもしないで、偉そうなこと言えないけど。\n
二人とも、大事だって思っているわ」"

hide m_twi6_5and7
show m_twi6_8 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_7")
voice dad_g0404
Dee "「……選ばないでいてくれたほうがいいよ。\n
入れ替わっても、そうでなくても、三人でいられる」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice dad_g0405
Dam "「選んだりしないで。\n
二人で大事にするから……、壊れちゃわないでね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぎょ、とせざるを得ない言葉を、ダムが耳元で囁いた。\n
いや、もしかしたらダムではないのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人は、左右から、すがるように私を抱きしめる。"

play sound se_0328
play sound se_0148
hide m_twi6_8
show m_twi6_9 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのまま押し倒されて、背中からベッドに着地した。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふかふかに柔らかいベッドには、何気なく私のタオルケットも一緒にかけられていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0406
Dee "「好きだよ、お姉さん。\n
大好き」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "好き、と。\n
呪文のように繰り返す "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "囁く声は、どちらのものか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_17")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_14")
T "（……どっちでもいい）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人ともいてくれれば、それでいい。\n
それで、私は満たされる。"

with dis
$ hi_mes()
hide m_twi6_9


scene bg_par15_rg_hat_nig
with stripe_l_medium

scene bg_map_nig
with stripe_l_long
##endmemory
jump gakuen_dad_end
