label gakuen_dormitory_castle_hatter1:
label gakuen_dormitory_castle_tower1:
$ clockanim()


scene bg_par15_rg_ros_day with Dissolve(1.2)

play music gallery_front_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私達は遊園地寮から、赤薔薇寮のある方向へと逃げていたらしく、そこから赤薔薇寮まではすぐだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "赤薔薇寮は、その名の通り赤薔薇に囲まれた美しい洋館だった。\n
むしろ城、といっていいほどかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "赤薔薇の生垣が演出する迷路のような庭を、矢印の案内で抜けて、私は赤薔薇寮の執務室を目指す。"

with dis
$ hi_mes()

scene bg25_rr_day
with stripe_l_medium

scene bg_par16_rs_ros_day
with stripe_l_long

play music drawingroom_day_p_wam

show m_ryou1_siro1 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "辿り着いた赤薔薇寮の執務室は、塔のそれよりも豪華で、華美だった。\n
クラスメイトの言っていた『華やか』という言葉の意味を理解する。"

jump gakuen_dormitory_castle2
label gakuen_dormitory_castle_amuse1:
$ clockanim()


scene bg_par15_rg_ros_day with Dissolve(1.2)

play music gallery_front_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "赤薔薇寮は、その名の通り赤薔薇に囲まれた美しい洋館だった。\n
むしろ城、といっていいほどかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "赤薔薇の生垣が演出する迷路のような庭を、矢印の案内で抜けて、私は赤薔薇寮の執務室を目指す。"

with dis
$ hi_mes()

scene bg25_rr_day
with stripe_l_medium

scene bg_par16_rs_ros_day
with stripe_l_long

play music drawingroom_day_p_wam
hide m_ryou1_siro1
show m_ryou1_siro1 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "辿り着いた赤薔薇寮の執務室は、塔のそれよりも豪華で、華美だった。\n
クラスメイトの言っていた『華やか』という言葉の意味を理解する。"

jump gakuen_dormitory_castle2
label gakuen_dormitory_castle_castle1:
$ clockanim()


scene bg_par15_rg_ros_day with Dissolve(1.2)
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_14")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（ここが……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私達は遊園地寮から、赤薔薇寮のある方向へと逃げていたらしく、そこから赤薔薇寮まではすぐだった "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "赤薔薇寮は、その名の通り赤薔薇に囲まれた美しい洋館だった。\n
むしろ城、といっていいほどかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "塔、帽子屋寮、遊園地寮とこれまで見てきたが、ここもすごい。\n
どれも、学生寮なんていう言葉から想像する以上の建物ばかりだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "赤薔薇の生垣が演出する迷路のような庭を、私は矢印に導かれて歩いていく。\n
そして、ようやくエントランスが見えたところで、矢印がふと動きを止めた。"


show guide_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sat_g0083
Guide "「さあ、ここが終点だよ！\n
ここが赤薔薇寮だ！」"

play sound se_0058
hide guide_2
show guide_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sat_g0084
Guide "「これで俺の任務は完了！\n
後は自治会員の登録をするだけだ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ガイドである矢印が案内してくれるのは、ここまで。四つの寮を巡る間だけだというのに、ずいぶん長い時間を一緒に過ごしたような気がした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "少しばかり、寂しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「ここで、お別れ？\n
少し、寂しいわ」"

hide guide_6
show guide_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice sat_g0085
Guide "「寂しく思うことなんかないさ！\n
俺は君が迷子になったら、すぐにでも飛んでいくからね！」"

hide guide_1
show guide_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice sat_g0086
Guide "「だって俺は……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_15")
T "「迷子を安心できるところまで案内してあげる、一流のガイド？」"

hide guide_4
show guide_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_15")
voice sat_g0087
Guide "「その通り！\n
俺は超一流のガイドだからね、迷子を見つけるのも上手なんだ！」"

hide guide_3
show guide_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_15")
voice sat_g0088
Guide "「だから安心して迷子になるといいよ！\n
俺に会いたければね！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「安心して迷子って……」"

play sound se_0082
hide guide_5

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本来、迷子を案内するためのガイドであるはずの矢印が、迷子を推奨しながらしゅわしゅわと消えていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "元々半透明で見えにくかった矢印が、首に繋がれた紐ごとしゅわしゅわとぼやけて見えなくなっていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_20")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぱちり、と瞬きした次の瞬間には、もうそこに矢印の名残はなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「……無茶を言うわね」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_8")
T "（行っちゃった……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今まで紐を持っていた手の中が、空っぽになってしまっているのが寂しい。\n
よく知らない場所で一人きり……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（また、会えるわよね……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（…………。\n
……いや、会っちゃ駄目か）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あのガイドに会うということは、迷子になるのと同義だ。\n
積極的に会いたいような相手ではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが……、半透明で見つけにくいとはいえ、あんなに騒々しいガイドなのだ。\n
これから始まる学園生活の中で、また見かけることもあるだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「……よし」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "気持ちを切り替え、赤薔薇寮の中へと足を踏み入れた。"

