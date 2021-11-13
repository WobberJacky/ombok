label gakuen_dad6:
scene bg_map_day
with dis
$ clockanim()


scene bg10_sb_day
with dis

play music corridor_day_p_wam

scene bg27_rk_day with Dissolve(1.2)
play sound se_0541
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうこうしているうちに、ブリーズの日がやってきてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちょうど、ストームの夜から一週間後のことだ。\n
ストームの日と同じように、寮全体がざわざわと落ちつかない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一週間前のストームの日には、何が起こるのか分からないまま時間を過ごしていたが、今回は違う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何が起ころうとしているのかを把握して、その上で迎えることになるのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ホームルームが終わり、いつものようにエントランスへ向かう。"


show dee_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0331
Dee "「あ！\n
お姉さん！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "先に待っていた二人が、私を見つけて駆けてくる。\n
子犬が飼い主を見つけてじゃれついてくるようにも見えた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_17")
T "（可愛いだけじゃないってことは、充分知っているはずなのに……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "口元が笑みに緩んでしまう。"

hide dee_m_01_2
show dee_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0332
Dee "「お姉さん！\n
今日は何して遊ぶ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まっすぐな好意を無碍に出来る者などそうそういない。\n
自分も好意を持ってしまうのは自然な流れといえる。"

hide dee_m_02_1
show dee_m_02_1 at left
with dis

show dam_m_02_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0333
Dam "「何して遊ぼうか！\n
僕は、ネズミ駆除ごっこがいいな！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「……それ、ごっこじゃなくて割と本気でしょう」"

hide dam_m_02_4
show dam_m_02_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice dad_g0334
Dam "「だって、ネズミのくせにお姉さんと同じクラスなんて、生意気だよ。\n
ねえ、兄弟」"

hide dee_m_02_1
show dee_m_02_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice dad_g0335
Dee "「そうだね、兄弟。\n
ネズミは存在そのものが死刑に値するよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……害獣駆除は業者に任せておきなさい」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もっとも、ピアスは「ネズミみたいな人」であって、ネズミではない。\n
たとえ、耳と尻尾が生えていようとも、だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「あのね、二人とも今日は悪いんだけど遊べないわ。\n
私、ちょっと用事があるの」"

hide dee_m_02_2
show dee_m_02_6 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice dad_g0336
Dee "「えええええ！？\n
お姉さん、遊んでくれないの！？」"

hide dam_m_02_3
show dam_m_02_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice dad_g0337
Dam "「どうして！？\n
お姉さん、僕達と遊ぶの嫌になっちゃった！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「違うわよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はゆるりと首を横に振って、否定した。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「本当に用事があるの。\n
だから、今日はごめんね？」"

hide dee_m_02_6
show dee_m_02_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
Dee "「…………」"

hide dam_m_02_7
show dam_m_02_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
Dam "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人は顔を見合わせて、少しの間を挟んだ。"

hide dee_m_02_8
show dee_m_03_7 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0338
Dee "「しょうがないね、兄弟。\n
お姉さんにだって一人の時間は必要だよ」"

hide dam_m_02_8
show dam_m_03_6 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0339
Dam "「……そうだよね、兄弟。\n
束縛はよくないよね」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（……あ）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「……ありがとう。\n
明日また誘ってくれる？」"

hide dee_m_03_7
show dee_m_02_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice dad_g0340
Dee "「もちろんだよ！毎日だって、お姉さんに遊んでほしいよ！\n
明日は遊んでね？」"

hide dee_m_02_4
show dee_m_01_7 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice dad_g0341
Dee "「それじゃあ、僕達はネズミを探して遊ぶとするよ！\n
お姉さん、また明日ね！」"

play sound se_0311
hide dee_m_01_7

hide dam_m_03_6


play music flower_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうやら、結局ピアスが酷いめにあうことは決定事項。\n
私に出来るのは、彼が無事逃げ切ることを祈るぐらいのことだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_11")
T "（……駄目だわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人が走り去っていくのを見送る。\n
自分から誘いを断っておきながら、聞き分けよく諦めてくれたことに物足りなさを覚えてしまう。"


