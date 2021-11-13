label gakuen_julius_end:
scene bg_map_day
with dis
$ clockanim()


scene bg_par15_rg_tow_day
with dis

play music morning_a_wam

scene bg25_rr_day with Dissolve(1.2)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "朝方、まだ生徒が廊下に出てくる前の時間帯にユリウスは私を女子寮まで送ってくれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "人が少ないとはいえ、まったくの無人ではない。\n
早起きの男子生徒とすれ違ったりもするのだが……。"


show boy_c1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kaz_g0071
Seito "「おはようございます、寮長」"

hide boy_c1_3
show boy_c1_3 at left
with dis

show yuri_m_01_12 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0276
Julius "「ああ、おはよう」"

hide yuri_m_01_12

hide boy_c1_3

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな挨拶が成立するだけで、誰も私へと奇異の眼差しを向けない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "男子寮に女子生徒がいて、しかも朝帰りの現行犯だというのに。\n
誰一人として、ユリウスを問いただそうとはしないのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（これが、信用度ってものか……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "皆して、ユリウスならばそうするだけの正当な理由があると信じているかのようだ。\n
咎めることなど、思いつきもしない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "男子生徒とすれ違い、充分声が届かなくなったのを確認してからぼそりと口を開いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「……どれだけ信用されているのよ」"


show yuri_m_01_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice jul_g0277
Julius "「日頃、積み重ねた実績だろう。\n
私は、融通がきかないとの噂もあるらしい、風紀委員長だからな」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（融通……、かなりきくと思うんだけどな）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "公私混同もはなはだしい。\n
少なくとも、昨夜の件では。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「……日頃の行いって大事ね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しみじみと呟いた。\n
これが彼でなければ、表立っては言われずとも、もっと好奇の目で見られていたことだろう。"

with dis
$ hi_mes()
hide yuri_m_01_7
##[chara1 PAY ATTENTION="fales"]

show white onlayer master
with check_long
pause .15
hide white
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "女子寮の入り口に到着する。\n
そこにいたメイドへと、ユリウスは簡単な説明をしてくれた。"


show maid_d_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0102
Maid "「ああ、それでしたら連絡を受けています。\n
彼女が、その女子生徒ですね」"

hide maid_d_3
show maid_d_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0103
Maid "「分かりました。\n
ここより先は、私が責任をもって送り届けます」"

hide maid_d_2
show maid_d_2 at left
##[rchara1 PAY ATTENTION="fales"]
show yuri_m_03_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0278
Julius "「ああ、よろしく頼む」"

hide maid_d_2
show maid_d_9 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0104
Maid "「はい」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "メイドも、これまたあっさりと事情を把握……、というか騙されてくれた。"

hide yuri_m_03_9
show yuri_m_03_2 at center
with dis
hide maid_d_9

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Julius "「……[firstname]」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女に連れられて、自室へと向かおうとした矢先、呼び止められる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「何？\n
どうしたの？」"

hide yuri_m_03_2
show yuri_m_02_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice jul_g0279
Julius "「や……、その、うむ。\n
体が辛いようなら今日は休め。……以上だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「……っ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぼっと火でもついたように顔が熱くなる。\n
こんなに赤くなってしまっては、メイドに不審に思われてしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_8")
T "（ま、真面目なんだろうけど……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "タチが悪い。\n
心の中で彼を罵ることで、顔の熱を散らそうとする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちらりと見やれば、それを口にした本人も微妙に顔を赤らめているようだった。\n
そんな相手の様子を見てしまうと、お互いに気恥ずかしさは増すばかり。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_7")
T "「き、気遣ってくれてありがとう。\n
部屋に帰ってから考えるわ」"

hide yuri_m_02_6
show yuri_m_02_12 at left
with dis

show maid_d_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_7")
voice tad_g0105
Maid "「無理はなさらないでくださいね。\n
欠席なさるようでしたら、こちらに連絡をしてくだされば担任への連絡は私共でいたしますので」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「……あ、ありがとうございます」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女が、疑いもなくまっとうに気遣ってくれるのが、余計に罪悪感やら羞恥心を煽る。"

hide yuri_m_02_12
show yuri_m_02_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0280
Julius "「それでは、私は戻る。\n
……おまえも、ちゃんと休めよ」"

play sound se_0584
hide maid_d_1

hide yuri_m_02_2

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それだけを最後に言うと、ユリウスは足早に男子寮のほうへと戻っていった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……ああ、そうか）"


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスはシンフォニアの学生ではない。\n
すでに単位を気にしなくていい研究者格だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それ故に、どうしても出なくてはいけないというような必修の授業はないのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうでもなければ、徹夜で研究なんてことを週に何度も繰り返せるはずがない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（私は、今日も授業があるもんね……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "具合が悪いということで休むことは出来ても、休んだ分の内容は後で自力で取り返さなくてはいけない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "気遣いは嬉しいが、少々無理をしてでも授業に出たほうがいいような気がした。"


show maid_d_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0106
Maid "「では、お部屋のほうまでお送りします」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "メイドに促されて、彼の背中を最後まで見送ることなく、私は自室へと戻った。"

with dis
$ hi_mes()
hide maid_d_3


scene bg25_rr_day with Dissolve(.8)

scene bg_par15_rg_tow_day with stripe_l_medlong

scene bg24_rj_day
with stripe_l_long

