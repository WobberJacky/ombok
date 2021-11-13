jump fushigi_common2_tower
label fushigi_boris2_2:

scene charasel_bg_tower_day
with stripe_l_medium

scene cn_01
with stripe_l_long

play music tower_corridor_p_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_10")
T "「はあ……、どうしようかな」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "クローバーの塔に居候させてもらって、数時間帯。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "脱走を図るナイトメアの確保を手伝うことはあるものの、正規の職員ではない私を、彼らは客として扱ってくれている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（ただ飯食らいなんだから、扱き使ってくれてもいいのになあ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "遊園地ではテンションの高い従業員に混じって仕事をしている身の上としては、手持ち無沙汰なこの状況に思わず溜息が漏れた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（贅沢な悩みなんだろうけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "既に衣食住を甘えている身、この上部外者である私に暇潰しに何か用を与えてくれと言えるはずもない。"


show punk_c_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0033
Man "「あれ、こんなところでどうしたんですか？」"

hide punk_c_12
show punk_c_12 at left
show punk_d1_16 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice oto_f0026
Man "「あなたは確か遊園地にいると思っていたんですが……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「ん？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "声をかけてきたのは、二人組の男。\n
私も何度か顔を見掛けたことがある。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "クローバーの塔の近くにある、飲料を扱っているお店の職員だ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「あら、久しぶり。\n
今は……、そのちょっと事情があって、ここに滞在させてもらっているんだけど」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「あなた達は仕事で来たの？」"

hide punk_c_12
show punk_c_14 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice hos_f0034
Man "「ええ、頼まれていた品を納めに来たんです。\n
……と、こんなにのんびりしていたら、まずいな」"

hide punk_d1_16
show punk_d1_14 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice oto_f0027
Man "「ああ、まだ他にも回るところがあるからな。\n
この時間帯の間に、城にも行かないと終わりそうにない」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（何だか忙しそうね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつもならちょっとした顔見知りの彼らに口を出すことはしないが、今はとにかく暇だった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何か出来ることがあるのなら、近くの店なのだし、手伝ってあげてもいいだろう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「……手が足りないのなら、手伝いに行きましょうか？」"

hide punk_c_14
show punk_c_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice hos_f0035
Man "「え？\n
本当ですか、いやでもあなたは夢魔の……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_1")
T "「言ったでしょう、私はただの居候なの。\n
何か手伝えることがあるのなら、手伝わせてくれない？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "暇を持て余しているよりはいい。\n
そう告げると、彼らは目配せをしあってから、笑顔を向けてきた。"

hide punk_d1_14
show punk_d1_16 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Man "「…………」"

hide punk_d1_16
show punk_d1_14 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice oto_f0028
Man "「そうですか、それは助かります。\n
では……、次の夜の時間帯、店で待っていますから」"

hide punk_c_1
show punk_c_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0036
Man "「正直助かります。\n
最近、本当に人手不足で……」"

hide punk_d1_14
show punk_d1_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice oto_f0029
Man "「……おい、行くぞ。\n
では、待っていますから」"

play sound se_0773
play sound se_0774
hide punk_c_4

hide punk_d1_11

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう言って彼らは簡単な地図をメモに書いて渡してくれる。\n
そのまま早足に去っていった。"



$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（最後、急にばたばたしていたけど……。\n
余程仕事が立て込んでいたのかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だとすれば、呼び止めてしまってかえって悪いことをしてしまったかもしれない。\n
手伝いに行くと決めた以上、しっかりとしなければ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「ええと、場所は……。\n
やっぱり、いつものお店ね」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（この距離なら、時間帯が変わってすぐ行けば、いいかな）"


show gre_t_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_1")
voice gra_f0073
Gray "「[firstname]、どうかしたのか？\n
今の連中は、確か街の人間だと思ったが……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "入れ違いに、廊下でグレイと遭遇して、そう聞かれた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「グレイ。\n
ううん、何でもないの」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_15")
T "「ちょっと知り合いに会っただけよ」"

