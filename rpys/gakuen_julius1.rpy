
scene bg25_rr_day
with dis
label gakuen_julius1:
$ clockanim()


play music tower_t_ali
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "考えてみれば、私はまだこの塔のことをよく知らない。"


scene bg_par15_rg_tow_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "塔が学校寄りの、本来ならば教職員専用の住居施設だったということは知っているが、だからといってどんな特別な施設があるのか分からない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一応、ユリウスやナイトメアが偉いということは分かっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスが生徒の立場における責任者で、ナイトメアが教職員の代表管理者だ。\n
そして、グレイが塔で働く使用人の代表。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "錚々たる面子だ。\n
学生にとっては、こんな人達が身近にいるのは有難いことではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "塔は、各寮の中でも中心的な存在。\n
特別な施設だから、探索もしがいがある……はずだ。"


scene bg25_rr_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "堅い役職の人が多い場所だから、特に何もない可能性も高い。\n
とにかく、目的なく歩いてみることにした。"

with dis
$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME
play music corridor_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうして廊下を歩いているところで、一人の男子生徒に会った。"


show boy_c2_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kaz_g0054
Seito "「あ！\n
ねえ、君！今ちょっと時間あるかな！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（……ナンパみたいなセリフ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "街中だったならば、綺麗に無視するところだ。\n
だが、ナンパにしては、彼の表情や声は切羽詰っていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「どうしたの？\n
何か……、急いでいるみたいだけど」"

hide boy_c2_4
show boy_c2_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice kaz_g0055
Seito "「それが緊急事態でさ……！\n
俺、今、スリング教授に呼ばれているところなんだ」"

hide boy_c2_5
show boy_c2_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice kaz_g0056
Seito "「前回のテスト絡みの、どうしても外せない話で……。\n
このチャンス逃したら、単位が危うくなるぐらい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「なら、早く行ったほうがいいんじゃない？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私に説明している間も惜しいだろう。\n
そう、ばっさり切り捨てた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（再テストか、何か課題のチャンスでも貰ったのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まだ新学期も始まったばかりで、そんな大きなテストがあったというような話は聞かない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "前回のテストというのは、前年度のものなのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "世界一の魔法学校という名から抱いていた厳しいイメージと異なり、シンフォニアは生徒に多くのチャンスを与えてくれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "たとえばテストで失敗したとしても、レポートや再テストというような救済措置をとってくれることがままあるのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼にとってはまさしく、火急の用件だろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（何にしても、早く行ったほうがいいでしょうに）"

hide boy_c2_1
show boy_c2_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_10")
voice kaz_g0057
Seito "「そうなんだよ～！\n
なんだけど、ユリウス委員長に提出しないといけない書類もあってさ」"

hide boy_c2_5
show boy_c2_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_10")
voice kaz_g0058
Seito "「それで君にお願いしたいんだ！\n
これ、ユリウス委員長に渡してくれないかな！？」"

play sound se_0472
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これ、と示されたのは、茶色い封筒だ。\n
特に、扱いが難しそうな物にも見えない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いたって普通の、茶封筒。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが渡す相手に少々問題がある。\n
ユリウス＝モンレーは、この塔の生徒代表の寮長であり、風紀委員長なんていう堅物だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "会う機会も会う理由もほとんどないが、塔でたまにみかける際には常に仏頂面をしている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（き……、気が重いな……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "訪ねていったとして、間違いなく歓迎されないだろう。\n
代理なら、尚のこと。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "が、目の前の彼は時間に追われてそわそわと焦れている。"

menu:
    "代理を引き受ける。":
        jump gakuen_julius1_2a
    "断る。":
        jump gakuen_julius1_2b
label gakuen_julius1_2a:
$ lovechara_julius_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……相互扶助の精神って、大事よね）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「ユリウスに渡せばいいのね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "覚悟を決めて、引き受けることにした。"

hide boy_c2_4
show boy_c1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kaz_g0059
Seito "「ああ！\n
たぶん風紀委員会の会議室にいるか……、作業室にいると思う」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「分かったわ、渡しておいてあげる。\n
だからほら、急いだほうがいいんじゃない？」"

