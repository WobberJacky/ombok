label gakuen_gowland3:
scene bg_map_day
with dis
$ clockanim()

jump gakuen_dream_other
label gakuen_gowland3_2:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_12")
T "「……やな、夢」"

with dis
$ hi_mes()

scene bg24_rj_day with open_m

play music room2_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "寝起きの回らぬ舌。\n
ぼんやりと呟いて、目が覚めた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（……暗くなる）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "爽やかで明るい朝の光と、暗い気持ち。\n
カーテンの隙間から漏れ零れる陽光も、冷たくなった気持ちを温めてくれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最悪な目覚めだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……ああ、もう」"

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

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（……ピアノみたい）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私には弾けない曲を易々と演奏してみせる素敵な姉さん。\n
それを、私は羨望と嫉妬のこもった視線で見つめるしかなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "完璧に美しく、優しく、聡明な姉を思うと胸が痛んだ。\n
全寮制の学校に行きたかった、本当の理由。"

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

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（恋愛なんて……。\n
……向いていない）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "姉さんのようにはなれないと、未だ鬱々とした気持ちを抱えている。\n
恋は、私を嫌な人間にしてしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（……でも、今ならどうなのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あの頃弾けなかった曲が、今なら弾けるようになった。\n
自身が気付かないままでも、私は成長していた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あの頃届かなかったオクターブにも、指が届くようになった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それならば、同じように……、あの頃手に入らなかったものも、今なら手が届くのではないだろうか。"


scene bg06_sk_h_day
with dis
jump gakuen_cafeteria_notjoker
label gakuen_gowland3_3:
with dis
$ hi_mes()
$ time_effect()##PLEASE MANUALLY ADJUST ME
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつものようにホームルームを終え、教室を出ようとしたところでゴーランドに呼び止められた。"


play music gowland_t_ali

show go_m_03_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0076
Gowland "「[firstname]、ちょっといいか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_8")
T "（……何？）"

menu:
    "私が失敗をした？":
        jump gakuen_gowland3_4a
    "友人がトラブルでも起こした？":
        jump gakuen_gowland3_4b
label gakuen_gowland3_4a:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（私……、何か呼び出されるようなこと、しちゃったっけ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私も、そそっかしいところがある。\n
気付かぬうちにミスをしてしまったのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……勉強の失敗？\n
小テストが悪かった？）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_11")
T "（それとも、何か素行上の……）"

jump gakuen_gowland3_5
label gakuen_gowland3_4b:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（誰かが……、何かまずいことをしでかしたの？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何かの事情聴取だろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今までにもこういうことはあった。\n
私自身が何かしたというよりも、友人連中が何かしたと考えるほうが普通だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……ボリス？\n
それともピアスかしら？）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_11")
T "（それとも、他の……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "遊園地寮には賑やかな面子が揃っている。\n
その分、お祭り騒ぎのような問題も派生しやすい。"

jump gakuen_gowland3_5
label gakuen_gowland3_5:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……でも、なんにしても、悪意あってのことじゃないわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドは振り返った私相手に、なんだかとても難しい顔をしていた。\n
言おうか、言わざるか逡巡するような、そんな顔だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（……なんだろう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "教師としてのゴーランドは、あまりそういった迷いを見せない。\n
指針がしっかりとしてから話すタイプなのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私達生徒に対しては、常に筋の通った対応をしてくれている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だから、こうしてゴーランドが迷っているということはプライベート絡みの可能性が高い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう思うと気負っていたものが抜けた。\n
教師と生徒ではあるが、プライベートでのゴーランドはもっと気安い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "親しい相手だと、少なくとも私は、そう思っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「どうしたの？\n
……ここではしにくい話？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちらりと周囲の様子を伺ってみる。\n
未だ何人かの生徒が教室内には留まっているが、特にこちらを気にしている様子はない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私とゴーランド、という組み合わせは、珍しくないのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドとボリスが一緒にいて誰もおかしいと思わないぐらいには、馴染んでしまっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それでも彼が気にするようならば、場所を変えても構わない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「何か、相談事でも？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（変なの）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これでは立場が逆転している。\n
私のほうが生徒なのに。"

hide go_m_03_7
show go_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0077
Gowland "「ああ……、まあ、うむ。\n
う～……、ぐああああ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ばりばり、とゴーランドが髪をかきむしる。\n
なんだか非常に悩ましげだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「？？？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何をそんなに悩んでいるのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（悩み事？\n
私で力になれるかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_13")
T "「私に何か、出来ること？」"

hide go_m_02_1
show go_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_13")
voice gor_g0078
Gowland "「あ～……、あんたにしか、出来ねえことだよ。\n
でもなあ……、うーん」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「難しいことなの？\n
危なかったりする？」"

