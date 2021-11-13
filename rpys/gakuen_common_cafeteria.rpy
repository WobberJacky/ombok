label gakuen_cafeteria_notjoker:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "懐かしくも苦い夢の記憶を洗い流すように、顔を洗い、制服に着替える。\n
身だしなみを整えてから、カフェテリアへと移動した。"

with dis
$ hi_mes()
pause 1
play sound se_0774

play music corridor_day_p_wam

scene bg25_rr_day
with stripe_l_long
play sound se_0498
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（……ん？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そこに向かう間に気付いた。\n
なんだか、空気がざわざわとしている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "音、という意味だけでない。\n
寮内ですれ違う生徒が皆、そわそわしているような気がする。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "よくよく見れば、そんなふうに浮ついた空気を漂わせているのは生徒だけでもないようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "窓から見た先、何故か庭でバットを素振りする使用人の姿が見えた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_11")
T "（？？？）"

if routechara == "Vivaldi":
    jump gakuen_cafeteria_vivaldi_ace
if routechara == "Peter":
    jump gakuen_cafeteria_peter
if routechara == "Ace":
    jump gakuen_cafeteria_vivaldi_ace
if routechara == "Deedam":
    jump gakuen_cafeteria_notcastle
if routechara == "Blood":
    jump gakuen_cafeteria_notcastle
if routechara == "Boris":
    jump gakuen_cafeteria_notcastle
if routechara == "Elliot":
    jump gakuen_cafeteria_notcastle
if routechara == "Gowland":
    jump gakuen_cafeteria_notcastle
if routechara == "Gray":
    jump gakuen_cafeteria_notcastle
if routechara == "Joker":
    jump gakuen_cafeteria_notcastle
if routechara == "Julius":
    jump gakuen_cafeteria_notcastle
if routechara == "Nightmare":
    jump gakuen_cafeteria_notcastle
if routechara == "Pierce":
    jump gakuen_cafeteria_notcastle

label gakuen_cafeteria_vivaldi_ace:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何かスポーツ大会がある、というような話は担任であるゴーランドからも聞いていないし、周囲で話題になったこともない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そもそも、使用人がそれに備える理由が分からない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（クラスメイトか、ゴーランドにでも聞いてみよう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "分からないなら、聞けばいい。\n
幸いにして、手紙の押し付けが出来なかった私にも、夢の気持ちの切り替えくらいは出来そうだ。"


with dis
$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME
play sound se_0617
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "{size=+20}「げ」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "カフェテリアの前までやってきて、そこにいる人物を確認するや否やそんな声が出た。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_12")
T "（朝から血圧の上がりそうな相手が……）"

jump gakuen_cafeteria_castle
label gakuen_cafeteria_peter:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何かスポーツ大会がある、というような話は担任であるゴーランドからも聞いていないし、周囲で話題になったこともない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そもそも、使用人がそれに備える理由が分からない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（クラスメイトか、ゴーランドにでも聞いてみよう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "分からないなら、聞けばいい。\n
幸いにして、手紙の押し付けが出来なかった私にも、夢の気持ちの切り替えくらいは出来そうだ。"


with dis
$ hi_mes()
$ time_effect()##PLEASE MANUALLY ADJUST ME
play sound se_0617
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "{size=+20}「げ」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "カフェテリアの前までやってきて、そこにいる人物を確認するや否やそんな声が出た。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（あんな夢を見た直後で……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうにも、気まずい。"

jump gakuen_cafeteria_castle
label gakuen_cafeteria_notcastle:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_17")
T "（魔法学校で、バットって……。\n
いよいよ、何学校だか分からなくなってくるな……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何かスポーツ大会がある、というような話は担任であるゴーランドからも聞いていないし、周囲で話題になったこともない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そもそも、使用人がそれに備える理由が分からない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（クラスメイトか、ゴーランドにでも聞いてみよう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "分からないなら、聞けばいい。\n
幸いにして、手紙の押し付けが出来なかった私にも、夢の気持ちの切り替えくらいは出来そうだ。"


with dis
$ hi_mes()
$ time_effect()##PLEASE MANUALLY ADJUST ME
play sound se_0617
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "{size=+20}「げ」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "カフェテリアの前までやってきて、そこにいる人物を確認するや否やそんな声が出た。"

if place_of_stay == "Hatter":
    jump gakuen_cafeteria_hatter
