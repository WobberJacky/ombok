label gakuen_common_classroom:
play sound se_0497

play music classroom_day_p_wam

scene bg01_cr_day
with stripe_l_long
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ホームルームが終わった後。\n
クラスメイトがそれぞれの授業に移動する前に、聞いてみた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「ねえ。\n
今日何か……、いえ、今日というか、そのうち何かイベントでもあるの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「なんだか、皆ざわざわしているみたいなんだけど」"


show bor_m_02_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice bor_g0298
Boris "「そりゃあそうだろ、だって……。\n
あ！あんた、そういえば新入生だっけ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_13")
T "「忘れないでよ」"

hide bor_m_02_7
show bor_m_02_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_13")
voice bor_g0299
Boris "「あははは、ごめんごめん。\n
だって、あんた、すっかり馴染んじゃってるからさあ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_7")
T "「それは……、どうも」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "馴染めていると言われれば、悪い気はしない。"

if routechara == "Ace":
    jump gakuen_classroom_ace
jump gakuen_classroom_2
label gakuen_classroom_ace:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "魚釣りを妨害された後も、ボリスは私への態度を変えないでくれている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最近エースと行動することが多いが、風紀委員の仲間というふうには見られていないようだ。"

label gakuen_classroom_2:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「で？\n
何かあるのね？」"

hide bor_m_02_6
show bor_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice bor_g0300
Boris "「ある、と言っちゃああるんだけど……。\n
新入生はその時までのお楽しみ、なんだよね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「ええ？」"

hide bor_m_01_10
show bor_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice bor_g0301
Boris "「だから、内緒」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「教えてよ！\n
ネタバレとか、気にしないから！」"

hide bor_m_03_10
show bor_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice bor_g0302
Boris "「駄目駄目。ルールだからさ。\n
ルールは、基本的には守らなきゃ。……だろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_2")
T "（……むう）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_16")
T "（校則違反くらい平気でしちゃいそうなのに……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「いいわよ。\n
教えてくれないなら、他をあたるわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "というわけで、他のクラスメイトにも聞いてみる。"


show boy_a2_4 at center
with dis
hide bor_m_03_4

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0000
Seito "「え？\n
今日が何の日かって？」"

hide boy_a2_4
show boy_a2_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0001
Seito "「そりゃあ、もちろん……」"

hide boy_a2_8
show boy_a2_8 at left
with dis

show girl_a1_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0000
Seito "「あ！こらこら、駄目よ？\n
彼女は新入生なんだから」"

hide boy_a2_8
show boy_a2_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0002
Seito "「あー……、それじゃあ言えないなあ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（むむ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "皆、反応はボリスと一緒だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_10")
T "（こうまで隠されると……、知りたくなっちゃうじゃない）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ピアスなら何とかなるんじゃないかとも思ったのだが……。"


show pia_m_03_1 at center
with dis
hide boy_a2_5

hide girl_a1_7

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0104
Pierce "「あれ？あれあれ？\n
[firstname]、君は知らないの？」"

hide pia_m_03_1
show pia_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0105
Pierce "「一人だけ知らないなんて可哀想だよね！\n
俺が教えてあげるよ！今日はね、ス……」"

hide pia_m_01_6
show pia_m_01_6 at left
with dis

show bor_m_01_12 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0303
Boris "「ピ～ア～ス～？」"

hide pia_m_01_6
show pia_m_02_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0106
Pierce "「ぴ！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "という具合で、ピアスが口を滑らせる前にボリスによって妨害されてしまい、聞き出すまでには至らなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "とりあえず、そんな周囲の反応からすると、何かあることだけは確実なようだ。"

hide bor_m_01_12
show bor_m_03_6 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0304
Boris "「[firstname]、駄目だぜ？\n
ルールを守って、いい子にしてなよ」"

hide bor_m_03_6
show bor_m_01_10 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0305
Boris "「今は、知らないほうが楽しいって。\n
本気で調べりゃ分かっちゃうけど、サプライズのほうが面白いからさ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（……まあ、悪いことでもなさそうだし、むきになって探り出すこともないか）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……分かったわ。\n
おとなしくしている」"

hide bor_m_01_10
show bor_m_02_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice bor_g0306
Boris "「うん、いい子」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "猫に誉められ、不思議な気分。"

with dis
$ hi_mes()
hide pia_m_02_5

hide bor_m_02_4
##[chara1 PAY ATTENTION="false"]
if routechara == "Vivaldi":
    jump gakuen_vivaldi3_3
if routechara == "Peter":
    jump gakuen_peter3_3
if routechara == "Ace":
    jump gakuen_ace3_7
if routechara == "Blood":
    jump gakuen_blood2_3
if routechara == "Elliot":
    jump gakuen_elliot3_5
if routechara == "Deedam":
    jump gakuen_dad3_3
if routechara == "Gowland":
    jump gakuen_gowland3_3
if routechara == "Pierce":
    jump gakuen_pierce3_3
if routechara == "Nightmare":
    jump gakuen_nightmare3_5
if routechara == "Joker":
    jump gakuen_joker3_3
if routechara == "Boris":
    jump gakuen_boris3_3
if routechara == "Gray":
    jump gakuen_gray3_4
if routechara == "Julius":
    jump gakuen_julius3_3
