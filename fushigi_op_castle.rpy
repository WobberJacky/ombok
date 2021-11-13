label fushigi_op_castle1:
$ place_of_stay = "Castle"
scene map_bg_spring_day
with stripe_l_medium

scene charasel_bg_castle_day
with stripe_l_medium

play music castle_garden_p_ali

scene hn_spr_01
with stripe_l_long
play sound se_0569
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_2")
T "「本当に……、この城の薔薇は綺麗よね」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_15")
T "（そして、見事なだけに……。\n
手入れが大変）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（見た目の綺麗さだけで終わらないあたり、現実的とも言えるかもしれないけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ホースの先に付けられた口から溢れた水が、緑の葉を濡らし、赤い花弁に潤いを与えていく様を見つめていると、自然と溜息が出てしまう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "感嘆と、手入れをする人の苦労を労う意味で。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "家具の色調から咲く花まで、赤で統一された城。\n
この庭で水やりをするのは、本来であれば、私の仕事ではない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この薔薇を美しく保つ仕事は兵士や庭師が担当している。\n
メイドの一人にすぎない私は、本来であればハウスキーピングが主な担当だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんな私が、どうして水やりをしているのかというと……。"

$ hi_mes()

scene charasel_bg_castle_day
with stripe_l_medium

scene hr_01
with stripe_l_long

show heisi_t_02_09 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0000
Soldier "「ああっ、大変だ！噴水傍の薔薇にまだ水をやっていない！」"

hide heisi_t_02_09
show heisi_t_02_09 at left
show heisi_t_02_03 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice oto_f0000
Soldier "「女王陛下に知られたら、私達は……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "たまたま仕事が終わって手が空いたところだった私の前で、兵士が絶望の声を上げたせいだったりする。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "『首を刎ねよ』は、この城の女王様の口癖。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼女の愛する薔薇の手入れを怠ったと知られたら、間違いなく、兵士の首は刎ねられてしまう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "こと処刑に関して、ビバルディの命令が甘くなることはあり得ない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それも原因が薔薇の手入れ不足とあっては、仕事を果たしていないのだから……。\n
私が口を挟んでも撤回は難しいだろう。"

hide heisi_t_02_09

hide heisi_t_02_03

$ hi_mes()

scene charasel_bg_castle_day
with stripe_l_medium

scene hn_spr_01
with stripe_l_long
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（全部が全部防げるわけじゃないけど……。\n
目の前で、知っている人の首が刎ねられるのは、遠慮したいわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "かくて、ちょうど手の空いていた私が手伝うことになったわけだが、これが思った以上に難儀だった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この城は、広い。\n
小さな街なら難なく収まってしまうくらいに、広いのだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "城にとっては小さな区画であっても、私という小さい人間にとっては、十分すぎる広さがある。"

play sound se_0569
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「……とはいえ、手は抜けないものね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "女王様の愛する薔薇は、私にとっても決して軽いものではない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この城に来たときからずっと、綺麗で、強くて……。\n
憧れにも似た気持ちで、いつも見ていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今までの眼福を思えば、多少の手入れぐらい手伝おうという気にもなる。"

play sound se_0183
play music ace_t_ali

show ace_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0000
Ace "「あれ、[firstname]。\n
君が水撒きなんて珍しいね、はは」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「エース」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ちょうど水を撒こうとしていた繁みから、薔薇のように赤い人が現れる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつも変わらぬ爽やかな笑みを浮かべた彼は、そのまま無造作に私のほうへと近付いてきた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "よく見れば、その頭には薔薇の葉っぱや、他にも木々の小さな枝がついている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（今度は、一体どこを抜けてきたんだか）"

hide ace_t_02_4
show ace_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_11")
voice ace_f0001
Ace "「旅に出ていたら、水音が聞こえたからさ。\n
知らない間に川の近くにでも出たのかと思ったぜ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "{size=+20}「ここは、城よ。\n
川辺じゃないわ」{/size} "