if place_of_stay == "Amuse":
    jump gakuen_cafeteria_amuse
if place_of_stay == "Tower":
    jump gakuen_cafeteria_tower
label gakuen_cafeteria_castle:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのまま、回れ右。\n
回避しようと思ったものの、あっさりと発見されてしまった。"


show per_m_01_2 at center
with dis
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Peter "「[firstname]！！！」"

hide per_m_01_2
show per_m_02_13 at center
with dis
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0108
Peter "「ああ、いい朝ですね！！\n
あなたがいると、ますます光り輝くようです！！」"

hide per_m_02_13
show per_m_03_11 at center
with dis
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0109
Peter "「ふふ、見てください！！！\n
庭の赤薔薇も僕達を祝福するように咲き誇っていますよ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_14")
T "{size=+20}（錯覚よ）{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここの庭の薔薇が綺麗なのは元々だし、いつもよりも輝いて見えるとすれば、目の錯覚。"

hide per_m_03_11
show per_m_02_12 at center
with dis
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0110
Peter "「さあ、[firstname]、朝食にしましょう！\n
一日は朝食の質で決まるとも言いますからね！！」"

hide per_m_02_12
show per_m_02_5 at center
with dis
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0111
Peter "「僕と一緒に素敵な朝食をとって、今日も素敵な一日を送りましょう！！」"

hide per_m_02_5
show per_m_01_2 at center
with dis
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0111_5
Peter "「ああ、もちろんあなたに会えただけで、僕の一日は最高に素敵になることが決定していますけどっ！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターは高らかに歓喜の声をあげている。\n
もう何度か見た光景だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「そ、そう……。\n
毎日、素敵に過ごせていいわね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここは赤薔薇寮のカフェテリアで、そしてペーターは副寮長。\n
彼がここにいること自体は何の問題もない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それでもさすがに、こうも度々待ち構えられていると頭が痛くなる。\n
これでもマシになったほうなのだが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "入学当初は、毎日のようにカフェテリアの前で待ち構えていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "毎日来るようならばもう一緒にご飯は食べない、と半ば脅しつけるように説得し、毎朝の襲撃は避けたのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おかげで今では、何日に一回といった割合で顔を出してくる程度ですんでいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……それでも、結構な回数なんだけど）"

hide per_m_01_2
show per_m_01_10 at center
with dis
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice pet_g0112
Peter "「ええ！あなたのおかげですよ、[firstname]！\n
あなたとの食事が僕の人生の糧となっているのです！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_9")
T "「そう……」"

hide per_m_01_10
show per_m_02_5 at center
with dis
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_9")
voice pet_g0113
Peter "「席も確保してあるんですよ！！\n
あなたのために！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "（朝からテンション高いなあ……）"

hide per_m_02_5
##[chara1 PAY ATTENTION="false"]
with dis
$ hi_mes()

scene bg25_rr_day with Dissolve(.8)

play music dining_day_p_wam

scene bg_par02_ct_ros_day
with stripe_l_long
play sound se_0617
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "てきぱきと案内されて、カフェテリア内へと足を踏み入れる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最初のうちは、副寮長が新入生にべったりということで注目されていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、最近は私達が幼馴染であるという事情も知れたのか、少しずつそういった好奇の視線も落ち着いてきている。"

play sound se_0213
##[rchara1 PAY ATTENTION="false"]
show per_m_02_1 at center
with dis
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0114
Peter "「はい、あなた、朝はオレンジジュースですよね！\n
ふふ、こうしてあなたと一緒に朝食をとることが出来るなんて夢のようです！！」"

hide per_m_02_1
show per_m_03_4 at center
with dis
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0115
Peter "「あなたが僕と同じ赤薔薇寮に来てくれて、本当によかったです！\n
やっぱり運命なんでしょうかっ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（いや、運命とかじゃなくて、私が自主的に選んだからなんだけど……。\n
……言ったら余計に調子に乗りそうだからやめておこう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "夢みるようにうっとりとした表情で、楽しげに。\n
ペーターは、甲斐甲斐しく私のために朝食を用意してくれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "用意といっても魔法で呼び出すだけなので、別にペーターにしてもらう必要はない。ただ、それで彼が満足するならばさせておこうと思うだけだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（そうしないと、有り余ったエネルギーで何をし出すことか……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "幼馴染というだけあって彼は私の習慣や好みをしっかりと把握している。\n
世話を焼かれるのにも、もう慣れた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こんな学校生活が癖になるのは嫌だなと思いつつ、赤薔薇寮での朝はペーターとの朝食から始まることが多い。"