hide boy_c1_3
show boy_c1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice kaz_g0060
Seito "「ありがとう！！\n
感謝する！！」"

play sound se_0591
hide boy_c1_2

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は私に茶封筒を渡すと、心底助かったというように大きく手を振って、そのまま走り去っていった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それを見送ってから、私は再び探索を続ける。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どの道、医務室を目指すつもりだったのだ。"

jump gakuen_julius1_3
label gakuen_julius1_2b:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（それに……、私なんかに預けて大丈夫なものなの？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "風紀委員長であるユリウスに提出しなくてはいけない書類なのだ。\n
それなりに、扱いには気をつけないといけないものなのではないのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「悪いけど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "力になれそうにないと、そう言うつもりだった。\n
が、彼はそれよりも早く私へと茶封筒を押し付けた。"

play sound se_0472

show boy_c1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kaz_g0061
Seito "「ユリウス委員長なら、風紀委員会の会議室か作業室にいるからさ！\n
頼んだ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「え！？\n
ちょ、待ってよ、私引き受けていないわよ！？」"

hide boy_c1_3
show boy_c1_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_7")
voice kaz_g0062
Seito "「よろしくー！！」"

play sound se_0591
hide boy_c1_2

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "（えええ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのまま彼は勢いよく走り去っていってしまった。\n
私の手の中に、その茶封筒だけが残される。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_10")
T "（……もう、マイペースなんだから）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "他の寮に比べると真面目な生徒が多いのが塔の特色ではあるのだが……。\n
マイペース具合では負けていない気がする。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（私が捨てたり、放置したらどうするのかしら……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……しないって分かっているんだろうなあ。\n
根が真面目な塔の生徒同士だし……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "個性はあるものの、真面目というのが塔の特性。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まあ、もともと探索ついでに、医務室にいく予定だったのだ。\n
仕方ないから届けるとしよう。"

jump gakuen_julius1_3
label gakuen_julius1_3:
with dis
$ hi_mes()

scene bg25_rr_day with Dissolve(.8)

scene bg_par16_rs_tow_day
with stripe_l_long

play music gag1_a_wam

show nai_m_02_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
voice nig_g0242
Nightmare "「なんだ、君。\n
私に会いに来てくれたわけじゃないのか」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……え？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "医務室を訪ねて、ユリウスへの届け物を持ってきたと伝えたところ、ナイトメアは露骨に嫌そうな顔をした。"

hide nai_m_02_7
show nai_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0243
Nightmare "「私は君が、私に会いに来てくれたのかと思って喜んだのに。\n
とんだぬか喜びじゃないかっ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は拗ねたように、ぷいっとそっぽを向く。"

hide nai_m_03_2
show nai_m_02_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0244
Nightmare "「私の繊細な心は傷ついた！\n
深く、傷ついた！」"

hide nai_m_02_9
show nai_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0245
Nightmare "「だから今日はもう仕事は無理だ！\n
[firstname]、遊ぼう！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "{size=+20}「駄目人間」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "傷ついた傷ついたと主張するから、こちらも殊勝に話を聞いていたらば結論がろくでもなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "見やれば傍らで待機するグレイは、聞かなかったことにしたらしく遠い目をしている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "手間のかかる子供……、もとい上司を持つと苦労するといういい見本だ。"

hide nai_m_02_12
show nai_m_02_12 at left
with dis

show gre_m_01_13 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0057
Gray "「……ナイトメア先生。\n
彼女は、用事があって委員長を探しているんです」"

hide gre_m_01_13
show gre_m_01_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0058
Gray "「邪魔しては悪いですよ。\n
だからほら、あなたもあなたの仕事を進めてください」"

hide nai_m_02_12
show nai_m_03_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0246
Nightmare "「なんと！？\n
上司の脆くも崩れ去った繊細なハートを、おまえは放置しようというのかっ！！」"

hide gre_m_01_5
show gre_m_01_12 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0059
Gray "「はいはい、俺がボンドででも糊ででも組み立て直してさしあげます。\n
ですからほら、仕事の方を……」"