hide ace_t_02_10
show ace_t_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_12")
voice ace_f0002
Ace "「おかしいなあ。\n
クローバーの塔に向かっていたはずなのに、何で城に戻ってきちゃったんだ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「ええ……、その上どうして入り口以外から現れるのかしらね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "相変わらず、凡人の私には理解しがたい迷いっぷりだ。\n
ここまでいくと、いっそ見事と言ってもいい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（ああ、毒されている）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "最初の頃は彼の迷子癖に呆れるゆとりもあったのだが、最近は「エースだから」という免罪符に、何となく納得してしまう自分がいる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（慣れって恐ろしい）"

hide ace_t_02_2
show ace_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0003
Ace "「ははは、そうだよなあ。\n
こんな目に痛い、真っ赤な城、二つもあったら堪らないぜ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「ここはあなたにとっては自分の職場でしょう、間違いなく」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "納得しているのか、皮肉なのか分からない発言をするエースを置いて、私は水撒きを再開した。"

play sound se_0569
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "葉を打つ水音が不思議と心地よい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界では普通、雨が降ることがない。\n ・
天候はいつも一定で、エイプリル・シーズンという特殊な期間を除いては、季節さえ変わることはない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_17")
T "（雨の音が懐かしいなんて、変な話だけど。\n
でも……、たまに恋しくて、切ない気持ちになる）"

hide ace_t_03_3
show ace_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_17")
Ace "「[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「？\n
何、エース？」"

hide ace_t_03_11
show ace_t_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice ace_f0004
Ace "「それ、俺にもやらせてくれない？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「は？\n
それって……、薔薇の水やりのこと？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "予想もしなかった申し出に思わず声が跳ね上がってしまった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "驚いたようにエースを見返すと、彼は彼で不思議そうに首を傾げてくる。"

hide ace_t_01_1
show ace_t_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0005
Ace "「えー、何だよ、その反応。傷つくなあ……。\n
騎士たるもの女の子に優しくするのは、当然だろう？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "子供のように唇を尖らせてくるエースは、私の言葉が不満だったようだ。\n
だが、相手はエースである。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この城一の……、いや、{size=+20}他領土を含めても一、二を争うトラブルメーカーだ。{/size} "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（……任せたら、何かまた揉めごとが起きそう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "率直な感想は秘めたまま、私はそっと首を横に振った。\n
気持ちをオープンにするほど素直な性格をしていないのは、私も同じだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「いいわよ、あなただって忙しいでしょう？」"

hide ace_t_01_8
show ace_t_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice ace_f0006
Ace "「でも、薔薇の手入れは君の仕事じゃない。\n
君だって、誰かの手伝いをしているんだろう？」"

hide ace_t_03_2
show ace_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice ace_f0007
Ace "「俺だって君の手伝いがしたいんだよ。\n
好きな子の力になりたいって思うのは、変なことじゃないはずだ！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "にこりと笑って彼は大きな手を私に向けてきた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "日頃大剣を軽々と振り回すその手は、私の手とは比べものにならないほど大きく、しっかりとしている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それはつまり、彼ならば私の意思を無視してでもホースを奪い取れることを暗示しているのだが……。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースにその気があれば、何だかんだと言い訳をつけながら、ホースを手に取っているだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あくまで私から預かりたい、そういう雰囲気を感じた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（うーん……。\n
そうは言われてもなあ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼に任せること自体不安もある。\n
何よりも、人から預かった仕事を放り出すようで、すっきりしない。"

hide ace_t_02_4
show ace_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0008
Ace "「ほら、[firstname]。\n
貸して」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、催促するでもなく自然に手を伸ばされて、とうとう私は頷いた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「……そこまで言うなら、この区画だけお願いするわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "たかが水撒き用のホースを恭しく受け取られて、私のほうが落ち着かなくなってしまう。"

hide ace_t_02_10
show ace_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0009
Ace "「そんなに遠慮しなくていいのに……、君と俺の仲じゃないか」"

play sound se_0569

show t_op_siro1 onlayer master
with dis
hide ace_t_03_11

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ホースを手にしたエースはその長身を活かして、私よりも少し高い位置から周囲の木々に水を撒いていく。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "きらきらと乱反射する光が、爽やかな笑顔に混じった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（こうしていると、格好いいし……、確かに騎士そのものなんだけどなあ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界の人間ときたら、誰も彼もが一筋縄ではいかない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "とりわけエースの言動や行動に散々振り回されてきている身としては、何とも複雑だ。"