hide per_m_03_4
##[chara1 PAY ATTENTION="false"]
with dis
$ hi_mes()

scene bg_par02_ct_ros_day with Dissolve(.8)

scene bg_par15_rg_ros_day
with stripe_l_medium

scene bg_map_day
with stripe_l_medium
jump gakuen_common_classroom
label gakuen_cafeteria_hatter:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのまま、回れ右。\n
回避しようと思ったものの、あっさりと発見されてしまった。"

##[rchara1 PAY ATTENTION="false"]
show per_m_01_2 at center
with dis
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Peter "「[firstname]！！！」"

hide per_m_01_2
show per_m_02_13 at center
with dis
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0108
Peter "「ああ、いい朝ですね！！\n
あなたがいると、ますます光り輝くようです！！」"

hide per_m_02_13
show per_m_03_11 at center
with dis
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0109
Peter "「ふふ、見てください！！！\n
庭の赤薔薇も僕達を祝福するように咲き誇っていますよ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "{size=+20}（錯覚よ）{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここの庭の薔薇が綺麗なのは元々だし、いつもよりも輝いて見えるとすれば、目の錯覚。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ついでに、このウサギ耳の幼馴染の存在も幻覚だったりしたならば、嬉しいのだが。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「……ペーター。\n
ここ、帽子屋寮よ？」"

hide per_m_03_11
show per_m_01_2 at center
with dis
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice pet_g0375
Peter "「ええ、知っていますとも！！\n
迷子のエース君じゃあるまいし、僕はちゃんと目的地に辿り着ける賢いウサ……、じゃなくて書記ですからね！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……そう。\n
理解しているのね、自分の立場を」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "分かっていて来たならば、ある意味そっちのほうが問題だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "抗争があるというような類で敵対しているわけではないが、自治会と帽子屋寮は仲がいいとは言い切れない関係にあるらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何せ自治会は生徒の管理を志しており、帽子屋寮は素行不良な者も多いとされる自由な寮だ。"

hide per_m_01_2
show per_m_02_12 at center
with dis
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0110
Peter "「さあ、[firstname]、朝食にしましょう！\n
一日は朝食の質で決まるとも言いますからね！！」"

hide per_m_02_12
show per_m_02_5 at center
with dis
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0111
Peter "「僕と一緒に素敵な朝食をとって、今日も素敵な一日を送りましょう！！」"

hide per_m_02_5
show per_m_01_2 at center
with dis
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0111_5
Peter "「ああ、もちろんあなたに会えただけで、僕の一日は最高に素敵になることが決定していますけどっ！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターは高らかに歓喜の声をあげている。\n
もう何度か見た光景だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「そ、そう……。\n
毎日、素敵に過ごせていいわね」"

hide per_m_01_2
show per_m_01_10 at center
with dis
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice pet_g0112
Peter "「ええ！あなたのおかげですよ、[firstname]！\n
あなたとの食事が僕の人生の糧となっているのです！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_9")
T "「そう……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一応確認してみたところ、寮でも男女共同区域にあたる場所においては、他寮生の利用も認められているのだそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だから、ペーターが帽子屋寮のカフェテリアを利用することは、校則的には違反していない。\n
校則的には違反していないが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（赤薔薇寮の副寮長が、帽子屋寮で朝食なんていいのかしら……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "禁止されていなくとも、例のないことではないのだろうか。\n
目立っているし、面白くなさそうな者もいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（……ま、大体が無関心だけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "さすが、自由な寮というだけあって、そのあたりは寛大だ。"

hide per_m_01_10
show per_m_02_5 at center
with dis
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0113
Peter "「席も確保してあるんですよ！！\n
あなたのために！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「どうも……」"

hide per_m_02_5
##[chara1 PAY ATTENTION="false"]
with dis
$ hi_mes()

scene bg25_rr_day with Dissolve(.8)

play music dining_day_p_wam