hide nai_m_03_3
show nai_m_02_6 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0247
Nightmare "「嫌だっっ！\n
おまえに直させると、違う部品が混じるか違うものに仕上がるに決まっているんだ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_7")
T "（……この二人はもう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "面白がって聞いてしまっていたが、いつまでもこの主従漫才を聞いているわけにもいかない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「ここ、ユリウスの部屋じゃなかったのね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この部屋で学生証を発行してもらったこともあり、そのイメージが強かった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "よくよく思い出してみれば、確かに執務机に座って中央を占めていたのはナイトメアだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（ここじゃないのなら、風紀委員の会議室ってどこかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すっかりここだとばかり思っていたため、違うと言われると困ってしまう。"

hide nai_m_02_6
show nai_m_02_10 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0248
Nightmare "「……うう。\n
私の存在感はそんなにも薄いのか……っ、血を吐きそうだ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「そう簡単に、人が吐血するわけないでしょう」"

hide gre_m_01_12
show gre_m_03_11 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice gra_g0060
Gray "「いや、するんだ。\n
……ナイトメア先生は吐血が大得意だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「……そんな得意技、いらなくない？」"

hide nai_m_02_10
show nai_m_01_7 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice nig_g0249
Nightmare "「私だって好きで血を吐いているわけでは……、っぐげふっ！！\n
げほっがふっ……！！」"

play sound se_0631
$ flash_color("red", .4)
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "{size=+20}「！？」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本当に血を吐いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "生吐血だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "落ち着いて見ている場合ではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「グ、グレイ！\n
医者呼んで！医者……！！」"

hide gre_m_03_11
show gre_m_02_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_4")
voice gra_g0061
Gray "「いや、[firstname]、落ち着け。\n
{size=+20}ナイトメア先生が医者だ{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "{size=+20}「使えない医者じゃなくて、使えるのを呼んで！！」{/size} "

hide nai_m_01_7
show nai_m_02_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice nig_g0250
Nightmare "「{size=+20}ぐさああああ！？{/size}\n
今、とんでもなく鋭い言葉のヤジリが私の胸を貫いたぞ！！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "吐血する病人イコール医者なんてことを言われたら、誰だってそれぐらいの反応をすると思う。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……って、血を吐いたわりには元気そうね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "顔色がよくないが、ナイトメアは元より青白い顔をしている。\n
今が、特別悪いわけではなさそうだ。"

hide gre_m_02_4
show gre_m_03_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0062
Gray "「……心配ない。\n
これは、吐血というよりも軽い喀血だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……どう違うの？」"

hide gre_m_03_9
show gre_m_01_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice gra_g0063
Gray "「吐血は消化器系の出血が逆流するものだ。喀血は呼吸器系の出血だな。今回は、喉が裂けているだけのようだから、心配ない」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_7")
T "{size=+20}（充分に心配よ？）{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイの「心配ない」の判断基準は、ちょっとばかり敷居が高いような気がする。"

hide nai_m_02_8
show nai_m_03_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0251
Nightmare "「心配してくれるのはありがたいがグレイの言う通り、私が血を吐いてもあまり気にするな。\n
すぐに収まる……」"

hide nai_m_03_5
show nai_m_03_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0252
Nightmare "「……くれぐれも、他の医者を呼んだり、病院へ連れて行こうなどとは思うなよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぐいっと口の端からたれた赤いものを、ナイトメアがハンカチで拭った。\n
気にするなと言われても気になるわけだが……、どうもこれが日常であるらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（恐るべき日常ね……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「それじゃあ、話を戻すんだけど……。\n
ユリウスのいる風紀委員の会議室ってどこなの？」"

hide nai_m_03_8
show nai_m_02_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice nig_g0253
Nightmare "「グレイ！\n
か弱き女生徒が助けを求めているぞ、案内してきてやったらどうだ！」"

hide gre_m_01_4
show gre_m_03_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice gra_g0064
Gray "「その間、あなたがここでおとなしく仕事をしていてくれるのならば、喜んでそうしますが……。\n
……逃げないと約束してくださいますか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「いや、確実に逃げるわね。\n
……簡単に、場所だけ教えてもらえる？」"

