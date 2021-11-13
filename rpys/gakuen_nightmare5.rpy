label gakuen_nightmare5:
scene bg_map_day
with dis
$ clockanim()


scene bg_par15_rg_tow_nig
with dis

scene bg24_rj_day
with dis

play music morning_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "翌朝、妙にすっきりと目覚めることが出来た。\n
隣を確認する。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "さすがにそこにナイトメアの姿はなかった。\n
どうやら、私を寝かしつけた後に撤退してくれたらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "むくりと、ベッドの中で上身を起こして、伸びをする。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_1")
T "（んー……、いい朝……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "窓から差し込む朝日も柔らかで心地いい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「さすが、夢に関しては無敵とか言うだけのことはある……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すっかり熟睡してしまった。\n
疲れの類も取れたような気がする。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（夢も見なかったし……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_14")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_7")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そっと唇に指先で触れた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「～～～っ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あれは夢だったのか、それとも現実だったのか。\n
蕩けかけた五感の訴えなど、あんまりにも当てにならない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（夢……、かしら）"

menu:
    "夢だ。":
        jump gakuen_nightmare5_2a
    "現実だ。":
        jump gakuen_nightmare5_2b
label gakuen_nightmare5_2a:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（夢よ、夢）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（あれこそ、夢……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分に言い聞かせるように、心の中で呟いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、夢だとしても、だいぶ恥ずかしい。\n
まるで私がナイトメアにキスをしてほしいと、そう思っているみたいだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やはり、私は夢にみるほどに、彼のことが気になっているのだろうか。"

jump gakuen_nightmare5_3
label gakuen_nightmare5_2b:
$ lovechara_nightmare_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（あれは……、夢じゃなかった。\n
本物の感触だったわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアが私にキスをした、というのが事実だったとして、それが意味することにまた惑ってしまう。\n
彼は、私のことが好きなのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（好きでもないのにキスなんかしない……、わよね？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いや、幼子を寝かしつけるくらいの意味しかない可能性もある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、彼を多少なりとも意識している。\n
これはもう、認めざるをえない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、ナイトメアのほうが私を女性として意識しているかどうかは疑問だ。"

jump gakuen_nightmare5_3
label gakuen_nightmare5_3:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……はあ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "夢でも、そうでなかったとしても、そのどちらもが問題だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どちらにしろ、朝からあまり深くは考えたくない。\n
私は大きな深呼吸で気分を切り替えると、顔を洗って着替えることにした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、着替え始め……。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「……あら？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "リボンが見当たらない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "昨夜もいつもと同じように、風呂に行く前に外して、机の上に置いておいたはずだ。それなのに、机近辺を探してもみつからない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「風で飛んだ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちらりと窓を見るが、窓はしっかりと閉まっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "昨夜ドアのあたりでナイトメアと揉めて、どたばたしてしまったが……、たとえそれで飛んだとしても部屋の中にあるはずだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は床の上に屈みこみ、ベッドの下や机の下も覗きこんでみる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（……ない、わよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私のリボンはどこにもない。\n
そうなると、犯人として思い当たるのはナイトメアぐらいしかいない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_7")
T "（……あ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そういえば、昨日ストームの概要についてを教えてくれた男子生徒が言っていた。"


scene bg25_rr_nig_s
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0045_5
Seito "「ストームって、新入生男子の根性試し的側面のあるイベントなんです」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0045_8
Seito "「だから、自力で女子に説明しないといけないし、女子寮にも自力で辿り着かないといけないんです」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0040
Seito "「さらに、それらの任務を達成した証拠として、女子から何か私物を預かってくる必要もあるんです」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0040_5
Seito "「それが出来ないと、先輩達に認めてもらえないっていうか……」"


scene bg24_rj_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おそらく、それで、ナイトメアが持ち帰ってしまったのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「……一応、予備があるからいいんだけど」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（教師なんだから、戦利品なんて持っていく必要はないでしょうに……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "盗られたリボンは、盗られっぱなしになるのだろうか。\n
それとも、ストームの事後に返しに来てくれるのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その辺がよく分からない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（カフェテリアで、誰かに聞いてみよう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "引き出しから取り出した予備のリボンを結ぶと、部屋を後にした。"

with dis
$ hi_mes()

scene bg24_rj_day with Dissolve(.8)