play music room1_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "部屋に戻ってシャワーを浴び、それから朝食までの少しの時間、まどろんだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "時間にして一時間もなかったとは思うのだが、それだけでも少しは体力を回復できたように思う。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（寝不足できついかなと思ったんだけど……、なんとか大丈夫そう）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「よし」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "むくりとベッドから起き上がると、制服へと着替える。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "リボンはしっかり取り返してきた。\n
それを留めれば、身支度は完成だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_7")
T "（リボン……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "姿見の前で一度身だしなみを確認するとき、また顔が赤くなってしまう。\n
気を引き締めてから、カフェテリアへと向かった。"

with dis
$ hi_mes()
play sound se_0397 ##PAY ATTENTION="false"

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
T "昨夜の連絡は女子寮を担当するメイドさんには行き渡っているのか、途中何度か呼び止められて大丈夫かと体調を確認されてしまった。"


show maid_d_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0118
Maid "「体調のほうはいかがですか？\n
もしも、まだ辛いようでしたら……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「ありがとう。\n
もう平気よ」"

hide maid_d_5

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_14")
T "（こんなに心配されるなんて……。\n
ユリウス、大袈裟に言ったわね？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一晩引き止めるのだから、それくらいに言っておかなければならなかったのだろう。\n
分かるが、いたたまれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "寝不足ではあるものの、実際に魔力酔いを起こしていたわけではないので、私はぴんぴんしている。\n
少なからず罪悪感を覚えた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……彼女達はどうかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "「彼女達」というのは、カフェテリアで親しくなり、私のブリーズを応援してくれた二人の女子生徒のことだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この時間ならば、もう来ているはず。"


play music dining_day_p_wam

scene bg_par02_ct_tow_day with stripe_l_medlong
play sound se_0617
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "昨夜のブリーズの名残か、いつも以上に賑やかなカフェテリア。\n
私はきょろきょろと彼女達を探して歩く。"


show tower_a2_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0057
Seito "「あら、おはよう、[firstname]。\n
こっちの席にいらっしゃいよ」"

hide tower_a2_3
show tower_a2_3 at left
with dis

show tower_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0080
Seito "「おはよう、[firstname]。\n
今日はあなた、お休みかと思っていたわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（いた）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女達のほうから私のことを見つけてくれた。\n
人ごみをすり抜けて、そちらへと向かう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "休みかと思っていたなんて言いつつも、しっかり私の分の席は確保しておいてくれている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ざわざわと賑やかな中、席に座れたことに安堵の息が漏れた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "少し休んで回復したとはいえ、昨日の今日でこの混雑はきついものがある。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_10")
T "「ふふ。\n
イベントを満喫して、疲れたから学校を休むなんてことしないわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "疲労のせいか、食欲はあまり感じない。\n
フルーツサラダと、ヨーグルトと、オレンジジュースにしておこう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつもより軽めの朝食を呼び出した。"

hide tower_a2_3
show tower_a2_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0058
Seito "「あなたの場合、昨日、大変だったんでしょう？\n
具合が悪いなら無理しないほうがいいわ」"


play music gag1_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……え？」"

hide tower_b1_2
show tower_b1_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice chi_g0081
Seito "「私達も聞いているわ。\n
昨夜具合の悪くなっちゃった子がいるって……、それがあなただって聞いて心配していたのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（えー……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスの信用度を、私はなめていたかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まさか私とユリウスが発展途上の関係にあると分かっていて、後押しして応援してくれていた彼女達までもが、あんな方便にあっさりと引っかかっているなんて。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（ユリウスの人徳って、すごい……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "皆して、本当に私が保護されたと信じているのだ。"

hide tower_a2_1
show tower_a1_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0059
Seito "「でも……、災い転じて福となすって言うじゃない？\n
昨夜は少しぐらい寮長と仲良くなれたの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「…………」"

hide tower_b1_5
show tower_b1_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice chi_g0082
Seito "「一晩面倒みてもらったんでしょう？\n
少しは話せたんじゃない？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "少しどころではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（話せたどころか告白までしちゃったし、それ以上の進展もあったんだけど……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "取っ掛かりでも打ち明けてしまうと、そのままなし崩し的に昨夜の諸々がすべてバレてしまう。\n
さすがにそこまで話せない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「そうね……。\n
今までよりは仲良くなれたと思うわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（……嘘ではない）"

hide tower_a1_3
show tower_a1_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_1")
voice hei_g0060
Seito "「本当にっ？\n
よかったわね、この調子で少しずつでも近付いていけるといいわね！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_10")
T "（う……）"

hide tower_b1_9
show tower_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_10")
voice chi_g0083
Seito "「これからも応援しているから！\n
何か困ったことがあったら、いつでも相談してね！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "（うう……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_2")
T "「ええ、もちろん。\n
……これからも、よろしく」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "罪悪感が募っていく。"

with dis
$ hi_mes()
hide tower_a1_2

hide tower_b1_3


scene bg_par02_ct_tow_day with Dissolve(.8)

scene bg_par15_rg_tow_day
with stripe_l_medium

scene bg_map_day
with stripe_l_medium

scene bg_par15_rg_tow_day
with stripe_l_medium

scene bg_par06_jr
with stripe_l_long
play sound se_0170

play music study_taught_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "カップルになったからといって、私とユリウスの生活が変わるわけではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "放課後は相変わらず、カフェテリアか作業室かの二択。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスの生活も似たようなもので、ひたすら塔の中でひっそりと完結している感がある。"