scene bg_par02_ct_hat_day
with stripe_l_long
play sound se_0617
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "手を引かれ、カフェテリア内へと足を踏み入れる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（あら？\n
あそこにいるのは……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "{size=+20}「え！？」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "驚愕の声をあげてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "帽子屋寮のカフェテリアにペーターがいることよりも、驚きだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あの極端に朝を嫌うというブラッドが、健康的なこの時間にカフェテリアにいるなんて。"


show m_kyoutuu_bousi1 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0134
Blood "「……やあ、おはよう。\n
忌々しいほど、いい朝だな」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0376
Peter "「…………。\n
……どうしてあなたがここにいるんですか」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0377
Peter "「ここは僕が、彼女のためにとっておいた席です！！\n
あなたが座っていい場所じゃありませ\n
ん！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0135
Blood "「……朝から元気だな、書記殿。\n
見ているだけでだるくなるほど、健康的で実にいい……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0136
Blood "「……ここは私の寮だ。\n
私がどこに座ろうと、誰かに指図されるいわれはない」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "気だるげにだるだるとしながらも、ペーターに向かってちらりと投げかけられるブラッドの視線は鋭い。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_17")
T "（……機嫌は悪そう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのことに、むしろ安心する。\n
爽やかに朝を過ごすブラッドなど、別人だ。"

hide m_kyoutuu_bousi1
show m_kyoutuu_bousi2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0378
Peter "「……ああ、でも僕は心が広いので許してさしあげます。\n
ちょうど僕も、あなたに用事があったんですよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0137
Blood "「……ほう？\n
私に用件とはなんだ？」"

hide m_kyoutuu_bousi2
show m_kyoutuu_bousi3 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0379
Peter "{size=+20}「僕の、帽子屋寮への転寮を認めてください」{/size} "

play sound se_0545
play sound se_0701 volume .5
camera at hpunch
camera at vpunch
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_7")
T "{size=+20}「ぶっ！？」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_7")
voice blo_g0138
Blood "「な……？\n
なんだと？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_6")
T "「げほげほっ！\n
な、何を言っているの、ペーター！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "むせた。\n
赤薔薇寮の副寮長が、帽子屋寮に転寮希望というのはどういうことだ。"

play sound se_0498
play sound se_0617
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kaz_g0007
Seito "「は……？\n
誰がどこに移るって？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0017
Seito "「転寮……？\n
まさか……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0133
Seito "「ええ？\n
自治会の書記が……！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kaz_g0008
Seito "「冗談だろう？\n
何を企んでいるんだか……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "特に声を抑えるということをしていないせいか、ペーターの声はしっかりとカフェテリア内に響き渡り、波紋を呼んでいる。"

hide m_kyoutuu_bousi3
show m_kyoutuu_bousi4 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0139
Blood "{size=+20}「……断固断る」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "当然の判断だ。\n
寮長として、賢明な判断。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……大分、私情も含まれていそうだが。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "{size=+20}「支持するわ」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice pet_g0380
Peter "「何故ですか！！？\n
彼女が赤薔薇寮に来てくれないのなら、僕が帽子屋寮に移動するのが道理というものじゃありませんか！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_13")
T "「そんな道理、知らないわよ！！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_13")
voice blo_g0140
Blood "「……はあ。\n
では、私のほうからの用件に入らせてもらおう」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_13")
voice pet_g0381
Peter "「何です？\n
あなたも僕に用事があるんですか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_13")
voice blo_g0141
Blood "「そうでなければ、誰がこんな時間に……。\n
ああ、時間というのは煩わしいものだ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_13")
voice blo_g0142
Blood "「朝っぱらから余所の寮に攻め込んでくるのはやめてくれ。\n
迷惑だから帰れ。\n
二度と来るな。……以上」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドの要求は簡潔だった。\n
それ以降はペーターのことを無視するようにして、眠たげに紅茶のカップを傾けている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が帽子屋寮にきて、結構な頻度で押しかけてくるペーターに対しての苦情が高まった結果の行動……、なのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（……いや、大分、私情が入っているわよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何度か居合わせたが、ブラッドは何かとペーターに冷たい（しかし、相手には通じない）。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットから受けているオレンジ色のあれこれの仕返しを、同じウサギっぽいものに当り散らしているようにも見える。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0382
Peter "「残念でしたね、ブラッド＝デュプレ！\n
僕は赤薔薇寮の人間なので、あなたに従う理由はありません！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「……だからその赤薔薇寮の人間が、朝っぱらから帽子屋寮にいることがおかしいって言っているのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice blo_g0143
Blood "「最初から言葉が通じるとは思っていなかったが……。\n
ああ、眠い」"

