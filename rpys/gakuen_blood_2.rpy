label gakuen_blood2:
scene bg_map_day
with dis
$ clockanim()


scene bg_map_eve
with dis

scene bg_par12_hct_eve
with dis

play music evening_a_wam

scene bg_par12_hct_nig_s with Dissolve(1.2)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それから、放課後度々ブラッドの茶会に招かれるようになった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドは毎度種類の違う茶葉を用意しては、美味しい茶菓子とともに私をもてなしてくれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ときたま、会話の端々に危険な匂いを感じずにはいられなかったりもするが、基本的には紳士な男だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何かを要求するにしても、引き際は心得ている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうして幾度となく逢っているうちに、やはり次第にその横顔が、雰囲気が、知る誰かに似ているんじゃないか、という思いはますます強くなっていった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（誰、だっけ……？）"

with dis
$ hi_mes()

scene bg_par12_hct_eve
with dis

scene bg_par15_rg_hat_eve with Dissolve(.8)

scene bg25_rr_eve
with stripe_l_medium

scene bg24_rj_eve
with stripe_l_medium

scene bg24_rj_nig with Dissolve(.8)

scene black with close_long

play music dream_inside_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、そんなある日の夜、私は夢を見た。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "嫌な夢だった。\n
いや、正確には懐かしい夢で、ちっとも嫌な要素はないはずだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "怖いものに追いかけられるわけでも、何かひどいことが起こるわけでもない。\n
ただ、穏やかな時間に、穏やかな会話を交わすだけの夢だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それだけの夢なのに、その夢だと知覚した瞬間に、「あ、嫌な夢だ」と思ってしまったことに気が沈んだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（まだ、引きずっているんだわ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "起こったこと事態が、なんでもない、些細なことだということは分かっている。\n
それに、もうずっと前のことだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分でも忘れていたぐらい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それなのに今こうして夢に見て、悪夢だと思ってしまったことが……、癒えていなかった傷口を見せ付けられたようで悔しくなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……心の傷なんて、大層なものでもないのに）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、間違いなくトラウマになっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな弱い自分が嫌で嫌で仕方がない。"

with dis
$ hi_mes()
##special anime old film
show m_kyoutuu_yume1 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_t_06_16")
T "夢の中の舞台は、窓から日が差し込む小さな部屋。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_t_06_16")
T "壁際には古い本棚がいくつか置かれており、そこにはもう誰も必要とはしていないんじゃないかと思わざるを得ないような古びた資料が、整然と並べられている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_t_06_16")
T "夢の中だというのに、匂いまでが鮮明だ。\n
黴臭いような、それでいてどこか甘い古い紙の匂い……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_t_06_16")
T "部屋の中ほどでは、なにやら机の上の私物を整理している人物の姿が見える。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_t_06_4")
T "（……先生）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_t_06_4")
voice blo_g0126
Seinen "「……ん？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_t_06_16")
T "心の中で呟いただけの呼び名は、夢の中だからか、伝わった。"

hide m_kyoutuu_yume1
show m_kyoutuu_yume2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_t_06_16")
T "彼がふっと顔をあげ、私を見て笑った。\n
穏やかな笑顔だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_t_06_16")
T "全然似てなんかいない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_t_02_15")
T "（……誰に？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_t_06_16")
T "一瞬頭の中によぎる人を、軽く頭を左右にすることで振り払った。"

jump gakuen_dream_all
label gakuen_blood2_2:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_t_01_1")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_t_06_13")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_t_01_7")
T "「わ～い、ラブレターが二通に増えたー……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_t_01_6")
T "「…………」"

with dis
$ hi_mes()


hide m_kyoutuu_yume2 with open_medium
play sound se_0328
camera at hpunch
camera at vpunch

play music room2_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "むくっ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_10")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「……虚しい」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、痛々しい。\n
最悪な寝起きだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……ああ、もう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "気にしたくないし、もう平気。\n
と、少なくとも、今までは思っていたが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それなのにこんな夢を見る、ということは、やはり気にしているということなのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんでもない振りをしようとしている傍から、それを裏切る自分の深層心理が憎たらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は、ずっと姉に憧れていたらしい。\n
彼自身がそう言ったわけではないが……、きっと私に親切にしてくれたのも、私が姉の妹だったからなのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼にとって私は、「[firstname]＝[familyname]」ではなく、「ロリーナ＝[familyname]の妹」だったのだ。"


