label fushigi_op_hatter1:
$ place_of_stay = "Hatter"
scene map_bg_autumn_day with ImageDissolve("gui/stripe_l.png", .8, ramplen=128, reverse=True)

scene charasel_bg_hatter_day with ImageDissolve("gui/stripe_l.png", .8, ramplen=128, reverse=True)

play music hatter_gate_p_ali fadein 1

scene bm_aut_01_1 with ImageDissolve("gui/stripe_l.png", 1.2, ramplen=128, reverse=True)
play sound se_0365

show dee_t_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice dad_f0001
Dee " 「この前買ったばっかりの、新型手榴弾！\n
この威力、現場で盛大に試さなくちゃ」"

hide dee_t_02_1 at center
show dee_t_02_1 at left
show dam_t_02_5 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice dad_f0002
Dam " 「そうだね、兄弟。\n
必要経費で落としたんだもの、ぱあっと使わなくちゃもったいない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 門の前で交わされている会話の物騒なこと。\n
漏れ聞こえてくる内容は、穏やかとはいえない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 門番がこんな会話をしていたら、誰も屋敷の中へ入りたくないだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_17")
T " （なんだって、いつもいつも物騒そうな……）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_11")
T " （……いや、物騒そう、じゃないわね。\n
実際に物騒なのよ、あの子達が安全だなんて口が裂けても言えない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 何しろ、ついている二つ名が『ブラッディ・ツインズ』だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 片時もその手から離さない大きな斧といい、彼らの持ち物で、安全なものなど私はこれまで見たことがない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 外見だけでなく、中身も。\n
無邪気そうな見た目を裏切る子供達。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_11")
T " 「……また、仕事かしら」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 帽子屋屋敷に滞在して短くないが、ここの仕事の状況は不規則すぎて、いまだに掴めない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_6")
T " （時間帯さえ、ころころと変わる世界なんだから……。\n
不規則なのは当たり前だけど）"

hide dee_t_02_1 at left
show dee_t_01_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_6")
voice dad_f0004
Dee " 「あ、お姉さん！\n
どこかに行くの？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_4")
T " 「！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 見つかってしまった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 門に近付いたところで、こちらに気が付いた二人が振り返り、敷地へ入ってくる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_8")
T " 「あ……、わ……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 駆け寄られて、隠れていたわけでもないのに、慌ててしまう。\n
いつだって、彼らの手にはぎらぎらした斧があるのだ。"

hide dam_t_02_5 at right
show dam_t_01_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice dad_f0005
Dam " 「どこかへ行くなら、護衛として僕達がついていってあげるよ。\n
ねえ、どこへ行くの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " まだ何も答えないうちから、出掛けることが決めつけられてしまっている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_14")
T " 「出掛けるとは言っていないでしょう？」"

hide dee_t_01_2 at left
show dee_t_01_5 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_14")
voice dad_f0006
Dee " 「え？でも、出掛けるんだよね？\n
……僕達には言えないようなところへ行くの？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_7")
T " 「そ、そういうわけじゃないわよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 外見上は私のほうが年上。\n
だが、完全に押し負けてしまっている。"

hide dam_t_01_2 at right
show dam_t_01_6 at right
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice dad_f0007
Dam " 「じゃあ、ついていってもいいよね？\n
いいでしょ、お姉さん」"

hide dee_t_01_5 at left
show dee_t_01_7 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice dad_f0008
Dee " 「僕達がいれば、安全だよ？」"

play sound se_0621
pause .3
play sound se_0621
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 今までずっと引き摺っていた物騒な箱から手を離した二人が、駆け寄ってくる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_17")
T " （いやあ……、むしろ、危険じゃないかしら。\n
……特に、その得体の知れない箱の中身とか、いかにも）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_02_18")
T " 「いいわよ、私は一人でも平気。\n
あなた達、これから仕事でしょう？」"

hide dee_t_01_7 at left
show dee_t_03_13 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_02_18")
voice dad_f0009
Dee " 「平気だよ、ちょっとだけなら休憩の範囲だもん。\n
お姉さんの護衛なら、ボスも怒らないよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " まとわりつく双子は私の手を引いて、今にも門を出ようとしている。\n
どちらが出掛けようとしていたのか分からなくなる構図だ。"

