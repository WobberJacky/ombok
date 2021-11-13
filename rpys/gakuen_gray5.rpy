label gakuen_gray5:
scene bg_map_day
with dis
$ clockanim()


scene bg_par15_rg_tow_day
with dis

play music morning_a_wam

scene bg24_rj_day with Dissolve(1.2)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "気持ちがふわふわと落ち着かなくて、いつもよりも早い時間に目が覚めた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……夢、じゃないわよね？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "昨夜何があったのかを思い出して、まず確認したくなるのがそこだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイがストームに便乗して私の部屋へとやってきて……、好きだといってキスをした。\n
私も、彼に好きだと伝えた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_7")
T "「～～……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "寝起きだというのに、また頭が沸騰しそうになる。\n
そう、「また」だ、昨日のように。"

play sound se_0328
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "邪念（？）を追い払うように頭を揺らして、起き上がった。\n
カーテンの隙間からは気持ちのいい朝日が差し込んできている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はベッドを抜け出すと、洗面所に向かった。\n
顔を洗ってすっきりとして、それから制服に着替え出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（……あ、やっぱり夢じゃない）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつもなら、私はリボンを机の上に置いておく。\n
そのリボンが、なくなっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "昨夜、グレイがストームの戦利品といって持ち帰ったのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "誰も、彼を相手にストームの成否を聞いたりはしないと思うのだが……、気分の問題だろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "引き出しから予備のリボンを取り出して、頭に留めた。\n
これで、準備は万端だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最後、部屋を出る前に、姿見の前で身嗜みを確認してから部屋を出た。"

with dis
$ hi_mes()

scene bg24_rj_day with Dissolve(.8)

scene bg25_rr_day
with stripe_l_medium

scene bg_par02_ct_tow_day
with stripe_l_long
jump gakuen_storm_gow_nig_gra_jok1
label gakuen_gray5_2:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（まさか、グレイが来たとも言えないし……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「そうねえ、……。\n
ただただ驚いたとしか……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "わざとらしくげんなりとした声を作れば、二人は嬉しそうに視線を交し合う。"


show tower_a1_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0061
Seito "「ふふ。\n
新入生なら、皆通る道だわ」"


show tower_b2_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0084
Seito "「私達だって、入学したてのとき、どんなに驚かされたことか。\n
ああ、でもあなたは特別に大変だったらしいじゃない？」"

hide tower_a1_3
show tower_a1_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0062
Seito "「ああ、そうそう、エース先輩の暴走に巻き込まれたって聞いたわ。\n
せっかくのストームなのに、グレイ執務長に事情聴取されちゃったんでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……え？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……事情聴取？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなものをされた覚えはない。"

hide tower_a1_1
show tower_a1_9 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0063
Seito "「あら？\n
違うの？」"

hide tower_b2_4
show tower_b2_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0085
Seito "「グレイ執務長が事情を伺うことになって、あなたのストームは潰れちゃったって聞いていたんだけれど」"

hide tower_a1_9
show tower_a2_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0064
Seito "「私の知り合いがあなたの部屋の近くだったらしくてね。\n
心配していたわ」"

hide tower_a2_1
show tower_a2_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0065
Seito "「驚きもあるとはいえイベントごとだし、潰れちゃったのは災難だったわね」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（……ああ、なるほど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "昨夜、エースがターゲットを探していた際に素早く逃げた女子生徒達。\n
その中に、彼女の友人がいたのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "窓から顔こそ引っ込めたとしても、きっとその後も外の様子を窺っていたに違いない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイはそれも予想して、情報を流したはず。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「ああ、そうそう、そうなの。\n
災難だったわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_6")
T "「でも、潰れたってほどじゃ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "せっかくグレイが予防線を引いてくれたというのに、つい余計なことを言ってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私にとって、昨夜のイベントは失敗などではなかった。"

hide tower_a2_5
show tower_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0066
Seito "「それじゃあ、あなたちゃんとストームは出来たの？\n
ちゃんと誰かに戦利品は渡せた？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_1")
T "「ええ、もちろん」"