play music honobono1_a_ali
with dis
$ hi_mes()
show m_bra2_1 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（……姉さん）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "完璧に美しく、優しく、聡明な姉を思うと胸が痛んだ。\n
私が、全寮制の学校に行きたかった、本当の理由。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私を通り越して姉を見ていた彼に、自分を見てくれているという幻想を抱いていたなんて、今思い出しただけで羞恥で死にたくなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう、私は文字通り、逃げ出したのだ。\n
唯一の救いは、誰にも私の想いを知られることなく終わったことだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いや、救いにもならない。\n
手紙を押し付けて、玉砕すればまだすっきりと出来たのかもしれないが、私は結局あのときから凍結したままでいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "未練がましく、引きずりまくって……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "根暗な私は、失恋すると引きずりすぎる。\n
それが、私が恋愛なんかしないと決めた理由だ。"

play sound se_0586

scene bg06_sk_h_day
with dis
hide m_bra2_1

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（恋愛なんて……。\n
……向いていない）"

play sound se_0693
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "姉さんのようにはなれないと、未だ鬱々とした気持ちを抱えている。\n
恋は、私を嫌な人間にしてしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自立したい、なんて格好つけたことを言って、本当はただ、姉の後を追いかけるのが嫌だったからなのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "姉と同じ場所にいては、比べられてしまうのが分かっていたから。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "忘れていたふりをして、本当はじくじくと傷口を膿ませていただけだったのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（私は……、逃げたのよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あのときと同じ。\n
変わっていない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……臆病者だ。\n
今なら彼が、私を眼中に入れていなかったのも分かる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……鬱陶しいな、私）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それが嫌で、距離を置いたのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "姉は何も悪くないし、私には成長が必要だ。\n
そういうふうに考えれば、建設的。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（あのときも、預かった手紙を捨てるなんて真似はしなかったし……。\n
私だって、捨てたものじゃないわよね？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "増えた、ラブレター。\n
彼のラブレターはきちんと姉へと渡した。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "さりげなく、なにげなく。\n
学校でお世話になった人から預かってきたの、と。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんでもない顔で言えた……、と思う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "姉は、あらあら……と困ったように微笑みながら、その手紙を受け取っていた。\n
それを姉が読んだのか、そして返事を出したのかを、私は知らない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "けれど、彼が姉の恋人として家に来るようなことはなかったので、きっと姉にはふられてしまったのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……あ。\n
そういえば……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_11")
T "「……私が書いたのは、どこへやったんだっけ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "燃やしたか、捨てたか。\n
どうにかして処分した気はするのだが、具体的にどうしたのかを思い出せない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "忘れた頃に、どこかからひょっこり出てきたりなどしたら、笑い話にしてしまえるのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……今でも充分、笑い話ね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ラブレターを渡しにいった相手から、別の人宛のラブレターを託されてラブレターが増えるなんて。\n
充分な笑い話だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（笑えないのは、私だけ）"


scene bg24_rj_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "鬱陶しく沈みながらも、ベッドを抜け出し、朝の身支度に取りかかる。"

jump gakuen_cafeteria_notjoker
label gakuen_blood2_3:
with dis
$ hi_mes()

scene bg_map_day
with stripe_l_medium

scene bg_map_eve with Dissolve(.8)

scene bg25_rr_eve
with stripe_l_medium

play music corridor_nig_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "放課後、一度自室に戻って教科書などの荷物を置いてから、テラスに向かう。\n
もはや放課後のお茶会は、私にとっても日課だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_6")
T "（今日の紅茶は何かしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなのを楽しみにしてしまっているあたり、絆されている自覚もある。\n
ブラッド＝デュプレの思うつぼだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "分かっていても、あまり嫌な気がしないのは私が彼に慣らされてきているのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_1")
T "（美味しい紅茶が飲めるんだから、いいわよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつものように、ドアを開ける。"

play sound se_0200

play music hatter_garden_p_ali

scene bg_par12_hct_eve
with dis

show eri_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0000
Elliot "「お、[firstname]！\n
遅かったな！」"

hide eri_m_01_4
show eri_m_01_4 at left
with dis

show dee_m_01_6 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0000
Dee "「お姉さんだ！\n
お姉さん、おかえり！」"