play sound se_0365
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 彼らは、私をずるずる……。\n
先ほどまでじゃれついていた、物騒な箱を放置して……。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_02_4")
T " （箱……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " あの箱の中身が、ただのおもちゃでないことくらい、私にも分かる。\n
彼らのおもちゃ箱は、いつだって危険でいっぱいなのだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_7")
T " 「いや、そういうわけにはいかないでしょう。\n
ブラッドやエリオットだって、怒るわよ？」"


show t_op_bousi1 onlayer master with dis
hide dee_t_03_13 at left

hide dam_t_01_6 at right

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_7")
voice eri_f0000
Elliot " 「……そう、その通りだ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_7")
Dee " 「！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_7")
Dam " 「！！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_7")
voice eri_f0001
Elliot " 「おまえら……、なに油売っているん\n
だっ！！！」"

play sound se_0309
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_7")
Dee " 「……！！！」"

play sound se_0309
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_7")
Dam " 「……！！！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_7")
voice dad_f0010
Dee " 「～～っ！\n
な、何するんだよ、ひよこウサギ！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_7")
voice dad_f0011
Dam " 「子供に手をあげるなんて、最低だよっ！\n
横暴ウサギっ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_7")
voice eri_f0002
Elliot " 「だから、俺はウサギじゃねえって、何度言ったら分かるんだっ！この、～～～\n
～～～ガキ！\n
頭に何も入ってねえんじゃねえのか！？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_7")
voice dad_f0012
Dee " 「頭の上に変なものをはやしているおまえに言われたくないよっ！！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_7")
voice eri_f0003
Elliot " 「黙れ！\n
クソガキ共！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 二人と真っ正面から睨み合ったエリオットは、彼らが持っていた箱を指差して、説教を続ける。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice eri_f0004
Elliot " 「火薬の取り扱いは慎重にしろって言っただろうがっ。\n
中途半端にしやがって……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice eri_f0005
Elliot " 「いいか！？\n
箱から取り出したままにしておいたら、\n
{size=+23}湿気って威力が落ちるだろ！」{/size} "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_17")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_12")
T " （えっ、そっちの心配……？）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_17")
voice may_f0000
Maid " 「そうですよ～。\n
私達だって困ってしまいます～」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_17")
voice kat_f0000
Servant " 「威力が弱くなると、倒せる数が減って面倒臭いですよ～？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_17")
voice may_f0001
Maid " 「そう、もし逃げられたりなんかしたら面倒ですもの～。\n
あとで追いかけるの、だるいですよ～」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 屋敷から出てきた使用人達（勿論武装済みだ）が、口々に訴える。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " マフィアとしては真っ当すぎる指摘なのだろうが、彼らもまた、どこか的外れな突っ込みをしている。"
show t_op_bousi2 onlayer master with dis
hide t_op_bousi1 with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0000
Blood " 「……はあ。\n
おまえ達、いつまで門前でどうでもいい言い争いをしているつもりだ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 気だるげな声に振り返れば、そこには見慣れた屋敷の主がいつも以上にだるそうに立っていた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_11")
T " （かったるそうにしちゃって……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " それはそうだろう、今の時間帯は昼。\n
彼のもっとも嫌悪する時間帯だ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_12")
T " 「……火薬の扱いについては、どうでもよくないと思うわよ。\n
ブラッド」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_12")
voice blo_f0001
Blood " 「どうでもいいさ。\n
すべてがだるくて、面倒で、退屈だ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_8")
T " 「だから、火薬の扱いは退屈なんてものじゃないと……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 私からすれば、退屈どころか、スリリングすぎる。\n
しかし、マフィアのボスときたら、退屈そのものの様子。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0002
Blood " 「火薬なんて、爆発しない限りは退屈なものさ、お嬢さん。\n
爆発でもすれば別だがね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_14")
T " 「……爆発すればいいとでも？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_14")
voice blo_f0003
Blood " 「まさか。片付けがだるい。\n
だが、何もないというのも、それはそれで退屈なものだ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_14")
voice blo_f0004
Blood " 「ただでさえ昼に仕事に出なければならないせいで、気分が悪いというのに……。\n
これ以上だるいことになったら、私は……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_12")
T " 「……部屋に戻るとか言わないでよ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 釘を刺すと、帽子の下から視線が投げかけられた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 先手を打たれたことを不満に思っているような、よく分かったなと感心しているような。\n
どちらとも取れる眼差しだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " どちらにしたって、ろくなものではない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_13")
T " （でも、なんだかんだ言っても……、行くんでしょう？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " このマフィアのボスが直接出掛けなければならないような仕事。\n
それだけ大きな仕事ということになる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 私だって、この世界のことも、この屋敷のことも理解し始めている。\n
そして、このけだるげなマフィアのボス、ブラッド＝デュプレについても。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 我らがボスは、やる気のない様子を装うのが上手。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " だが、大嫌いな昼に屋敷の門の近くまで出てきているのが、今回の仕事の重要性を物語っていた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_15")
T " （そうよ、なんだかんだと言っても、放り出したりしないくせに……。\n
見栄っ張りな人だわ）"