hide t_op_siro1
show t_op_siro2 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0010
Ace "「よっと……。\n
あれ、あそこには届いていないか」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0011
Ace "「でも、ホースはこれ以上伸びそうもないし」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼の視線が向かっているのは、生け垣になった少し高い薔薇の繁みだ。\n
くいくいとホースを引くが、固いゴムで出来たホースはそう簡単に伸びない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0012
Ace "「うーん、参ったな。\n
もう少しで届きそうなんだけど……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「だったら、別の場所から水を取りましょうか？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "広大な庭には、各所に取水用の噴水や蛇口がある。\n
何も同じ場所から取らなくても、他に方法はいくらでもあるのだ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0013
Ace "「あ、[firstname]。\n
別にホースをつなぎ替えなくても大丈夫だぜ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「え？\n
だって、そこからだとどうやっても届かないでしょう？」"

hide t_op_siro2
show t_op_siro3 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いくらエースの手足が長くても、ホースの長さまでは変えられない。\n
そう思っていたのだが、彼は何を思ったか、ホースの先端の注ぎ口を外した。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「エース？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（何をする気なんだろう？）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice ace_f0014
Ace "「よし、これでいいや。\n
[firstname]、ちょっと離れていてくれよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「？\n
う、うん、分かったわ」"

play sound se_0454
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "言われるままに数歩下がる。\n
彼の手元からは、ホースの水が流れ出たままだ。"

hide t_op_siro3
show t_op_siro4 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0015
Ace "「こういうのって、先を細くすれば……。\n
ほらな！」"

play sound se_0572
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「ああ、なるほど」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ホースの口を狭めたことで、水圧が増して、飛距離は伸びた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0016
Ace "「こうすれば、あっちの生け垣にだって届くぜ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_8")
T "「ええ、確かに充分だわ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（心配したけど、今回は取り越し苦労ですみそうね）"

play sound se_0572
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "絶妙な力加減で飛距離を変えながら、エースが手を動かす。\n
心地よい水音が響いて、より遠くに雫を運び……。"

hide t_op_siro4

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0000
Vivaldi "{size=+20}「誰じゃ！\n
そこで水を撒いている者\n
は！」{/size} "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0000
Peter "「この僕に水をかけるなんて……。\n
{size=+20}万死に値しますっ！{/size}」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "二種類の怒声が響いた。"


play music gag2_a_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_20")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「……え？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_7")
T "（今の……、聞き間違えようのないあの声は……！）"


show ace_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_7")
voice ace_f0017
Ace "「あれー、どうして陛下とペーターさんの声がするんだ？\n
気のせいかなー」"

play sound se_0572
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そして、彼の手元にあるホースはいまだに水を出し続けている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それも……、{size=+20}どばどば、勢いよいままに。{/size} "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_9")
T "（何で止めないのよ、この馬鹿っ！！）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_9")
voice viv_f0001
Vivaldi "「ええい、やめよと言うておるのが聞こえぬのか！\n
おまえ達、向こうにいる馬鹿者の首を刎ねよ！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_9")
voice viv_f0002
Vivaldi "「わらわに水をかけ、茶の時間を台無しにしたのだ。\n
即刻死刑にしてくれる！！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_9")
voice hos_f0001
Soldier "「か、畏まりました！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_9")
voice oto_f0001
Soldier "「直ちに参りますっ！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_9")
voice pet_f0001
Peter "「そんな顔なしの手を借りるまでもありません……。\n
僕を水浸しにした愚か者は、自分の手で処刑してやります」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（ああ……。\n
何で、よりにもよってこういうときに二人がいるのよ）"

play sound se_0588
pause .4
play sound se_0086

play music peter_t_ali

show per_t_01_1 at center
hide ace_t_01_3
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_11")
voice pet_f0002
Peter "「そこにいるのは、エース君！\n
また君ですか……って、ああ、[firstname]！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "繁みを飛び越えてやってきたペーターは、私を見つけるなり表情を一変させた。"