hide gre_t_01_12
show gre_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_15")
voice gra_f0074
Gray "「知り合い？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（グレイに知られたら、逆に気を遣わせちゃうものね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "居候にすぎない私を何かと気遣ってくれるのは、彼も同じだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今だって書類を手にして移動中だったはずだが、私の姿を見かけたから声をかけてくれたのだろう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「次の時間帯、ちょっと出掛けてくるわ。\n
あ、それとも、何か私で手伝えることがあったかしら」"

hide gre_t_03_9
show gre_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice gra_f0075
Gray "「いや、そういうわけではないが……。\n
出掛けるのなら、あまり遅くならないように気を付けなさい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（本当に、この人って過保護なんだから）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんなに子供じゃないのよ。\n
そう言ってしまうことは簡単だが、グレイから見たら、私なんてまだまだ子供の範疇だろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（これ以上、心配をかけないようにしなくちゃ）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_1")
T "「うん、ありがとう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "地図をポケットにしまって、私も離れていった。"

hide gre_t_01_11

$ hi_mes()

scene cn_01 with Dissolve(.8)

scene charasel_bg_tower_day
with stripe_l_medium

scene map_bg_winter_day
with stripe_l_medium

scene map_bg_winter_night with Dissolve(1)

scene mm3_win_03
with stripe_l_medium

play music tension_a_ali

scene bg_gen26_ur
with stripe_l_long
play sound se_0535
camera at hpunch
camera at vpunch
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どんという音と共に背中が冷たい壁に押しつけられる。\n
上がりかけた悲鳴は乗せられた手のひらによって潰された。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「っ！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_7")
T "（まずい）"


show punk_c_17 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
voice hos_f0037
Man "「本当に来たぜ。\n
馬鹿じゃねえのか、この女」"

hide punk_c_17
show punk_c_17 at left
show punk_d1_17 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
voice oto_f0030
Man "「いいじゃねえか。\n
役持ちと仲良くしているから、どうせ大したことないとでも思ったんだろうよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "唐突な展開に、私の頭がついていかない。\n
約束の時間帯になって店に入ろうとしたら、裏口から回るよう指示された。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（従業員の入り口だからって、油断していた……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "入り口に鍵がかかっていた時点で、気付くべきだった。\n
何の警戒もせずにいた自分を悔やむ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "薄暗い裏路地では、ひとけもない。\n
一人は私の肩を押さえ込み、もう一人に口を塞がれていては、助けを呼ぶことも出来なかった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "警戒心が薄すぎた。\n
思い上がっていたと言われても仕方ない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界の住人に好かれるのが前提の余所者としての立場に、甘えていた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_8")
T "（逃げなきゃ……！）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「……ん、ふ！」"

play sound se_0007
hide punk_c_17
show punk_c_8 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice hos_f0038
Man "「じたばたするなよ、大人しくしていればそんなに手荒なことも……。\n
……いってえ、足、動かすなよ！」"

hide punk_d1_17
show punk_d1_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice oto_f0031
Man "「足癖の悪い女だな。\n
これで、本当に買い手がつくのかよ？」"

hide punk_c_8
show punk_c_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice hos_f0039
Man "「あんな化け物みたいな役持ちに気に入られているんだぜ。\n
それだけでも……っ、いて！」"

play sound se_0055
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それでも抵抗を諦めるような私ではないので、思いっきり相手の足を踏みつける。\n
拘束から逃れることが出来れば、近くには塔があるのだ。"

hide punk_d1_1
show punk_d1_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice oto_f0032
Man "「この……、ふざけやがって」"

play sound se_0124
$ flash(.1)
camera at hpunch
camera at vpunch
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_6")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（いったあ……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "叩かれた頬がじんじんと痛む。\n
銃弾なんかよりもより明確な痛みの感覚に、頭の奧が痺れた。"

hide punk_c_10
show punk_c_7 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0040
Man "「そんなに痛い目に遭いたいなら、望み通りにしてやろうか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「……！！」"

hide punk_c_7

hide punk_d1_8

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ずるずると引き摺られて、身体が地面に沈み込んでいく。\n
薄暗い路地で、顔の見えにくい男達の口元だけが、三日月のように浮かんでいる。"