with dis
$ hi_mes()

scene bg25_rr_day
with stripe_l_medium

scene bg_par16_rs_ros_day
with stripe_l_long

play music drawingroom_day_p_wam
hide m_ryou1_siro1
show m_ryou1_siro1 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "赤薔薇寮の執務室は、塔のそれよりも華美だった。\n
クラスメイトの言っていた『華やか』という言葉の意味を理解する。"

jump gakuen_dormitory_castle2
label gakuen_dormitory_castle2:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何より、その執務室の中央に立つ女性が華やかで……、艶やか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（オーラがあるっていうか……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今までにもいわゆる金持ち、と呼ばれる人たちに会ったことはある。\n
その誰もが、やはり華やかで、綺麗な人たちだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、今私の目の前にいる人は、華やかで美しいというだけではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（……高貴な感じ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分とは違う世界の人なのだと、こうして同じ部屋の中にいても、ありありと分かる。\n
恐れ多いような、そんな美しさだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ただただ、うっとりと……出来れば遠くから眺めていたくなる。\n
ピアスや、双子達が女王と呼ぶのも納得がいく。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女の傍らには、女王を守る忠実な部下といったふうに、二人の男子生徒が控えていて……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「……ペーター？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "呼ぶ声は、訝しげに潜めてしまう。\n
その美しい人の傍らに、見慣れた幼馴染の姿。"

hide m_ryou1_siro1
show m_ryou1_siro2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_r0044
Peter "「はい！僕ですよ、[firstname]！！！\n
あなたがここにやってくるのを、今か今かと待っていました！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……間違いようもなく、ペーターだ。\n
特徴的な耳からしても、間違いようがない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「……なんで、あんたがここにいるのよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice pet_r0045
Peter "「何故って……、それは僕が自治会の書記だからですよ！\n
あなたのために、シンフォニアでも着々と権力を掴んでおいたんです！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_10")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "がくりと力尽きそうになってしまった。"
if place_of_stay == "Castle":
    jump gakuen_dormitory_castle_castle2
if place_of_stay == "Hatter":
    jump gakuen_dormitory_castle3
if place_of_stay == "Amuse":
    jump gakuen_dormitory_castle3
if place_of_stay == "Tower":
    jump gakuen_dormitory_castle3

label gakuen_dormitory_castle_castle2:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そういえば、そうだ。\n
考えるまでもなく、四つの寮のうちの一つにはハズレ（ペーター入り）が当然存在するはずなのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それを、私はうっかり失念していた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_3")
T "（……まさか、そのハズレを引いちゃうなんて。\n
四分の一の確率で）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "寮を決める前に、ペーターがどの寮に住んでいるのかを、確認しておくべきだった。"

jump gakuen_dormitory_castle3
label gakuen_dormitory_castle3:
play sound se_0179
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "カツンと高く、石を叩く音。"

hide m_ryou1_siro2
show m_ryou1_siro3and5 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "はっ、とそちらへと視線を戻した。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_r0000
Hatena "「赤薔薇寮の寮長であり、シンフォニア高位魔法学校の自治会会長であるわらわを無視するとは……。\n
おまえ、なかなかいい度胸をしているね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……っ！\n
ごめんなさい、そのようなつもりはありません」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "す、っと胸元に金色のステッキを突きつけられて、即座に謝った。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "予想もしない場所で知り合いの姿を見つけた。\n
そのことに動揺したとはいえ、無礼な態度をとってしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（って、先生相手でもないのに、こんなふうに畏まっちゃうあたり、やっぱりオーラがあるっていうか……）"

hide m_ryou1_siro3and5
show m_ryou1_siro4 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice pet_r0046
Peter "「[firstname]！！あなたが謝ることなんてないんですよ！！\n
会長なんて、無視してくださって結構です！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "動物には、オーラなんて通じないらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_r0047
Peter "「あなたには僕がついていますからね！\n
僕があなたのために、何だってしてあげます！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_r0000
Hatena "「はは。\n
君、ペーターさんに愛されているね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_4")
T "「……やめてよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターとは逆の側に控えていた青年が、爽やかに笑いかけてくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（この人もなんだか、オーラ的なものが……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（きらきら爽やかで……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_16")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_8")
T "（……でも、どす黒いような）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（……いや、{size=+20}爽やかでどす黒いって何{/size}）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice viv_r0001
Hatena "「ホワイト、エース。今は、わらわがこの子と話しておるのだぞ？\n
おまえ達は、黙っておれ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice ace_r0001
Ace "「はいはい、分かりましたよ。\n
仰せの通り、黙ります」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
Peter "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースと呼ばれた青年だけでなく、ペーターも不満そうながら黙り込む。\n
一応命令を聞くつもりはあるらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（この女性……、本当に権力者なんだわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼らの様子を見届けてから、美しい「女王様」は再び私へと視線を戻した。"