hide per_t_01_1
show per_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0003
Peter "「あなたまでこんな場所にいるなんて、どうしたんです？\n
僕に会いに来て下さったんですか？」"

hide per_t_02_12
show per_t_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0004
Peter "「一言呼んでくれれば、僕はいつでもあなたの元に飛んでいくのに！」"

play sound se_0623
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "頭から盛大に水を被った（正確に言えばかけられた）ペーターは、大きく手を広げて抱きつこうとやって来る。"


show t_op_siro5 onlayer master
with dis
hide per_t_02_13

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「ペ、ペーター」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_12")
voice pet_f0005
Peter "「[firstname]、[firstname]……、ああ、僕の愛しい人！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_12")
voice pet_f0006
Peter "「あなたに水撒きなんて汚れ仕事をさせるとは……。\n
あとでこの区画担当の兵士は、皆処刑して……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「{size=+20}するなっ{/size}。\n
そして濡れた身体で抱きつかないでっ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この城の重役達は、何かというと兵士達を処刑しようとするので気が気ではない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0007
Peter "「どうしてですかっ、あなたを愛している僕なら、いつ抱きついてもいいでしょう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_13")
T "「いいわけがないでしょう！\n
少なくとも、全身ずぶ濡れのウサギに抱きつかれる趣味はないわっ」"

play sound se_0055
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しっかりと抱きついてくるペーターを引き剥がそうとするが、水滴のついた服のせいか、指が滑ってなかなかうまくいかない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "水も滴るいい（男ならぬ）ウサギに抱きつかれながら、思わず手を握り締めていると、繁みの横から更にもう一人現れた。"

play sound se_0183

play music vivaldi_t_ali
hide t_op_siro5
show t_op_siro6 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0003
Vivaldi "「エース、またおまえか……。\n
わらわのお茶会を邪魔するなど、不敬罪と知らなかったとは言わせぬぞ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "普通の神経の持ち主なら一睨みされただけで身動きが出来なくなる鋭い眼差し。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "怒りを滲ませた女王の一瞥だが、騎士の厚い皮膚には効果はなかった。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0018
Ace "「えー、だって繁みの奧にあるのって小さな噴水だけでしょう？\n
まさかあんなところでわざわざお茶をするなんて、陛下って酔狂ですよね」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0019
Ace "「ははは。\n
こんなに無駄に広い城の中で、わざわざ狭い場所を選ばなくてもいいのに」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0004
Vivaldi "「そういう気分のときもあるのだ。\n
おまえみたいに無神経な騎士には分からぬだろうがな」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0005
Vivaldi "「ああ、髪から水が落ちてくる……。\n
気持ちが悪い、最悪じゃ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ペーターと同じく髪から滴る水を煩わしそうに払いながら、ビバルディが顔を顰める。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0020
Ace "「大丈夫ですよ、陛下。\n
陛下の厚壁みたいなお化粧は、ちゃんと守られていますから、お化けみたいになんてなっていませんよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_5")
T "（エースの馬鹿……！）"


play music tension_a_ali
play sound se_0582 volume .7
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "びしっと空気が張り詰めたのが分かる。\n
逆撫でした神経に、更に塩を塗り込んでどうするのだ、この男は。"

play sound se_0771 volume .7
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Vivaldi "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0006
Vivaldi "「わらわに楯突く気か、エース？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0021
Ace "「えー、そんな無礼なことなんて俺はしませんよ。\n
心配してあげただけなのに、心外だなあ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ビバルディの殺人光線並の視線を受けても、鋼鉄製の騎士の顔は少しも傷ついた様子はなかった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "大体、エースがビバルディやペーターの気配を察せないわけがないのだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（つまり、確信犯よね……）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice viv_f0007
Vivaldi "「……はあ、もういい。\n
それと、エース、おまえいつまでそれを持っておる？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice viv_f0008
Vivaldi "「おまえがホースなぞ持っていると、ろくでもないことにしかならぬわ、早く水を止めぬかっ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice viv_f0008_5
Vivaldi "「またいつ水をかけるのではとイライラする」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice ace_f0022
Ace "「心配しなくても、俺は濡れていませんよ。\n
薔薇に水をやっていただけですしね！」"