scene bg_par15_rg_tow_day
with stripe_l_medium

scene bg25_rr_day
with stripe_l_long

play music corridor_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "カフェテリアへと向う途中の廊下、すれ違ったメイドへといつものように挨拶をしかけて、ふと思い出した。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（……ドア）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「あの、ちょっといいですか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "知り合いのメイドではなかったので、畏まってしまう。"


show maid_d_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0098
Maid "「はい、なんでしょう？\n
何か御用でしょうか」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「昨日の騒ぎで、部屋の扉のノブが壊れちゃったんです」"

hide maid_d_3
show maid_d_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice tad_g0099
Maid "「まあ、それは大変！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「一応、今は応急手当で使えるようになっているんですけど、いつまた外れちゃうか分からない状態で……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「悪いんですが、見てもらってもいいですか？」"

hide maid_d_4
show maid_d_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice tad_g0100
Maid "「はい、承りました。\n
授業から戻られるころには新品に変わっているかと」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「よかった！助かるわ！\n
ありがとう」"

hide maid_d_1
show maid_d_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice tad_g0101
Maid "「いえいえ。\n
昨夜のストームを楽しんでいただけたなら何よりです」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「びっくりしたけれど楽しかったです。\n
それじゃあ……、よろしくお願いします」"

hide maid_d_2

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "会釈をして、別れる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こうして塔内の平穏を守らなければいけないはずのメイドまでが、ストームの成否を聞いてくるあたり、本当に学校公認のイベントらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（さすが世界一の魔法学校……って言うべきなのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普通は公認されないような内容だ。"

with dis
$ hi_mes()

scene bg25_rr_day with Dissolve(.8)

scene bg_par02_ct_tow_day
with stripe_l_medium
jump gakuen_storm_gow_nig_gra_jok1
label gakuen_nightmare5_5:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（ナイトメアが来たって言ってもいいものなのかしら……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアというのは、シンフォニアの教職員の中でも気安いほうに入るだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなナイトメアが生徒と一緒に悪ふざけに混じったとしても、問題はないような気がする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう思う一方で、それを私が気にしてしまうのは、何かしら後ろ暗いと私自身が思っているから……、なのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（ナイトメアもストームに参加するのは初めてだと言っていたし……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "初めてのイベントなので、教職員がどこまで関わるかという範囲も定かではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（ああいうこと……、やたらとするわけじゃないわよね？\n
たとえば……、キスだとか？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "昨夜夢の淵、薄れかけた意識の中で触れた気がした感触を思い出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_7")
T "「～～……っ！！」"


show tower_a2_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_7")
voice hei_g0031
Seito "「……？\n
どうしたの？」"


show tower_b1_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_7")
voice chi_g0049
Seito "「……顔、赤いわよ？\n
[firstname]」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_8")
T "「……ええ。\n
分かっているから、触れないでいてくれると嬉しいわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はそっと彼女達から視線をそらし、頬に昇った熱を冷ますべくオレンジジュースを喉に流し込んだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "視線を戻した先、彼女達はいかにも興味津々といった風に私を見つめている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一度、大きく深呼吸を挟んで空気を切り替える。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「……ところで。\n
ストームには戦利品があるじゃない？」"

hide tower_a2_1
show tower_a2_7 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice hei_g0032
Seito "「……こら、[firstname]、その話題転換はずるいと思うわよ。\n
ちゃんと、何があったのかを……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_1")
T "「頼りになる先輩なんだから、新入生の疑問に答えてくれるわよね？」"

hide tower_b1_5
show tower_b1_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_1")
voice chi_g0050
Seito "「……っく。\n
仕方ないわね」"

hide tower_b1_9
show tower_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_1")
voice chi_g0051
Seito "「そうね、ストームには戦利品がつきものよ。男の子達は、自分が本当に女子の部屋に辿り着いたことを証明するために、何か持って帰らないといけないのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「私も、昨夜それを盗られたんだけど……。\n
戦利品って盗られっぱなしになっちゃうの？」"

hide tower_a2_7
show tower_a2_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice hei_g0033
Seito "「え？\n
あなた、ブリーズのことは何も聞いていないの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（ブリーズ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "昨夜のナイトメアとのやりとりを思い出そうとしてみるものの、そんな単語は出てこなかった。\n
初耳だ。"