hide tower_b2_5
show tower_b2_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_1")
voice chi_g0086
Seito "「それはよかったわ！\n
これでブリーズにも参加できそうね！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_16")
T "「ブリーズ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "また聞き覚えのない単語が出てきた。\n
会話の合間の朝食を進めながらも、私は首を傾げる。"

hide tower_a2_3
show tower_a2_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0033
Seito "「え？\n
あなた、ブリーズのことは何も聞いていないの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（ブリーズ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "昨夜のグレイとのやりとりを思い出そうとしてみるものの、そんな単語は出てこなかった。\n
初耳だ。"

hide tower_b2_2
show tower_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0052
Seito "「あらあら。\n
あなたから戦利品を取っていった男の子は、大事な説明を忘れちゃったのね？」"

hide tower_a2_4
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
$ face("ali_m_06_5")
T "（ブリーズ、か。\n
でも……、グレイは参加できるのかしら）"

hide tower_a2_6

hide tower_b1_3

with dis
$ hi_mes()

scene bg_par02_ct_tow_day with Dissolve(.8)

scene bg_par15_rg_tow_day
with stripe_l_medium

scene bg_par16_rs_tow_eve with Dissolve(1.2)

play music flower_eve_p_wam

show gre_m_02_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
voice gra_g0167
Gray "「……ブリーズ、か」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "朝方ふと思った疑問の答えは、放課後の医務室で休憩している折のグレイの苦い顔からすぐに分かった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（やっぱり、参加できないのね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "男子側が女子寮に攻め込むストームの場合、彼は外を見回るついでに私の部屋へこっそり立ち寄ることぐらいは出来ただろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、ブリーズの場合、その立場が逆転する。\n
彼は部屋で待ち構えなければいけないのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "外の見回りと、待機。\n
両立は難しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「いいの、ごめんなさい。\n
半分分かっていて聞いたから、気にしないで？」"

hide gre_m_02_7
show gre_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice gra_g0168
Gray "「だが……。\n
君だって、学校行事には参加したいはずだろう？」"

hide gre_m_03_3
show gre_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice gra_g0169
Gray "「俺の都合で、君まで参加できないなんて……。\n
……いや、駄目だな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「グレイ？」"

hide gre_m_02_12
show gre_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice gra_g0170
Gray "「だったら他の誰かと楽しんでくれ……、なんていうふうには言えそうにない。\n
狭量な男だと思うかもしれないが……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「そこは、他の人と……、なんて言われていたほうがショックでしょう。\n
別にいいわ、参加しなければ困るようなイベントじゃないんだし」"

hide gre_m_02_10
show gre_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice gra_g0171
Gray "「そうか？\n
君は物分りがよすぎるんじゃないか、[firstname]」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイは、コーヒーカップを持つのとは逆の手を伸ばして私の頭を撫でる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "聞き分けのいい子供へとしてみせるような仕草だが、それは充分私にとってもご褒美としての価値がある。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_9")
T "「そんなこと……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "お互いに視線を重ねて微笑みあい……。"


play music gag1_a_wam

show nai_m_02_10 at center
with dis
hide gre_m_03_3

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0288
Nightmare "{size=+20}「なんなんだ、この会話は」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "間に挟まれていたナイトメアが、ようやく耐えかねたというように口を開いた。"

hide nai_m_02_10
show nai_m_01_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0289
Nightmare "「うう……。まったく、なんなんだ？\n
血ではなく、砂を吐きそうだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私としてはもっと早くツッコミが入るかと思っていたのだが、一応最後まで聞いてくれたらしい。\n
律儀だ。"

hide nai_m_01_12
show nai_m_01_12 at left
with dis

show gre_m_02_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0172
Gray "「何って……。\n
恋人同士の甘やかな会話ですが」"

hide nai_m_01_12
show nai_m_03_3 at left
with dis
play sound se_0761 volume .7
##special anime"kaminari"loop="false"with Dissolve(1)
pause .20

hide nai_m_03_3
show nai_m_03_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0290
Nightmare "「はあ！？こ、こここ、恋人同士！？\n
私は聞いていないぞそんなことっ！！」"

hide gre_m_02_9
show gre_m_03_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0173
Gray "「今、言いました」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「ええ、今、報告したわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私とグレイは視線を重ね……。"