hide t_op_siro6
show t_op_siro7 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice viv_f0009
Vivaldi "「濡れているのはおまえではなく、{size=+20}わらわじゃ、このたわけっ{/size}」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice viv_f0010
Vivaldi "「ホワイト、おまえもいい加減離れぬか。\n
わらわの可愛い子が冷えてしまう」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice viv_f0011
Vivaldi "「女の身体は男と違ってデリケートなのだぞ。\n
風邪でもひいたら、おまえの首如きでは釣り合わぬわ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「……そうよ、ペーター。\n
いい加減離れてちょうだい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "メイド服は動きやすく、また丈夫に作られているが、これだけぴったりとくっつかれれば水が染み込んでしまう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "こんな面倒ごとまで起こした挙げ句に風邪をひくのでは、何のために手伝いを買って出たのか、分からない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0008
Peter "「彼女は確かにデリケートだと思いますが……。\n
陛下と彼女が同列というのは、どうかと」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0023
Ace "「男だって、陛下が言うほど単純じゃないですよ。\n
女の人とは違った意味で、デリケートな生き物だし……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0024
Ace "「な、ペーターさん」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0009
Peter "「僕に同意を求めないでください。\n
気持ち悪い」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "{size=+20}「気持ち悪いのは、濡れた身体でひっついてくるあんたも一緒よ」{/size} "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（まあ、この世界では気温も変わらないから、風邪をひくこと自体があまりないけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "体調不良を訴えている姿など、元々病弱などこかの夢魔ぐらいしか見たことがない。"

hide t_op_siro7
show t_op_siro8 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T "「エースも、もう水やりはいいからホースを片付けましょう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ようやく引き剥がしたペーターから離れてそう声をかけると、赤い騎士は珍しく素直に頷いた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0025
Ace "「それもそうだな。\n
この調子で水を撒き続けていたら、薔薇じゃなくて俺達が水浸しになりそうだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「あれ、でも……。\n
ホース、もう水が止まっているみたいだけど？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先程まで流れ出ていた水は、今やホースから雫となって滴る程度。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（誰かが止めてくれたのかしら？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ビバルディがいるということは、お付きの兵士やメイドが控えていたはずだ。\n
そのうちの誰かが止めてくれたのだろうか。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0010
Peter "「そもそも、君には五時間帯前に兵士の模擬訓練があったのに、また出て来なかったでしょう。\n
いい加減、君の迷子癖にはうんざりです」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0011
Peter "「君はどこでも迷惑をかけずにいられないんですから、いっそ戻らずに、どこかでのたれ死んでくれればいいのに」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0026
Ace "「ははは、ペーターさんってばそんなに冷たくしないでよ。\n
愛情の裏返しにしても、あんまり熱烈にされると俺じゃあ応えきれないし」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "心底嫌そうな顔をするペーターと、にこにこと笑うエース。\n
その足下にあるホースが目に入る。"

hide t_op_siro8
show t_op_siro9 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_7")
T "（……あれって、もしかしなくても、踏んでいる？）"

play sound se_0145
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースの足という枷のせいか、ホースはびったんびったんと跳ねている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そこだけ見ていると、まるで別の生き物のようだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_8")
T "（限界ぎりぎりっぽい……？）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「エ、エース……。\n
あの、あなた、ホースだけど」"

hide t_op_siro9
show t_op_siro10 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice ace_f0027
Ace "「ああ、そうだった。\n
いい加減水を止めないといけないよな」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice ace_f0028
Ace "「ちょっと待っていてくれよ、[firstname]。\n
今、俺が……」"

play sound se_0625
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_9")
T "{size=+20}「違う、動かないで！！」{/size} "

play sound se_0568
play sound se_0576
hide t_op_siro10
show white onlayer master with spread_short
hide white
show t_op_siro11 onlayer master with spread