play sound se_0007
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_15")
T "（嫌……、こんなの、嫌っ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "怖い、気持ち悪い。\n
ばたばたと最後の悪あがきのように足をばたつかせたが、それも難なく抑え込まれてしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_9")
T "（嫌っ！！）"

play sound se_0007
play sound se_0104
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "服が破けて、心もとなくなっていく。\n
助けを呼ぶことも、逃げ出すことも出来ない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_3")
T "（弱いことは分かっていたのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "銃も使えない。\n
刃物だって扱えない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界でも無力な女にすぎない私に、彼らから逃れる術なんて……、あるはずがない。"


show punk_d1_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice oto_f0033
Man "「おい、傷物にすれば値段が下がるぜ」"

hide punk_d1_9
show punk_d1_9 at left
show punk_c_17 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0041
Man "「じゃじゃ馬のまま渡すほうが不親切だろう？\n
サービスの一環だ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_4")
T "「！！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "顔が近付いてきた。\n
男の薄笑いは私にとって絶望以外の何ものでもなかった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_10")
T "（誰か……！）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "幾つもの知り合いの顔が浮かんで消えて、最後に残ったのは遊園地を出る直前に見た、彼の顔。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_9")
T "（……ボリス！）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "口を塞がれて出ない声の代わりに、胸の内で最後の頼みのようにその名を呼びながら。"



$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "反射的に目を閉じて。"

pause .6
play sound se_0440
hide punk_c_17

hide punk_d1_9

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「…………？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_12")
T "（……今の音は、何？）"

hide black with open
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "目を見開いて、私はそこでようやく状況を理解した。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私を押さえ込んでいた男が地面に転がりながら、何かを叫んでいる。\n
もう一人の男も怯えたように私の隣を見ていた。"

play sound se_0553

play music opposition1_a_ali

show punk_c_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hos_f0042
Man "「ぎゃああっ、いてえ！！\n
やめて……、ぎゃっ」"

play sound se_0439
pause .5
play sound se_0564
$ flash_red(.1)
hide punk_c_5

hide splatter with Dissolve(1.5)

show punk_d1_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice oto_f0034
Man "「あ、ああ……、な、なんで、おまえが」"


show gre_t_01_2 at center
hide punk_d1_3
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0076
Gray "「……[firstname]、すまない、遅くなった」"

show t_cut_bor2_1u onlayer master
with dis
hide gre_t_01_2

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "薄暗い路地裏に立つ、黒い影。\n
街灯の明かりを弾く、硬質なナイフの輝きが夜の闇に浮いている。"

hide t_cut_bor2_1u
show t_cut_bor2_1 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「グレイ！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_7")
T "（どうして、ここに？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼のナイフは赤く染まっている。\n
そして、私の上に覆い被さろうとしていた男からも、同じように濃厚な鉄の香りが漂っていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それらの状況から考えられることは、ただ一つなのに、凍りついた思考はなかなか動き出せない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gray "「…………」"

play sound se_0063
hide t_cut_bor2_1
show black onlayer master with Dissolve(.7)
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「グレイ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（これじゃ、何も見えない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "傍にやってきたグレイに、頭からコートをかけられる。\n
外そうとすると、やんわりと止められた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "男達と私の間に立って、こちらに背を向けていることは、気配で察することが出来る。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0077
Gray "「すぐに片付く、少しの間そうしていてくれ。\n
今の俺は、自制が利きそうもないからな」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0078
Gray "「ここから先は、君は見ないほうがいい。\n
俺はナイトメア様と違って、悪い夢を見たとしても追い払ってやれない」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Man "「！！」"

play sound se_0454
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice oto_f0035
Man "「ト、トカゲ……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（グレイが怒っている）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "見えない視界でも、簡単に想像が付く。\n
きっと、今の彼は冷たい金の目で、男達を見下ろしている。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0079
Gray "「ここで殺しはしない。\n
安易に殺してやれないほど、今の俺は気が立っているんだ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0080
Gray "「てめえらのしでかしたことの大きさを、苦痛と絶望で理解させてやるよ」"

$ hi_mes()

scene map_bg_winter_night
with dis
play sound se_0675
pause .4
play sound se_0605
pause .20
hide black with Dissolve(.7)


scene mm3_win_03
with stripe_l_medium