show t_op_bousi3 onlayer master with dis
hide t_op_bousi2 with dis

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_05_2")
T " 「ほら、仕事なんでしょう。\n
行ってらっしゃい」"

play sound se_0155
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " しっかりやってきなさいよ、というようにぽんぽんと白い上着を叩いてあげる。\n
彼は少し驚いたように目を見張り、にやりと笑った。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 相変わらず、本心の読みにくい、だが満更でもなさそうな顔だ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0005
Blood " 「何だかうまくあしらわれた気もするが……。\n
いいだろう」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0006
Blood " 「ふふ。\n
他でもない君がそう言うのなら、昼に出掛けるのも悪くないな」"


show t_op_bousi4 onlayer master with dis
hide t_op_bousi3 with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice dad_f0013
Dee " 「あ、ずるいよ、お姉さんっ。\n
僕達もちゃんと見送ってくれなくちゃ、不公平だよっ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice dad_f0014
Dam " 「僕達にも、いってらっしゃい、ってしてよ……。\n
ボスだけなんて、ずるいや」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " いつのまにエリオットの横を抜けたのか、間近に来た二人は自分の頭を出してくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 無邪気なその様子。\n
彼らの手にはそれぞれ身の丈よりも大きな斧があるが、それでも……。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_15")
T " （可愛いな）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 怖いという感覚よりも、自分を慕ってくれるその様子が何とも可愛く見えてしまう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 物騒そのもの。\n
それは、この屋敷に住む誰もが該当する。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 誰もが私にとっては同居人であり、同僚あるいは上司なのだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_02_17")
T " （私も、一員）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_03_15")
T " 「ディー、ダム、行ってらっしゃい。\n
無事に帰ってきてね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 期待に応えるように、色違いの帽子が乗った頭を撫でた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice dad_f0015
Dee " 「はーい、もちろん、お姉さんを心配させたりなんかしないよ。\n
超過勤務は労働者にとって損なだけだし、すぐに帰ってくるね」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice dad_f0016
Dam " 「うん。\n
特別手当は嬉しいけど、お姉さんのところに早く帰ってくるほうがもっと嬉しいからね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " にこにこと満足そうに笑う彼らは、斧を持っていても、幼く見える。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 見た目だけだ。\n
本当は私なんかに心配されるほど弱くないことは、分かっていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " だが、見送る立場としてはこれ以上の言葉はなく、その思いを否定する気にもなれない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 二人だけではない。\n
ブラッドにしても、エリオットにしても、彼らが仕事に出るときにはいつだって……。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 早く、無事に帰ってきてほしいと願っている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_02_15")
T " 「うん。\n
早く……、帰ってきて」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 差し出された頭に手をのせたまま、そう告げる。"

hide t_op_bousi4 with dis


show dee_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice dad_f0017
Dee " 「えへへ……。\n
お姉さんがそう言ってくれるのなら、すぐに帰って来られるように、僕ら頑張るねっ」"