menu:
    "外にも出てみたい。":
        jump gakuen_julius_end2a
    "今のままで充分。":
        jump gakuen_julius_end2b
label gakuen_julius_end2a:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（付き合っているんだし……、たまには外にも出掛けてみたいわよねえ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニアの敷地は広大で、自然も楽しめる。\n
動植物の観察をかねてのピクニックなど、気持ちがいいに違いない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが……、問題のユリウスときたら、ここ数日なにやら真剣な顔でひたすら机に向かっているのだ。"

jump gakuen_julius_end3
label gakuen_julius_end2b:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_6")
T "（これでも充分……、よね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私も、元々が出無精な人間。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスほどではないとはいえ、どちらかというと外で遊びまわるよりは、室内で読書やちょっとしたゲームに興じているほうが好きだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それにユリウスときたらここ数日、何かアイディアが降りてきたのか、ひたすら机に向かって作業に没頭している。"

jump gakuen_julius_end3
label gakuen_julius_end3:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何を作ろうとしているのかは分からない。\n
研究者である彼を詮索することは、ルール違反だと感じていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここはユリウスの工房で、魔法使いにとっての研究室。\n
神聖で不可侵なものでなくてはいけない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、ここでは異物だ。\n
ひっそりと息を殺し、おとなしくユリウスの作業の音を聞きながら、読書をする。"

play sound se_0718
pause .4
play sound se_0718
pause .4
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "静かで穏やかな時間は、いつもの通りに過ぎていく。\n
今日も……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（……そろそろ、かな）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はそっと立ち上がると、部屋の隅にある珈琲セットへと向かった。\n
これまで作業室で珈琲というと、ユリウスが淹れるものだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が用意するときには、カフェテリアからの差し入れが精々。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "でも、それはユリウスの淹れた珈琲ほど美味しくなくて、自然と持ってこなくなった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼の淹れたものが一番。\n
だが、こうしてここで長く時間を過ごすようになったからには、毎回淹れてもらってばかりというのも悪い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "少し前に珈琲ブレイクの準備をやらせてもらえないかと申し出たのである。\n
ミルやその他の道具の使い方を習い、今に至る。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（あら？）"


play music quiet_a_wam
show m_yuri_end1 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "見慣れないカップがある。\n
ユリウスの珈琲カップは、縦にすらりと長い深い青色のものだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それは見慣れているのでよく分かる。\n
対して私が使っているのは、カフェテリアで使われている至ってシンプルな白の珈琲カップだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一度この部屋に持ち込んで以来、そのまま洗って使ってしまっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その白の珈琲カップが見当たらなくなっている代わりに、ユリウスの青色珈琲カップの色違いが置かれていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスのが深い青、紺に近い色をしているとしたならば、それはもう少し明るい藍色だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が戸惑っているのが分かったのか、ユリウスが口を開いた。"

hide m_yuri_end1
show m_yuri_end2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0281
Julius "「客なんておまえぐらいしか来ないんだ、おまえ専用のカップを用意しても構わんだろう。……気に入らないようなら、新しく自分で用意するんだな」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_4")
T "（……！！\n
私のカップ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスが選んで、用意してくれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_8")
T "「気に入らないわけないじゃない……！\n
ありがとう、ユリウス、大事にするわ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_8")
voice jul_g0282
Julius "「大事になんてしなくていい。\n
傷んでもいいから……、それくらい使え」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "振り返った先、彼は手元から視線を持ち上げてすらくれない。\n
けれども、その目元がうっすら上気しているのが分かる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_9")
T "（分かりにくいようで、分かりやすい人よね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "胸の奥がじんわりと暖かくなった。\n
ここが私の居場所だと、認めてもらえたようで嬉しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_1")
T "「……ふふん♪」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "鼻歌まで歌ってしまう。\n
うるさいと怒られるかと思ったが、彼は何も言わずに作業に戻っていったので、続行する。"

hide m_yuri_end2


play music daytime_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふんふんと上機嫌に歌いながら、以前習ったとおりに珈琲を淹れていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ミルの中に豆をワンスクープとちょっと。\n
それから後は魔力を流し込んでしまうだけだ。"

play sound se_0779
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "流し込んだ魔力に反応し、自動的に豆がごりごりと削れていく。\n
豆を挽くにつれ、珈琲のほろ苦い芳香が部屋の中へと満ちていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "悪くない。\n
ユリウスが淹れるときと、そう差がないように感じる。"


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "挽いた豆に湯を注いで、こして、珈琲を淹れた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「はい、どうぞ」"

play sound se_0213
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "かたりとユリウスの前に紺色の珈琲カップを置いて、私はわくわくとその反応を待った。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_14")
T "（今回は……、どう？）"


show yuri_m_01_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_14")
Julius "「…………」"

hide yuri_m_01_13
show yuri_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_14")
voice jul_g0283
Julius "「……６８点」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「ええええっ、今日のはいい出来だと思ったのに！」"

hide yuri_m_01_4
show yuri_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_5")
voice jul_g0284
Julius "「……喚いても、結果は変わらないぞ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「何よ、何が原因なのよ！」"

hide yuri_m_03_10
show yuri_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice jul_g0285
Julius "「豆の挽きが均一じゃない。\n
だから味わいにもムラが出来てしまっている」"