hide eri_m_01_4

hide dee_m_01_6
show dee_m_01_6 at left
with dis

show dam_m_01_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0001
Dam "「お姉さんだ、お姉さんだー！\n
お姉さん、おかえり！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "かけられた声に、目をぱちくりとさせてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「あら、あなた達も来ていたの……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "たいていは私とブラッドの二人で、だるだるとひたすら紅茶を愛でるお茶会なのだが、たまにエリオットや双子が加わることもある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今日はその、珍しくエリオットや双子が茶会に加わっている日、だったようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットは日頃からいろいろなことで忙しくしているし、双子は悪戯に夢中で、こうして一所に集まっておとなしくしているということがあまりない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それでも、何度かともに茶会に参加しているうちに、すっかり打ち解けてしまっていた。"

hide dee_m_01_6
show dee_m_02_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0002
Dee "「お姉さん、こっちこっち！\n
今日は僕達がお姉さんをもてなしてあげるよ！」"

hide dam_m_01_2
show dam_m_01_6 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0003
Dam "「ほら、座って座って。\n
お姉さん、こっちだよ！」"

play sound se_0161
hide dee_m_02_4

hide dam_m_01_6

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "双子に促されて、私はその隣へと腰掛けた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつもならばブラッドの向かいに座るのだが、現在その彼は何故かテーブルの端にいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その顔色が少しよくないように見えるのはどうしてだろう。"


show dee_m_02_10 at left
with dis

show dam_m_02_10 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（この子達が、もてなすって……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "テーブルの上にはこれでもか、といわんばかりのお菓子の山。\n
この三人が加わったときの茶会の特徴だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "双子が持ち込んだ原色が毒々しいお菓子の数々から、エリオットの前に広がる鮮やかなオレンジ色の世界……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドはいつも、それらをなるべく視界に入れないようにして茶を啜っている。\n
さすがにボスとはいえど、部下達の食に関する好みにまでは口出ししないらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "妙なところで律儀というか……。\n
自分も自分で食にこだわりがあるが故かもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「珍しいわね、あなた達がこうしてお茶会に参加するなんて」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットはたまに顔を出したりすることもあったが、双子達がこうして茶会に顔を出すのは本当に珍しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "日頃は、帽子屋寮の警備担当という言葉を疑わしく思ってしまうほどに寮内でその姿を見かけないのだ。"

hide dee_m_02_10
show dee_m_02_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0004
Dee "「今夜のことで打ち合わせがあったからだよ、お姉さん。\n
僕達子供だから、普段は座って話するだけなんて飽きちゃうんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……打ち合わせ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "顔を上げて様子をうかがってみるが、向かいのエリオットは嬉しそうに顔をほころばせてオレンジ色のケーキをもりもり食べている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、ブラッドは視線を遠くにやったまま茶を啜っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何か話が立て込んでいるようならば席をはずそうかと思ったのだが、すでに打ち合わせは終わっているようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「打ち合わせって……。\n
あなた達まで何かするの？」"

hide dee_m_02_4
show dee_m_02_12 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice dad_g0006
Dee "「僕達までって？\n
そりゃあ、他の連中も皆……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_15")
T "「使用人が何人か庭でバットを振っているのを見かけて気になっていたのよ。\n
それに、皆もなんだか浮かれているみたいだし……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスとのやりとりで深く追及しようとする気はなくなっていたが、気にならないわけではない。\n
朝からの疑問を口に出してみる。"

hide dee_m_02_12
show dee_m_02_12 at left_center
hide dam_m_02_10
show dam_m_02_10 at center
with dis

show eri_m_01_5 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0001
Elliot "「あんた、新入生だもんな」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "三人が思い当たった、というように視線を交し合う。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「皆、その時までは内緒って言うばかりで、教えてくれないのよ」"

hide eri_m_01_5

hide dee_m_02_12

hide dam_m_02_10


show bra_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice blo_g0146
Blood "「そうだな、楽しみは最後まで取っておいたほうがいい。\n
……今日の夜には分かるさ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「夜に？」"


show dee_m_01_6 at center
with dis
hide bra_m_02_8

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_4")
voice dad_g0009
Dee "「そう、夜のお楽しみ！\n
ふふふ、楽しみだね兄弟！」"

hide dee_m_01_6
show dee_m_01_6 at left
with dis