hide dee_t_02_4 at center
show dee_t_02_4 at left

show dam_t_02_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice dad_f0018
Dam " 「お姉さん、言葉だけだと寂しくない？\n
不安なら、お見送りのキスをしてくれてもいいよ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_12")
T " 「……見送りのキスで不安が解消されるとも思えないけど」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 呆れたように肩を竦めると、大きな影が彼らの顔に被さる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 青と赤の服が遠退く代わりに、にょっきりと生えた長い耳と、ふわふわの髪が視界で揺れた。"


show eri_t_02_3 at center
hide dee_t_02_4 at left
hide dam_t_02_9 at right
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice eri_f0006
Elliot " 「ませガキ共が……。\n
調子に乗ってるんじゃねえよ」"

hide eri_t_02_3 at center
show eri_t_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice eri_f0007
Elliot " 「出掛けるところだったんだろうが……、悪いな、[firstname]。\n
仕事が終わったらすぐに戻ってくるから、留守番、頼むぜ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " つまり、今は危険だから、外出は控えろということ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " にこっと笑いかけてくる顔は、とてもこれから物騒な仕事に出るとは思えないほど穏やかだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 彼らの職業（といっていいものか）は、マフィア。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " それも今から出向こうとしているのは、ボスとその腹心が欠かせない、大きな仕事。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 双子が持っていた手榴弾にしてもそうだが、物騒なことになるのは避けようがない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 人を傷つけることになるだろうというのも予測がつく。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_6")
T " （でも、皆が無事に帰ってきてくれるなら……、それでいい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " ずるいと思っても、その他のことには目を瞑る。"


show bra_t_02_1 at center
hide eri_t_01_8 at center
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0007
Blood " 「早めに戻るから……。\n
いい子にしておいで、お嬢さん」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_13")
T " 「ええ、分かったわ」"

hide bra_t_02_1 at center
show bra_t_03_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_13")
voice blo_f0008
Blood " 「では……、そろそろ行くぞ、おまえ達。\n
昼はだるい、面倒なことはさっさと片付けるに限る」"

hide bra_t_03_13 at center
show bra_t_03_13 at left

show situji_t_01_06 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_13")
voice tan_f0000
Servant " 「……留守はお任せを～」"

hide bra_t_03_13 at left

hide situji_t_01_06 at right
show situji_t_01_06 at left

show eri_t_02_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_13")
voice eri_f0008
Elliot " 「ああ、手はず通りにな？」"

hide situji_t_01_06 at left
show situji_t_02_01 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_13")
voice tan_f0001
Servant " 「……心得ております～」"


show bra_t_01_11 at center
hide situji_t_02_01 at left
hide eri_t_02_4 at right
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_13")
Blood " 「…………」"

play sound se_0384
play sound se_0580
hide bra_t_01_11 at center
with dis

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " ブラッドとエリオット、それにつき従うように、使用人達が続く。\n
もちろん屋敷に残る者も相当数いるのだが、代表してか、数人が見送った。"


show situji_t_01_01 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice tan_f0002
Servant " 「いってらっしゃい～」"

hide situji_t_01_01 at center
show situji_t_01_01 at left
show bousi_t_01_02 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice chi_f0068
Maid " 「ご無事で～」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_7")
T " （いつのまに……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 気付かないうちに増えていた人数に、内心驚く。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " この屋敷の住人は皆、芝居染みて感じるほど喧しいかと思えば、気配も感じ取れないほどひっそりと動くのだ。"

hide situji_t_01_01 at left

hide bousi_t_01_02 at right
with dis

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 見送りが終われば、音もなく解散。\n
ばいばいと最後まで手を振っていた双子に応えていた私も、彼らの姿が見えなくなってからそっと手を降ろした。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " ぎゃあぎゃあと騒いだり、緊張感もなく、とても抗争に向かうとは思えない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " いつもの様子で出て行くが、屋敷にいる人数が減ってひとときの静寂が訪れるたびに、不安になる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_11")
T " （……本当に、早く帰ってきてよ？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 彼らは強い。\n
その辺の人間が束になってかかってきたところで、傷を負うことなど想像も出来ない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " だが、けして血を流さないわけではないことを、私はもう知っている。\n
不死身なわけでもないのだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_1")
T " （胸の中にあるものは違っていても、同じ赤が流れている）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 止まってしまう可能性があるのは、彼らも私と同じ。"