hide m_ryou1_siro4
show m_ryou1_siro3and5 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_r0002
Hatena "「おまえの名は、なんという」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「[firstname]＝[familyname]と申します」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
Hatena "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（？？？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "問われたままに名乗ったのに、彼女は何故か不満そうな顔をした。\n
元々知っていた答えとは別の答えを得た、というような、そんな表情だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_12")
T "（……あ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その顔の意味に、私は思い当たってしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いわゆる……、例の、違和感だ。\n
ゴーランドや、その他でも感じた、例のアレ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（……なんなのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女はここ、赤薔薇寮の寮長で、シンフォニア高位魔法学校の自治会会長。\n
肩書きだけでなく、その佇まいには自ら跪きたくなるほど。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だというのに……、敬語を使うことに違和感を覚える。\n
恐らく、彼女も同じなのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Hatena "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_r0003
Hatena "「……おまえは不思議な子だね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女は、軽く眉間に皺を寄せ、戸惑ったような顔をしている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「そ、そうかしら……？\n
え、ええと、あなたは……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice viv_r0004
Vivaldi "「……わらわは、ビバルディ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice viv_r0005
Vivaldi "「おまえにはビバルディと呼ぶことを許そう。\n
おまえには、特別に」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それは、敬語を使わなくてもいい、と言う許可。今までの男性陣と同じく……、だが、彼女を名前で呼ぶと想像しただけで恐れ多くて眩暈がしそうになる。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_r0006
Vivaldi "「さ、呼んでみろ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「え」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「え……、っと」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "促されて、言葉が喉で詰まる。\n
にこやかな笑顔で、さあ、と迫る彼女をどうしたらいいのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_r0007
Vivaldi "「……さあ。\n
呼んでいいのだぞ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "逃げられない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「ビ……、ビバルディ……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "呼び捨てで呼ぶのは勇気がいったが、それでも、違和感はなかった。"

hide m_ryou1_siro3and5
show m_ryou1_siro6 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_r0008
Vivaldi "「ああ。\n
……ふふ、おまえは可愛いのう」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「か、可愛い……？\n
私が？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_7")
voice viv_r0009
Vivaldi "「ああ。\n
なんだか……、とても可愛く思える」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「そ、そう。\n
ありがとう、ビバルディ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "覚悟を決めて呼んでみた名前は、意外に思ってしまうほどにしっくりときた。\n
女王様のほうも上機嫌だ。"

hide m_ryou1_siro6
show m_ryou1_siro7and9 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Peter "「！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_r0048
Peter "「ずるいです！！会長も恩着せがましく、呼び捨てでいいなんて……！\n
僕の名前も呼んでください、[firstname]！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_r0049
Peter "「僕の名前はペーター＝ホワイトです！！\n
さあ！！さあ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "{size=+20}「知っているわよ」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "きらきらした目で、名前を呼んでくれと迫るペーターに半眼を向ける。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_r0050
Peter "「ええ、ええ、もちろん、あなたは僕のことをご存知でしょうとも！\n
僕もあなたを知っています！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……そりゃあ、幼馴染だもの」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice pet_r0051
Peter "「ええ！\n
でも、いくら知っていても、もっと知りたいと思うものです」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_8")
T "「……私は思わないけど」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_8")
voice pet_r0052
Peter "「それが愛！愛なんですよ、[firstname]！\n
僕は愛に生きているんです！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_7")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（……幼馴染じゃなきゃ、ストーカーだわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice ace_r0002
Ace "「……ねえ、ちょっと待ってよ、ペーターさん。\n
ペーターさんは、その子の知り合いなんだろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice ace_r0003
Ace "「だったら、まずは俺の紹介をしてくれるか、俺に紹介の機会をくれるのがフェアってものじゃないか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice pet_r0053
Peter "「……僕はフェアじゃなくていいです。\n
あなたと彼女が知り合う機会を作るなんて御免ですね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私に対するときとはまるで違う、冷たい声。\n
外でのペーターについてはよく知らないが、知人である私でさえぞっとした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "が、対する青年のほうは、堪えた様子もない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_r0004
Ace "「しょうがないなあ、ペーターさんは。\n
まあ、いいや、勝手に自己紹介させてもらうよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_r0005
Ace "「自分の道は自分で切り開くもの。\n
それでこそ、風紀委員ってものだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（……風紀委員？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "たしか、塔にいたユリウスも風紀委員長だとか何とか言っていた。\n
しかし、ここにいる彼は自治会だとか何とかのはずで……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（シンフォニアの組織ってややこしいなあ……）"

hide m_ryou1_siro7and9
show m_ryou1_siro8 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_16")
voice ace_r0006
Ace "「ってことで、はじめまして」"