scene bg06_sk_h_day with Dissolve(1.6)
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_2")
T "（我侭ね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ストームの日以来、いや正確に言うとストームの次の日以来、私はディーとダムのことを意識してしまっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "否定したのは私だ。\n
それなのに、二人が女の子達に囲まれているのを見て、苦しくなった。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0033
Seito "「あれ？\n
ツインズじゃない？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0144
Seito "「今は子供なのね」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0034
Seito "「やっぱり、見慣れている分、子供のほうがしっくりくるわね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今も、女子生徒達の会話が耳に響く。\n
なにげない内容でも、気にしてしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_7")
T "（この気持ちは何？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "姉さんが結婚した、といわれて果たしてこんな気持ちになるだろうか。\n
イーディスに恋人ができた、といわれて、こんな気持ちになるだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……弟のように思っても、別物だ。\n
ディーとダムに当てはめると、どうしようもない苦味を覚える。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "誰にも譲りたくない。\n
独占欲がある。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（好き……って、思う。\n
これは、親愛じゃないのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "誰にも譲りたくないのに、どちらか一人を選ぶなんてことも出来そうにない。\n
これも、ひどく我侭な話だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "対象は二人で、私はそのどちらも失いたくない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズの夜までに、答えを見つけようと思っていたのに、いまだ私は答えを見つけられずにいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「……ブリーズ、か」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一人、寮までの道のりを歩きながら考える。\n
私と、ディーとダムとの関係はストームの夜をきっかけに変わった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "崩れたバランスを取り戻すなら、ブリーズはいい機会だ。\n
きっかけにはなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（でも、何のきっかけに……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "元に戻すのか、進展させるのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "大体、二人の子供相手に進展も何も……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "三人で仲良くつきあいましょう、なんて無理に決まっている。\n
親愛なら成り立ったとしても、それが恋愛なら三人では無理だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一人引かなければ、成立しない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（……それは当然、私であるべきよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "大人ならば。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0570
Blood "「……お嬢さん。\n
そんなにぼんやりしながら歩いていると、ウサギに轢かれるぞ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「……え？」"


play music hatter_gate_p_ali

scene bg_par15_rg_hat_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "突如かけられた声に顔をあげた。\n
いつの間にか、私は帽子屋寮まで戻ってきていたらしい。"


show bra_m_01_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "目の前では帽子屋寮の寮長たるブラッドが、呆れた面持ちで立っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「……ウサギに轢かれる？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "聞き違いだろうか。"

hide bra_m_01_9
show bra_m_01_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0571
Blood "「我が校に在籍するウサギはどれも暴走しがちだからな」"

hide bra_m_01_9
show bra_m_01_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0571_5
Blood "「お嬢さんのように心ここにあらずといったふうに歩いていれば、轢かれてしまったとしてもおかしくはない」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「そんなわけ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_7")
T "（……{size=+20}ある{/size}）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "充分に有り得る。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何せ、この学校にいるウサギさんは揃って素晴らしい暴走癖を持っているのだ。\n
轢かれたらひとたまりもない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……気をつけるようにするわ。\n
忠告をありがとう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はそう言ってブラッドの隣を通りぬけ、自室へと向かおうとするが……。"

play sound se_0011
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドは、すれ違いざまに私の腕を捕まえた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_6")
T "「何？\n
私、ちょっと今、考えごとがあって忙しいの」"

hide bra_m_01_5
show bra_m_03_18 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_6")
voice blo_g0572
Blood "「そうか。\n
私はお茶会がしたい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_17")
T "「…………。\n
したら？」"

hide bra_m_03_18
show bra_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_17")
voice blo_g0573
Blood "「お茶会、というからには一人でするものじゃあないだろう。\n
付き合ってくれ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_1")
T "「あなた、普段一人でもお茶ばかり飲んでいるじゃない。\n
一人が嫌ならエリオットでも付き合わせればいいでしょう？」"

hide bra_m_03_10
show bra_m_01_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_1")
voice blo_g0574
Blood "「あいつを呼ぶと、ティーテーブルをオレンジ色のブツで汚染されるから嫌だ。\n
……ツインズばかりが君を独占するのはずるいじゃないか」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_2")
T "「……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "予想もしなかったところで、ツインズの名前を出されて、びくりと肩を揺らしてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そろ、っと視線を持ち上げると、にたりとブラッドが笑った。"