$ hi_mes()

scene charasel_bg_hatter_day with ImageDissolve("gui/stripe_l.png", .8, ramplen=128, reverse=True)
pause .8

scene map_bg_autumn_day with ImageDissolve("gui/stripe_l.png", .8, ramplen=128, reverse=True)
pause .8

scene map_bg_autumn_eve with Dissolve(.8)

scene charasel_bg_hatter_eve with ImageDissolve("gui/stripe_l.png", .8, ramplen=128, reverse=True)

play music hatter_corridor_p_ali fadein 1

scene br_02 with ImageDissolve("gui/stripe_l.png", 1.2, ramplen=128, reverse=True)
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 何度、時間帯が変わったのか。\n
なるべく数えないようにしても、ついつい気にしてしまう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 数えても数えなくとも、願う結果はただ一つ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " あの、物騒で、危険な……、それでも愛着を持つ人達が無事に帰ってきてくれることだけ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_15")
T " （ん？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 屋敷の中で仕事をしている最中、聞き慣れた声がした気がして、階段の下へ目を向ける。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 入り口からブラッド達が入ってくるのが見えた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_05_14")
T " （帰ってきたのね）"

play sound se_0417
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 私とは反対側へ歩いて行こうとする彼らを追いかけていく。"


show t_op_bousi5 onlayer master with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0009
Blood " 「……というわけで、おまえ達。\n
手を抜くんじゃないぞ？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice eri_f0009
Elliot " 「おう、当たり前だろ。\n
とびっきりいいものにするように、俺、協力するぜ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice dad_f0019
Dee " 「僕達だって、全力で頑張るに決まっているじゃない。\n
ねえ、兄弟」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice dad_f0020
Dam " 「当然だね、兄弟。\n
僕達が本気で取り組むんだもの、いいものになるに決まっているよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 先頭を歩くブラッド、そのすぐ後ろにいるエリオット。\n
そして彼らの間をちょこまかと動き回る、ディーとダム。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_15")
T " （話している内容はよく分からないけど……。\n
……やっぱり、落ち着くな）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " いつもと変わらぬ日常の光景。\n
賑やかに、戻ってくる。"


show t_op_bousi6 with dis
hide t_op_bousi5 with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_04_8")
T " 「皆、お帰りなさい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " そこに加わりたくて、声をかけた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
Blood " 「！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice eri_f0010
Elliot " 「え……、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice dad_f0021
Dee " 「あ、お姉さん……？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice dad_f0022
Dam " 「いつから、そこに？\n
気付かなかった……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_04_6")
T " 「？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 人の気配に敏感な彼らにしては珍しい。\n
私の声に、振り向いた一同は驚いた様子だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " よほど大事な仕事の話だったのだろうか。\n
そうなら邪魔をして悪いと思うが、密談だったら、彼らはもっとうまくとぼけるはず。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 大体、屋敷の廊下で話したりしないだろう。\n
それくらいの慎重さを持ち合わせている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_12")
T " （何か、仕事とは関係ないところで、ろくでもない相談でもしていたんじゃ……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 充分に、ありうる話だ。\n
退屈嫌いのマフィアのボスは、今までにも突拍子もないことを命じては、周囲を振り回した前科が山ほどある。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_12")
T " （エリオットはブラッドの言うことには二つ返事で頷くし、ディーやダムもちゃんと見返りがあればあっさりなびくものね……）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_11")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_7")
T " 「どうかしたの？\n
えらく、慌てているじゃない？」"


show t_op_bousi7 with dis
hide t_op_bousi6 with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_7")
voice blo_f0010
Blood " 「いや、何でもない、過剰反応をしてしまった……。\n
ああ、エリオット、例の報告書の件で話があるから、私の部屋に来い」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_7")
voice eri_f0011
Elliot " 「お、おう……。\n
あの件だな。行く行く、すぐに行くっ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_7")
voice dad_f0023
Dee " 「っと、僕達も仕事で疲れちゃった。\n
一休みしようよ、兄弟。休みは有意義に過ごさなくちゃっ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_01_7")
voice dad_f0024
Dam " 「そうだね、兄弟。\n
早く戻ろう……、早く早くっ」"