hide m_kyoutuu_bousi4
show m_kyoutuu_bousi5 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「ちょ、ブラッド！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice pet_g0383
Peter "「ああああ！寄りかからないでください！\n
彼女にばい菌がつきます！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice blo_g0144
Blood "「なんだ。\n
ばい菌とやらに負けるくらいに儚いものなのか、君の愛とやらは」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice pet_g0384
Peter "「まさか！\n
それくらいで怯んだりするほど、僕の愛は浅くありません！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice blo_g0145
Blood "「そうか、そうか。\n
そうこなくてはな。私を退屈させないでくれ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドとしても、本気でペーターを追い出そうとはしていないようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "寮長として、あくまでペーターに対峙したという事実だけがほしかったようで、後はもう朝なのでだるいといった様子。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなわけで。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その日の朝食は、だるだるとひたすら紅茶を飲み続ける帽子屋寮の寮長と、押しかけてきた赤薔薇寮副寮長に挟まれてという嫌な事態になった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（……日常になりそうで怖い）"

with dis
$ hi_mes()
hide m_kyoutuu_bousi5




scene bg_par02_ct_hat_day with Dissolve(.8)

scene bg_par15_rg_hat_day
with stripe_l_medium

scene bg_map_day
with stripe_l_medium
jump gakuen_common_classroom
label gakuen_cafeteria_amuse:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのまま、回れ右。\n
回避しようと思ったものの、あっさりと発見されてしまった。"

##[rchara1 PAY ATTENTION="false"]
show per_m_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Peter "「[firstname]！！！」"

hide per_m_01_2
show per_m_02_13 at center
with dis
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0108
Peter "「ああ、いい朝ですね！！\n
あなたがいると、ますます光り輝くようです！！」"

hide per_m_02_13
show per_m_03_11 at center
with dis
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0385
Peter "「遊園地寮なんて騒がしいところで耐えがたきを耐え、健気に生きるあなた！\n
素敵です……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（普通に生活しているだけなんだけど……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "別に耐えていないし、健気でもない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「……ペーター。\n
ここ、遊園地寮よ？」"

hide per_m_03_11
show per_m_02_5 at center
with dis
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice pet_g0386
Peter "「ええ、知っていますとも！！\n
迷子のエース君じゃあるまいし、僕はちゃんと目的地に辿り着ける賢いウサ……、じゃなくて書記ですからね！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「……そう。\n
理解しているのね、自分の立場を」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "分かっていて来たならば、ある意味そっちのほうが問題だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "禁止されているわけではないが、他寮のカフェテリアへ押しかけて、騒ぎ立てている。"

hide per_m_02_5
show per_m_02_12 at center
with dis
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0110
Peter "「さあ、[firstname]、朝食にしましょう！\n
一日は朝食の質で決まるとも言いますからね！！」"

hide per_m_02_12
show per_m_02_5 at center
with dis
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0111
Peter "「僕と一緒に素敵な朝食をとって、今日も素敵な一日を送りましょう！！」"

hide per_m_02_5
show per_m_01_2 at center
with dis
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0111_5
Peter "「ああ、もちろんあなたに会えただけで、僕の一日は最高に素敵になることが決定していますけどっ！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターは高らかに歓喜の声をあげている。\n
もう何度か見た光景だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「そ、そう……。\n
毎日、素敵に過ごせていいわね」"

hide per_m_01_2
show per_m_01_10 at center
with dis
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice pet_g0112
Peter "「ええ！あなたのおかげですよ、[firstname]！\n
あなたとの食事が僕の人生の糧となっているのです！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_9")
T "「そう……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "寮でも男女共同区域にあたる場所においては、他寮生の利用も認められている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だから、ペーターが遊園地寮のカフェテリアを利用することは、校則的には違反していない。\n
校則的には違反していないが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（こんなに騒ぎ立てて……）"

hide per_m_01_10
show per_m_02_5 at center
with dis
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice pet_g0113
Peter "「席も確保してあるんですよ！！\n
あなたのために！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「どうも……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自寮でもないのに、完全に我が物顔だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（……誰か、叱ってくれないかなあ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が言っても聞かない。\n
すでに何度も試して分かっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（……ま、誰が言っても聞かなさそうだけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それが、先生であっても、だ。"