hide tower_b1_2
show tower_b2_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0052
Seito "「あらあら。\n
あなたから戦利品を盗っていった男の子は、大事な説明を忘れちゃったのね？」"

hide tower_a2_5
show tower_a2_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0034
Seito "「ストームから一週間後にね、今度はブリーズというイベントがあるのよ」"

hide tower_a2_2
show tower_a2_6 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0034_5
Seito "「ブリーズは、女子生徒が男子寮に忍びこんで、奪われたものを取り返すってイベントなの」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「……この学校って、意外とイベント好きよね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どの学校も、学生寮のお祭り騒ぎは珍しくない。\n
ただ、学校公認のものとしては、多いのではないだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニアは世界一の魔法学校という優等的なイメージが強いが、やたらとおおらかだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こうして実際シンフォニアの生徒になるまで、まさかこんなにも自由な学校だとは思っていなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（ブリーズ……、か）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（……仕返しってことね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "リボンを取り返しに、ナイトメアの部屋に押しかける。\n
それはなんだか、とても楽しそうに思えた。"

hide tower_a2_6
show tower_a1_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0035
Seito "「ほら、私達はあなたの疑問に答えたんだから。\n
次は、あなたの番だと思わない？」"

hide tower_b2_1
show tower_b2_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0053
Seito "「あなたの頬を赤らめるような、一体何があったの？\n
ほら、口を割りなさいって」"

play sound se_0260 volume .8
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……ん、あら、残念。\n
ベルが鳴っちゃったから私は行かなくっちゃ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「いろいろ教えてくれてありがとうね。\n
また、ブリーズについては聞かせてほしいわ」"

hide tower_a1_3
show tower_a1_7 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice hei_g0036
Seito "「あ、こら……」"

play sound se_0161
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちょうど響いた時刻を知らせるベルの音に助けられた。\n
いそいそと立ち上がって、カフェテリアから離脱した。"

hide tower_b2_2
show tower_b2_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0054
Seito "「また今度、話しなさいよ～？」"

hide tower_a1_7

hide tower_b2_3
##[chara2 PAY ATTENTION="false"]
with dis
$ hi_mes()

scene bg_par02_ct_tow_day with Dissolve(.8)

scene bg_par15_rg_tow_day with stripe_l_medium
scene bg06_sk_h_day with stripe_l_medium

scene bg06_sk_h_eve with Dissolve(1)

scene bg06_sk_h_nig with Dissolve(1)

scene bg06_sk_h_day with Dissolve(1)

scene bg_par15_rg_tow_day with stripe_l_medium

scene bg25_rr_day with stripe_l_long

play music corridor_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズも近くなったある日、私はナイトメアの医務室を訪ねていた。\n
ノックをしようとして、躊躇う。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0110
Nightmare "「う～……、うう～～～……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "中からは不気味な唸り声が聞こえた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……何をやっているのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "唸り声の主はおそらく……、というか間違いなく、ナイトメアだろう。\n
留守でないことは分かったが、入っていいものなのか。"

play sound se_0303
pause .20
##[rchara2 PAY ATTENTION="false"]
show gre_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0002
Gray "「ああ、何の用……、って君か。\n
どうしたんだ？何か困ったことでも？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ノックをすると、すぐに内側からグレイがドアを開けてくれた。"

hide gre_m_02_4


scene bg_par16_rs_tow_day
with dis

show nai_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0111
Nightmare "「[firstname]！！\n
なんという素晴らしいタイミングだ、ちょっと私を助けてくれ！！」"

hide nai_m_02_10
show nai_m_03_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0112
Nightmare "「グレイが私を苛めるんだ！\n
上司を苛めるそこの人でなしに、君からも何とか言ってやってくれ！！」"


play music drawingroom_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の姿を認識するなり、そう主張しだしたナイトメアの目の前には、こんもりと積まれた書類の山がある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつものように書類を溜めまくったらしいナイトメアは、グレイによって監禁、強制的に書類を片付けさせられていたようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「いつもながらお疲れ様、グレイ。\n
そんな忙しいところ、邪魔して悪いのだけど……」"

hide nai_m_03_8
show nai_m_03_8 at left
with dis

show gre_m_01_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice gra_g0003
Gray "「ああ、用事があるのだろう？\n
俺か？それともナイトメア先生にか？」"