play sound se_0584
pause .4
play sound se_0584
hide t_op_bousi7 with dis

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " ぱたぱたと彼らはろくに挨拶も交わさぬまま、まるで蜘蛛の子を散らすように散っていく。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 見事な逃げ足の速さ。\n
呆然とする私を残して。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_4")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_7")
T " （な、何なの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " この屋敷に滞在して短くないが、こんな態度を取られるのは初めてだ。\n
まさしく、取り残されたような感じ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_11")
T " （何があったっていうのよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 彼らの仕事には深入りしない。\n
しかし、このマフィアの屋敷が、私の居場所。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 家族ではないが、似たようなもの。\n
ファミリーと名がつくくらいなのだから……。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_6")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 突然の、この態度の変化は一体何だというのか。"

$ hi_mes()

scene charasel_bg_hatter_eve with ImageDissolve("gui/stripe_l.png", .8, ramplen=128, reverse=True)

scene map_bg_autumn_eve with ImageDissolve("gui/stripe_l.png", .8, ramplen=128, reverse=True)

scene map_bg_autumn_night with Dissolve(.8)


scene charasel_bg_hatter_night with ImageDissolve("gui/stripe_l.png", .8, ramplen=128, reverse=True)

scene bn_aut_03 with ImageDissolve("gui/stripe_l.png", .8, ramplen=128, reverse=True)

play music hatter_garden_p_ali fadein 1

show t_op_bousi8 onlayer master with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0011
Blood " 「はあ……。\n
それでは華やかさに欠けるだろう……、却下だな」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice eri_f0012
Elliot " 「ええっ、何で！？\n
最っ高に華やかだろうっ！なあ？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice dad_f0025
Dee " 「馬っ鹿じゃないの、ひよこウサギ。\n
僕はボスに賛成」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice dad_f0026
Dam " 「うんうん、そんなのを見せたら全部台無しになっちゃうよ。\n
馬鹿ウサギが自滅するのは勝手だけど、僕達を巻き込まないでよね」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice eri_f0013
Elliot " 「おまえら……、好き勝手なこと言いやがって……。\n
俺のアイディアを……」"


show t_op_bousi9 onlayer master with dis
hide t_op_bousi8 with dis

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_14")
T " 「皆揃って、何の相談会？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 主の好む夜のお茶会。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 庭に備え付けられたティーテーブルで話していた男達に背後から声をかけると、彼らは傍目にも分かるほど動揺した。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
Elliot " 「……[firstname]！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0012
Blood " 「……お嬢さんか。\n
急に加わってくるものではないよ、男同士の話し合いだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_2")
T " 「へえ？\n
どんな話？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 引きさがらない私に、ブラッドがたじろく。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0013
Blood " 「いや……、だから男同士の話し合いだよ、お嬢さん。\n
君のようなレディには聞かせられないような話だ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_6")
T " 「……ふうん？\n
淑女扱いしてもらえるのは嬉しいけど……」"

show t_op_bousi10 onlayer master with dis
hide t_op_bousi9 with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_14")
T " 「…… {size=+23}猥談には聞こえなかったわよ？{/size}」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_14")
voice blo_f0014
Blood " 「……ごほっ、それこそ、淑女としてはあるまじき発想じゃないか。\n
男には色々あるんだ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_14")
voice eri_f0014
Elliot " 「そ……、そうだぜ、[firstname]、男っていうのは諸々の事情が……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_04_16")
T " 「今までなかったような事情が……？\n
それも、ディーやダムまで加わるような男の事情って何かしら……？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_04_16")
Dee " 「！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_04_16")
voice dad_f0027
Dam " 「っ！\n
そ、それは、もう、僕らだって子供だけどたまに大人っていうか……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 言い訳しながら、四人はそれぞれ別の方向へと視線をずらし、私とまともに視線を合わせようとしない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_02_10")
T " （……そんなに、私に知られたくないわけ？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_03_9")
T " （…… {size=+23}怪しい{/size}）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 彼らのおかしな態度は、あの仕事のあとからずっと続いている。\n
追及しようとすると、今のように話を逸らされることも珍しくない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_13")
T " 「ブラッドが、この程度の話で、ご自慢の紅茶でむせるなんて……。\n
……よっぽどよね？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 軽くむせたままのマフィアのボスは、顔を背けながら「気のせいだ」と空惚けている。"