play sound se_0492 volume .6
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ひょい、と爽やかな好青年風（あくまで風だ）の彼は、私のもとまでやってくるとにこやかに手を差し出した。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_r0007
Ace "「挨拶が遅れてごめんね？\n
俺はエース。自治会では風紀を担当している」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「風紀委員長は、塔にもいたみたいだけど……。\n
自治会のあなたはどういったことをしているの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice ace_r0008
Ace "「校内の、清く正しい生活を守るため、日夜暗躍しているんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「へ、へえ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_7")
T "（清く正しく……、{size=+20}暗躍？{/size}）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_16")
T "「……暗躍って、清く正しくないんじゃないかしら？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_16")
voice ace_r0009
Ace "「そう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「少なくとも、堂々としていないんじゃ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice ace_r0010
Ace "「清く正しいからこそ、どんなふうに活動しようと堂々としていられるんだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "半眼で睨んでも、ペーターと同じく、きかないらしい。\n
エースは、にこにこと爽やかなまま。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「……私は、[firstname]＝[familyname]。\n
よろしく」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（……とりあえず、権力には逆らわないでおこう）"

play sound se_0361 volume .6
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼の差し出した手を握り返し、握手を交わす。"

hide m_ryou1_siro8
show m_ryou1_siro7and9 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_r0054
Peter "「[firstname]！！！そんな奴に触れてはいけません！！\n
汚れてしまいます！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_r0011
Ace "「はは、ペーターさん失礼だよ？\n
俺は清潔だぜ……、動物じゃあるまいし、ね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_r0055
Peter "「……っっ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_r0012
Ace "「おっと、会長もお気に入りの新入生の前だ、落ち着いてよ？\n
すぐに興奮しないで……動物じゃないんだから、ねえ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "と、エースは爽やかに笑いながら私の手を放してくれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "爽やかに、にこやかに。\n
人の神経を逆撫でするのがうまい男だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_r0056
Peter "「……そうですね、動物じゃないからこそ、侮辱を無視できないんですよ。\n
しかも、彼女の前で……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_r0013
Ace "「……はは。\n
ご執心なんだ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Peter "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_r0014
Ace "「……らしくないなあ。\n
でも、そういうペーターさんだと、対戦しがいがありそうだ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターが無言で懐へと手をやれば、エースも楽しそうな笑みを浮かべながら軽く身構えて向き直る。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_7")
T "（け、喧嘩……っ！？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は助けを求めて彼らのトップであるビバルディへと視線をやるものの、彼女はつまらなそうに肩を竦めただけだった。"

hide m_ryou1_siro7and9
show m_ryou1_siro10 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_r0010
Vivaldi "「愚かな男どもは勝手に殺し合いでも何でもやっておればよいのだ。\n
男どもが阿呆なことをしているうちに、手続きをすませてしまおう」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_r0011
Vivaldi "「さあ、[firstname]。\n
こちらへおいで」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「え……、えっと……？\n
放っておいて大丈夫なの……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースはにこにこと笑っているが、ペーターは本気で苛立っている。\n
いや、エースのほうだって、表情はともかく物騒な雰囲気で……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつ魔法を使っても、おかしくないように見えた。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_r0012
Vivaldi "「ああ、いいとも。ほら、おいで。\n
くだらないことを心配する必要などないよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「ええ？\n
でも……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice viv_r0013
Vivaldi "「いつものことだ、放っておいても死人は出まい。\n
……残念だが」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あっさりとビバルディは言う。\n
まるでどちらかの、というよりも、両方の死を願っているかのような口ぶりだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女は、執務机につくと私へと手を差し出した。"

hide m_ryou1_siro10
show m_ryou1_siro11 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_r0014
Vivaldi "「おまえの学生証をお出し。\n
もう、塔で契約してきたのだろう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「ええ。\n
契約は済んでいるわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私よりこの二人のやりとりに慣れているであろう、ビバルディ。\n
彼女が大丈夫だというのだから、きっと大丈夫なのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（……と、考えることにしよう）"

play sound se_0660
$ flash(.1)
pause .5
play sound se_0761
$ flash(.2)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "背後から、ちゅどーんとかごおおっとか、ばりばりばりとか……、聞こえてくるのは気のせいだ。"

play sound se_0659 volume .6
$ flash(.1)
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「これが、私の学生証」"

hide m_ryou1_siro11
show m_ryou1_siro12 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "先ほど契約したばかりの学生証を、差し出された手のひらの上へと載せた。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_r0015
Vivaldi "「[firstname]＝[familyname]。\n
……おまえは自治会員になることを望むか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_r0016
Vivaldi "「会員になれば、わらわがおまえを守ってやろう。\n
そのかわり、おまえは、わらわのものになる」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「あ、あなたのもの……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_7")
voice viv_r0017
Vivaldi "「そう。\n
わらわのもの」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふふ、と艶やかに女王が笑う。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（所属する、ってことよね？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自治会員になれば、会長の保護下に入ることができる。そのかわり、シンフォニアの生徒としての権限を、会長である彼女に委ねることになるのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「……ええ。\n
構わないわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice viv_r0018
Vivaldi "「……よい子じゃ。\n
では、契約を交わそう」"


play music magic_a_wam
hide m_ryou1_siro12
show m_ryou1_siro13 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "す、っと綺麗に赤く塗られた爪先が、私の学生証の上を撫でる。"