hide yuri_m_02_4
show yuri_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice jul_g0286
Julius "「魔力の供給の仕方を、もう少し工夫するんだな。\n
がむしゃらに回せばいいというものではない」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「～～～っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "悔しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が珈琲を淹れるようになって以来、ユリウスは毎度その珈琲に点数をつけて評価してくれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最初それを言われたときには、またこの男は意地の悪いことを言って……、ぐらいにしか思わなかった。\n
何せ、同じ道具を使っているのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "豆を挽くのは魔力を動力源に動くミルだし、その後の工程は湯でこすだけ。\n
それだけで味が変わるとは思えなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが実際に口をつけて味わってみると、その違いは明白。\n
彼が淹れる珈琲と比較すると、明らかに劣っているのがよく分かる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今回も、何がよくなかったのかと首を捻りながら、新品のカップへと口付け……。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「……本当だわ。\n
こう……、ぼけたような感じになっちゃっている」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "豆の種類も、量も、使っている道具も同じであるはずなのに。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が淹れた珈琲の味わいはユリウスが淹れたものに比べるとどこかピントがずれているような感じがする。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……難しいわね」"

hide yuri_m_03_9
show yuri_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice jul_g0287
Julius "「まだまだだな。\n
……次はもっと工夫してみろ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_12")
T "「……頑張るわ」"

hide yuri_m_01_2

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "点数は辛口だし、その肥えた口に適うだけの珈琲を淹れるまでの道は遠く厳しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "けれど彼は私に珈琲を淹れるなとは言わないし、毎回文句を言いながらも最後まで飲んでくれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_10")
T "（いつか、絶対に満点をとってやるんだから）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう固く決意する一方で、誰がどう魔力を供給しても美味しい珈琲を淹れることの出来るマシーンこそ、是非とも開発してもらいたいとも思ってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぼけた味わいの珈琲と、遠くから聞こえるような作業音。\n
穏やかな時間はまったりと過ぎていく。"

with dis
$ hi_mes()

scene bg_par06_jr with Dissolve(.8)

scene bg_par15_rg_tow_day
with stripe_l_medium

scene bg_map_day
with stripe_l_medium

play music flower_day_p_wam

scene bg06_sk_h_day
with stripe_l_medium
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私とユリウスの時間というのは、いつも穏やかに過ぎていく。\n
穏やか過ぎるのか、妙な苦情も出ていた。"


scene bg06_sk_h_day_s
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0660
Blood "「……君らは老夫婦か。\n
もう少し若々しいカップルらしく、活きのいいオーラを流せないのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0661
Blood "「見ていて面白くない。\n
ああ……、こうなるのならば、もっと邪魔して楽しんでおくんだったな」"


scene bg06_sk_h_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（人の色恋沙汰に首をつっこんで、何を好き勝手なことを抜かしているのか……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私とユリウスの関係は、何もない時間の中で築かれていったものだ。\n
別に活きのよさなど必要ない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、文句を言うのはブラッドくらいだとしても、私達を穏やかなままに放って置いてくれない事情というものがある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "大体穏やかだが、いつもではない。\n
どうしてかというと……、ユリウスの役職柄。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は、風紀委員長。\n
このシンフォニア高位魔法学校の風紀を守ることこそが、彼の任務だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "つまり、それは、風紀を乱す連中と戦う必要があるということで……。"

with dis
$ hi_mes()

scene bg06_sk_h_day
with dis

scene bg_map_day
with stripe_l_medium

scene bg27_rk_day
with stripe_l_long

play music corridor_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「……あら、ユリウス？\n
こんなところで会うなんて珍しいわね、どうしたの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ばったりと、校舎内でユリウスに出会った。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスは研究生という立場もあり、当然ながら新入生である私と授業や実験の場が重なることはほとんどない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "毎日のように顔を合わせている私達でも、こうして校舎内で鉢合うのは珍しい。"


show yuri_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0288
Julius "「……双子を探していたんだが、見なかったか？\n
またあいつらがとんでもない悪戯をやらかしてな……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「……また？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "頭が痛いと訴えるような渋面でユリウスが呻く。\n
帽子屋寮の名物双子は、トラブルメーカーとしても名高い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "毎回何かしらやらかしては叱られるといったことを、懲りずに繰り返し続けている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「残念だけど、私は見ていないわ。\n
今回は、あの子達、いったい何をやらかしたの？」"

hide yuri_m_01_3
show yuri_m_03_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice jul_g0289
Julius "「実に馬鹿らしいことだが、質量増減魔法の乱用だ。\n
早い話が、巨大化だな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「きょ、巨大化……っ！？\n
何を巨大化させちゃったの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "嫌な予感がする。\n
彼らは男の子らしく、爬虫類だとか蜘蛛だとか、そういった生き物が大好きだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "大きいとかっこいいよね！なんて盛り上がった結果、そういったゲテモノの類の生物を巨大化させている可能性も高い。"

play sound se_0090
camera at hpunch
camera at vpunch

show bg06_sk_h_day onlayer master
with dis

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0336
Elliot "{size=+20}「くそガキ共！どこだ、出て来い！\n
踏み潰してやる！」{/size} "


play music gag1_a_ali
play sound se_0090
camera at hpunch
camera at vpunch
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "窓の外を、何かとてつもなく巨大なものが過ぎていった。"


with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「…………。\n
……エリオット？」"