hide nai_m_02_2
show nai_m_03_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice nig_g0254
Nightmare "「な！？\n
どうして君が答えるんだ、しかもそんな力いっぱい言い切らなくても！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「うるさいわね！\n
あんた、絶対に逃げる気でしょう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まだ短い付き合いのはずなのに、なぜか断言できてしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「自力で探してみることにする」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "改めてグレイへと向き直った。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「まだ塔のこと知らないことだらけなんですもの。\n
探索するいい機会だわ」"

hide gre_m_03_7
show gre_m_02_11 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice gra_g0065
Gray "「……そうか。君は気遣いの出来るいい子だな。\n
それに比べて……、ナイトメア先生」"

hide nai_m_03_3
show nai_m_02_10 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice nig_g0255
Nightmare "「な、なんだ……！？\n
何が言いたい！？」"

hide gre_m_02_11
show gre_m_02_10 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice gra_g0066
Gray "「いいえ？……それじゃあ、今、簡単に地図を用意しよう。\n
そう難しくないはずだから、すぐに分かるよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「ありがとう、グレイ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぎゃあぎゃあと騒ぐナイトメアを尻目に、グレイは手際よく地図を作成してくれた。\n
それを片手に、私は医務室を後にした。"

hide nai_m_02_10

hide gre_m_02_10

with dis
$ hi_mes()

scene bg_par16_rs_tow_day with Dissolve(.8)

scene bg25_rr_day
with stripe_l_long

play music corridor_day_p_wam
play sound se_0397

scene bg_par19_fi with stripe_l_medlong
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイの書いてくれた地図を頼りに、まずは風紀委員会の会議室を訪ねてみた。\n
ナイトメアの医務室と違って、個人の部屋のような印象はまったくない部屋だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ただ長机が四角く配置され、それこそ会議のためだけの部屋といった形。\n
そこにはユリウスどころか、誰の姿もなかった。"

play sound se_0399

scene bg25_rr_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここではない、と、もう一つの候補である作業室へと行ってみることにした。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（……一番、得体のしれない部屋よね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "医務をするから医務室だ。\n
風紀委員会が会議をするからの、風紀委員会議室だろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もっとも、医務室が執務室を兼ねているような学校だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（それじゃあ、作業室って？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "誰が、どんな作業をする部屋だというのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかも、地図に従っているはずなのに、どんどんとひとけのないところへ入り込んでいく。"


play music secret_day_p_wam

scene bg_par23_jr_k with stripe_l_medlong
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "廊下も細く、暗くなっていき……。\n
最終的に辿り着いたのは、塔の最奥なのではないかというような部屋だった。"

play sound se_0217
pause 1
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ノックをして、しばらく待つ。\n
返事はない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここにもユリウスはいないのだろうか。\n
医務室でも、会議室でも、そしてここでもないとなると、他にユリウスのいそうな場所に心当たりはない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もう、茶封筒をドアの隙間から中に放り込んで、帰ってしまいたい。\n
だが、一度預かってしまったからには責任がある。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_12")
T "（うう、これだから預かりものって苦手……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一旦は部屋に戻るか何かして、後でもう一度出直してくるしかないだろうか。"

play sound se_0301 volume .15
pause .5
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「……？？？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今、何か、聞こえたような気がした。\n
耳を澄ます。"

play sound se_0301 volume .25
pause .5
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんだろう。\n
小さくだが、部屋の内側から音が聞こえる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……ユリウス？\n
中にいるの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今度はノックをするのではなく、声をかけてみる。\n
耳を澄ます。"

play sound se_0301 volume .35
pause .5
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「？？？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やはり留守なのだろうか。\n
試しに、ドアのノブへと手をかけてみる。"

play sound se_0274
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "留守ならば鍵がかかっているだろうと思っていたドアノブが、最後まで普通に回ってしまったことに驚く。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……？？？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "居留守を使いたいのかと思ったが、それなら鍵はかけるはず。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（入って……いいのかな？）"

play sound se_0713
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "許可なく入るのは失礼だが、それでも好奇心に負けて扉をゆっくりと開けていった。"


play music tower_room2_p_ali