play sound se_0138
$ flash(.5)
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「わ……！」"

with dis
$ hi_mes()
hide m_ryou1_siro13
show m_ryou1_siro14 onlayer master
with dis
pause .5
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぱあ、っと一瞬学生証が光ったかと思うと、学生証の背景に薄く薔薇の模様が浮かんだ。\n
これが、自治会員の証だ。"


play music drawingroom_day_p_wam
hide m_ryou1_siro14
show m_ryou1_siro15 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_r0019
Vivaldi "「校内で誰ぞにいじめられたら、わらわにお言い。\n
おまえの代わりにたっぷりと仕返ししてあげる」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「頼りにしているわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "学生証を受け取りながら、頷いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（そんな機会はないに越したことはないけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice viv_r0020
Vivaldi "「ああ、頼りにしておいで。\n
……ところで、[firstname]、おまえはもう寮は決めたのか？」"
if place_of_stay == "Castle":
    jump gakuen_dormitory_castle_castle3
if place_of_stay == "Hatter":
    jump gakuen_dormitory_castle_not1
if place_of_stay == "Amuse":
    jump gakuen_dormitory_castle_not1
if place_of_stay == "Tower":
    jump gakuen_dormitory_castle_not1

label gakuen_dormitory_castle_not1:

scene bg_par16_rs_ros_day ##instantPAY ATTENTION="true"]
hide m_ryou1_siro15


show viv_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice viv_r0029
Vivaldi "「まだ決めていないのなら、ここはどうじゃ？\n
よいところだぞ、赤薔薇寮は」"
$ gakuen_dormitory_castle_not2a_seen = False
menu:
    "ええ、素敵ね！":
        jump gakuen_dormitory_castle_not2a
    "そんなに魅力は感じない。":
        jump gakuen_dormitory_castle_not2b
label gakuen_dormitory_castle_not2a:
$ gakuen_dormitory_castle_not2a_seen = True
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「ええ、素敵なところだと思うわ！\n
でも残念なことに、私、ここにくる前にもう寮を決めてしまっているのよね……」"

hide viv_m_01_3
show viv_m_01_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice viv_r0030
Vivaldi "「なんと。\n
実際にその目で見る前に決めてしまうとは……、せっかちな子じゃ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「ごめんなさい……。\n
でも、ここが素敵だと思うのは本当よ？」"

hide viv_m_01_5
show viv_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice viv_r0031
Vivaldi "「当たり前じゃ。\n
ここはわらわの城なのだからね」"

hide viv_m_03_10
show viv_m_03_10 at left
with dis

show per_m_01_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice pet_r0063
Peter "「そんな！\n
まさか、ここ以外の場所に決めてしまっただなんてことはありませんよね！？」"

hide viv_m_03_10

hide per_m_01_5
show per_m_01_5 at left
with dis

show ace_m_01_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice ace_r0021
Ace "「だから、そう言っているじゃないか。\n
はは、ペーターさんってば空気も読めなければ会話の流れも読めないの？」"


show viv_m_03_9 at center
with dis
hide per_m_01_5

hide ace_m_01_4

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice viv_r0032
Vivaldi "「……どこの寮に決めたのじゃ？\n
ここを選ばなかったのだ。さぞや、魅力的な場所なのだろうな？」"
if place_of_stay == "Hatter":
    jump gakuen_dormitory_castle_hatter2
if place_of_stay == "Amuse":
    jump gakuen_dormitory_castle_amuse2
if place_of_stay == "Tower":
    jump gakuen_dormitory_castle_tower2
label gakuen_dormitory_castle_not2b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「う～ん……、わ、悪いんだけど……。\n
ちょっと遠慮したいわ」"

hide viv_m_03_9
show viv_m_03_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice viv_r0033
Vivaldi "「む……。\n
何が気に入らないのだ、言ってごらん」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「気に入らないなんてことはないわ。\n
ここは素敵な場所だもの」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「ただちょっと……。\n
ちょっと……、ね？」"


show per_m_02_13 at center
with dis
hide viv_m_03_7

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice pet_r0064
Peter "「ああ、[firstname]っ、あなたはどうして僕を見るんですかっ？\n
ああっ、分かっています、分かっていますとも！」"

hide per_m_02_13
show per_m_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice pet_r0065
Peter "「あなたの視線から、僕を包み込むような柔らかで温かな愛情を感じますっ！！\n
大丈夫ですよ、同じ寮ともなれば、僕がずっとずっと傍にいますからね！！！」"

hide per_m_03_1
show per_m_03_1 at left
with dis

show ace_m_03_11 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice ace_r0022
Ace "「ははは。その耳は飾り物なの？\n
ペーターさん」"

hide ace_m_03_11
show ace_m_02_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice ace_r0023
Ace "「会長、理由は明白ですよね！\n
俺でも、寮を飛び出したくなっちゃいますよ」"


show viv_m_02_7 at center
with dis
hide per_m_03_1