hide bra_m_01_5
show bra_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0575
Blood "「ふふ。\n
たまには私にも付き合ってくれ」"

hide bra_m_01_10
show bra_m_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0576
Blood "「……ちょうどいいだろう？\n
考えごとなら、私が相談にのってあげよう」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「い、いらないわよっ！\n
相談なんて……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（ブラッドになんか相談したら、かえってややこしくなるのがオチだわ）"

hide bra_m_03_1
show bra_m_02_18 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice blo_g0577
Blood "「おとなしくしていなさい。\n
君が協力的であれば、手荒なことはしないよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_9")
T "「……どこの人攫いのセリフよ」"

hide bra_m_02_18

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ずるずる、と半ば引きずるようにして、男女共同区域のテラスまで連行されてしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "途中からは抵抗するのも馬鹿らしくなり、だからといって自分からついていくのも癪で、引きずられるままにされておく。"

with dis
$ hi_mes()

scene bg_par15_rg_hat_day
with stripe_l_medium

scene bg_par12_hct_day
with stripe_l_long

play music hatter_garden_p_ali
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドは私を席につかせると、彼自身も私の向かいに座って「ふむ」と満足げに頷いた。"

play sound se_0544
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここのティーテーブルも、食堂やカフェテリアと同じように魔法がかかっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "違うのは、紅茶に関しては出来合いのものが出てくるわけではないという点だ。"

play sound se_0242
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドは必ず、茶器と、茶葉と、そして湯とを別々に用意して、その場で淹れて飲むようにしている。\n
彼なりのこだわりがあるのだろう。"

play sound se_0175
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "以前ゴールデンルール云々と、夢見がちな瞳でうっとりと語っているのを見たことがある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "例に漏れず、今回もブラッドはてきぱきと茶器の用意を整えると、私の分までカップに注いでくれた。"

play sound se_0174
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_1")
T "「ありがとう」"


show bra_m_03_15 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_1")
voice blo_g0578
Blood "「本日の茶葉はシッキムにしてみた。\n
ダージリンよりも柔らかな味わいが楽しめる」"

play sound se_0198
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "目の前に差し出されたティーカップからは、紅茶のいい匂いが立ち上っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "早速口をつけると、その柔らかな味わいに、ぐるぐると堂々巡りの思考で硬直していた頭までもがほぐされるような気がする。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……ふう」"

hide bra_m_03_15
show bra_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice blo_g0579
Blood "「……ずいぶんとお疲れのようだな、お嬢さん。\n
ツインズに悩まされているのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「ディーとダムのことで悩んではいるけれど……。\n
別に、あの子達のせいではないの」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の問題だ。\n
紅茶が美味しかったからか、ブラッドの問いに素直に答えることができた。"

hide bra_m_03_4
show bra_m_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0580
Blood "「まあな……。\n
二人を一度に相手にするのは大変だろう」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「ええ……」"

hide bra_m_02_2
show bra_m_02_17 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
Blood "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（？？？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何気なく同意したというのに、ブラッドがまさか同意されるとは思わなかった、というような微妙な顔をする。"

hide bra_m_02_17
show bra_m_03_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0581
Blood "「……恋人間の事情を打ち明けるほど、君に信用されていると思うと光栄だな。\n
いや、あてられた」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「は？\n
恋人間というのはどういう……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「…………」"

hide bra_m_03_7
show bra_m_01_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
Blood "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_10")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_9")
T "「……っ最低！！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "遅れて、ブラッドが何を言わんとしていたのかに思い当たって、私は頬を赤らめて目の前のセクハラ男を睨み付けた。"

hide bra_m_01_1
show bra_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0582
Blood "「……私は何も言っていないよ、お嬢さん」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_13")
T "「私が同意したのは、元気のいい双子の男の子の面倒をみるのは大変よ、って意味よ！\n
妙な勘繰りはしないでちょうだい！」"

hide bra_m_03_9
show bra_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_13")
voice blo_g0583
Blood "「だから、何も……。まあ、照れるな。\n
私にはあいつらの監督責任がある」"