hide per_m_02_5
##[chara1 PAY ATTENTION="false"]
with dis
$ hi_mes()

scene bg25_rr_day  with Dissolve(.8)

play music dining_day_p_wam

scene bg_par02_ct_amu_day
with stripe_l_long
play sound se_0617

show m_kyoutuu_yuu1 onlayer master
with dis
##[rchara1 PAY ATTENTION="false"]

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「……おはよう、ゴーランド」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice gor_g0067
Gowland "「よ、おはよーさん。\n
……あんた、よくよく動物に懐かれているな」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターによって連れて行かれた先の席。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そこで一人先に優雅にモーニングコーヒーを味わっていたのは、遊園地寮の責任者、そして担任の先生。\n
ゴーランドだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0387
Peter "「…………。\n
……どうしてあなたがここにいるんですか」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0388
Peter "「ここは僕が、彼女のためにとっておいた席です！！\n
あなたが座っていい場所じゃありません！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0068
Gowland "「細かいことは気にするなよ、ホワイト。\n
ほら、おまえも朝飯を食いにきたんだろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0069
Gowland "「早くしないと時間なくなるぜ？\n
[firstname]、あんたもほら」"

play sound se_0719
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぽんぽん、と隣の席を叩いてゴーランドが促す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は促されるままそこ、彼の隣に腰掛けようとして……、それをペーターによって阻止された。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0389
Peter "「どうしてあなたが、彼女の隣なんですかっ！！\n
図々しい！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0070
Gowland "「何を言ってんだ。\n
この子だって、自分から座ろうとしてるだろ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0390
Peter "「そんな！\n
[firstname]、あなたはここに座りたいんですか！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「そこに、と限定するつもりはないけれど……。\n
とりあえず、さっさと座って朝ごはんを食べたいわね」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
voice pet_g0391
Peter "「分かりました。\n
……背に腹はかえられません」"

play sound se_0313
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
voice pet_g0392
Peter "「これでどうですか、[firstname]！\n
さあ、席についてください！！」"

play sound se_0161
pause .1
play sound se_0161

play music gag1_a_wam
hide m_kyoutuu_yuu1
show m_kyoutuu_yuu2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「どう、って……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice gor_g0071
Gowland "「ちょっと待て！！\n
ホワイト、なんでおまえが俺の隣に座るんだ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice pet_g0393
Peter "「苦渋の決断です！！\n
彼女があなたの隣に座るのを見るよりは、僕があなたの隣に座ったほうがマシです！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice pet_g0394
Peter "「ああ、しかし、耐え難い！\n
しかし、彼女も我慢しているのだから、僕だって耐えてみせます！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice gor_g0072
Gowland "「耐えなくていい！\n
俺だって、朝からおまえの隣なんて御免だ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "（……朝から、テンション高いわね）"

hide m_kyoutuu_yuu2
show m_kyoutuu_yuu3 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は目の前でぎゃあぎゃあと言い争うゴーランドとペーターを尻目に朝食を呼び出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつもの、トースト、サラダ、そしてオレンジジュースといった定番メニューだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0073
Gowland "「……[firstname]、あんた、そんな量で足りるのか？\n
若いんだから、もっと食ったほうがいいぜ？」"

play sound se_0338
hide m_kyoutuu_yuu3
show m_kyoutuu_yuu4 onlayer master with grad_b
play sound se_0346 volume .7
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ひらり、とゴーランドが手を揺らして机の上においしそうなマフィンの入った籠を呼び出す。\n
焼きたてなのかほかほかと美味しそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（……けど、量的にきついな）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "朝からは、あまり量をこなせない性質なのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0395
Peter "「そうですよ、あなたは食が細すぎます。\n
しっかり食べて力をつけてくださいね……！」"

play sound se_0339
hide m_kyoutuu_yuu4
show m_kyoutuu_yuu5 onlayer master with grad_b
play sound se_0783
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今度はペーターがヨーグルトの器を呼び出して、ずいと私の元へと差し出してくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「ちょ……っ！\n
ペーター！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice gor_g0074
Gowland "「お、ヨーグルトはいいな。\n
健康にもいいし、朝から食べるにはばっちりだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice pet_g0396
Peter "「僕は彼女のことを誰よりも思っていますからね！\n
当然です！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice gor_g0075
Gowland "「だったらフルーツもつけるべきじゃねえか？\n
やっぱ朝は果物だろ」"