hide ace_m_02_4

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice viv_r0034
Vivaldi "「……うむ。\n
明白であったな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_16")
T "「……うん、ごめんね？」"

hide viv_m_02_7
show viv_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_16")
voice viv_r0035
Vivaldi "「いや、構わぬ。\n
それでおまえは、どこに決めたのじゃ？」"

hide viv_m_01_3
show viv_m_03_9 at center
with dis




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_16")
voice viv_r0036
Vivaldi "「……さぞや、快適な場所なのだろうな？\n
ウザったいウサギのいない……」"
if place_of_stay == "Hatter":
    jump gakuen_dormitory_castle_hatter2
if place_of_stay == "Amuse":
    jump gakuen_dormitory_castle_amuse2
if place_of_stay == "Tower":
    jump gakuen_dormitory_castle_tower2
label gakuen_dormitory_castle_hatter2:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「ええ、帽子屋寮よ。\n
帽子屋寮に決めたの」"


show per_m_01_5 at center
with dis
hide viv_m_03_9

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
Peter "「！！！」"

hide per_m_01_5
show per_m_01_5 at left
with dis

show ace_m_03_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
Ace "「！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の言葉に、ぎゃんぎゃんと言い争っていたペーターとエースが反応する。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "正確には言い争う、というよりも、エースがペーターをおちょくって遊んでいた、に近いような気もしないでもない。"

hide per_m_01_5

hide ace_m_03_9

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターがそれこそウサギのように、ぴょんと跳ねて一息に私へと距離を詰めてきた。"


show per_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_r0066
Peter "「酷い……！！酷いですよ、[firstname]！！！\n
どうしてあんなところに行ってしまうんですか！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「どうしてって……。\n
特に理由はないんだけど」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（酷いとか言われても……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうしても帽子屋寮でなくてはいけない、というような理由はない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ただ、その飄々とした、ルールに縛られない寮のあり方が面白そうだと感じたからだ。"


show viv_m_03_2 at center
with dis
hide per_m_01_6

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_r0037
Vivaldi "「わらわの寮が選ばれなかったのは残念だが……。\n
いつでも遊びにおいで、なんだったら越してきても構わないのだからね」"

hide viv_m_03_2
show viv_m_03_2 at left
with dis

show ace_m_01_10 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_r0024
Ace "「帽子屋寮で命の危機を感じたら、いつでもこっちにおいでよ。\n
君なら大歓迎だからさ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（……命の危機？）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「命って……」"

play sound se_0052
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースに尋ねようとすると、間にペーターが割り込んでくる。"

hide viv_m_03_2

hide ace_m_01_10
show ace_m_01_10 at left
with dis

show per_m_01_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_r0067
Peter "「僕は納得いきません……！\n
どうして僕のいる赤薔薇寮でなく、よりによって帽子屋寮なんですか……！！」"

jump gakuen_dormitory_castle_not3
label gakuen_dormitory_castle_amuse2:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「ええ、遊園地寮よ。\n
遊園地寮に決めたの」"

hide per_m_01_4
show per_m_01_5 at center
with dis


with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
Peter "「！！！」"

hide per_m_01_5
show per_m_01_5 at left
with dis
hide ace_m_01_10
show ace_m_03_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
Ace "「！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の言葉に、ぎゃんぎゃんと言い争っていたペーターとエースが反応する。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "正確には言い争う、というよりも、エースがペーターをおちょくって遊んでいた、に近いような気もしないでもない。"

hide per_m_01_5

hide ace_m_03_9

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターがそれこそウサギのように、ぴょんと跳ねて一息に私へと距離を詰めてきた。"


show per_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_r0066
Peter "「酷い……！！酷いですよ、[firstname]！！！\n
どうしてあんなところに行ってしまうんですか！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「どうしてって……。\n
知り合いが多かったから、かしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（酷いとか言われても……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "誰がいるか分からないところよりも、クラスメイトや担任がいると分かっている遊園地寮のほうが安心できたからだ。"


show viv_m_03_2 at center
with dis
hide per_m_01_6

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_r0037
Vivaldi "「わらわの寮が選ばれなかったのは残念だが……。\n
いつでも遊びにおいで、なんだったら越してきても構わないのだからね」"

hide viv_m_03_2
show viv_m_03_2 at left
with dis

show ace_m_01_10 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_r0026
Ace "「遊園地寮の騒音に耐えられなくなったら、いつでもこっちにおいでよ。\n
君なら大歓迎だからさ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（……騒音？）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「騒音って……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エースに尋ねようとすると、間にペーターが割り込んでくる。"

hide viv_m_03_2

hide ace_m_01_10
show ace_m_01_10 at left
with dis

show per_m_01_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_r0069
Peter "「僕は納得いきません……！\n
どうして僕のいる赤薔薇寮でなく、よりによって遊園地寮なんですか……！！」"

jump gakuen_dormitory_castle_not3
label gakuen_dormitory_castle_tower2:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「ええ、塔よ。\n
塔に決めたの」"

hide per_m_01_4
show per_m_01_5 at center
with dis