hide bg06_sk_h_day

hide yuri_m_03_13
show yuri_m_01_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice jul_g0290
Julius "「ああ。\n
何がしたかったんだろうな……、はあ、私には奴らの考えていることが分からん」"

hide yuri_m_01_13
show yuri_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice jul_g0291
Julius "「どうして、ウサギを巨大化させるんだ？\n
元々でかいあの男を、あれ以上巨大にしてどうしようと……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……さあ。\n
どうしようとか、考えていなかったのかもしれないわよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "嫌がらせか、思いつきか……。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「普段から充分大きいのにね、エリオットって……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "体格はいい。\n
そして、あの特徴的な耳を含めた全長で考えると、更に大きくなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（それを更に巨大化……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ずーんずーんっと足音を響かせ、窓の外を通り過ぎていった巨大なエリオットの影。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウス同様、私まで頭が痛くなってくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_10")
T "「なんであの子達は……」"


show dee_m_01_3 at center
with dis
hide yuri_m_01_4

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_10")
voice dad_g0490
Dee "「それはお姉さん、薬の仕込みやすさだよ！\n
ひよこウサギはオレンジ色さえしていれば、何でも食べるからね！」"

hide dee_m_01_3
show dee_m_01_3 at left
with dis

show dam_m_01_6 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_10")
voice dad_g0491
Dam "「そうだよ、お姉さん！\n
それに寮が一緒だから、仕込むチャンスもいっぱいあるしね！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「！！」"


show yuri_m_03_7 at center
with dis
hide dee_m_01_3

hide dam_m_01_6

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_4")
voice jul_g0292
Julius "「……！？\n
おまえ達……！！」"


play music deedam_t_ali
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちょうど私達が彼らのことを話題にしているタイミングで、双子達が姿を現した。"


show dee_m_01_2 at center
with dis
hide yuri_m_03_7

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0492
Dee "「ピアスの奴も候補だったんだよ！\n
ほら、あいつもチーズなら何でも食べるからね！」"

hide dee_m_01_2
show dee_m_01_2 at left
with dis

show dam_m_01_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0493
Dam "「でもクラスも違うし、寮も違うからね。\n
今回は一番手近で簡単なひよこウサギに実験台になってもらったんだよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人とも楽しそうだ。\n
悪びれる様子もない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスは、二人を捕まえようと一歩大きく踏み出す。"

play sound se_0604
pause .6
play sound se_0097

show white onlayer master with spread_short
hide dee_m_01_2

hide dam_m_01_4

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぽーんっと軽い爆発音と共に、もくもくと煙が噴出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「な……！？\n
なに！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice jul_g0293
Julius "「……ちっ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ディーが何かを投げたと思ったら、それが目の前で炸裂した。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "隣のユリウスが咄嗟に庇うように抱え込んではくれたものの、もくもくと溢れた煙が目にしみる。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0494
Dee "「あはは、お姉さんごめんね！\n
お姉さんを巻き込んじゃうつもりはなかったんだよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0495
Dam "「そうだよ、お姉さん、ごめんね？\n
僕達、謝ったから許してくれるよね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自由の利かない視界の向こう側から、ツインズの声が聞こえる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_13")
T "（許すわけないでしょう！？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これは煙玉なのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今のところ、煙が目にしみる以外の害はないようだ。\n
私を庇ったユリウスも、やはり煙たげにしている他に影響はないように見える。"

hide white with Dissolve(1.5)
##[cg wait="1500"]
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぱたぱたと自分の手でも煙を払いのけながら、私は二人を叱りつけようとした。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_14")
T "{size=+20}「ディーっ、ダムっ、あんた達、よくやったわ！\n
もちろん、許すわよ！」{/size} "


show yuri_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_14")
Julius "「……！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスがびっくりしたように私へと視線をやり、私自身も驚いて息が詰まった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……な、何を言っているの？\n
私？）"

hide yuri_m_03_3
show yuri_m_02_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_10")
voice jul_g0294
Julius "「おまえ達！\n
どんなことをしたって許してやるぞ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「……っ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今度はユリウスが訳の分からないことを言い出した。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私にしたってそうだ。\n
よくやったなんて褒めるつもりは一切なかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "むしろ私が言いたかったのは、「よくもやってくれたわね」、だ。\n
どうして、私達は思ってもいないことを口にしてしまっているのだろうか。"


show dee_m_02_1 at center
with dis
hide yuri_m_02_7

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0496
Dee "「あはは、ねえねえ、委員長さん！\n
僕達のこと、許してくれるよね？」"


show yuri_m_01_8 at center
with dis
hide dee_m_02_1

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0295
Julius "「許すに決まっているだろう！！\n
この{size=+20}可愛い子供達め！{/size}」"

hide yuri_m_01_8
show yuri_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Julius "「！！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "またしても、衝撃。\n
こんな悪戯をされたからというだけでなく、普段からだってユリウスが双子を可愛い子だとか言えば気持ち悪い。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「ユ、ユリウス？\n
あなた、おかしくなっちゃったのね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（うわあ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "「大丈夫？」と聞きたかったはずなのに、私の問いかけはより攻撃的になってしまっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "別に、ユリウスに喧嘩を売りたいわけではないのに。"

hide yuri_m_03_2
show yuri_m_03_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0296
Julius "「おかしくなんてなっていない！\n
おまえのほうも平気そうだな！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「大丈夫に決まっているじゃない！」"