show t_op_bousi11 onlayer master with dis
hide t_op_bousi10 with dis

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 視線の冷たさはそのままに、顔を動かして、そっぽを向いているウサギ男の背中をじっと見つめた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_14")
T " 「エリオットがにんじんクッキーも食べずに話に熱中するなんて、本当に大事な話なのよね？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_04_16")
T " 「ディーとダムも夢中になるような……。\n
……どうして、私も混ぜてくれないの？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_04_16")
voice eri_f0015
Elliot " 「だ……、だって、さ、な、何でもないから……。\n
なあ、おまえら？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_04_16")
voice dad_f0028
Dee " 「う、うん。何でもないんだよ、だからお姉さんは混じりようがないっていうか……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_04_16")
voice dad_f0028_5
Dee " 「労働条件について、上司に直接交渉していたところだから」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_04_16")
voice dad_f0029
Dam " 「そうそう……。\n
給料を上げてもらおうと思って……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_04_17")
T " 「あら、だったらいつもみたいに私の前でも交渉すればいいでしょう。\n
{size=+23}いつもみたいに{/size}」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 彼らとはもう短くない付き合いだ。\n
何に近付いてはいけなくて、どこまでが構わないのかの距離感だって掴めているはず。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 長い期間、マフィアの本拠である帽子屋屋敷にいるというのに、私は彼らの仕事について立ち入らずにいる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " それは、屋敷の人間が見せないようにしてくれているおかげでもある。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 隠しごとだって多いに決まっているが……。\n
内容による。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_04_12")
T " （私を混ぜてくれてもいい内容でしょう？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 遮断されなくていい、そんな雰囲気だった。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice blo_f0015
Blood " 「エリオット……。\n
私は仕事を思い出した、部屋に戻るから、あとは任せたぞ」"

play sound se_0623
show t_op_bousi12 onlayer master with dis
hide t_op_bousi11 with dis

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " ブラッドはそんなことを言いながらいそいそと消えていく。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " マフィアのボスが、たかだか小娘一人のプレッシャーに負けたとは思えないが、こういった家族的な……父親が娘に勝てないようなやりとりがたまにあった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " こういうとき、私はとても安心する。\n
加われないことがあっても、一員なのだ、と。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_5")
T " （だけど……、今の話って、別にマフィアの仕事とかそういう関係じゃないわよね？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 仕事絡みなら、皆もっとうまく口裏合わせをする。\n
ぎこちないのは、いつもと異なる内容だからなのだろう。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice eri_f0016
Elliot " 「え、ブ、ブラッド！？\n
ええ、それはないだろっ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_14")
T " 「あんた達……、一体どういうことなのか、そろそろ話してくれるでしょう？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 誤魔化されるのが続いている。\n
いいかげんに白状しろと睨み付けると、エリオットの耳が垂れ、双子はそわそわしだした。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_02_10")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_11")
T " （まだ、誤魔化す気？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 彼らだって、我らがボスほどではないにしろ、人を言いくるめることなんて慣れているだろうに……。\n
こういった家族的な甘さを見せてくれる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 一体何を隠し立てしているのか知らないが、悪い内容ではないのだろう。\n
だが……、ちらちら見せられては気になって仕方がない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_02_10")
T " （普段は斬りかかったり、銃をぶっ放したりするのに、こういうときだけ結託するんだから）"