scene bg_gen01_gb
with stripe_l_long

play music forest_town_pub_p_ali
play sound se_0561 volume .6
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_11")
T "「…………」"


show gre_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_11")
voice gra_f0081
Gray "「少し落ち着いたか、[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「うん、大丈夫。\n
ありがとう、グレイ」"

hide gre_t_03_3
show gre_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice gra_f0082
Gray "「そうか……。\n
なら、よかった」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "賑やかな雑踏を横目に、私達は小さなバーにいた。\n
時間帯も夜から昼に変わり、すっかり街の様子も変わっている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あの後、彼らがどうなったのか、私は見ていない。\n
グレイの上着にくるまれて、解放されたときには、もう現場からは離れていた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「でも、どうしてグレイが……。\n
見回りの最中だったの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "気になって聞いてみると、グレイは苦笑を零した。"

hide gre_t_01_11
show gre_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0083
Gray "「いや……、ナイトメア様にどうにも気になるから君のところに行けと言われて。\n
もっと早くに駆け付けるべきだった、すまない」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（グレイは何も悪くないのに……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "悪かったのは、迂闊な行動に出た私だ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「謝らなくていいのに」"

hide gre_t_01_10
show gre_t_03_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_16")
voice gra_f0084
Gray "「そういうわけにはいかない。\n
別に、管理者側の人間として言っているわけじゃないんだ」"

hide gre_t_03_8
show gre_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_16")
voice gra_f0085
Gray "「大切な友人の危機に駆け付けられないなんて……、情けない」"

play sound se_0666
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "苦く笑ったグレイは、握っていたグラスを傾けて、大きくあおった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼と違い、私の前に置かれているのは暖かいお茶だ。\n
カップに手を伸ばしてそっと指先で包み込む。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T "（温かい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "冷え切った指先と心があたたかくなっていく。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それでようやくかたかたと震えていた手は、少し落ち着いてくれた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_20")
T "「……上着、もう少し借りていてもいい？」"

hide gre_t_02_11
show gre_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_20")
voice gra_f0086
Gray "「ああ、どうぞ」"

hide gre_t_03_9

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイとは逆に小さく一口含んで、ゆっくりと飲み込んでいく。\n
身体の中を通っていく温かな心地よさに、ようやく人心地ついたときだ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice chi_f0033
Cat "「……みゃお」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（猫？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "足下から動物の鳴き声が聞こえた気がして視線を落とせば、そこには一匹の猫がいた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice chi_f0034
Cat "「みゃあ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "猫は私の足下に擦り寄るように顔を押し付けてくる。\n
匂いを付けるように、すりすりと。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「…………？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_16")
T "「グレイ、ここって、動物が入ってもいいお店だったの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "飲食店の大半は動物禁止だ。\n
衛生上、動物の立ち入りを断る店も珍しくない。"


show gre_t_01_15 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gray "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「グレイ？」"

hide gre_t_01_15
show gre_t_01_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice gra_f0087
Gray "{size=+20}「可愛い」{/size} "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（こ、これは……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "猫を見つめるグレイの眼差しは、先ほどまでの冷たさが嘘のように甘くとろけている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（それとも、実は酔っているとか？\n
いやいや、酔っているにしてもこの顔はないでしょう、この顔は）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「グレイ……。\n
あ！」"

play sound se_0134

play music honobono2_a_ali

show t_bor2_1 onlayer master
with dis
hide gre_t_01_7

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice chi_f0035
Cat "「みゃあ……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「うわ……。\n
温かいのね、あなた」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_8")
T "（ふわふわ……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "膝に飛び乗ってきた猫を、ゆっくりと撫でてみた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "足下では薄暗くてよく見えなかったが、毛の色は派手なピンク色をしている。\n
縞模様が全身に広がっていて、顔のあたりの毛は少し長めに伸びていた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「ピンクの猫、か」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "蛍光ピンクをした猫なんて、ボリスぐらいだと思っていたが、例外は存在するらしい。"

menu:
    "ボリスによく似ている。":
        jump fushigi_boris2_3a
    "似ているけど、違う猫よね。":
        jump fushigi_boris2_3b