show dam_m_01_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_4")
voice dad_g0010
Dam "「うん、楽しみだね、兄弟！\n
……今年こそは勝ちたいよね」"


show eri_m_02_6 at right_center
hide dee_m_01_6
show dee_m_01_6 at left_center
hide dam_m_01_7
show dam_m_01_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_4")
voice eri_g0002
Elliot "「おまえらまだやってんのか？\n
そういうイベントじゃないだろ、アレ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一体、何があるというのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（勝つ、ということはゲーム大会？\n
勝負事？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だがエリオットの口ぶりでは、双子の楽しみ方は趣旨に反しているらしい。\n
……謎だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "が、とりあえず楽しそうではある。\n
気になるが、夜になるのをおとなしく待つとしよう。"

hide eri_m_02_6

hide dam_m_01_7
show dee_m_02_4 at right
with dis
hide dee_m_01_6
show dee_m_01_7 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0013
Dee "「それよりお姉さん！\n
僕達、お姉さんをおもてなししようと思って待っていたんだよ！」"

hide dee_m_01_7
show dee_m_02_4 at left
with dis
hide dee_m_02_4
show dam_m_02_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0014
Dam "「いつもボスだけがお姉さんとお茶なんてずるいからね！\n
今日は僕達がお茶を淹れてあげるよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「え？\n
あなた達が？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そういえば先ほどから、そんなことを言っていたような気がする。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_7")
T "（この子達が……、おもてなし？\n
出来るの？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "双子達はそれぞれ懐から杖を取り出した。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（……んん？）"

hide dam_m_02_2
show dam_m_01_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice dad_g0016
Dam "「僕達がスペシャルな紅茶を淹れてあげるからね！」"

play sound se_0457
hide dee_m_02_4
show dee_m_03_15 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
Dee "「…………」"

play sound se_0458
hide dam_m_01_2
show dam_m_03_15 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
Dam "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「ねえ……。\n
どうして、紅茶を淹れるのに、呪文が必要なの？」"

play sound se_0727

show white onlayer master with expand
hide dee_m_03_15

hide dam_m_03_15

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_9")
T "「……っ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ディーとダム、それぞれの呪文が完成すると同時に、机の上で光が弾ける。\n
そして光が引いた頃、テーブルの上で繰り広げられていた光景に私は呆然とした。"

hide white with compress
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「は……！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ティーカップやポットが出現したのはいい。\n
それは分かる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが……。"

show m_bra2_2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「な、なんで{size=+20}手足が生えている{/size}のよ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう。\n
テーブルの上に出現したティーセットには、すべて細い人形のような手足が生えていた。"

play sound se_0171
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "体操でもするように、不気味なティーセットがうごめいている。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0017
Dee "「そりゃあ、お姉さんにスペシャルな紅茶を淹れてあげるためだよ！\n
全自動でやってくれるからね！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0018
Dam "「手足が生えていれば、自力で全部やってくれるでしょう？\n
いい考えだと思ったんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人はにこにこと得意顔だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "確かに手足が生えていれば、自分でティーポットを傾けて紅茶をカップに注いでくれるかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ソーサーやカップに手足が生えていれば、自力で客の前にやってきてくれるかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、どう見てもその光景は{size=+20}不気味{/size}だ。\n
紅茶を楽しめるかどうかというと、甚だ疑問だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0019
Dee "「まずは充分なスペースを確保しないとね、兄弟」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ディーの声に反応するように、手足の生えたティーセット達がぞろぞろと動き出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その向かった先は、エリオットのオレンジワールドだ。"

play sound se_0171
pause .3
play sound se_0545

scene bg06_sk_h_eve
with dis
hide m_bra2_2

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼ら（？）はオレンジ色の茶菓子の乗った皿に次々と手をかけると、ぶんっ、ぶんっと勢いよく振り回すようにして遠投し始めた。"

play sound se_0765
pause 1
play sound se_0318
$ flash(.2)
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Elliot "{size=+20}「！！！？」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0003
Elliot "「俺の、にんじんマカロンとにんじんショートケーキが……っ！！\n
何しやがる、てめえら！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0022
Dam "「見ても分からないなんて、本当にひよこウサギって馬鹿だよね。\n
邪魔なものをどかしているのが分からないの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう言っている間にも、次々とオレンジ色の茶菓子が皿ごとテーブルの外へと弾き出されていく。"