hide yuri_m_03_7
show yuri_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_12")
Julius "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "お互い、はたと唇に指を当ててさすがに気付いた。\n
これでは会話が成立していない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私達は互いに、言おうとしたことの逆を口にしてしまっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（……っ！\n
先刻の煙玉ね！？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "きっと、双子が悪戯用に改造したマジックアイテムだ。\n
あれのせいで、こんなろくでもない効果を生んでいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……あんた達！\n
解毒剤を捨ててしまいなさい！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_6")
T "（違う違う違う！\n
持ってこいって言いたかったのよっ！！）"


show dee_m_02_6 at center
with dis
hide yuri_m_02_3

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_6")
voice dad_g0497
Dee "「え？\n
お姉さん、ずっとそのままでいいの？」"

hide dee_m_02_6
show dee_m_02_6 at left
with dis

show dam_m_02_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_6")
voice dad_g0498
Dam "「それはそれで面白いとは思うけど、安心してね。\n
三時間ほどで効果は切れるよ」"


show yuri_m_03_11 at right_center
hide dee_m_02_6
show dee_m_02_6 at left_center
hide dam_m_02_4
show dam_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_6")
voice jul_g0297
Julius "「たった三時間……！？\n
そんな短いとは……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "三時間も……と、責めたかったに違いない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言いたいこととは真逆のことしか言えない私達に、双子はけらけらと楽しそうに笑っている。"

hide dee_m_02_6
show dee_m_02_4 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0499
Dee "「あはは。\n
委員長に謝ってこいってボスに言われたときにはどうしようかと思ったけどね、兄弟」"

hide dam_m_02_4
show dam_m_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0500
Dam "「謝るってことは許しを得るってことでしょう？\n
僕達、ちゃんと許してもらえたから、これでオッケーだよね！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「それで、こんな……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "無茶な理屈だが、口では責められない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（こうなったら……）"

menu:
    "力づくでも解毒剤を手に入れる。":
        jump gakuen_julius_end4a
    "効果が切れるまで撤退する。":
        jump gakuen_julius_end4b
label gakuen_julius_end4a:

play music opposition2_a_ali
show m_yuri_end3a_1 onlayer master
with dis
hide yuri_m_03_11

hide dee_m_02_4

hide dam_m_02_2

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、懐から杖を取り出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0298
Julius "「素晴らしいアイディアだな……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう言うユリウスの言葉に背中を押され、杖を構え、呪文を唱えた。"

play sound se_0496
pause 1
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_1")
T "「…………」"

play sound se_0726
hide m_yuri_end3a_1
show m_yuri_end3a_2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「？？？」"

play sound se_0739
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の放った光の玉は、まっすぐに双子へと向かう……、ことなく何故か私自身のところへと戻ってきた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_13")
T "「こっちよ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "「あっちよ」と誘導したいのに、言葉がままならないせいかコントロールまでおかしくなっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が口にする言葉そのままに、こちらへと迫ってくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（……ならばっ）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_13")
T "「あっちよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こっちに来いを念じながら言えば、光の玉は空中で迷うように揺れて、やっぱりこちらへと向かってきだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「！？\n
なるほど、思った通りね！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_8")
T "（思っていない、思っていない！\n
なんで？どうして？）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_8")
voice jul_g0299
Julius "「……おまえ、本当に頭いいな。\n
意思と言葉と、その両方に反応しないからこうなるんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスが呆れたように言う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "明らかにその本意は褒めていないのに関わらず、双子の悪戯のせいで言葉尻だけだとものすごく褒められている気分を味わえる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "奇妙な具合で、新鮮だ。\n
アイディアを褒められたのも、彼としては止めようとしていたのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "翻訳するなら、「やめろ、馬鹿なことを……！」ぐらいだろうか。\n
実際、魔法は失敗している。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "口にするさかさまの言葉と、それを口にするときの意志の力との間で惑って光球が揺れる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（……まずい）"

play sound se_0376
hide m_yuri_end3a_2


show dee_m_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice dad_g0501
Dee "「ふふ、バチバチすきなんだね、お姉さん！\n
すっごくバチバチして……、不安定」"

hide dee_m_02_2
show dee_m_02_2 at left
with dis

show dam_m_02_10 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice dad_g0502
Dam "「お姉さんはバチバチ愛好家なんだよ、兄弟！\n
楽しんでいるところを邪魔しちゃ悪いから行こうよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスが苦虫を噛み潰したような顔で黙ったままになっているのをいいことに、二人は勝手極まりないことを言い捨て、立ち去るつもりのようだ。"

hide dee_m_02_2
show dee_m_01_9 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0505
Dee "「それじゃあ、またねお姉さん！\n
委員長も、あっさり許してくれてありがとう！」"

hide dam_m_02_10
show dam_m_02_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0506
Dam "「子供に対する思いやりの気持ちって、大事だよね！\n
二人がとっても優しくて僕達、嬉しいよ！普段からそうだともっと嬉しいな！」"

play sound se_0311
hide dee_m_01_9

hide dam_m_02_2

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人は、軽やかな足音をたてて本当にそのまま去っていってしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "後に残されたのは、言葉に不自由した私とユリウス。\n
そして、バチバチいっている光の玉だ。"

play sound se_0376
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "双子がバチバチと言っていたように、この光球は電気を帯びている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "火や水ほど派手でなく、それでいてそれなりにダメージを与えるものということで雷撃系の魔法を選んだのだが……、後悔している。"