with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
Peter "「！！！」"

hide per_m_01_5
show per_m_01_5 at left
with dis
hide ace_m_01_10
show ace_m_03_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
Ace "「！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の言葉に、ぎゃんぎゃんと言い争っていたペーターとエースが反応する。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "正確には言い争う、というよりも、エースがペーターをおちょくって遊んでいた、に近いような気もしないでもない。"

hide per_m_01_5

hide ace_m_03_9

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターがそれこそウサギのように、ぴょんと跳ねて一息に私へと距離を詰めてきた。"


show per_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_r0066
Peter "「酷い……！！酷いですよ、[firstname]！！！\n
どうしてあんなところに行ってしまうんですか！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「どうしてって……。\n
特に理由はないんだけど」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（酷いとか言われても……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうしても塔でなくてはいけない、というような理由はない。\n
ただ、真面目に学生生活を送るのならば、一番適していると感じた。"


show viv_m_03_2 at center
with dis
hide per_m_01_6

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_r0037
Vivaldi "「わらわの寮が選ばれなかったのは残念だが……。\n
いつでも遊びにおいで、なんだったら越してきても構わないのだからね」"

hide viv_m_03_2
show viv_m_03_2 at left
with dis

show ace_m_01_10 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_r0027
Ace "「塔なら俺もよく遊びに行くんだ！\n
あっちで会っても、仲良くしてくれよな！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（……よく遊びに行く？）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「あなた、塔の人達と親しいの……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やはり、ユリウスだろうか。\n
エースに尋ねようとすると、間にペーターが割り込んでくる。"

hide viv_m_03_2

hide ace_m_01_10
show ace_m_01_10 at left
with dis

show per_m_01_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_r0070
Peter "「僕は納得いきません……！\n
どうして僕のいる赤薔薇寮でなく、よりによって塔なんですか……！！」"

jump gakuen_dormitory_castle_not3
label gakuen_dormitory_castle_not3:
hide ace_m_01_10
show ace_m_03_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_r0025
Ace "「はは。\n
彼女がここを選んでくれないのは、ペーターさんがいるからなんじゃないかな」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "{size=+20}（ご明察）{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まさしくその通りだ。\n
この人は、意外とまともなことも言う。"

hide per_m_01_4
show per_m_01_11 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_r0068
Peter "「そんなこと、あるわけないじゃないですか！！\n
僕と彼女は愛し合っているんですよ！？ねえ、[firstname]！」"

hide per_m_01_11
show per_m_01_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Peter "「……[firstname]！！？」"

play sound se_0769
hide ace_m_03_3

hide per_m_01_5

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "背中にペーターの声を聞きながら、赤薔薇寮の執務室を後にした。"

with dis
$ hi_mes()

scene bg_par15_rg_ros_day
with stripe_l_medium

scene bg_map_day
with stripe_l_long

scene bg06_sk_h_day
with dis

play music gallery_front_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "赤薔薇寮を出たところで、これから自治会員になりに行こうとしているのであろう新入生達に出会った。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が入ったときは運よくすいていて、一人で向き合うことが出来たが、どうやら混み合ってきたようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0112
Seito "「ドキドキするわね！\n
赤薔薇寮の寮長さんってどんな人なんだろう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0171
Seito "「すごい美人で、ゴージャスって聞いたわ！\n
でも、なんだかちょっと怖そう……、よね？」"

menu:
    "怖くない。":
        jump gakuen_dormitory_castle_not4a
    "怖い。":
        jump gakuen_dormitory_castle_not4b
label gakuen_dormitory_castle_not4a:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（怖くない、わよ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "美人という言葉は間違えていないし迫力もあったが、怖い人ではない……、はずだ。"

with dis
$ hi_mes()

scene bg_map_day
with stripe_l_long
if place_of_stay == "Hatter":
    jump gakuen_dormitory_hatter_hatter1
if place_of_stay == "Amuse":
    jump gakuen_dormitory_amuse_amuse1
if place_of_stay == "Tower":
    jump gakuen_dormitory_tower_tower2
label gakuen_dormitory_castle_not4b:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……確かに怖い、かも）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "悪い人達ではないのだが……。\n
赤薔薇寮からは、権力を持つ者独特の威圧感を感じた。"

with dis
$ hi_mes()

scene bg_map_day
with stripe_l_long
if place_of_stay == "Hatter":
    jump gakuen_dormitory_hatter_hatter1
if place_of_stay == "Amuse":
    jump gakuen_dormitory_amuse_amuse1
if place_of_stay == "Tower":
    jump gakuen_dormitory_tower_tower2
label gakuen_dormitory_castle_castle3:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「ええ、ここよ。\n
赤薔薇寮に決めたの」"


show m_ryou1_siro16 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
Peter "「！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
Ace "「！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の言葉に、言い争っていたペーターとエースが反応する。\n
正確には言い争う、というよりも、魔法が飛び交っていたのだが。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターがそれこそウサギのように、ぴょんと跳ねて一息に私へと距離を詰めてきた。"