menu:
    "グレイに用事がある。":
        jump gakuen_nightmare5_6a
    "ナイトメアに用事がある。":
        jump gakuen_nightmare5_6b
label gakuen_nightmare5_6a:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「グレイに用事があるの。\n
……って言いたいところなんだけど、残念なことにナイトメアなのよね」"

hide nai_m_03_8
show nai_m_02_6 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
voice nig_g0113
Nightmare "「残念ってなんだ！？\n
今、何か失礼な言葉を聞いたような気がしたぞ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアのあげる抗議の声は、聞こえないふりでスルーしておく。"

jump gakuen_nightmare5_7
label gakuen_nightmare5_6b:
$ lovechara_nightmare_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「ごめんなさい、グレイ。\n
仕事の邪魔をするつもりはなかったんだけど……、ナイトメアに用事があって来たの」"

hide nai_m_02_6
show nai_m_02_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice nig_g0114
Nightmare "「そうか！\n
私に用事か！いい！実にいいタイミングだぞ、[firstname]！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "仕事から逃げたいナイトメアは、私を理由にすることが出来ると顔を輝かせている。ちらりとそれを横目で見やって、グレイへと視線を戻した。"

jump gakuen_nightmare5_7
label gakuen_nightmare5_7:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「出直したほうがいいならそうするわ」"

hide nai_m_02_3
show nai_m_02_10 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_13")
Nightmare "「……！！」"

hide gre_m_01_3
show gre_m_01_13 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_13")
Gray "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイは少しだけ考える間を挟んだ。"

play sound se_0330
hide gre_m_01_13
show gre_m_03_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0004
Gray "「長く時間のかかりそうな用事なのか？\n
それなら、少しスケジュールを調整する必要も出てくるが……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "懐から取り出した手帳を開いて、グレイが眉間に皺を寄せる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "塔の管理責任者なのに、常に逃げ回るナイトメア。\n
彼を追いたて、仕事をさせるためには当然そのスケジュール管理も必要だろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（ナイトメアにはもったいないぐらい、有能な補佐よね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "責任者だと普段言い張ってやまないナイトメアだが、グレイがいなくなってしまったら、塔の運営はおそらく崩壊する。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「いいえ、そんなに長くはかからないわ。\n
ちょっと聞きたいことがあって来ただけなの」"

hide gre_m_03_9
show gre_m_02_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice gra_g0005
Gray "「……そうか。\n
なら、俺はお茶の用意をしてこよう」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「……ありがとう」"

play sound se_0774
hide nai_m_02_10

hide gre_m_02_2

pause .15
play sound se_0284
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイはすかさず気を利かせて、お茶の準備という名目で部屋から出て行ってくれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は本来、使用人を統括する立場にある。\n
そんな彼自身がわざわざ自分でカフェテリアまでいき、飲み物の準備をする必要はない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "空いているメイドを呼び、命じればいいだけなのだ。\n
だが、グレイはそうしなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "わざわざ自分でカフェテリアまで行ってくれるのは、私達への気遣いだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（本当、有能な人）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイが出て行くのを見送ってから、私はナイトメアへと改めて向き直った。"


play music high_nig_p_wam

show nai_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0115
Nightmare "「……あれからもう、悪い夢は見ていないか？\n
ちゃんと眠れているか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつもならぎゃあぎゃあと騒ぐ調子のナイトメアの声が、いつになく穏やかで優しい。\n
あの夜に見せた切り替えのようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのギャップに、どちらが本物のナイトメアなのかが分からなくなる。\n
おそらくはどちらもが、彼なのだろうけれど。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……知っているんでしょう？\n
うなされるような夢は、見ていないわ」"

hide nai_m_03_10
show nai_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice nig_g0116
Nightmare "「君は……やっぱり、あの夢には遠慮するんだな。\n
うなされるような夢なんて表現ではすまない、あれは悪夢だよ」"