play sound se_0340
hide m_kyoutuu_yuu5
show m_kyoutuu_yuu6 onlayer master with grad_b
play sound se_0346 volume .7
play sound se_0346 volume .7
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今度はテーブルの上に、季節の果物の盛り合わせが出現する。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「えええっ？\n
ゴーランド！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice pet_g0397
Peter "「それなら動物性たんぱく質も必要ですよね？\n
ステーキなど……」"

play sound se_0341
pause 1
play sound se_0783
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「朝っぱらからそんな重いもの、食べられるわけがないでしょう！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人に悪気がないようだが、朝から食べ物攻めはきつい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……食べる前から、おなかいっぱいだわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "朝から濃すぎる面子だ。"

play sound se_0346 volume .7
pause .4
play sound se_0783
pause .4
play sound se_0346 volume .7
pause .2
play sound se_0783
pause .3
play sound se_0346 volume .7
play sound se_0346 volume .7
pause .1
play sound se_0783
play sound se_0783
with dis
$ hi_mes()
hide m_kyoutuu_yuu6


scene bg_par02_ct_amu_day with Dissolve(.8)

scene bg_par15_rg_amu_day
with stripe_l_medium

scene bg_map_day
with stripe_l_medium
jump gakuen_common_classroom
label gakuen_cafeteria_tower:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのまま、回れ右。\n
回避しようと思ったものの、あっさりと発見されてしまった。"


show per_m_01_2 at center
with dis
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Peter "「[firstname]！！！」"

hide per_m_01_2
show per_m_02_13 at center
with dis
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0108
Peter "「ああ、いい朝ですね！！\n
あなたがいると、ますます光り輝くようです！！」"

hide per_m_02_13
show per_m_03_11 at center
with dis
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0398
Peter "「塔なんて陰気臭いところで耐えがたきを耐え、健気に生きるあなた！\n
素敵です……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（普通に生活しているだけなんだけど……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "別に耐えていないし、健気でもない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「……ペーター。\n
ここ、塔よ？」"

hide per_m_03_11
show per_m_02_5 at center
with dis
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice pet_g0375
Peter "「ええ、知っていますとも！！\n
迷子のエース君じゃあるまいし、僕はちゃんと目的地に辿り着ける賢いウサ……、じゃなくて書記ですからね！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「……そう。\n
理解しているのね、自分の立場を」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "分かっていて来たならば、ある意味そっちのほうが問題だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "禁止されているわけではないが、他寮のカフェテリアへ押しかけて、騒ぎ立てている。"

hide per_m_02_5
show per_m_02_12 at center
with dis
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0110
Peter "「さあ、[firstname]、朝食にしましょう！\n
一日は朝食の質で決まるとも言いますからね！！」"

hide per_m_02_12
show per_m_02_5 at center
with dis
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0111
Peter "「僕と一緒に素敵な朝食をとって、今日も素敵な一日を送りましょう！！」"

hide per_m_02_5
show per_m_01_2 at center
with dis
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0111_5
Peter "「ああ、もちろんあなたに会えただけで、僕の一日は最高に素敵になることが決定していますけどっ！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターは高らかに歓喜の声をあげている。\n
もう何度か見た光景だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「そ、そう……。\n
毎日、素敵に過ごせていいわね」"

hide per_m_01_2
show per_m_01_10 at center
with dis
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice pet_g0112
Peter "「ええ！あなたのおかげですよ、[firstname]！\n
あなたとの食事が僕の人生の糧となっているのです！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_9")
T "「そう……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "寮でも男女共同区域にあたる場所においては、他寮生の利用も認められている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だから、ペーターが塔のカフェテリアを利用することは、校則的には違反していない。\n
校則的には違反していないが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（こんなに騒ぎ立てて……）"

hide per_m_01_10
show per_m_02_5 at center
with dis
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice pet_g0113
Peter "「席も確保してあるんですよ！！\n
あなたのために！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「どうも……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自寮でもないのに、完全に我が物顔だ。"

hide per_m_02_5
##[chara1 PAY ATTENTION="false"]
with dis
$ hi_mes()