show yuri_m_02_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0300
Julius "「戦うぞ。\n
あれは、私に任せろ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「え？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（ユリウスだって魔法はままならない……、わよね？）"

play sound se_0492
pause .4
play sound se_0311
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう疑問に思うより先に、ユリウスに手をとられ廊下を走り出していた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言葉が逆になっていると分かっていても、すぐには慣れない。\n
言われた言葉をそのままに受け取ってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今の、「戦う、任せろ」にしてもその逆なわけで……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（逃げる、放置するってこと……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それしかないと分かっていても、あんな不安定な状態の攻撃魔法を放置して逃げるのは心苦しい。"

hide yuri_m_02_7


scene bg06_sk_h_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（大丈夫……、よね？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここはシンフォニアだ。\n
巨大化しているエリオット含め、誰かがきっと何とかしてくれると信じよう。"

jump gakuen_julius_end5
label gakuen_julius_end4b:

play music battle_ali
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_12")
T "（ここは、一度退却したほうがいいかもしれない）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "魔法の媒介は呪文だ。\n
普段私達が使っている言語とは違っても、あれも言葉には違いない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今こうして思う言葉の逆しか言えないという状況で、呪文詠唱だけがうまくいくとは思えない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "下手に自爆する前に、退いたほうがいいだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「ユリウス、一人で行くわよ！」"


show yuri_m_03_4 at center
with dis




with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_12")
voice jul_g0301
Julius "「愚かだな、おまえは。\n
勝手に一人で行け」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「…………」"

hide yuri_m_03_4
show yuri_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
Julius "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "耳から聞いたままの会話だと、とんでもなくギスギスしたやりとりだ。\n
だが……、その声音はいかにも私に同意するといった調子。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言葉が逆になっていると分かっていても、すぐには慣れない。\n
頭が混乱する。"

play sound se_0492
pause .4
play sound se_0311

show m_yuri_end3b onlayer master
with dis
hide yuri_m_02_3

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "賛成なのか反対なのか。\n
その答えを手っ取り早く示そうというかのように、ユリウスが私の手を取って走り出した。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0507
Dee "「えええっ！？\n
お姉さん遊んでくれないの！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice dad_g0508
Dam "「委員長とだけ遊ぶなんてずるいよ！\n
僕達とも遊んでよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_7")
T "（いやいや、遠慮するわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "声に出すと快諾してしまいそうなので、お断りの言葉は今は心の中で呟くだけにしておく。"


scene bg06_sk_h_day
with dis
hide m_yuri_end3b

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここはシンフォニアだ。\n
巨大化しているエリオットも、誰かがきっと何とかしてくれるだろう。"

jump gakuen_julius_end5
label gakuen_julius_end5:
with dis
$ hi_mes()

scene bg_par15_rg_tow_day with Dissolve(.8)

scene bg_map_day
with stripe_l_medium

scene bg_par23_jr_k
with stripe_l_medium

scene bg_par06_jr
with stripe_l_long

play music tower_room1_p_ali
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人して、塔の作業場へと逃げ込んだ。\n
この状態で、双子の相手をするのは無理だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もともと口が達者なディーとダムを相手に、言いたい事が真逆になるハンデを持ったままやりあうなんて無謀すぎる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "口喧嘩にしても勝ち目はないし、要らない言質を取られるだけで終わるだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「……ふう。\n
これはまた、楽勝よね、簡単……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_11")
T "（全然、楽勝なんかじゃないわ。\n
難題よ、面倒だわ……）"


show yuri_m_02_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice jul_g0302
Julius "「そうだな。\n
……嬉しい限りだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスは、とても「嬉しい」ようには聞こえない疲れきった声音で吐き捨て、作業机の向こうへと歩いていく。"

hide yuri_m_02_11

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この状態では風紀としての仕事は無理だろう。\n
効果が解けるまで、作業を進める気らしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（私は、どうしようかな）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「珈琲を淹れてくれる？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の声にユリウスが立ち上がりかけるのを手で制した。\n
口を開くと余計に混乱を招きそうなので、静かに首を横に振るだけにする。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（私が淹れるって言いたかったのよ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本当に、迷惑な悪戯だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスも、首を振る所作や、珈琲道具のほうへと移動するのを見て本意を察したらしい。\n
再び座る音を背中で聞く。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうして、いつものように珈琲を淹れた。\n
豆はワンスクープとちょっと、それからミルに魔力を流し込んで起動する。"

play sound se_0779
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふわり、と香ばしい珈琲の香りが部屋の中に満ちていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_8")
T "「……嫌な匂い」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "うっとりとした声で呟いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（珈琲ミルが、呪文を必要とするタイプでなくてよかった）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "魔法が使えない、うまくコントロール出来ないというのは、かなり大変だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんでも、ルーンビナスの王族には何百年かに一度、魔法のまったく使えない者が出現するのだという。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私には魔法が身近すぎて、それを奪われたときの生活というのが想像することも出来ない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「ユリウス、あなたの分はないわ」"


show yuri_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice jul_g0303
Julius "「私が感謝するとでも思ったか？\n
そんなものが飲めるか」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（……え～と、これ、多分お礼を言われているのよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "妙な会話だ。"

hide yuri_m_02_1