label fushigi_boris2_3a:
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（ペーターがウサギになるのはよく見るけど、ボリスが猫になったらこんな感じかしら？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "色合いもそうだが、特に顔を隠すように長く伸びた毛は、彼を連想させる。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0088
Gray "「可愛いな。\n
猫はいい……、癒される」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_2")
T "「そうね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一度似ていると思うと、特徴のすべてをボリスに繋げてしまう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "柔らかな毛並みも、ボリスがいつも身に付けているあのファーに近いのではないかとか。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "薄く開いた目の色も、彼に近いのではないかとか。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（ボリスのと同じぐらい、柔らかいんだもの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "確証は何もないし、気のせいだ。\n
ボリスが猫の姿になったのだったら、さすがに私とて気付く。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この猫は似ているだけ。\n
でも、同じような手触りにほっとする。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T "（ごめんね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "膝の上で寛いでいた猫を手で持ち上げた。\n
猫は大人しくされるがまま、大きな金色の目で私とグレイを見ている。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice chi_f0036
Cat "「みゃあ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「ねえ、グレイ。\n
この猫、ボリスに似ていないかしら？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice gra_f0089
Gray "「チェシャ猫に……？\n
さあ、どうだろう、猫の区別は俺にはつかないが」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイが確かめるようにじっと猫の顔を覗き込むと、猫はひらりと私の手の中から離れて、再び膝の上で丸くなった。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0090
Gray "「どうやら、君の膝の上が気に入ったらしいな」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "からかうような声を無視して、猫はもう一度「みゃお」と私のほうを見て鳴いた。"

jump fushigi_boris2_4
label fushigi_boris2_3b:
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（まさか、ボリスが猫になってくるはずがないわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ボリスはチェシャ猫だ。\n
普通の猫とは違う。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "常日頃から「あんなよわっちい猫と一緒にするな」とよく言っている彼である。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（ボリスが猫になったとしたら、さすがに分かるだろうし……。\n
それに、動物姿で出てくるのはペーターだけで十分よ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そっと丸くなった背中に触れる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "触れられることを嫌がる猫もいるから、いくら相手が機嫌よく丸くなっていたとしても気を付けなければいけない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "毛並みを確かめるように触れると、柔らかな感触が手のひらに広がった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_8")
T "「……気持ちいい」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（動物の毛並みって、どうしてこう触っていて気持ちがいいのかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "慎重に触れたあと手を離すと、まるで咎めるように猫が私のほうを向く。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice chi_f0037
Cat "「にゃあ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_14")
T "「…………？」"

jump fushigi_boris2_4
label fushigi_boris2_4:
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_10")
T "（撫でてほしいのかな）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そっと手で撫でてやると、気持ちよさそうに眼を細めてくれる。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice chi_f0038
Cat "「にゃあ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（そういえば、ボリスもやたらと撫でてほしがるときがあったわよね）"


scene yug_01
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私が他の領地から戻ったときは、特に撫でろと言われたものだ。"

$ hi_mes()
pause .8
hide t_bor2_1
show bg_gen01_gb_s onlayer master
with dis
hide bg_gen01_gb_s
show yug_01_s onlayer master
with dis

play music amuse_guestroom_p_ali
hide yug_01_s


show bor_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice bor_f0218
Boris "「[firstname]……、遅いよ。\n
今度はどこに行っていたんだよ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「どこにって……、ハートの城よ。\n
ビバルディに薔薇を見せてもらっていたの」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "遊園地にある自室に戻ったところ、ボリスが待っていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "始めの頃は勝手に部屋に入ってくる相手に怒っていたものの、気付けば当たり前になってしまっている。"

hide bor_t_02_8
show bor_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0219
Boris "「ハートの城か。\n
どうりで、薔薇の匂いがすると思った」"

play sound se_0551
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「！！？」"