hide bra_m_03_10
show bra_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_13")
voice blo_g0584
Blood "「君がそんな疲れた顔をしているのなら、私のほうからあいつらに言い聞かせても……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_14")
T "「誤解しないでってば！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドは根本的なところで勘違いをしている。\n
私と双子がそういう関係であることが前提だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_9")
T "「私達は……、そういう関係じゃないわよ。\n
二人は弟みたいなもので……」"

hide bra_m_03_2
show bra_m_02_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_9")
voice blo_g0585
Blood "「……またずいぶんと白々しいことを。\n
私を相手に、下らない誤魔化しはやめなさい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_8")
T "「……っ」"

hide bra_m_02_13
show bra_m_02_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_8")
voice blo_g0586
Blood "「……煙にまくのは好きだが、自分がそうされるのは好きじゃないんだ、私は。\n
子供達相手にも、そうやって曖昧にしているのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "先ほどまでのからかう調子とは変わって、ぴしゃりといわれて私は口を噤んだ。\n
しばらく、沈黙が続く。"

menu:
    "私達ってそういうふうに見えるの？":
        jump gakuen_dad6_2a
    "どうしたらいいのか分からなくなったの。":
        jump gakuen_dad6_2b
label gakuen_dad6_2a:
$ lovechara_deedam_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「……ねえ」"

hide bra_m_02_9
show bra_m_03_18 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice blo_g0587
Blood "「なんだ、お嬢さん」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「私と双子達って、そういうふうに見えるの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すなわち、そういう関係に。\n
恋愛関係が成立しているように見えるのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（それなら、どちらと？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "客観的に見て、私達の関係はどういうふうに見えるのだろう。\n
私は、どちらと付き合っているように見えているのだろう。"

hide bra_m_03_18
show bra_m_01_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0588
Blood "「そうだな。\n
君達が戯れている姿は、微笑ましい幸せな恋人同士のように私には見えるが」"

hide bra_m_01_13
show bra_m_01_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0589
Blood "「……やや、幼い、な」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どちらと、と聞けばいいのは分かっているが、それを聞いてしまうのが怖くて、たった四文字のその言葉を口にすることが出来ない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どちらも選べない。\n
そもそも、恋なのかも曖昧で。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（……よくて二股）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こんな堂々とした二股が未だかつてあっただろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "黙ってティーカップの中の紅茶の水面を見つめていると、追加するようにブラッドが口を開いた。"

jump gakuen_dad6_3
label gakuen_dad6_2b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「どうしたらいいのか分からなくなったの。\n
……何が正解なのかしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の双子への気持ち、双子から私への気持ち。\n
何が正しくて、どうすべきなのか、どうしたらいいのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_12")
T "（そもそも三人という時点で、大幅に間違っている気がするわ）"

hide bra_m_01_9
show bra_m_03_15 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice blo_g0590
Blood "「……ふむ。\n
お嬢さん、君は根本から間違えているように思うぞ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「根本？」"

hide bra_m_03_15
show bra_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice blo_g0591
Blood "「正解などないだろう。\n
重要なのは……、当人達がどうしたいか、だ」"

hide bra_m_01_8
show bra_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice blo_g0592
Blood "「君があいつらのことを好きだと思うのならば、恋人にでも何でもなるがいい。\n
この世の春を謳歌したらいいじゃないか」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（……他人事だなあ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "他人なのだから、それも当然。"

jump gakuen_dad6_3x
label gakuen_dad6_3x:
hide bra_m_01_10
show bra_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0593
Blood "「……お嬢さん。\n
まさか君は、あの二人のうちのどちらかを選ばなければいけないなどと、考えているんじゃないだろうな？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言い当てられて、私は目を瞠って顔をあげる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私のそんな反応に図星であることを確信したのか、ブラッドは呆れ混じりの溜息を吐き出した。"

hide bra_m_03_11
show bra_m_03_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0594
Blood "「そんな不毛なことはやめなさい。\n
まあ、君がそう言えばあいつらも納得するだろうが……」"

hide bra_m_03_13
show bra_m_03_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0595
Blood "「まず間違いなく、殺し合いが起きるぞ？\n
子供の思考はシンプルだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「こ、殺し合いって！？」"