hide nai_m_03_5
show nai_m_02_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0291
Nightmare "「だーかーらー！\n
いつの間にそんなことになったんだ、おまえ達は！？」"

hide nai_m_02_5
show nai_m_03_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0292
Nightmare "「ずるいぞ！？\n
私の知らないところで、いつのまに……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「ずるい、って……。\n
許可が必要なことでもないでしょう」"

hide gre_m_03_9
show gre_m_02_12 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice gra_g0174
Gray "「……ごほん。\n
いえ、一応、上司であるあなたに報告しておきます」"

hide gre_m_02_12
show gre_m_03_10 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice gra_g0175
Gray "「昨夜のストームで、俺のほうから彼女に告白し、めでたく恋人同士になりました」"

hide gre_m_03_10
show gre_m_03_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice gra_g0175_5
Gray "「そこのところをよく理解して、俺のためにさっさと仕事を進めてくださいね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_7")
T "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私のほうが、言葉に詰まる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "先ほどのように、半ばナイトメアをからかってやろうというノリで言う分には恥ずかしくなかったが、こうしてはっきり断言されてしまうと気恥ずかしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_8")
T "（ああ……、私達って、お付き合いしているんだなあ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "未だ現実味がないが、言葉に出されるとじわじわとくるものがある。"

hide nai_m_03_2
show nai_m_02_9 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0293
Nightmare "「……グレイ。\n
おまえそれ、私を脅しているだろう！？」"

hide gre_m_03_4
show gre_m_01_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0176
Gray "「そんな……。俺はただ、ナイトメア先生が仕事をてきぱきこなしてくださったら、俺はもっと多くの自由時間を得られるのにな、と示唆しているだけですよ」"

hide nai_m_02_9
show nai_m_01_12 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0294
Nightmare "「そ、それが脅しじゃなくてなんなんだ……！？\n
その薄ら笑いが怖いんだ、おまえは昔から！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……昔？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そういえば、グレイとナイトメアは、どれくらいの付き合いになるのだろう。\n
阿吽の呼吸というか、付き合いの長さは感じる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（一方的に、グレイが合わせているようにも見えるけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それでも二人が並んでいる姿は当たり前のようにしっくりとくる。\n
ナイトメアの言葉のように、ずいぶんと昔から一緒にいるかのようだ。"

hide gre_m_01_3
show gre_m_03_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0177
Gray "「それが分かっていらっしゃるんでしたら、ほら。\n
仕事を進めてくださいね」"

hide nai_m_01_12
show nai_m_02_10 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0295
Nightmare "「まだ休憩中だ！！」"

hide gre_m_03_3
show gre_m_01_13 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0178
Gray "「もうカップの中身は空ですよ。\n
充分に休んだでしょう」"

hide nai_m_02_10
show nai_m_03_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0296
Nightmare "「なら、お代わりを……っ！\n
ああ、鬼っ、悪魔……！！」"

hide gre_m_01_13

hide nai_m_03_3


play music drawingroom_nig_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイは、ナイトメアのマグカップが空になったタイミングで追いたて、彼を仕事へと引き戻す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして渋々ながらナイトメアがペンを手にとり、書類に目を通し始めたのを見届けると、私の隣へとやってきた。"


show gre_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0179
Gray "「それで、先刻の話の続きなんだが……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「ああ。\n
平気よ、ちゃんと部屋でおとなしくしているわ」"

hide gre_m_03_9
show gre_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice gra_g0180
Gray "「いや、そうじゃなくて。\n
ブリーズに一緒に参加できない代わりに……、今度の週末、一緒に街に出掛けないか？」"

hide gre_m_01_3
show gre_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice gra_g0181
Gray "「ちょうど、街まで買い物に出掛けなければいけない用事があったんだ。\n
イベントごとほど楽しめはしないだろうが、君さえよければ……」"
menu:
    "即答で了承する。":
        jump gakuen_gray5_3b
    "躊躇う。":
        jump gakuen_gray5_3a
label gakuen_gray5_3b:
$ lovechara_gray_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_2")
T "「行くわ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "即答で返事をした。"