scene bg_par06_jr
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「ユリウス？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "部屋の主の名を呼びながら、中を覗き込む。\n
雑多なものの詰まれた部屋は、「作業室」の名に相応しかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "部屋の造りとしては、ナイトメアの医務室と似ていないこともない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、ナイトメアの執務机が見るからに高級品だったのと異なり、ここにある机は頑丈さが売りといったような素朴なものだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_4")
T "（作業机……、なんだわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その名にしみじみと納得した。\n
書類仕事をするための机というよりも、実際にその机の上で何か作業をすることを想定している部屋だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "実際机の上には、工具と、造りかけのアイテムのようなものが乗っていた。\n
だが、ユリウスの姿はない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_12")
T "「……ユリウスは、いないのかしら。\n
留守なのに鍵がかかっていないなんて、無用心だわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もしかしたら、施錠の必要がない部屋なのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こういうと失礼かもしれないが、この部屋に置いてある雑多なものはどうも、ガラクタというような印象を受ける。"

play sound se_0216
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "壊れて、日常での役目を終えてしまったもの達のようだ。\n
私は物珍しさから部屋の中へと一歩を踏み出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0117
Julius "「……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「？？？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "足元から形容詞しがたい声が聞こえたような気がした。\n
これだけ物に溢れる部屋だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何か足元に落ちていただろうか。\n
何気なく足元を確認すべく視線を落として、私は息を呑んだ。"


play music flower_day_p_wam
show m_yuri1_1 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "{size=+20}「え！？」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_7")
Julius "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そこに、ユリウス＝モンレーがいた。\n
不機嫌そうにむっつりと眉間に皺を寄せ、視線だけで子供なら泣かせられそうな渋面だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、そのサイズは全長十五センチほど。\n
先ほど部屋の外から聞こえていた小さな音は、十五センチユリウスが手にした工具でドアを叩いていた音だったらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうやら私は、完全に死角に入ってしまっていた彼を危うく踏み潰しかけたというところのようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_8")
T "（ふ、踏み潰さなくてよかった……！！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こんなことで人殺しにはなりたくない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「ユ、ユリウス？\n
どうしてそんな縮んでいるの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice jul_g0118
Julius "「……っ……、から……だ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_16")
T "「……？？？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "顰めっつらでユリウスが何か言うものの、うまく聞き取ることが出来ない。\n
身体が縮んでしまっている分、声まで小さくなってしまっているのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は彼の前に屈みこんで手を差し出した。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Julius "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ますます、ユリウスの眉間の皺が深くなる。"

hide m_yuri1_1
show m_yuri1_2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それでも私の意図は汲んでくれたのか、小さな彼はぴょんと私の手のひらの上に乗ってくれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なるべく揺らしたりしないよう、そろそろっと手を顔の高さまで持ち上げる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「もう一度聞くけど……。\n
どうして、そんなことになっているの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice jul_g0119
Julius "「双子の悪戯だ。\n
……忌々しい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今度はしっかりと聞こえたユリウスの声に、謎の感動があった。\n
こんなにも小さいのに、声は彼のものだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（本人なんだから、当たり前だけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「双子がここまでやってきたの？\n
あの子達は、塔のことを毛嫌いしているのだとばかり思っていたわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ツインズの悪戯好きは、他寮生である私の耳にも届くほどだ。\n
授業のために校舎に赴けば、所属する寮に関係なく、彼らの悪戯を見かける。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、悪戯好きなツインズと風紀委員会との関係は天敵同士といった具合だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "校内で何か問題を起こしたのか、ぎゃあぎゃあと抵抗する二人を……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "力ずくでずるずると連行していくユリウス（あるいは引き取りにきたエリオット）の姿を何度か見たことがある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いくらユリウスに悪戯を仕掛けたいからといって、あの二人がわざわざ塔までやってくるというイメージはなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0120
Julius "「……違う。ここには来ていない。\n
ああくそ、我ながら間抜けなミスを犯した」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0121
Julius "「あいつらの仕掛けた悪戯用マジックアイテムを解体している途中だったんだ。\n
……まさか、最初から私が狙いだったとは」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「……ああ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "視線を机の上へとやる。\n
私は作りかけなのだと思っていたが、あれはどうやらその逆だったらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（解体中だったのね……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "風紀委員でもある彼は、日頃から爆弾処理ならぬ悪戯処理のプロとして活躍している。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "が、今回は珍しくそんな性質を逆手にとられ、罠にハメられてしまったようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「それで、そんな小さくなってしまっていたのね。\n
魔法で解除できないの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice jul_g0122
Julius "「強制的に小さくされてしまっているせいで、魔力が思うようにコントロール出来ない」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice jul_g0123
Julius "「そうでなければ、誰が好き好んでこんな小さな身体をしていると思うんだ？\n
おまえは馬鹿か？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "見た目はミニサイズと可愛くなっても、中身は変わらなかった。\n
小さいだけに小生意気に感じられ、向けられる辛辣な言葉にむっとする。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（……ぷちっとしたい）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「それじゃあ、自分では元に戻れないのね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "危険思想を振り払うよう、話題を変える。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0124
Julius "「元に戻れないどころか、一時的にだろうが魔法を使うことすら出来ない。\n
それで困り果てているところでおまえが来たというわけだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0125
Julius "「ふん、助けが来たかと思えば踏み潰されかけるとはな。\n
おまえは注意力に欠ける」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「……あのねえ。\n
まさか、足元に十五センチサイズの人形男がいるとは思わないわよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "生命の危険を感じさせてしまったのは悪いとは思うが、それでも散々な言われようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……まあ、でも、いきなり体が縮めばパニックにもなるか。\n
気が立っているのかも）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼を落としてしまわないように気をつけながら、ゆっくりと立ち上がった。\n
そっと机の上へと下ろす。"

