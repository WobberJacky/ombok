label gakuen_nightmare3:
scene bg_map_day
with dis
$ clockanim()

jump gakuen_dream_other
label gakuen_nightmare3_2:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "世界が暗転する。\n
真っ暗な闇の世界だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（そろそろ、目が覚めるの……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これだけはっきりと、夢だと認識できている夢も珍しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これは、夢。\n
だが妄想ではなく、過去あったことそのまま。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（夢じゃなくて、現実）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ただ、時間が異なるだけ。\n
今ではないというだけの、現実だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_3")
T "（夢じゃなくて……）"

play sound se_0167 volume .4
pause 1
play sound se_0167

show white onlayer master with grad_t_short
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どこかで音が聞こえた。\n
見回すより先に、まばゆいスポットライトが目に飛び込んでくる。"

hide white
show m_nai3_1 onlayer master
with dis

play music tragedy2_a_ali
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "闇を丸く切り取るその光の中。\n
浮かび上がる人影は二つ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのどちらもが、私のよく知るものだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_7")
T "（……私と、姉さん？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぞっとした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あの夢の続きのようにして見る、私と姉の組み合わせ。\n
まともな続きであるわけがない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（やめて）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "（見たくない）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "夢を見ている自分を、こんな夢を見せようとしている自分を止めたい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「姉さんなんて……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「姉さんがいなければ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（言わないで）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それは言ってはいけない言葉だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "幼いゆえの過ち。\n
たとえ勢いでも、言っていけないことがある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言葉は力。\n
呪詛になる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（やめてよ、そんな酷いこと……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（言っても、傷つけるだけ。\n
それに傷つくだけ）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_3")
T "（みじめになるだけだわ）"

hide m_nai3_1
show m_nai3_2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_3")
voice ari_g0054
Lorina "「……あなたは酷い子だわ、[firstname]。\n
私のために止めてくれるんじゃないのね」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_7")
T "（……！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつのまにか、スポットライトの下にいるのは姉さんだけになっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふと持ち上がった彼女の視線が、夢の中漂うように希薄な存在である私を見つめている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（姉さんの言うとおりだわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（姉さんに酷いことを言わないようにするのは、私自身のため……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "傷つけたくないのではない。\n
傷つきたくないというほうが大きい。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ari_g0055
Lorina "「あなたはずるい子だわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ari_g0056
Lorina "「ずっと面倒をみてあげたのに。\n
私を残していく」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ari_g0057
Lorina "「ねえ、家から出たいなんて我侭じゃない？\n
私は……、家から出られないのに」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "早くに亡くなった母親に代わり、姉はいつだって私や末の妹の面倒を見てきてくれていた。\n
感謝している。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が卒業したら、今度は私が姉の代わりに家を預かり、姉を外に出してあげるべきだったのではないか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "結局、私は優しい姉に背中を押され、進学の道を選んだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "姉は素晴らしい人で、私は頼りきりの子供。初恋の相手が姉を好きになったからといって、彼女を責めるなんて恩知らずどころの話ではすまない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "夢であっても、こんなふうに姉を責めるなんて、最低だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_3")
T "（言ったら、一生後悔する）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（取り返しがつかなくなる）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "時間は戻せない。\n
夢であっても、それくらい理解しなくては。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "過ちは戻らない。"

play sound se_0670 volume .6
hide m_nai3_2
show white onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ari_g0058
Lorina "「[firstname]。\n
私もね、あなたのことが……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "（……嫌っ！）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「姉さんなんて……」"

play sound se_0106
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
Hatena "「[firstname]……っ！！」"

play sound se_0581
play sound se_0722
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（……？？？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "名前を呼ばれたと思った次の瞬間、ガラスを砕くような澄んだ音が聞こえた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "夢の中の世界のことなので、こんな表現はおかしいのかもしれないが、私はおそるおそると目を開く。"

with dis
$ hi_mes()

scene yume01 ##instant]
hide white with open_long

play music dream_inside_p_ali

scene yume01 with Dissolve(.8)