scene bg25_rr_day with Dissolve(.8)

play music dining_day_p_wam

scene bg_par02_ct_tow_day
with stripe_l_long
play sound se_0617
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……あら？\n
あそこにいるのは……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「おはよう、ユリウス」"


show m_kyoutuu_tou1 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
Julius "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（……うわあ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスはとんでもなく不機嫌そうだ。\n
いつもの三割増し、負のオーラをまとっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もしかすると、朝はあまり強くなかったりするのだろうか。\n
いかにも低血圧そうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……そうでなくても、朝からペーターだと、テンション差で不機嫌にもなるか）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice pet_g0376
Peter "「…………。\n
……どうしてあなたがここにいるんですか」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice pet_g0377
Peter "「ここは僕が、彼女のためにとっておいた席です！！\n
あなたが座っていい場所じゃありません！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「ペーター、あんたねえ……、自分の寮でもないのに……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……ん？\n
あれ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あらかじめ、とっておいた席。\n
そう言うからには、印なり魔法なりをつけて離席したはず。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ということは、ユリウスはわざわざペーターの用意した席に座り、私達を待ち構えていたということになるのだが……。"

hide m_kyoutuu_tou1
show m_kyoutuu_tou2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0170
Julius "「……ペーター＝ホワイト。\n
貴様に人間の言葉が通じるかどうかは知らんが、一応言っておくぞ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0171
Julius "「人道的見地から鑑みても、夜討ち朝駆けはやめてくれ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0171_5
Julius "「おまえがそうやってけたたましく乱入してくるたびに、我が寮の平和な朝がぶち壊されるんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスは、腹に据えかねて朝から来てくれたようだ。もしかしなくとも、ペーターの所業に対する苦情が風紀に殺到しているのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（さもありなん）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私に会えば、所構わず騒ぎ立て。\n
今回の席取りなどは可愛いほうで、あらかじめ居る者を追い払ったり、脅したり。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "席だけでなく、色んなことに適用される。\n
周囲への被害もあるだろうし、恩恵（迷惑な）を与えられる私も困り果てている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「……ねえ、ユリウス、私からも頼みたいんだけど。\n
風紀に訴えたら、ストーカーって止められるかしら？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
voice jul_g0172
Julius "「…………。\n
……そうだな、ストーカーは止められる」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
voice jul_g0173
Julius "「だが、残念ながら、ペーター＝ホワイトは止められる気がしない」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その言いようでは、ペーターがストーカー以外の、もしくはストーカー以上の何かのようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「風紀委員なら、なんとかしてよ。\n
ユリウス、委員長でしょう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は当事者だが、もはや本人が何を言っても無駄だ。\n
権威あるところに、なんとかしてもらいたい。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0174
Julius "「動物の躾は、私の仕事の範囲外だ。\n
……調教師を呼べ、調教師を」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（……ウサギの調教？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちらりっとペーターへと視線を流す。"

hide m_kyoutuu_tou2
show m_kyoutuu_tou3 onlayer master
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
voice pet_g0399
Peter "「ああ、[firstname]、そんな熱い目で僕を……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0399_5
Peter "「あなたに虐げられるのなら、{size=+20}調教されても構わないです！！{/size}」"

play sound se_0498
hide m_kyoutuu_tou3

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "{size=+20}ざわざわざわ{/size}。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "爽やかな朝の朝食の空気が、一気に澱んだ。"


show yuri_m_02_4 at center
with dis
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Julius "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "朝はあまり食べない主義なのか、ユリウスはひたすらにコーヒーを喉に流し込んでいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本気でペーターを追い出そうとはしていないようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "風紀委員長として、あくまでペーターに対峙したという事実だけがほしかったようで、実際には諦めの境地といった様子。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……そうよね。\n
言って無駄なのは、私もよく分かっている）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私もそれに倣って、無心を追及することにした。\n
しかし、それすらも、受け入れてしまっているようで。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_7")
T "（……日常になりそうで怖い）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニアの生活にも慣れてきた、今日この頃。"

hide yuri_m_02_4
##[chara2 PAY ATTENTION="false"]

with dis
$ hi_mes()

scene bg_par02_ct_tow_day with Dissolve(.8)

scene bg_par15_rg_tow_day
with stripe_l_medium

scene bg_map_day
with stripe_l_medium
jump gakuen_common_classroom