hide nai_m_03_9
show nai_m_02_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice nig_g0117
Nightmare "「悪い夢は、今の自分をも喰いつぶす。\n
たかが夢でも、精神を喰うんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "夢使いだというナイトメアは、心を読めるだけでなく、私の夢の中まで見たのだろうか。\n
私の夢……、過去の記憶を。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あれは、自分でも見たくない、過去だ。\n
当然、他の誰にも見られたくない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼の能力がどこまでのものなのか、私は知らない。\n
だが、見られてしまったと考えると……。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「……悪いだけの夢でもないわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "出来ることならば見たくない夢だが……、それにもきっと意味はあったのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（警告みたいなもの）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "カフェテリアの男女と変わらない。\n
私も浮ついていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "馬鹿なことは繰り返すなと警告のつもりで、深層意識があんな夢を見せたのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私を浮つかせる、当のナイトメアが、悪い夢を追い払ってしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あの夢を見るから、あの苦しさと切なさを追体験するからこそ、私は浮ついた気持ちに無関心でいられたというのに。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（……あなたのせいよ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "心の中でぽつり呟いて、私はナイトメアの執務机までの距離を詰めた。"


play music flower_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「ねえ、ナイトメア。\n
私、あなたの私室の位置を知りたいの」"

hide nai_m_02_13
show nai_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice nig_g0118
Nightmare "「私の私室？\n
塔の最上階にある部屋が、私の部屋だが……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「最上階？\n
ずいぶんと高いところに住んでいるのね」"

hide nai_m_01_2
show nai_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_7")
voice nig_g0119
Nightmare "「私は偉いからな！\n
権力を持つものはそれに比例して、高いところに部屋を持つものだよ」"