scene yume02 with Dissolve(1)

scene yume03 with Dissolve(1)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうやら夢のシチュエーションが変わったらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「……あれ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "周囲が明るい。\n
明るいといっても、光源のはっきりしたまともな世界にいるわけでもないようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "様々な色を適当に混ぜて流し込んだというような、曖昧な世界だ。\n
上下左右の感覚もない中に、私は漂っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "先ほどまでの眺めるだけの夢とは違い、どうやら今の私にはちゃんとした個としての存在がある。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（……姉さんは？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "胸に痛みを覚えながら、夢の空間の中で姉の姿を探してきょろきょろと周囲を見やる。\n
姿はもう見えない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その事実に、安堵を覚えてしまう自分がますます嫌になる。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0060
Hatena "「……もう、大丈夫だ。\n
怖い夢は見ないよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どこからか、知っている声が響く。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（ナイトメア……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうして彼の声を夢に聞くのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0061
Nightmare "「安心してゆっくりお休み……。\n
私がいるから、悪夢は君には近寄れない」"

menu:
    "落ち着く声だ。":
        jump gakuen_nightmare3_3a
    "耳障りだ。":
        jump gakuen_nightmare3_3b
label gakuen_nightmare3_3a:
$ lovechara_nightmare_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（……落ち着く）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "柔らかな声音は、子供に言い聞かせるように穏やかな響きを伴っている。"

jump gakuen_nightmare3_4
label gakuen_nightmare3_3b:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（……嫌な声だわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こんなところでは聞きたくなかった。\n
私自身の醜さが、ここまで暴かれた場所で聞きたい声ではない。"

jump gakuen_nightmare3_4
label gakuen_nightmare3_4:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……どこにいるの？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "声だけが、どこからともなく響く。\n
そしてその声が響くと同時に、急速に眠気に襲われた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "目が開けていられないほどの、睡魔。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "妙な話だ。\n
ここはすでに夢の中で、私は眠っているはずなのに。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "夢の中で、さらに眠くなっている。\n
一段深い眠りに攫われていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "このまま意識を失ったら、どうなるのだろう。倒れるのか、それとも私の意識がなくなると同時にこの世界にある私の体が消えるのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（でも……、大丈夫なのよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "低く、柔らかに響いたナイトメアの声は、信用できる気がした。"

show black onlayer master with close_long
pause 1
play music morning_a_wam

scene bg24_rj_day ##instant]
hide black with open_long
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふ、と瞼を持ち上げた。\n
嫌な夢を見ていたはずなのに、目覚めが穏やかであることに内心驚く。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（どうして……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "悪い夢にならなかった。\n
夢の中で私は姉を罵らなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつも、そんな愚かな行動で目が覚める。\n
現実にはやらなかったことでも、夢ではみっともなく失敗してしまうのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（今回は、落ち着いている）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最悪な夢には変わりないが、それでも目覚めは暗いものではなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_15")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は、ずっと姉に憧れていたらしい。\n
彼自身がそういったわけではないが……、きっと私に親切にしてくれたのも、私が姉の妹だったからなのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼にとって私は、「[firstname]＝[familyname]」ではなく、「ロリーナ＝[familyname]の妹」だったのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（……だけど、ここでは[firstname]＝[familyname]だわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう思えるだけ、シンフォニアに来た効果はあったということだろうか。\n
昔はこの夢をみては、酷い結末に泣きながら起きた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（そういえば）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "夢の中、悪夢から救ってくれた声。\n
姿を見ることはなかったが、あれはナイトメアの声だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（でも、どうして？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "夢からの救出者がナイトメアだという演出には疑問が残る。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……夢にみるほど意識している、とか？）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……ないない）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "身体測定のときもそうだが、考えすぎだ。"

jump gakuen_cafeteria_notjoker
label gakuen_nightmare3_5:

scene bg01_cr_day with Dissolve(.8)

scene bg27_rk_day
with stripe_l_medium

scene bg_map_day
with stripe_l_long
##endmemory
jump gakuen_nightmare4