play music gag1_a_ali
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼の足がそこから離れた瞬間、豪雨を思わせる飛沫が周囲に散った。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう、エースは良くも悪くも有言実行の男である。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼はホースを手にしたまま……、歩いていた。\n
そしてその先端は、地面を向いている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、それも突然勢いを増した水量に煽られるように、ぐるんぐるんと方向を変えたものだから堪らない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0012
Vivaldi "「エース！\n
おまえ、まだっ！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0012
Peter "「エース君！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0029
Ace "「ええ、どうして水がこんなに？\n
俺、蛇口を止めに行ったのに」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_10")
T "「あ」"

play sound se_0109
play sound se_0111
hide t_op_siro11
show t_op_siro12 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "水と土が混じり合った泥が、私のみならずその場にいた全員に盛大に飛んできた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_9")
T "（……うわ、最悪）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "全身水と泥にまみれた、ハートの女王と、白ウサギ、そしてハートの騎士。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "なかなか見られる光景ではない。\n
同時に、けして見たくもなかった。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Vivaldi "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "二人は何も言わない。\n
いや、言えぬまま、凍りついている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "汚れなど、時間帯と共に消える世界であっても、今現在身体についたそれは瞬時に消えない。"

hide t_op_siro12
show t_op_siro13 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0013
Vivaldi "「二度は言わぬ……。\n
{size=+20}その大馬鹿者な男の首を、今すぐ刎ねよ！{/size}」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0013
Peter "「ああ、僕が間違っていました。\n
君が自然にのたれ死ぬのを待つまでもありませんでしたね」"

play sound se_0515
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0014
Peter "{size=+20}「今すぐこの場で始末して差し上げます」{/size} "

play sound se_0022
hide t_op_siro13
show white onlayer master ##instant


hide white ##instant

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0030
Ace "「ちょっと、陛下、ペーターさん。\n
これ不幸な事故なんだから、そんなに目くじら立てないでよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0031
Ace "「はははは、困ったなあ」"

play sound se_0022
pause .3
play sound se_0022
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ちっとも困っていなさそうな騎士の声に銃声が重なった。"



$ hi_mes()

stop music
$ renpy.movie_cutscene("Opening_video.mpg")

label fushigi_op_castle_skip:

scene map_bg_spring_day
with stripe_l_medium

scene charasel_bg_castle_day
with stripe_l_medium

play music castle_corridor_p_ali

scene hr_01
with stripe_l_long

show heisi_t_02_02 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0002
Soldier "「あの、どうか気にしないでくださいね？」"

hide heisi_t_02_02
show heisi_t_02_02 at left
show heisi_t_01_02 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice oto_f0002
Soldier "「そうです。\n
あなたが悪いわけでは……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「そんなことはないわ、私が悪かったんだもの……、どう考えても」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつものようにペーターはエース相手に銃を乱射、ビバルディは機嫌を損ねていつにも増して斬首を命じる始末。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（この城で、いえ、この世界で銃撃戦なんて珍しくもないけど……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その原因が自分にあるとなれば、無視することも出来ない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_11")
T "（ああ、頭が痛い）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「同僚のメイドさん達にも、あなた達にも迷惑をかけてしまったし……。\n
しばらく城の外で頭を冷やしてきたほうがいいかも」"

hide heisi_t_02_02
show heisi_t_01_06 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice hos_f0003
Soldier "「え？」"

hide heisi_t_01_02
show heisi_t_02_09 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice oto_f0003
Soldier "「いえ、むしろあなたが離れるほうが……。\n
皆様は、その、お怒りになるかと」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「元凶はエースに水撒きを手伝ってもらった私だもの。\n
大丈夫よ、ちゃんと出掛ける前に説明に行ってくるから」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「あなた達に迷惑はかけないわ」"

hide heisi_t_01_06
show heisi_t_01_02 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
Soldier "「…………」"

hide heisi_t_02_09
show heisi_t_02_02 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
Soldier "「…………」"

hide heisi_t_01_02

hide heisi_t_02_02

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何故かすっきりしない表情の彼らを残して、私は歩き出した。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「さてと、出掛けるって話しに行かなくちゃ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "やはり最初に話しに行くべきなのは、あの人だろう。"

$ hi_mes()

play music map_spring_jok

scene charasel_bg_castle_day
with dis

show screen castle_man_choice
$ ui.interact()