hide m_yuri1_2
show m_yuri1_3 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「私が、試してみましょうか」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice jul_g0126
Julius "「何をだ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「その魔法の解除よ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "懐から杖を取り出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "天才児と名高いツインズの仕掛けた魔法ともなると、私程度で歯が立つかは怪しいが……。\n
試す価値くらいはあるだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「駄目だったら、ナイトメアのところまで連れて行ってあげるわ。\n
ナイトメアなら、解除できるはずでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "仕事をしたがらないサボり魔なナイトメアだが、彼が嫌いなのは専らデスクワークだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "学校医としての実務については、しっかりとこなしているらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0127
Julius "「……ナイトメアに頼らざるを得ないのも腹立たしいな。\n
解けるまで放置しようかとも思ったが、時間ももったいない」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「そうね……。\n
どれくらいで解けるか、っていう目安があればそちらでもいいと思うんだけれど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ツインズの悪戯ともなると、どれくらいその効力が続くのかもはっきりしない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（まさか永久とは言わないだろうけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "片手に杖を構えて、ユリウスへと向かう。\n
神妙な顔で解呪を待つその姿は、ちょっと可愛い。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0128
Julius "「どうした？\n
何か問題でもあったか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「いえいえ、何でもないわ」"

hide m_yuri1_3

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "口に出してしまえば、倍返しどころか何を言われるか分かったものではない。\n
あくまで感想は心の中で呟くだけにして、杖を振った。"

play sound se_0496

show magic_y onlayer master with Dissolve(1.5)
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「…………」"

play sound se_0650
hide magic_y
show white onlayer master
with expand
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（……んん？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "妙な音が聞こえた。\n
魔法解除をしたにしては、手応えがおかしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "光が消えた後には……。"

hide white with compress
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「……{size=+20}っ！！？{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "硬直した。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "机の上には相変わらずミニチュアサイズのユリウスがいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それだけなら、やはり双子の魔法ともなると私には解呪できなかったのかと、少し悔しいながらも納得できる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、問題はその頭上だ。"


play music gag2_a_ali
show m_yuri1_4 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Julius "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「…………」"

play sound se_0058
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスの頭上には、にょきりと伸びた二本のウサギ耳がひよひよと揺れている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "凝視する私の視線に気付いたのか、ユリウスがおそるおそるといったふうに自らの頭へと触れた。"

play sound se_0058
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Julius "「……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「…………」"

play sound se_0058
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_5")
Julius "「？？？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_5")
Julius "「！？」"

play sound se_0042
hide m_yuri1_4
show m_yuri1_5 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_5")
voice jul_g0129
Julius "「……っ！？\n
ふ、ふざけた真似を……！！」"