hide bor_t_01_11
show bor_t_03_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
Boris "「すごい、薔薇の匂いだね……。\n
酔いそう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "椅子に座っていたボリスが、こちらに近寄って、首元に顔を近づける。\n
その位置で囁かれると、吐息が肌に触れた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_8")
T "（くすぐったいような、恥ずかしいような……。\n
だいたい、どうして帰ってくる早々、こんなにくっついて来るのよ！？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今回の外出は予めボリスにも言っておいたはずだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "特に約束をしていたわけではないが、城の薔薇を見ていたのも、一時間帯だけ。\n
遅いと言われるほど遊園地を離れてはいない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（何かあったのかしら？）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「城の薔薇は、他の場所に咲いているものとは全然違うのよ。\n
ボリスも、よかったら一緒に見に行く？」"

hide bor_t_03_13
show bor_t_03_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
Boris "「…………」"

hide bor_t_03_6
show bor_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice bor_f0221
Boris "「い、いいよ。\n
城なんて堅苦しくて、猫向きの環境じゃない」"

hide bor_t_01_2
show bor_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice bor_f0222
Boris "「その上、あの女王様に宰相さんに、騎士さんがいるんだろ？\n
すんごく、疲れそう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（確かに、両極端な反応を見せそうよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ボリスが僅かに逡巡して出した結論に、納得する。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ビバルディは猫好きだから、文字通り猫可愛がりするだろうし、ペーターは追い出しそうだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エースはエースで、余計な茶々を入れて、引っかき回すに違いない。"

hide bor_t_01_3
show bor_t_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0223
Boris "「そんなことよりもさ、[firstname]。\n
もっと近くに来てよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「近くにいるじゃない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "立ったまま、抱きしめられている。\n
今だって十分近い距離だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "部屋は静かで、互いの鼓動が聞こえてきそう。"

hide bor_t_02_1
show bor_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0224
Boris "「だめだよ、全然足りない。\n
あんたからも俺にくっついてよ」"

hide bor_t_01_10
show bor_t_03_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0225
Boris "「俺のこと、撫でて」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_1")
T "「ずいぶん素直に甘えてくるのね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ボリスが自分から甘えるなんて、珍しい。\n
私が出かけている間も、遊園地で働いている間も、彼はいつも勝手にふらふらと出かけている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "戻ってきて、近付いてくることはあるが、ここまではっきりと甘える姿勢を取ることはほとんどない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「何かあったの？」"

hide bor_t_03_4
show bor_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice bor_f0226
Boris "「なんにもないよ。\n
ただ、あんたに撫でてほしい気分なだけ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（本当かしら？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "甘える猫の理由は分からない。\n
彼の気持ちを察することも、私には難しい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（でも……、応えることくらいは出来るわ）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_13")
T "「はいはい、これでいい？」"

play sound se_0252
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ふさふさのファーと、同じ色をしている髪の毛。\n
柔らかなそれに手を伸ばして、優しくさすった。"

hide bor_t_01_13
show bor_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Boris "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「なんで、固まっているの？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_11")
T "（自分から撫でてって、言ったくせに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "髪の毛を引っ張ったわけでもないし、固まってしまう理由など思い当たらない。"

hide bor_t_01_2
show bor_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0227
Boris "「ねえ、[firstname]。\n
俺もあんたに触っていい？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「いいわよ、どうぞ」"

hide bor_t_03_10
show bor_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_13")
Boris "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "断る理由も見当たらないので、頷いた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "手が髪の毛に触れて、そっと撫でてくる。\n
そのまま背中へ、そして首筋に戻る。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T "（何だか、私まで猫になった気分）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "家で飼っていたダイナが他の猫とじゃれ合うのを見たことはあったが、まさか自分がそんな気分になるとは思わなかった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_8")
T "（温かい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "撫でられていると、気持ちが穏やかになっていく。\n
包まれるような感覚に、声が零れた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_8")
T "「気持ちいい」"

hide bor_t_01_13
show bor_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_8")
Boris "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "相手の沈黙が気になって、ちらりと視線を向ける。\n
ボリスは仕方ないなという表情を浮かべていた。"

hide bor_t_02_10
show bor_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0228
Boris "「あんたさ……、出かけるなとは言わないけど、もう少し警戒心持ったほうがいいって」"

hide bor_t_01_3
show bor_t_03_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0228_5
Boris "「そんな無防備な姿見せていたら、襲われちゃうぜ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先ほどまでは驚いた顔をしていたはずのボリスの口元には、鋭い歯が見える。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（……猫なのに、狼みたいな顔）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「ボリスなら、襲っちゃう？」"