jump gakuen_gray5_4
label gakuen_gray5_3a:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「でも……、用事で行くんじゃないの？\n
私がついていってもいいものなのかしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は用事があって街に行くのだ。\n
ただ遊びに行くというわけでもないのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そこに私がついていって、大丈夫なのだろうか。"

hide gre_m_01_4
show gre_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0182
Gray "「よくなければ、最初から誘っていないさ。\n
……どうだろう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_2")
T "「それなら、お言葉に甘えるわ。\n
是非、同行させてちょうだい」"

jump gakuen_gray5_4
label gakuen_gray5_4:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズに一緒に参加できないのは残念だが、彼が塔の管理という職務についている限り仕方のないことだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "残念なことではあるが、一緒に街に出るというのも、その代替案として魅力的だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "外出は禁じられてはいないものの、たいていのものが学園内で手に入ってしまうこともあり、わざわざ街まで出る機会はほとんどない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "許可を得る手続きが面倒だというのもある。\n
だが、彼と一緒に街に出るなら、書類を作成するのも苦にはならない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_19")
T "（これって……、デートよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "頬が緩んでしまう。"

hide gre_m_01_8
show gre_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0183
Gray "「はは、喜んでもらえたようでよかった。\n
それじゃあ、今週末は一緒に街に行こうか」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_10")
T "「ええ、楽しみにしているわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そっとグレイを見上げる。\n
彼もまた私へと視線を返す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私達は見詰めあって……。"


show nai_m_01_10 at center
with dis
hide gre_m_03_4

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0297
Nightmare "{size=+20}「お願いだから、他所でやってくれ」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "三度目のツッコミは、素早く入った。"

with dis
$ hi_mes()
hide nai_m_01_10


scene bg_par16_rs_tow_eve with Dissolve(.8)

scene bg_par15_rg_tow_eve
with stripe_l_medium

scene bg06_sk_h_eve with stripe_l_medlong

scene bg06_sk_h_nig with Dissolve(1)

scene bg06_sk_h_day with Dissolve(1)

scene bg24_rj_day
with stripe_l_long

play music room1_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "今日は、グレイと一緒に街に行く日だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_s_01_2")
T "（き、気合入りすぎてないかしら……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "姿見の前で、念入りにチェックする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "何せ、初デートだ。\n
変な格好は出来ない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "だからといって、気合が入りすぎて浮くのもまずい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "彼はきっといつものスーツ姿だろうから、その彼に合った、隣に並んで恥ずかしくない格好をしなくてはいけない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "そんなわけで、少し大人っぽい落ち着いた色合いのワンピースを選んだ。\n
これならば、彼の隣に並んでも不釣合いなほど子供っぽくは見えないだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "だが……、今度は逆に気合が入りすぎているのではないかと心配になるのだから、困ったものだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "おかげで、もう何度も姿見の前で回転してみる羽目になっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_s_05_5")
T "（あ、でも、そろそろ時間）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "待ち合わせ場所は、塔のエントランス。\n
階段を下りてすぐなので、そんなに急がなくても平気だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_s_02_17")
T "（でも、きっとグレイは早めに着いて待ってくれていそうよね。\n
そういうイメージ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "彼のことだ。\n
五分前どころか、十分前行動もありうる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_s_06_11")
T "「変……、じゃないわよね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "今度こそ最後にしようと決めて、もう一度鏡を覗きこむ。\n
鏡に映る私は頬を上気させ、どことなく緊張した顔をしていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "いかにも初デートに期待を寄せるといったふうで、自分自身にこそばゆくなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_s_01_6")
T "（落ち着くのよ、私）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "子供みたいにはしゃいでいては駄目だ。\n
大人の彼に相応しいだけの、落ち着きがほしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "一度大きく深呼吸して気を落ち着け、自室を後にした。"

with dis
$ hi_mes()

scene bg24_rj_day with Dissolve(.8)

scene bg25_rr_day
with stripe_l_medium

scene bg_par20_re
with stripe_l_long