show t_op_bousi13 onlayer master with dis
hide t_op_bousi12 with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_02_10")
Elliot " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_02_10")
Dee " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_02_10")
Dam " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 三人はそのまま目線だけで意思を交わして、大きく頷いた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice eri_f0017
Elliot " 「悪い、[firstname]！\n
その……、俺も仕事に戻るからさっ！\n
忙しいんだ！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice dad_f0031
Dee " 「僕達も、もう戻らないと……。\n
僕ら、職務に励む勤勉な門番だもんね、兄弟」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice dad_f0032
Dam " 「そうだね、兄弟。給料分は働かないと……。\n
行こう、行こうっ」"

play sound se_0619
show t_op_bousi14 onlayer master with dis
hide t_op_bousi13 with dis

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_02_12")
T " 「あ！\n
こら、待ちなさいよっ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_9")
T " 「……一体、何を隠しているのよ、あんた達！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_9")
voice eri_f0018
Elliot " 「何も隠したりしてねえって！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 元々、身体能力に開きがありすぎる。\n
逃げ出していく背中に、私の手など届くはずもなく。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice dad_f0033
Dee " 「そうだよお姉さん。\n
今回はウサギの言うことも嘘じゃない」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice dad_f0034
Dam " 「そうそう、たまにはウサギだって正しいことを言うんだよ！\n
気にしないでね！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice eri_f0019
Elliot " 「しつけえんだよ！\n
俺は、ウサギじゃねえ！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice dad_f0035
Dee " 「そういうことを言うと、正しくないって思われるだろ！？\n
墓穴を掘るなよ、穴掘りウサギ！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face ("ali_t_06_16")
voice eri_f0020
Elliot " 「だから、ウサギじゃねえと……！」"

hide t_op_bousi14 with dis

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " ぎゃあぎゃあ、騒がしくも素早く。\n
あっというまに離れていく後ろ姿。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " コミカルなやりとりに、やはり悪いものは感じないが……。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_02_16")
T " （悪い内容でなくても……）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_02_3")
T " 「……気になるじゃない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " すっきりとしない気持ちを抱えたまま残される。"



$ hi_mes()



$ renpy.movie_cutscene("Opening_video.mpg")

label fushigi_op_hatter_skip:

play music heartrending_a_ali fadein 1

scene bg_03_1 with ImageDissolve("gui/stripe_l.png", 1.2, ramplen=128, reverse=True)
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_6")
T " （……のけものになったみたい）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_01_1")
T " （ただでさえ、余所者なのに……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 仕事の本質に触れぬまま、マフィアの一員になっている、中途半端な仲間だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_02_16")
T " （…………）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " こういったときに感じる疎外感は、罪悪感によるものなのだろうか。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_04_11")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_04_15")
T " 「……全員にまとめて話を聞こうとするから、逃げられるんだわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 使用人である同僚達も何かを知っていそうだが、ばらした者が後で咎められても気の毒だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " マフィアだけあって、情報流出には非常に厳しい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 結局、ブラッド、エリオット、双子あたりまでしか問い質せないことになる。\n
しかし、彼らを捕まえるのは、よほど不意でもつかない限りは難しい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_11")
T " （……どっちにしても厳しいなあ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " この世界の役つきの人達ときたら、高いところから飛び降りても傷一つ負わない。\n
足だって、私とは比べものにならない健脚ぶりだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_06_11")
T " （……動物並みよね）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face ("ali_t_02_4")
T " （特に一名は完璧に動物だし……、いや、本人は否定するけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 今までは現場を押さえる意味で、全員が揃ったところで声をかけていたが、逃げられてしまうのなら追及も出来ない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " ならば、ターゲットを絞って戦略を立てたほうが確実だ。\n
複数でなければ、責任を押し付ける相手もいない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 問題は、その標的を誰に絞るかということ。\n
何しろ、誰にあたっても一癖も二癖もある。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " この時間帯ならば、彼らは全員自分の部屋に待機している。\n
誰でも条件は同じだが……。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_5")
T " 「誰に、話を聞きに行こうかしら」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face ("ali_t_06_16")
T " 特に、私に弱いのは……。"

$ hi_mes()

play music map_autumn_jok fadein 1

scene charasel_bg_hatter_night with dis
show screen hatter_man_choice
$ ui.interact()