with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_10")
T "「ま、待って！待って待って！！\n
私、普通に解呪の魔法を唱えたわよ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「あなただって、聞いていたでしょう！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな、ユリウスの頭にウサギ耳を生やすような面白い……、違った、無謀な魔法など私が使うわけがない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "後でどんな仕返しを受けるのかを、考えるだけでも恐ろしい。\n
私が唱えたのは、極々一般的な解呪の魔法だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0130
Julius "「分かっている……！！\n
ふざけているのはあの双子どもだ……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0131
Julius "「解呪の魔法に反応して効果が連鎖反応するように、魔法が仕込んであったんだ……！\n
……っ、手の込んだことを……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「解呪魔法に反応って……、そんな」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "確かに条件つきで魔法が発動するように仕込むこと自体は、そんなに難しいものではない。たとえば、マジックアイテムなどがそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "使い手がある一定の行動を満たすと、それに反応して効果が起こるようになるのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、解呪の魔法に反応して、新しい呪いを発動させるなんていうのは想定外だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "解呪というのは、呪いを解くからこその解呪と呼ばれる魔法なのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それを利用して、呪いを解くどころか追加効果を仕込むなんて、かなり難易度が高い技。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "双子達の魔法使いとしての才能を見せ付けられた気分だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、やたらめったら高度なだけに……、馬鹿馬鹿しい効果。"


play music tower_room2_p_ali
hide m_yuri1_5
show m_yuri1_6 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_4")
T "「……ごめんなさい。\n
仕込んだのは双子だけれど、実行しちゃったのは私だわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "申し訳なさがこみ上げる。\n
ミニチュアサイズにされたあげくにウサ耳だなんて、可愛すぎる……、ではなくて酷すぎる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "日頃からエリオットというウサギさんモドキを見慣れている双子ならではの、嫌がらせだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（それにしても……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターとも、エリオットとも色の違う、真っ黒の艶々したウサギ耳……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_9")
T "（さ、触りたい……っ！！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "申し訳ないと謝りたい気持ちも本当なのだが、その反面とてもときめく。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "小さなミニチュアサイズになっているせいだろうか。\n
いつもと変わらぬ鉄面皮ながら、威圧感も感じずにすむ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0132
Julius "「おまえのせいではないだろう。\n
私だって、気付くことが出来なかった」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「……ナイトメアのところまで、連れて行きましょうか」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "責任を感じて申し出る。\n
これだけ小さな身体で、しかも魔法が使えないともなれば不便きわまりないだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "さっさと解呪してもらったほうがいい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（ナイトメアなら……、大丈夫よね？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "専門の学校医ならば、私のように双子の引っ掛け魔法を発動させてしまったりというようなうっかりミスはしないだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、机の上のミニチュアユリウスは、沈欝な表情で首を横に振った。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0133
Julius "「嫌だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "きっぱりと、断られる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「……なんでよ。\n
早くこんな呪い、解いてしまったほうがいいでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice jul_g0134
Julius "「おまえは馬鹿か。\n
こんな姿をあいつらに見せたら、何を言われることか」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……確かに）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "十五センチサイズのミニチュア、さらにウサギ耳付きなんて格好のネタだ。\n
グレイはともかくナイトメアは、確実にいじりにくるだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（何を言われるか、じゃなくて……、どれくらい笑われるか、の問題よね）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「それじゃあ、どうするの？\n
このままっていうわけにもいかないでしょう」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice jul_g0135
Julius "「…………。\n
……効果がきれるまで、ここにいる」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice jul_g0136
Julius "「おそらく効果は数時間だ。\n
夕暮れまでには、なんとかなるだろう」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_10")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私には、きれるまでの長さなど見当もつかない。\n
だが、彼がそう言うからには、根拠があるのだろう。"

menu:
    "付き合うわ。":
        jump gakuen_julius1_4a
    "頑張ってね。":
        jump gakuen_julius1_4b
label gakuen_julius1_4a:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「付き合うわ。\n
一人じゃ退屈でしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice jul_g0137
Julius "「いや、別に」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "返事は即答だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それでも、あまり拒絶されたというふうに感じないのは、彼が誰に対してもそういう人だと知っているからだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もともと偏屈な男と名高い彼だ。\n
一人を好むとも聞く。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（帰ったほうがいいのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いても邪魔なだけならば、帰ったほうが彼にとってもいいだろう。"