play sound se_0765
pause .2
play sound se_0765
pause 1
play sound se_0315
$ flash(.2)
$ flash(.1)
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Elliot "「……！！」"


scene bg_par12_hct_eve
with dis


with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「ちょっとこら、あなた達」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いくらなんでも（それらすべてがオレンジ色だとしても）、食べ物を無駄にするのはよくない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は双子を止めようと口を開くものの、それより先にエリオットがキレた。\n
もともと堪忍袋の緒がそれほど強くないウサギさんだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その目の前で、彼のにんじん菓子を放り捨てたのだ。\n
これはもう、暴れないほうがおかしい。"


play music gag3_a_ali

show eri_m_02_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0004
Elliot "{size=+20}「てめえら～～～っ！！\n
ぶっ殺す！！」{/size} "


show dee_m_02_3 at center
with dis
hide eri_m_02_9

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0023
Dee "「やれるものならやってみろよ、ひよこウサギ！！」"

hide dee_m_02_3
show dee_m_02_3 at left
with dis

show dam_m_02_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0024
Dam "「遊んでやるよ、ひよこウサギ！！」"

play sound se_0161
pause .3
play sound se_0160
pause .3
play sound se_0013
pause .3
play sound se_0161
pause .3
play sound se_0161
hide dee_m_02_3

hide dam_m_02_2


scene bg06_sk_h_eve
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "全自動で紅茶を淹れるため……、だとか言っていたはずの手足をフルに活用し、ティーセット達がフォークやナイフを握ってエリオットへと飛び掛っていく。"

play sound se_0297
pause .5
play sound se_0297
pause .1
play sound se_0297
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それを迎撃すべく、引き抜かれたエリオットの銃が吼える。"

play sound se_0523
pause 1.5
play sound se_0281
$ flash(.1)
play sound se_0281
$ flash(.1)
play sound se_0281
$ flash(.1)
play sound se_0281
$ flash(.1)
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_9")
T "（……{size=+20}何、この惨状{/size}）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私に紅茶を淹れてもてなしてくれるという話は、いったいどこへ行ってしまったのか。"


scene bg_par12_hct_eve
with dis

show bra_m_02_17 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0147
Blood "「……巻き込まれる前に、避難することを推奨するがね。\n
それとも、巻き込まれたいのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「……まさか」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "横合いからかけられた声に、はっと我に返った。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "このままここにいれば、いつ流れ弾（もしくは流れ食器）に当たってもおかしくない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "慌てて頭を低くして、先に避難していたブラッドの傍らまで逃げ込んだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼がこうしてテーブルの端にいたのは、双子にもてなし役を譲ったからというわけでなく……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こうした馬鹿げた騒ぎに巻き込まれるのが目に見えていたからなのだろう。"

play sound se_0686 volume .7
pause .15
play sound se_0543 volume .7
$ flash(.1)
$ flash(.1)
$ flash(.2)
hide bra_m_02_17
show bra_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Blood "「…………」"

play sound se_0523 volume .7
pause 1.5
play sound se_0281 volume .7
$ flash(.1)
play sound se_0281 volume .7
$ flash(.1)
play sound se_0281 volume .7
$ flash(.1)
play sound se_0281 volume .7
$ flash(.1)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ほんの少ししか離れていないところで銃声やら皿の割れる音やら破壊音が次々と響く中、ブラッドは悠々と紅茶のカップを傾けている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "常日頃から我関せずといった様子は無責任にも見える。\n
だが、今は、私もその仲間に入りたい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……あっちには混ざりたくない）"


play music gag1_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……私にも、一杯いただけるかしら」"

hide bra_m_03_2
show bra_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice blo_g0148
Blood "「ああ、もちろんだとも」"

hide bra_m_03_4
show bra_m_02_18 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice blo_g0149
Blood "「せっかくダージリンのセカンドフラッシュを淹れたというのに、こいつらにはその味が分からないらしい」"

hide bra_m_02_18
show bra_m_02_14 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice blo_g0149_5
Blood "「お嬢さんなら、この味の素晴らしさを分かってくれるだろう？」"

menu:
    "分かると思う。":
        jump gakuen_blood2_5a
    "難しい。":
        jump gakuen_blood2_5b