hide bra_m_03_12
show bra_m_02_17 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_4")
voice blo_g0596
Blood "「……誇張抜きに。\n
この学園において、ウサギに轢かれるより有り得ることだ」"

hide bra_m_02_17
show bra_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_4")
voice blo_g0597
Blood "「いや、そういった修羅場もぜひ見てみたいな、退屈しなさそうだ。今後もしそういったことになったなら、是非とも私の目の前で決着をつけるようにしてくれ」"

hide bra_m_02_3
show bra_m_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_4")
voice blo_g0598
Blood "「茶でも飲みながら、観戦することにするから。\n
ああ……、審判でもいい」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（何を言い出すんだ、この男は）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「まって、まってまってまって！\n
どうしてあなた、三人であることを推奨するように言うの！？」"

hide bra_m_02_2
show bra_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice blo_g0599
Blood "「別に推奨などしていないさ。\n
同情はしているさ、一人で二人を相手にするのは大変だろう、と……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_9")
T "「そういうセクハラ発言が聞きたいわけじゃないわよっ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "常識的に考えておかしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どちらも好きで、選べないなんて間違っている。\n
選ぶことが出来ないのなら、選ぶべきじゃない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「私は一人で……、相手は二人よ？」"

hide bra_m_03_4
show bra_m_01_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice blo_g0600
Blood "「ああ、だから、絞りたいのなら一人に絞ればいい。\n
殺し合わせたくないのなら、二人を相手にするといい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_8")
T "「よくは……、ないでしょ」"

hide bra_m_01_12
show bra_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_8")
voice blo_g0601
Blood "「いいとも。君は誰に遠慮しているんだ？\n
あの子達も君のことが好きで、君もあの子達が好きなんだろう？」"

hide bra_m_01_4
show bra_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_8")
voice blo_g0602
Blood "「問題など、どこにもない」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_7")
T "（問題……、ない？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ないわけがない。\n
ありまくる気がするが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（どうして、この人はこんなに堂々としているのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "悩むのが馬鹿馬鹿しくなってきてしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「だって……、二人とも好き、なんて二股よ？」"

hide bra_m_01_11
show bra_m_03_15 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice blo_g0603
Blood "「それで、誰が困る？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「……え？\n
だって、ほら……、選べないなんて……、酷い話だわ」"

hide bra_m_03_15
show bra_m_03_19 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice blo_g0604
Blood "「だから、誰にとって酷い話なんだ、と聞いている。\n
私からしてみれば、誰も困らないし、誰も酷いとは思わないがね」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（誰にとって？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "他人ごとであるブラッドが困らないのは当然。\n
いや、ブラッドに限らず、他人は何と言っても他人だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "当事者の問題。\n
私と、ディーとダム。"

hide bra_m_03_19
show bra_m_03_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0605
Blood "「ああ、それとも……。\n
君が二人を占有することで、あぶれることになるかもしれない女性のことを心配しているのか？」"

hide bra_m_03_5
show bra_m_02_18 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0606
Blood "「仮定の話はくだらないが……、それに関しては、私がその可哀想な女性の面倒を見ると約束しよう。なあに、女性の一人や二人囲うのは男の甲斐性だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_2")
T "{size=+20}「あなた、いつか刺されるわよ」{/size} "

hide bra_m_02_18
show bra_m_02_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_2")
voice blo_g0607
Blood "「だが、君は刺されない」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "くくっ、と楽しげに笑って、ブラッドは紅茶のカップを傾ける。"

hide bra_m_02_6
show bra_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0608
Blood "「気が向けば、君のお相手も務めよう」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_7")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_8")
T "（最低ね）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_17")
T "（でも……、私よりずっと大人だわ）"

play sound se_0161 volume .7
hide bra_m_02_4
show bra_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_17")
voice blo_g0609
Blood "「おや、行くのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「ええ。\n
ブリーズの準備をしてくるわ」"

hide bra_m_03_10
show bra_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice blo_g0610
Blood "「お嬢さんの健闘を祈っているよ。\n
……また、私のお茶会にも付き合ってくれ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_3")
T "「ええ、気が向けば」"

with dis
$ hi_mes()
hide bra_m_01_11

jump gakuen_dad6_2