play music view_nig_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_s_02_2")
T "（……あれ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "最初に違和感に気付いたのは待ち合わせの時間五分前になっても、グレイが姿を現さなかったからだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "次に違和感を覚えたのは、慌しく階段を上り下りする使用人の姿に気付いたとき。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "そして、その違和感のトドメを刺したのは、目の前にいつのまにか出現したナイトメアだった。"


show nai_m_02_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_s_06_16")
Nightmare "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "ナイトメアは何も言わなかったが、それでも何かあったのだということは分かった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "そして、今日のデートが中止になってしまったことも。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "彼は無言で私の隣へとやってくる。"

hide nai_m_02_7
show nai_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_s_06_16")
Nightmare "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_s_02_3")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "どれくらい、沈黙が続いただろう。\n
彼がようやく口を開いた。"

hide nai_m_03_9
show nai_m_03_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_s_06_16")
voice nig_g0298
Nightmare "「……上司を顎で使うとは、酷い部下だとは思わないか？\n
まったく、私を何だと思っているのか」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_s_01_12")
T "（……優しい）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "いつもどおりにぼやくような言葉ながら、その中にはグレイに対するフォローが滲んでいる。\n
何か、トラブルが起こったのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "グレイが身動き取れなくなってしまい、ナイトメアに伝言を頼まざるを得ないようなことが。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "そうでもなければ、グレイは自分で「都合が悪くなってしまった」と伝えにくるだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_s_01_11")
T "「何があったの？」"

hide nai_m_03_6
show nai_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_s_01_11")
voice nig_g0299
Nightmare "「風紀のほうで取り締まった生徒の中に、校則で禁じられている魔法植物を繁殖させていた輩がいてな。\n
その一味の中に、塔の生徒もいたんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_s_05_10")
T "「……ああ。\n
それは……、グレイが抜けるわけにはいかないわね」"

hide nai_m_02_5
show nai_m_02_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_s_05_10")
voice nig_g0300
Nightmare "「ああ。\n
今、見つかった場所以外で密栽培していないかを、使用人総出で確認している」"

hide nai_m_02_7
show nai_m_01_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_s_05_10")
voice nig_g0301
Nightmare "「あとそうだな……、その植物は本来厳重に管理されているべきものだ。それをどうやって彼らが盗み出し、殖やしたのかをはっきりさせなくてはならない」"

hide nai_m_01_9
show nai_m_02_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_s_05_10")
voice nig_g0302
Nightmare "「私も、寝耳に水だった。\n
グレイも、出かけようとしたところで委員長に捕まり、報告を受けたようだったからな」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "おそらくそのまま、ユリウスと対策会議に入らざるを得なくなったのだろう。\n
立場上、そのまま動けなくなってしまったのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "まさか、生徒の一人とデートしようとしていたなんて公言できるわけもない。\n
今、その状態で、グレイ本人が動いてはそれを喧伝することになってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_s_01_12")
T "（……というか、相手が誰であれ、仕事を放り出すような人じゃないわね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "だから……、グレイはナイトメアに頼んだのだ。"

hide nai_m_02_9
show nai_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_s_06_16")
voice nig_g0303
Nightmare "「……怒っているか？」"

menu:
    "怒っていない。":
        jump gakuen_gray5_5a
    "少しだけ……。":
        jump gakuen_gray5_5b
label gakuen_gray5_5a:
$ lovechara_gray_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_s_06_15")
T "「……まさか。\n
怒っていないわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_s_02_18")
T "「それがグレイの仕事だもの。\n
仕方のないことだわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "そういう私の声音は、どうしたって自分自身に言い聞かせるように響く。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_s_01_7")
T "「ただ……、楽しみにしていたから。\n
残念なだけ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "仕事をするグレイが悪いはずもなく。私もそんな彼を好きになった。\n
だが、初デートがなくなってしまったのが残念という気持ちも正直なところだ。"

jump gakuen_gray5_6
label gakuen_gray5_5b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_s_06_13")
T "「……少しだけ、怒っているわ。\n
でも、グレイには内緒よ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "仕事をするグレイが悪いはずもなく。私もそんな彼を好きになった。\n
だが、初デートがなくなってしまったのが残念という気持ちも正直なところだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_s_01_6")
T "「それに、グレイに対して怒っているというわけじゃないの」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_s_04_11")
T "「問題を起こしたっていう生徒に対してだったり、仕方のないことだと分かっているのに落ち込んでいる自分に対してだったり……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_s_01_2")
T "（……ともかく、グレイは悪くない）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "これは、デートをすっぽかしたグレイに対する怒りではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "ただ、楽しみにしていた初デートが駄目になってしまったことが、ひたすらに残念で、悔しいのだ。"