label gakuen_blood2_5a:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「そうね……。\n
たぶん、分かると思うわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "少なくともにんじんマニアなエリオットや、まだまだ子供味覚のツインズよりは、紅茶の味が分かると思う。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_17")
T "（……ブラッドと比べたら、足元にも及ばないけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "むしろ、及びたくないので、それはいい。"

jump gakuen_blood2_6
label gakuen_blood2_5b:
$ lovechara_blood_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「どうかしら、難しいわ。\n
あなたの用意する茶葉はどれも最高級品で、これまで私が口にしたことのないものばかりなんだもの」"

hide bra_m_02_14
show bra_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice blo_g0150
Blood "「ふふ、最高級のものだと認識してもらえるだけでもありがたいよ。\n
やはり君は違いの分かるお嬢さんだ」"

jump gakuen_blood2_6
label gakuen_blood2_6:
play sound se_0161
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "薦められるままに、ブラッドの向かいの席へと座る。"

hide bra_m_03_4
show bra_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0151
Blood "「……さあ。\n
どうぞ？」"

play sound se_0174
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "慣れた手つきで紅茶を淹れたブラッドが、私の前へとティーカップを差し出してくれた。\n
甘い香りが、ふわりと香る。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "マスカットにも似た爽やかな香りは、それが上質な茶葉であることを示していた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「……っ、すごいわね。\n
こんなにもはっきりと香りのついたダージリンは初めてだわ」"

hide bra_m_01_2
show bra_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_7")
voice blo_g0152
Blood "「そうだろうそうだろう、君ならば分かってくれると思っていたんだ……！」"

hide bra_m_03_3
show bra_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_7")
voice blo_g0152_5
Blood "「これだけ強いマスカテルフレーバーを持つ意味、厳選された茶葉だけが持つこの味わい……！」"

hide bra_m_02_8
show bra_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_7")
voice blo_g0153
Blood "「茶葉ももちろん素晴らしいが、このブレンドがまた秀逸だ」"

hide bra_m_03_2
show bra_m_02_19 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_7")
voice blo_g0153_5
Blood "「葉はもちろん上質のフラワリー・オレンジ・ペコーだが、そこに含まれるチップの量がまた絶妙なバランスで柔らかな口当たりを演出していて……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドはきらきらとしている。\n
むしろ、めろめろ、だろうか。"

play sound se_0405 volume .7
pause .5
play sound se_0523 volume .7
pause 1.5
play sound se_0281 volume .7
$ flash(.1)
play sound se_0281 volume .7
$ flash(.1)
play sound se_0281 volume .7
$ flash(.1)
play sound se_0281 volume .7
$ flash(.1)
pause .7
play sound se_0543 volume .7
$ flash(.1)
$ flash(.1)
$ flash(.2)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その語り口調と、背後から響く破壊音とがなんとも……。"

hide bra_m_02_19
show bra_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0154
Blood "「紅茶とは、かくも素晴らしいもので……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "紅茶について語るときのブラッドは、日頃のどこか気だるげな様が嘘のように輝いている。\n
まるで別人だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなふうにきらきらしていると……、今朝方、夢に見てしまった彼に似ているように見えてしまって、戸惑う。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（似ているわけがないのに……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（似ていない……、わよね？）"

hide bra_m_03_9
show bra_m_03_16 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice blo_g0155
Blood "「……どうした、お嬢さん。\n
ダージリンは口に合わなかったか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「え？\n
あ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「いえ、そんなことないわ。\n
とっても美味しい」"


show dee_m_01_5 at center
with dis
hide bra_m_03_16

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice dad_g0025
Dee "「お姉さんは、ボスのテンションに呆れているんだよね、兄弟」"

hide dee_m_01_5
show dee_m_01_5 at left
with dis

show dam_m_01_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice dad_g0026
Dam "「そうだね、兄弟。\n
ボスの紅茶にかける情熱は異常だよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットと魔法大戦を繰り広げていたはずの双子が、ひょいっと会話に混ざってきた。"

play sound se_0371

show white onlayer master with spread_long
pause .1
hide white with spread_long
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それにより集中力が途切れたのか、手足の生えたティーセットたちがテーブルの上から消えていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットも、にんじん菓子を破棄されたことより、尊敬してやまない上司を異常扱いされたことの方が聞き捨てならなかったのか、銃を収めて席に戻ってきた。"

hide dee_m_01_5