hide go_m_03_2
show go_m_01_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_4")
voice gor_g0079
Gowland "「難しい……、そうだな、そうかも。\n
だが、危なくはねえな」"

hide go_m_01_7
show go_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_4")
voice gor_g0080
Gowland "「……つーか、教職にある俺が生徒にそうそう危ないことさせるわけないだろ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_4")
T "「え～？\n
結構、させるくせに」"

hide go_m_03_11
show go_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_4")
voice gor_g0081
Gowland "「う……。\n
そんなには……、ないだろ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「まあ、そこまでは、ね」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……ふむ）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_14")
T "「……いいわよ」"

hide go_m_02_10
show go_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_14")
voice gor_g0082
Gowland "「は？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_1")
T "「何か私に頼みたいことがあるんでしょう？\n
危なくないなら引き受けるわ」"

hide go_m_03_3
show go_m_03_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_1")
voice gor_g0083
Gowland "「ちょっと待て、あんた、内容も分からねえのに引き受けるってのか？\n
コラ、やめとけやめとけ、そういうのはよくないぜ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "大真面目に止められて、半眼になった。\n
頼みたいことがあると言ってみたり、それを止めてみたりと、はっきりしない男だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「分からないけれど、私にしてほしいことがあるんでしょう？」"

hide go_m_03_6
show go_m_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice gor_g0084
Gowland "「してほしい……、っていうか……。\n
してほしくねえっていうか……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブツブツとゴーランドは呟いている。\n
私には状況が読めない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（なんなのよ、はっきりしてよ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "夢のこともあり、これ以上もやもやするのは御免だ。\n
……それほど、言いよどむようなことなのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（でも、無理難題だったとしても、まともな用事よね？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ある種の信用はあるのだ。\n
彼の言う通り、教職という立場もある。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「いいわよ。\n
するもしないも、あなたの言うとおりにするわ」"

hide go_m_02_2
show go_m_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice gor_g0085
Gowland "「……っ！\n
だから、そう簡単にだな……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「……頼みたいのか、頼みたくないのかどっちなのよ。\n
用事があるのなら、はっきりしてちょうだい」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はゴーランドを信用している。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だからこそ、お願いの内容を知らずとも、それが酷いことではないと思えるのだ。\n
彼の頼みならば、私に出来る範囲で叶えたいと思う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドのほうにも、私を信用してほしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「……あ、でも。\n
{size=+20}あなたのリサイタルに参加しろっていうのは勘弁してね{/size}」"

hide go_m_03_1
show go_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_4")
voice gor_g0086
Gowland "「安心しろ、リサイタルじゃな……、って、なんだよ、それ。\n
リサイタル参加なら簡単だろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_9")
T "「いやいや、それ以上にないくらいに困難よ。\n
……で？リサイタルでないのなら、何？」"

hide go_m_01_6
show go_m_01_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_9")
voice gor_g0087
Gowland "「あー……。\n
今夜、夕食が終わったら、いつもの部屋に来てくれるか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "リサイタルでないにしても、音楽関係か。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_1")
T "「行けばいいのね？\n
もっととんでもないことを頼まれるのかと思ったけど、とりあえずは安全そうね」"

hide go_m_01_7
show go_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_1")
voice gor_g0088
Gowland "「危険はないっつったろ。\n
いや……、結構とんでもないこと、なんだけどなあ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「え？」"

hide go_m_03_2
show go_m_02_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice gor_g0089
Gowland "「……詳しくはそのときにな。\n
じゃあ、俺はちょっと授業の片付けがあるから、あんたは先帰ってろ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「ええ、分かったわ。\n
お仕事、頑張ってね」"

hide go_m_02_13
show go_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice gor_g0090
Gowland "「おう」"

hide go_m_03_4

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そういって、ゴーランドと別れる。"


play music corridor_day_p_wam

scene bg27_rk_day with stripe_l_medlong
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうも、生徒と教師の会話ではない。\n
特別な感じの別れ方に、なってしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……夕食の後に、いつもの部屋）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのとき、頼みごとをされるのだろう。\n
だが、どうせなら今言ってくれればいいものを。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（焦らされると気になっちゃうじゃない……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "夕食の時間以降は寮からの外出は禁じられているが、音楽室は寮の男女共同区域にある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "寮内での門限はもっと遅い。\n
ゴーランドの態度や、その頼みごとの内容を不審に思いつつも、今はおとなしく寮に戻ることにした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうせ、夜には分かることだ。"

with dis
$ hi_mes()

scene bg27_rk_day with Dissolve(.8)

scene bg10_sb_day
with stripe_l_medium

scene bg_map_day
with stripe_l_medium

scene bg_map_eve with Dissolve(1.2)
##endmemory
jump gakuen_gowland4