hide nai_m_01_6
show nai_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_7")
voice nig_g0120
Nightmare "「眺めもいいし、虫も入ってこないし、いい部屋だ。\n
……{size=+20}徒歩では辿り着けないが{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「ぶ……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふき出してしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言う通り、体力が人並み以下であるナイトメアには、階段を延々と登って最上階の部屋までというのは無理そうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「……自力で自室に行けないの？」"

hide nai_m_02_4
show nai_m_02_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
voice nig_g0121
Nightmare "「意地で試すんだが……。\n
よく途中で行き倒れてグレイに回収されている」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「自室に辿り着けないぐらいなら、徒歩でたどり着ける範囲内に部屋を用意したらよかったじゃないの。\n
……一階とか二階とか」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（三階ぐらいからもう危ういと思うんだけど、どうなのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の疑惑に、ナイトメアはぷいっと視線をそらすことで応えた。\n
おそらくナイトメアが自力で辿り着ける限界は三階ぐらいなのだろう。"

hide nai_m_02_9
show nai_m_02_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0122
Nightmare "「そんな低い階に住む管理者なんて嫌だっ！！\n
私は一番偉いんだから、一番高い場所に住むのが当然だ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……辿り着けもしないくせに」"

hide nai_m_02_6
show nai_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice nig_g0123
Nightmare "「ふふふ、そのために私には空間移動魔法がある！\n
……で、君はどうして私の部屋の位置なんか知りたかったんだ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "きょとんとした様子で聞かれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（……ブリーズのこと知らないの？\n
そんなわけ、ないわよね？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアはシンフォニアに赴任してきたばかりというわけではないはずだ。\n
ストームを知っているならば、ブリーズだって知っていて当然。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「なんで……、って。\n
そりゃあ、ブリーズのためなんだけど」"

hide nai_m_03_4
show nai_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
Nightmare "{size=+20}「！！！！？」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「えっ？なに、その反応。\n
どうしたの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "隻眼を瞠り、呆然とナイトメアは私を見つめている。\n
聞くはずのない単語が私の口から出てきたというような顔だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何かまずかっただろうかと心配になってくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "教師から生徒へのストームはセーフでも、生徒から教師へのブリーズは禁止だとか、そういう特別なルールでもあるのだろうか。"

hide nai_m_03_3
show nai_m_03_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0124
Nightmare "「き、君……、ブリーズに参加するのか。\n
その、私を相手に？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「え、ええ、だってストームに私の部屋に来たのはあなただもの。\n
それに、あなたは私のリボンを持っているでしょう？」"

hide nai_m_03_7
show nai_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice nig_g0125
Nightmare "「あ、ああ。\n
君が眠ってしまった後に、戦利品として持ち帰らせてもらった」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「でしょう？\n
なら、やっぱり、取り返さなくっちゃ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ストームの夜に奪われたものは、ブリーズの夜に取り返すのが道理……、らしい。"

hide nai_m_02_10
show nai_m_01_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0126
Nightmare "「まさか君が……、そういう意味で私を対象にしてくれるとは思わなかったぞ……。私には君を悪夢から守るという建前があったが……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぶつぶつ。\n
小声でナイトメアが呟いているが、その内容を聞き取ることはできなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ただ、それでも彼が自分が私のブリーズの対象に選ばれたことに驚いていることだけは分かる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_10")
T "（……イラっとするわね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアという男は、どこか浮世離れした部分を持っている。\n
それが、彼の持つ特殊能力のせいなのだということも、だいたい見当はつく。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、それが今はもどかしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼自身を世界の傍観者としてしまうような、登場人物の背中をちょっと押すだけというような関わり方をする彼に腹が立つ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だから、だろうか。\n
ぽろりと口にしてしまっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……私にキスしたくせに」"

hide nai_m_01_5
show nai_m_01_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice nig_g0127
Nightmare "「……{size=+20}！！！？{/size}\n
き……っ、きききき、君、起きていたのか！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "{size=+20}「！！！！！！」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "半ば引っ掛けのつもりだったのに、ナイトメアはあっさりと引っ掛かった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これには、私のほうが驚いた。\n
あっさり引っ掛かった上に、こんな反応……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_8")
T "（～～～っっ！！！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私まで、顔が赤くなる。\n
耳まで熱が昇る。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……へ、変な沈黙）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「…………」"

hide nai_m_01_12
show nai_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
Nightmare "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "お互い、視線を合わせることも出来ずに黙り込んでしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_12")
T "「…………」"

hide nai_m_01_3
show nai_m_01_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_12")
Nightmare "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「…………」"

hide nai_m_01_5
show nai_m_01_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
Nightmare "「…………」"

hide nai_m_01_7

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "誰か……、誰でもいいから、この空気を何とかしてほしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（そうでないと……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "変な気分になる。\n
変なことを言いそうになってしまう。"

play sound se_0302
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0006
Gray "「すまない。\n
ドアを開けてくれないか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「い、今、開けるわ……！！」"

play sound se_0590
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ノックの音と一緒に聞こえたグレイの声は、まさしく救世主のようだった。\n
ぱたぱたと扉へと駆け寄ると、ドアを開けてグレイを招きいれる。"

play sound se_0397
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ノックが出来るということは、片手は自由、つまり本来ならば自分で部屋に入ってくることも可能なはずだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それをグレイがしなかったのは、私達に気分を切り替えるための時間を数秒与えるためだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_7")
T "（本当……、気の利いた……、出来すぎた補佐官ね）"


show gre_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_7")
Gray "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "気の利いた素晴らしい補佐である彼は、医務室内に漂うおかしな空気にもすぐ気付いただろうに知らないふりをしてくれる。"

hide gre_m_02_12
show gre_m_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0007
Gray "「君も、お茶に付き合ってくれるだろう？\n
ナイトメア先生、少し休憩にしましょう」"

hide gre_m_02_2
show gre_m_02_2 at left
with dis

show nai_m_02_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0128
Nightmare "「あ……っ、当たり前だ！\n
ここでおまえと彼女だけで休憩とかいったら私は暴れていたぞ！」"

play sound se_0528
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうにかまともに戻ったナイトメアは素早く机の上を片付けると、そこにグレイの手のしていた銀色の盆を置くスペースを作る。"

play sound se_0546
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちゃんとテーブルに向かって、それなりのマナーのもとで開かれるお茶会はいいものだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、こんなふうに一つの机を囲み、立ちっぱなしで談笑しながらのコーヒータイムもなかなかに悪くない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイとナイトメアの二人はコーヒーで、私はココアだ。\n
苦味と、甘さの混じった空気が柔らかに室内を彩る。"

hide nai_m_02_5

hide gre_m_02_2

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうして三人のコーヒー休憩を楽しんでから、私は医務室を辞去した。"


scene bg25_rr_day
with dis

play music evening_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（ブリーズ……、か）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "奪い取り、取り返す。\n
そのやりとりには、特別なものがある。"

with dis
$ hi_mes()

scene bg_par15_rg_tow_day
with stripe_l_medium

scene bg_map_day
with stripe_l_long
##endmemory
jump gakuen_nightmare6