hide dam_m_01_5

show m_bra2_3 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0005
Elliot "「おい、こら……。\n
ブラッドを馬鹿にしたら……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0027
Dee "「ボスの紅茶好きって度を越していると思わないの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0006
Elliot "「いや……、う～ん、そうだな、マスカットの匂いも悪くないけどよ……。\n
俺は、にんじん茶のほうが好きだぜ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0156
Blood "{size=+20}「ダージリンのマスカテルフレーバーとにんじん茶を同列に語るな」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0157
Blood "「茶葉を使っていない茶など、私は茶とは断じて認めんぞ。\n
にんじん茶などにんじんを湯に溶かしただけだろう、にんじんを」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0007
Elliot "「え～、そうか？\n
うまいと思うんだけどなあ、にんじん茶」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0008
Elliot "「ああ、でもブラッドが好きな茶と違って、甘くないからなあ。\n
ハチミツでも入れたら、ブラッドでも飲めるか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0158
Blood "{size=+20}「何を入れようと、オレンジ色のものが入っている時点で飲まない」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0159
Blood "「足すよりも省け！\n
余計なものをだな……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0009
Elliot "「でもよお、にんじん茶からにんじんを抜いたら、それ、湯になるんじゃねえ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0160
Blood "「白湯のほうがいくらかマシ……。\n
いや、そもそも私は甘くないからにんじん茶を好まないというわけでなくだな……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0161
Blood "「茶というのは本来様々な工程を経て茶葉を発酵させ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0010
Elliot "「はまれば、癖になるのになあ。\n
[firstname]、今度あんたにも持ってきてやるよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「え……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice blo_g0162
Blood "「{size=+20}いらん{/size}。\n
私の茶会にそんなものを持ち込んだら、おまえごと始末するぞエリオット」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice blo_g0163
Blood "「お嬢さんのための茶は、私が用意すると決めているんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice blo_g0163_5
Blood "「違いの分かるお嬢さんの貴重な味覚を、オレンジ色の物体で破壊しようとするのはやめなさい」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice eri_g0011
Elliot "「え～……。\n
なんだよ、食わず嫌いになっちまうぜ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が答えるより先に、ブラッドがエリオットの親切な（つもりの）申し出を却下した。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "にんじんを愛好してやまない腹心の言葉に、ブラッドは心底嫌そうに顔をしかめている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドの言うとおり、にんじん茶、というのは名前にこそ茶とついてはいるものの、茶葉は一切使用していない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "他のフレーバーティーなどとは一線を画している。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何せ、にんじんを乾燥させ、粉末状にしたものをお湯に溶かして飲むというシンプルさだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドの言うとおり、にんじん以外の何物でもない。"

hide m_bra2_3
show m_bra2_4 onlayer master
with dis

play music flower_eve_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "嫌そうに顔をしかめたブラッドと、純粋な好意に顔を輝かせるエリオットの二人が面白くて、つい口元が緩んでしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ならず者と呼ばれる男達。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちょっとしたことをきっかけに杖を抜き、強力な魔法を駆使して喧嘩を繰り広げながらも、話題が変われば何事もなかったかのように席に戻って談笑する。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それが微笑ましく見えてきたのだから、私もだいぶこの寮に馴染んでしまったようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニア高位魔法学校の不良グループ（？）の幹部達に混じって、お茶をする。\n
日常の中の非日常だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0164
Blood "「……何を笑っているんだ、お嬢さん」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_7")
T "（……っと。\n
にやにやしすぎかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これでは、私のほうが危険人物のようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_13")
T "「なんでもないわ、ちょっと、その……。\n
そう、思い出し笑いよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_13")
voice blo_g0165
Blood "「……ふん。\n
思い出し笑いとは、いやらしい……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「……そう言う発想がいやらしいわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "茶化しつつも不機嫌そうなブラッドの追及を誤魔化すべく、ちらり、と顔をあげて景色を見やる。"



hide m_bra2_4

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "赤々とした夕日はすでに沈み、空のふもとをほの赤く染めるだけだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そろそろ、夕食の時間だ。\n
夜は近い。"

with dis
$ hi_mes()

scene bg_par15_rg_hat_eve
with stripe_l_medium

scene bg_map_eve
with stripe_l_medium
##endmemory
jump gakuen_blood3