jump gakuen_gray5_6
label gakuen_gray5_6:
hide nai_m_01_4
show nai_m_02_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_s_06_16")
voice nig_g0304
Nightmare "「……そうだな。\n
残念だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "ぽんとナイトメアの手が、私の頭に触れる。\n
慰めるようなその優しい仕草に、うっかり涙腺が緩みそうになった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "別に、泣くようなことではない。\n
一時的に感情が高ぶっているだけだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_s_02_5")
T "（……駄目駄目。\n
こんなところで愚図ったら、本当に子供だわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_s_06_15")
T "「ありがとう、ナイトメア。\n
連絡をしてくれた御礼に……、あなたの仕事を手伝ってあげるわ」"

hide nai_m_02_7
show nai_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_s_06_15")
voice nig_g0305
Nightmare "{size=+20}「げっ！？」{/size} "

hide nai_m_03_3
show nai_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_s_06_15")
voice nig_g0306
Nightmare "「グ、グレイがいないから今日はほら、私も休みだ……。\n
せ、せっかくだから、二人で羽を伸ばそうじゃないかっ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_s_01_10")
T "「いえいえ、せっかくの機会よ？\n
グレイがいなくてもちゃんと仕事が出来るってところ、見せてあげようじゃない」"

play sound se_0051
hide nai_m_02_10
show nai_m_03_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_s_01_10")
voice nig_g0307
Nightmare "「うええええええええ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_s_06_14")
T "「ほらっ、きりきり歩きなさい！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "ナイトメアへと発破をかけて、ずるずると彼を引きずるようにして歩く。"

play sound se_0562 volume .2
hide nai_m_03_6

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "彼も、逃げ出しはしない。\n
……付き合ってくれている分、ナイトメアもまた大人ではあるのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_s_02_17")
T "（勉強のときみたいに、気持ちを切り替えなくちゃ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "仕事が進んでいれば……、次のデートのチャンスは、意外と早く来るかもしれない。"

with dis
$ hi_mes()

scene bg_par20_re with Dissolve(.8)

scene bg_par15_rg_tow_day
with stripe_l_medium

scene bg06_sk_h_day
with stripe_l_medium

scene bg06_sk_h_eve with Dissolve(1)

scene bg06_sk_h_nig with Dissolve(1)

scene bg06_sk_h_day with Dissolve(1.2)

play music stream_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、考えが甘かった。\n
そのままグレイはこの密栽培問題にかかりきりになり、医務室にもほとんど寄ることが出来なくなってしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメア補佐の仕事すらままならず、塔の執務長としての仕事で手一杯だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（前と逆ね……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "以前は、私のほうが勉強に忙しく、立ち寄れなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、今は関係も違う。\n
恋人になりたてで、ここまで会えないというのは耐え難い。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_3")
T "（……寂しい）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "会いたいと思う。\n
会って、声を聞きたい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、彼にそんな余裕がないことも分かっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（待つ側になったら我慢できないなんて、我侭だわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は勉強があるとはいえ、比較的時間に余裕のある学生で……、彼は働いている。\n
しかも、その職務は塔の執務長なんていう責任のあるものなのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "構ってほしいなんていうのは、本当にただの我侭。\n
子供のエゴだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（私も、大人にならなきゃ。\n
愚図ったりしちゃ駄目よ、駄目）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう心の中で繰り返して、背伸びをする。\n
背伸びをしていれば、いつしか大人にもなれるはず。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな期待をこめて、彼を待つ。\n
いつのまにか、ブリーズの日が近づいてきていた。"

with dis
$ hi_mes()

scene bg_par15_rg_tow_nig
with stripe_l_medium

scene bg_map_nig with Dissolve(1.2)
##endmemory
jump gakuen_gray6