hide bor_t_03_8
show bor_t_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice bor_f0229
Boris "「勿論。\n
襲うなって言われても、我慢なんかしないよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "悪戯っぽく目を細めながらも、私を撫でる手に、いやらしさは感じない。\n
確かめるような、触るだけの手。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（……気持ちいいな）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "もっと深くて甘い、溶けるような感覚だって知っている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、この感覚はまた別のものだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_8")
T "（こうして、ただ撫でられているのも、私は好き）"

hide bor_t_02_2

$ hi_mes()

scene yug_01_s
with dis

scene bg_gen01_gb_s
with dis

scene bg_gen01_gb
with dis

play music forest_town_pub_p_ali

show gre_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
Gray "「[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「……あ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_7")
T "（私、ぼうっとしていたの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイの声に我に返ったときに動いたせいだろう、膝の上にいた猫もまた動き出す。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「ご、ごめんね。\n
まだ乗っていたいのなら、乗っていてもいいんだけど」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（って、猫を相手に何を真面目に話しているんだろう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ピンク色の猫。\n
ただそれだけで、つい彼を連想してしまう。"

hide gre_t_03_10


show t_bor2_2and2_4 onlayer master
with dis
hide t_bor2_2and2_4
show t_bor2_3 onlayer master with Dissolve(1.5)
show t_bor2_2and2_4 onlayer master with Dissolve(1.5)
hide t_bor2_3
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（本当にボリスだったら、私の上になんて乗せられないけど）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T "（でも、ボリスといるような気分になるなんて……。\n
不思議な猫）"

hide t_bor2_2and2_4 with Dissolve(1.5)

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_9")
voice chi_f0039
Cat "「……にゃあ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「ん？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一度は私の膝から降りた猫は、ぴょんっと軽やかに同じ位置に戻る。\n
見つめてくるガラスのような目に、顔を近付けてみると、鼻先を舐められた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_8")
T "（くすぐったい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "じゃれる仕草に、猫は私の頬を舐めようとする。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「あ、ごめんね。\n
そこは腫れているから……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "男達に叩かれた腫れが残る頬に触れようとした猫に声をかけると、私の言葉が分かったように動きを止めた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice chi_f0040
Cat "「みゃあ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "分かったと応えるようなタイミングで、鳴いてくれる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（賢い子だなあ）"


show gre_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_15")
voice gra_f0091
Gray "「俺も抱いてみてもいいだろうか？\n
おいで」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "我慢できなくなったのだろう。\n
グレイが横から手を伸ばしてくる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（グレイの手は大きいから、抱くのに不自由しなさそうよね）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「ええ、どうぞ……。\n
え？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice chi_f0041
Cat "「ふぅぅぅっ！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「あ……、どこに行くの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイの手から逃れるように床に下りた猫は、そのままそそくさと店の入り口に向かい、半開きになっていた扉から外へと出てしまった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（先刻まであんなにいい子だったのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あっというまの出来事に、私達は呆気にとられる。"

hide gre_t_01_4
show gre_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gray "「…………」"

hide gre_t_03_3
show gre_t_01_14 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0092
Gray "「嫌われてしまったようだな。\n
俺はどうにも可愛い生き物に嫌われる性質らしい」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（お、落ち込んでいる）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "可愛い物好きなグレイにとって、結構ダメージが大きかったようだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「そういう訳じゃないと思うけど……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_14")
T "（どちらかというと、触られそうになったから逃げたって感じだったような）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（私が触っているときは大人しかったのにな、あの子）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（トカゲが苦手な猫って、あまり聞かないけど……。\n
相性が悪かったのかしら？）"

hide gre_t_01_14

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "残ったのは、ふわふわの手触りと、膝の上の僅かな抜け毛だけ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（……どこの子なんだろう）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（また会ってみたいな）"

$ hi_mes()

scene bg_gen01_gb with Dissolve(.8)

scene charasel_bg_tower_day
with stripe_l_medium

scene map_bg_winter_day
with stripe_l_long
##endmemory
jump fushigi_common3_tower