play sound se_0177
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスの机の上にカップを置く。\n
色違いで揃いの、珈琲カップだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普段あまり恋愛関係での感情を表に出さないユリウスだが、だからこそ行動で示してくれたことが嬉しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼はゆっくりと珈琲をまずは香りで味わってから、口をつけた。\n
今日は何点ぐらいの出来だろうか。"


show yuri_m_03_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0304
Julius "「……飲めたものではないな。\n
８６点だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「……っ！\n
嘘！？」"

hide yuri_m_03_8
show yuri_m_01_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice jul_g0305
Julius "「ああ、嘘だ。\n
私は大嘘つきだからな、嘘しか言わない」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_2")
T "「悲しいわっ、そんなふうにしか言ってくれないなんて！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言っている内容とは裏腹に、私の声音は弾む。\n
今までにない高得点だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分でも、カップに口をつけてみる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_8")
T "「……なにこれ！\n
全然駄目ね！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まだまだユリウスの味に比べたら及ばないが、それでも及第点はつけられそうな味に仕上がっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "少なくとも、以前のようなピントがずれているような感じはない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "嬉しくて顔がにやける。\n
緩んだ口元で、ユリウスの傍らに立ったまま珈琲を飲んでいたところ、ふっとその手を引かれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「なに？」"

hide yuri_m_01_13
show yuri_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice jul_g0306
Julius "「別に、なんでもない」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "天邪鬼なことを言いながら、ユリウスはそのまま私を引き寄せて抱きしめた。\n
ふわりと珈琲の香りが強く漂う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "日頃から珈琲を愛飲している彼の制服には、珈琲の匂いがすっかり染み付いてしまっている。"

play sound se_0551

play music flower_eve_p_wam

show m_yuri_end4 onlayer master
with dis
hide yuri_m_03_4

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「どうしたの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すとんと、落ち着いた先は彼の膝の上だ。\n
すっぽりとその懐の中に収まって、珈琲を飲む。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_7")
T "（居心地いいんだけど……、悪い）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まるで、今の裏腹な状態のよう。\n
傍にいたいのに、逃げ出してしまいたくなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0307
Julius "「おまえが、まずい珈琲を淹れたからだ。\n
もっと努力しろ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_10")
T "「……頑張るわけないじゃない。\n
あなたに飲んでほしいわけじゃないもの」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（……だ、駄目だ、これは）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今すぐにでも双子を連行してきて、解毒剤を飲みたい。\n
せっかく漂う空気は甘やかなのに、言葉はそれに反比例して辛辣だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ただ、ユリウスの声音はとても優しい。\n
愛しいものを見るような目で、落ち着いた優しい声音で、とんでもない内容を囁く。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（……お互い様なんだけれど）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice jul_g0308
Julius "「おまえが、嫌いだよ。\n
大っ嫌いだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_8")
T "「……知らないわ、そんなの。\n
私だって、あなたのことなんて大っ嫌いだわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_9")
T "（……変な感じ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "真逆に変換されるのが分かっているから、余計に素直になれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普段の私達なら、好きだの大好きだのそんな言葉はなかなか出てこない。\n
お互い、ずるいのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Julius "「…………」"

hide m_yuri_end4
show m_yuri_end5 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスの手指が、私の顎をくいと持ち上げた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "上から唇を落とされる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言葉の必要ない時間。\n
重ねて、混ざって、吐息ごと一つになる。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0309
Julius "「……終わりにしたい」"

hide m_yuri_end5

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_6")
T "（もっと……、でいいのよね？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "真逆に変換された言葉を、ひっくり返して真意を捜す。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_19")
T "「……鍵が開いているなら」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_13")
T "（私は露出マニアか……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "鍵のかかっていない状態を希望するなんてどうかしているとしか思えないが、反対の意味だとユリウスも読み取ってくれるはず。"

play sound se_0468
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼はちらりと扉を確認し、ぱちんっと指を鳴らした。"

play sound se_0452

play music memory1_a_wam

show m_yuri_end5 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0310
Julius "「これで……、問題だらけだな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「そうでもないわよ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "元々ユリウスの作業室までやってくる人間は少ない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何か問題があった際に、風紀委員の部下が駆け込んできたり、エースが遊びにきたりする程度だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今は戦闘不能状態なので、何かあって呼ばれたとしても対処は出来ない。\n
部屋のドアに鍵をかければ、諦めて帰ってくれるだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_7")
T "（……いや、エースだとどうかな。\n
帰ってくれると願いたいけど……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "口にする言葉はすべて嘘になってしまうから、言葉は諦めた。\n
交わす口付け、声、触れる指先、そういったものから気持ちが伝わるといい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "せめて、私に伝わっているものと同じ程度には、伝えたい。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0311
Julius "「……大嫌いだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_9")
T "「……私は違うわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言葉でなんと言おうが、いや……、何も言わずとも、誤魔化せないものがある。\n
それは、普段から感じていることだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（嘘をついてもつかなくても、素直じゃない。\n
そんな私達だけど……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_8")
T "「……大嫌い」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あべこべな言葉を交わしながらも、素直なキスを交わした。"


##[bgimage ##instant]
hide frame_par_togaki
hide ali_m_06_16
with Dissolve(2)
hide m_yuri_end5
show white onlayer master
with compress_extralong
scene black with compress_extraextralong
pause 1
stop music
##endmemory
jump gakuen_a