jump gakuen_julius1_5
label gakuen_julius1_4b:
$ lovechara_julius_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「それじゃあ、私は行くけど。\n
……頑張ってね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "さらっと、薄情にも聞こえるかもしれないことを口にした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "相手が彼でなければ、元に戻るまで話し相手になるなんて選択肢もあったかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、相手は偏屈な男だ人嫌いだと名高いユリウス＝モンレーだ。\n
一人にしてやったほうが、よほど思いやりがあるような……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（うん、とっとと退散したほうがいい）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_1")
voice jul_g0138
Julius "「……ああ。\n
幸運を祈っていてくれ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そういう彼の声にも、どこかほっとしたような色が滲んでいるようだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（本当に、人が苦手なのね）"

jump gakuen_julius1_5
label gakuen_julius1_5:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……、っと）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "帰ろうとして、当初の目的を思い出した。\n
うっかり片手に抱えたまま、そのまま帰ろうとしていた。"

play sound se_0472
hide m_yuri1_6
show m_yuri1_7 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_14")
T "「そうそう、私、あなたに渡す物があって来たのよ。\n
これ、後で確認しておいて貰える？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "茶封筒を、彼の作業机の上に置く。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0139
Julius "「……書類、か？\n
おまえが私に？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「私からじゃないの。\n
廊下であった男の子に、予定がブッキングしたから届けてほしいって頼まれたのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice jul_g0140
Julius "「ああ。\n
男子生徒から、といえば……、あの件か」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "心当たりがあったのか、ユリウスは頷いた。"

hide m_yuri1_7

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（これでよし、と）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "頼まれた用事は、無事に達成することが出来た。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_8")
T "「それじゃあ、私は帰るわ。\n
……早く、元に戻るといいわね」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_8")
voice jul_g0141
Julius "「……ああ、本当にな。\n
忌々しい双子どもめ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今度こそ帰ろうと扉に向かった私の背に、呪詛めいた声が届く。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "小さいながら迫力がある。\n
元のサイズに戻ったら、さぞや怖いだろう（双子が怖がるかどうかは別として）。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（でも、今は……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼にとっては深刻な大問題だと分かっていても、つい口元に笑いが浮かんでしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あのユリウスが、十五センチサイズで、ウサギ耳を生やしているのだ。\n
これが笑わずにいられようか。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_9")
T "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_8")
T "（声に出して笑っちゃう前に逃げなきゃ……っ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "慌てて、ドアに手をかけた。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0142
Julius "「……おい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「な……、なあに？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "少しだけ声が震えた。\n
ふきだしかけているのが、ばれてしまったのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今振り返ったら、確実にふきだしてしまう。\n
固まった。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0143
Julius "「今はこのなりなので、何もしてやれないが……。\n
そのうちにまた、ここに寄るといい」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0144
Julius "「今日の礼に、美味い珈琲を淹れてやる」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "驚きすぎて笑いが引っ込んだ。\n
人嫌い、偏屈、と名高い風紀委員長に、そんな誘いを受けるなんて。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その驚きによる間を、彼は私が躊躇っていると勘違いしたらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0145
Julius "「……ふん。\n
嫌なら、無理にとは言わん」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「嫌だなんて、そんなこと。\n
あなたが誘ってくれるなんて、意外だったから驚いたの」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_1")
T "「喜んで、訪ねさせてもらうわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_1")
voice jul_g0146
Julius "「……ああ。\n
それじゃあな」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そっけない彼の声が、どこか照れているように聞こえたのは私の気のせいだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（もしかして、人嫌いってわけでもないのかしら。\n
……偏屈なだけで）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_6")
T "（……まあ、偏屈なのは確かよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなことを思いながら、作業室を後にした。"

play sound se_0199
with dis
$ hi_mes()

scene bg_par23_jr_k
with stripe_l_medium

scene bg_par15_rg_tow_day
with stripe_l_medium

scene bg_map_day
with stripe_l_long
##endmemory
$ routechara = "Julius"
jump gakuen_friend_check_tower