hide m_ryou1_siro16
show m_ryou1_siro17 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_r0057
Peter "「ああ、[firstname]！！\n
これから毎日あなたと共に寝起きできるかと思うと、僕はどうにかなってしまいそうです……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「……{size=+20}どうにでもなっていてちょうだい{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「この寮には決めたけど、あんたと寝起きするつもりはないわよ、ペーター」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "とんでもないことだ。\n
赤薔薇寮、と名前だけ聞くと一つの寮のように思えるが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "実際にはエントランスが一緒なだけで、男女共同区域を除き女子寮と男子寮では完全に分離している。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それに、ここシンフォニアには、学生や職員の他に使用人が常駐しており、それぞれの学生寮にも専任の使用人達が住み込んでいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エントランスには常にそのうちの誰かしらがおり、それぞれの寮を自在に行き交うようなことはできないようになっているのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（いや、誰もいなくても、年頃の男女が一緒に寝起きするなんてとんでもないわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "歪んだ情報が姉の耳にでも入ったら、卒倒してしまうだろう。"

hide m_ryou1_siro17
show m_ryou1_siro18 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_r0015
Ace "「ペーターさんの戯言はともかく、君が俺と同じ赤薔薇寮を選んでくれて嬉しいよ。\n
これから、よろしくな」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_r0016
Ace "「風紀を乱すうるさいストーカー男とか、我侭かつ傲慢な先輩だとかに耐えられなくなったら、いつでも相談してくれよな！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_r0021
Vivaldi "「おまえがわらわの治める赤薔薇寮を選んでくれたことは嬉しく思うが……。\n
……エース、その我侭で傲慢な先輩というのは誰のことだ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_r0017
Ace "「やだなあ、会長ってば思い当たることでもあるんですか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_r0022
Vivaldi "「……っ。\n
ホワイト、こいつをぶち殺せ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_r0058
Peter "「いいえ会長っ、それどころではありません！\n
彼女にストーカー疑惑とはどういうことですか！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「……ちょっと待って。\n
それ、私がストーカーしている犯人みたいよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ストーカー疑惑、では私が犯人側だ。\n
というか、ストーカー扱いされているのはペーター本人なのだと教えてやったほうがいいのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_10")
T "（明らかに自分のことなのに……）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
voice pet_r0059
Peter "{size=+20}「僕以外の奴がそんなことをするなんて許せません！！！」{/size} "

hide m_ryou1_siro18
show m_ryou1_siro19 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
Vivaldi "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
Ace "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_20")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「……あんた、自覚あったの」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターの叫びに、その場にいた全員がどん引きした。\n
だが、自覚があったとは驚きだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_r0060
Peter "「何を言っているんですか、僕は問題ありません。\n
僕はあなたの恋人ですからね！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_r0061
Peter "「ストーカー行為をしても問題なし！\n
ストーカーなどではありません！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……はあ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もはや訂正する気もおきない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_r0023
Vivaldi "「おまえも大変だな……。\n
こんな頭のおかしい男につきまとわれているとは……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_r0024
Vivaldi "「わらわならとっくに首を刎ね……。\n
……いや、魔法で切り刻んでやる」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_r0062
Peter "「安心してください。\n
僕が、会長につきまとうことはありえません」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_r0025
Vivaldi "「それは結構。\n
……しかし、なんだかイラつくな、その返答も」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_r0018
Ace "「はは、君、大変だね。\n
ペーターさんと会長のお気に入りなんてさ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_r0019
Ace "「でも、安心してくれ！この俺、風紀委員がついている！\n
いつでも力になるよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「……どうも、ご親切に」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なぜだろう。\n
安心するどころか、不安になってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ace_r0020
Ace "「ん？どうしたんだ？\n
疲れたのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「ええ、まあ。\n
今日は慌しかったから」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice viv_r0026
Vivaldi "「そうか、そうか。\n
それでは、今日は早く休むがよい」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice viv_r0027
Vivaldi "「わらわがおまえのために、安全で可愛い部屋を用意してあげるからね」"

play sound se_0179
play sound se_0284
hide m_ryou1_siro19
show m_ryou1_siro20 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice tad_g0113
Maid "「……はい。\n
参りました」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ビバルディが床を杖で叩くと同時に、すっとメイドさんが部屋へと入ってきた。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice viv_r0028
Vivaldi "「この子を部屋に案内するのじゃ。\n
とっておきの部屋を用意するのだぞ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0114
Maid "「かしこまりました。\n
ご案内させていただきます」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "メイドさんが恭しく頷いて、私を促す。\n
その後について歩き出しながら、これからの学園生活を思った。"


scene bg06_sk_h_day ##instantPAY ATTENTION="true"]
hide m_ryou1_siro20

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_1")
T "（……素敵なものになりそう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "美しい女王の治める赤薔薇寮。\n
きっとそこでの生活は、華やかで楽しいものになるはずだ。"

with dis
$ hi_mes()

jump gakuen_routechoice
