
scene map_bg_winter_day
with dis

scene charasel_bg_tower_day
with dis
label fushigi_gray1:
hide screen tower_man_choice
$ clockanim()

$ hi_mes()

scene cki1_01
with dis

play music tower_corridor_p_ali

scene cr_01 with Dissolve(1.2)
play sound se_0275
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_13")
T "「こっちにも、いない」"

play sound se_0399
play sound se_0584
pause 1
play sound se_0275
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「ここにも、いない」"

play sound se_0399
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先刻から私はずっと塔の階段を上り下りしながら、グレイを捜して歩き回っている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "小火騒動が落ち着いても、彼には後始末や倒れた上司の介護など、仕事が山ほどある。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それらの残務処理を取り仕切るグレイは、この塔で一番多忙な人だろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "仕事の内容から考えても一箇所に留まっているような人ではないと知っていたが、ここまで見つからないとは思わなかった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（どこだろう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアの執務室、資料室、会議場……。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "思い当たるところは探し尽くしているはずだが、なかなか目当ての彼の姿は見つからない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「はあ、はあ……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（それにしても、この塔、広すぎる）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "人ひとりを捜すのにこんなに苦労するとは思わなかった。\n
私も大分クローバーの塔の構造には慣れたつもりだったのに。"


show yuri_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0330
Julius "「[firstname]、おまえ、息を切らせて何をしているんだ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "歩き回っているとユリウスに声をかけられた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "普段部屋から出たがらないユリウスだが、肝心の私室が黒こげでは外に出ているのも当然のことだろう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「あ……、ユリウス。\n
どこかで、グレイを見かけなかった？」"

hide yuri_t_01_3
show yuri_t_03_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
voice jul_f0331
Julius "「トカゲだと？\n
あいつなら、ナイトメアのところに行くと言っていたが……、いないのか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「ええ。\n
ナイトメアの部屋にも行ったけど、もういなくて」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイが倒れた彼を放っておくはずがない。\n
私がグレイを捜して最初に向かったのも、この塔の主の部屋だった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（部屋にいたのは医者から逃げようとするナイトメアだけだったけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "助けを求める彼に「自業自得でしょう」と言い捨てて出てきたのだが、ここまで見つからないのであれば行き先ぐらい聞いておけばよかったのかもしれない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いかに情けなくとも、ナイトメアはこの塔の主だ。\n
部下の居場所ぐらい把握していただろう。"

hide yuri_t_03_8
show yuri_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「今のところ、資料室に、詰め所、会議場、グレイの部屋は見に行ったんだけど……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "矢継ぎ早に説明をしようとするが、息が整わない。\n
ぜはぜはと息を乱していると、ユリウスは溜息をついて首を振った。"

hide yuri_t_01_4
show yuri_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0332
Julius "「少しは落ち着け。\n
焦れば見落とすだけだ」"

hide yuri_t_01_3
show yuri_t_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0333
Julius "「……この塔は、特に禁煙というわけではないんだろう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「ええ。ただ、煙草が原因でこれだけの騒ぎになったから……。\n
しばらくは喫煙場所も限られるかもしれないけど」"

hide yuri_t_01_8
show yuri_t_03_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
Julius "「…………」"

hide yuri_t_03_13
show yuri_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice jul_f0334
Julius "「談話室は行ったのか？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "呼吸を整えながら答えると、彼は物思いに耽るように口を閉ざす。\n
だがその視線が私を見たときには、何か思い当たる場所があったらしい。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「え？\n
談話室は……、まだ行ってないけど」"

hide yuri_t_03_10
show yuri_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice jul_f0335
Julius "「あいつのことだ、終わらない仕事に無理矢理一区切りをつけて、一服しているんじゃないか？」"

hide yuri_t_02_10
show yuri_t_03_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice jul_f0336
Julius "「屋外で吸えば燃え移る心配も少ないだろうが、連絡も入りにくい。\n
だったら室内で堂々と吸える場所を選ぶだろう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（言われてみれば、確かにその通りかもしれない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "病弱なナイトメアに変わって、塔の管理を取り仕切るグレイだ。\n
そのくらいの配慮をしていてもおかしくない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「ありがとう、ユリウス。\n
探しに行ってみるわ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_14")
T "（仲がいいのか悪いのか分からないけど、よく見ているわよね）"

hide yuri_t_03_4
show yuri_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_14")
voice jul_f0337
Julius "「礼を言われるようなことじゃない。\n
あいつに用があったんだろう、早く行け」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_17")
T "「うん。\n
あ、でも……、その前に少しだけいいかしら、ユリウス」"

hide yuri_t_01_3
show yuri_t_03_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_17")
Julius "「？」"

hide yuri_t_03_8
show yuri_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_17")
Julius "「[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「あなたの部屋のこと、ちゃんと謝らなくちゃと思って。\n
焦がしてしまって、本当にごめんなさい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "勢いよく頭を下げる。\n
最後の審判を待つ罪人のような心地になるが、先ほどの様子から彼が怒っていないことは分かっている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（でも、甘えていいはずがない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "優しい人だから。\n
その好意には誠意を持って応えたかった。"

hide yuri_t_03_9
show yuri_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius "「…………」"

hide yuri_t_02_8
show yuri_t_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0338
Julius "「今更詫びてもらうようなことじゃない。\n
そんなことを気にするぐらいなら、早く、片を付けてこい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「うん、ありがとう、ユリウス」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "困ったように笑う友人に礼を言って、私は談話室へと足を向けた。"

hide yuri_t_02_1

$ hi_mes()

scene charasel_bg_tower_day
with stripe_l_medium

play music tower_inside_p_ali

scene co_01
with stripe_l_long
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "クローバーの塔の談話室は、さすが領主の住む場所らしく、内装も上品な空間に仕上げられている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "利用者が話しやすいようにソファも整然と並べられているが、その一つに黒い影が見えた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "室内に漂う紫煙の香りは、私にとっても馴染みのあるものだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（グレイの匂い）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "休んでいるところを邪魔するのも気が引けたが、遠くから声をかけるのも変な話だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "なるべく足音を出さずに近付こうとするものの、それはたった数歩の接近で終わった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "気配に敏感な彼はあっさりと私に気が付いて、顔を向けてくる。"


show gre_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0176
Gray "「[firstname]……、どうした？\n
またナイトメア様が……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「ううん、違うわ。\n
あなたを捜していたの、グレイ」"

hide gre_t_01_5
show gre_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice gra_f0177
Gray "「俺を捜していた？\n
どういうことだ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "意外そうに言いながら、そこで彼はまだ手元に持った煙草に火がついていることに気が付いたらしい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "慌てて灰皿で消そうとしたが、首を左右に振って止めた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「気にしないで。\n
あなたの休憩を邪魔したかったわけじゃないの」"

hide gre_t_03_9
show gre_t_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice gra_f0178
Gray "「いや、そろそろやめようと思っていたところだから、ちょうどいい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう言って彼は火のついた煙草を灰皿に押し付けた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（まだ火をつけたばっかりだったみたいなのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私自身は煙草を吸わないが、火がついたばかりかどうかぐらいは残った吸殻を見れば分かる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "邪魔してしまったのではないかと、申し訳なくなってしまう。"

hide gre_t_02_3
show gre_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0179
Gray "「それで、一体どうしたんだ？\n
君だって先刻の騒動で疲れているだろう？」"

hide gre_t_03_10
show gre_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0180
Gray "「そんな状況で俺を捜しに来るなんて……、余程の理由があるんじゃないのか」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "心配そうな、気遣うようなそんな態度でグレイは首を傾げてくる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（怒ったっていいのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "火を消したあと、ナイトメアの無事を確認したグレイは、それは壮絶に怒った。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "表面上はいつもと同じように穏やかな顔をしていたが、声の端々に棘がちくちくと混ざっていたことに気付かないほど、私も鈍くはない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（ナイトメアが本気で青ざめていたものね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "心の読める彼には、さぞかし恐ろしいものが感じ取れたことだろう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_12")
T "「あなたにちゃんと謝らなくちゃって思って」"

hide gre_t_02_4
show gre_t_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_12")
Gray "「[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「火の不始末で危ない目に遭わせた上に、余計な仕事を増やしてしまったでしょう。\n
本当に……、ごめんなさい」"

hide gre_t_02_7
show gre_t_01_14 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice gra_f0181
Gray "「君が謝ることはない。\n
元はと言えば、ナイトメア様をお一人にした俺にも非が……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_4")
T "「それを言ったら、私だって同じだわ。\n
グレイが休憩するって分かっていたんだから、少しずらして休憩を取ればよかったんだもの」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "逃亡癖のある上司を持つ以上、それは予測できたことだ。\n
グレイと私が一緒に休憩に立つときは、特に逃亡率が高かったのに。"

hide gre_t_01_14
show gre_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0182
Gray "「いや、それは君が悪いわけではないだろう。\n
あの方の体力の底を甘く見ていた俺にも甘さがあったわけで……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（……私のことは、怒ってくれないの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ナイトメアを叱責するのは、部下として彼の立場上必要なことだ。\n
だが、私だって彼の部下である以上、怒られて然るべきなのに。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「だから、ちょっと外に出て反省してこようと思っているの」"

hide gre_t_01_5
show gre_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_7")
voice gra_f0183
Gray "「何？\n
外に出てって……、街にという意味か？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「ううん、もうちょっと遠いところ。\n
少なくとも、クローバーの塔の領地からは出ようと思って」"

hide gre_t_02_10
show gre_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_12")
Gray "「！！」"

hide gre_t_02_4
show gre_t_03_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_12")
voice gra_f0184
Gray "「いや、君がそこまで責任を感じる必要はない。\n
君がそんなことを言い出すなんて……」"

hide gre_t_03_8
show gre_t_01_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_12")
voice gra_f0185
Gray "「……時計屋が、何か言ったのか？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "突然立ち上がった彼の空気に不穏なものが混じっている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「ユリウス？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（どうしてここでユリウスの名前が出てくるの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "思わず彼の名前を口にすると、グレイは苦い顔で溜息をついた。"

hide gre_t_01_9
show gre_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0186
Gray "「あの男に、言われたから君は責任を感じたのかと」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「……ユリウスはそんなことはしないわ。\n
今もグレイを捜している間に会えたから、謝ってきたけど……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「やっぱり、怒っていなかった」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "仕事第一のユリウスにとって部屋の火事なんて、あってはならない事態だっただろうに、嫌味を言われることもなかった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（ユリウスは、見た目よりもずっと優しいから）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "愛想がなくて、根暗で、引きこもりがちだけど、彼は謂われなく貶めたりしない。\n
怒るときは正当な理由があってのこと。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だから今回ばかりは私のことも怒るだろうと思っていたのに、怒られなかった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "わかりにくいが、彼は受け入れた人に優しい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（グレイと同じで、私に甘すぎるけど）"


play music secret_a_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「あのね、グレイ。\n
先刻、ちょっと長めのお休みをもらいたいってナイトメアに話してきたところなの」"

hide gre_t_01_13
show gre_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_13")
voice gra_f0187
Gray "「休み？\n
君が長期休暇を希望するなんて珍しい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「うん、自分でもそう思うわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "珍しいというよりも、初めてのことだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "時計塔から離れて、この緑の塔に留まらせてもらってから、私が自主的に休みを希望したことはあるが、そのどれも短いものばかりだった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「グレイのスケジュールを確認したら、この後はしばらく塔に詰めていてくれるみたいだし……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「今度は、グレイがちゃんと休めるように、私が先にお休みをもらおうかなって」"

hide gre_t_03_1
show gre_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
voice gra_f0188
Gray "「……え？\n
先に君が休む？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイは彼にしては珍しいことに、ぽかんとしている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あまりに突拍子もないことを言ったので、私のもう一つの狙いには気付いていないらしい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（休憩をずらすだけが目的なら、長い休みなんていらないんだけどね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "反省だけじゃなくて、本当はもう一つ、別の目的がある。\n
だが、それをグレイの前で告げてしまうのは、何だか恥ずかしかった。"

hide gre_t_02_4
show gre_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0189
Gray "「いや、[firstname]。\n
待ってくれ」"

hide gre_t_03_3
show gre_t_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gra_f0190
Gray "「君が休みを取るのはもちろんいいが……。それはつまり、これからは俺と休みが重ならないようにすると、そういうことなのか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「ええ、そのつもりだけど……。\n
ナイトメアから目を離すと大変なことになるのは、今回のことでもよく分かったし」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「なるべくどちらかが付いていられるほうが、同じことの繰り返しにならなくていいんじゃないかと思うの」"

hide gre_t_03_2
show gre_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
Gray "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイはまだどこかぽかんとしている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（私、なにか変なこと言った？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "予定していた休憩も、結局ナイトメアの捜索と小火騒動で潰れてしまった彼だ。\n
そんな忙しいグレイをいつまでも束縛するのは心苦しい。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「それじゃあ、少しの間留守にするけど……。\n
グレイがいるから、安心して任せていけるわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ユリウスは基本的に他人に不干渉なので、ナイトメアが駄々を捏ねようが放っておくに決まっている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "こんな思い切った行動に出られるのも、彼がいるからこそだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「なるべく早めに戻ってくるから、ナイトメアのことよろしくね」"

hide gre_t_03_11
show gre_t_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
Gray "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "手を振る私に、同じように手を振り返したグレイを最後に確認して、私は談話室を後にしたのだった。"

hide gre_t_01_6

$ hi_mes()

play music tower_t_ali

scene charasel_bg_tower_day
with stripe_l_long

show toustaff_a1_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice tan_f0040
Assistant "「それでは、お気を付けて。\n
ナイトメア様のお世話は、俺達が責任を持って務めさせて頂きます」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_4")
T "「ごめんなさい、私の我が侭に巻き込んで……」"

hide toustaff_a1_1
show toustaff_a1_1 at left
show toustaff_b1_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_4")
voice oto_f0039
Assistant "「いいえ、いつも誰よりも率先して仕事をしてくださっているんですから。\n
こういうときぐらい、心置きなく休んできてください」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "塔の出口、小さな手荷物だけ持った私を同僚が見送ってくれる。\n
普段グレイの傍で働いている、グレイの補佐をする人達だ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「ナイトメアがどうしても薬を飲まなかったら、下手に飲ませようとすると逆効果だから、そういうときは一度引いたほうがいいと思うの」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「薬の後にデザートを用意しておくと、結構機嫌を直しやすいし」"

hide toustaff_a1_1
show toustaff_a1_8 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
Assistant "「…………」"

hide toustaff_b1_1
show toustaff_b1_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
Assistant "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「どうしたの、二人とも？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（何だか笑いを堪えているみたいだけど）"

hide toustaff_a1_8
show toustaff_a1_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
voice tan_f0041
Assistant "「いえ……。\n
だって、なあ？」"

hide toustaff_b1_9
show toustaff_b1_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
voice oto_f0040
Assistant "「グレイ様がナイトメア様の心配をされるときと、まったく同じことをおっしゃるから、つい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「なっ！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（……でも、言われてみれば、確かにそうかも）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "グレイが私にナイトメアのことを頼むときの口調を思い出すと、同じようなことをいつも言われる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（私までお母さん属性が染みついちゃったのかしら）"

hide toustaff_a1_3
show toustaff_a1_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice tan_f0042
Assistant "「大丈夫ですよ、グレイ様もいるんです。\n
ちゃんとお世話をさせて頂きます」"

hide toustaff_b1_2
show toustaff_b1_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice oto_f0041
Assistant "「ええ、お気を付けて」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「うん、じゃあ……」"

hide toustaff_a1_1

hide toustaff_b1_3

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "行ってくると返そうとしたときだ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gray "「[firstname]！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「グレイ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "辺りを見渡し、声の主を探す。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "塔の上の窓から仕事中だったはずの、グレイの姿が見えた。"


play music happy_a_ali

show gre_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gray "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一瞬で噛み合った視線。\n
届くはずのない手が一瞬彼に向かって伸びそうになる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T "（……見送りに来てくれた）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ただそれだけのことが嬉しい。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「行ってくるわ、グレイ」"

hide gre_t_03_3
show gre_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
Gray "「…………」"

hide gre_t_01_13
show gre_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice gra_f0191
Gray "「ああ、行ってらっしゃい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「…………」"

hide gre_t_01_4

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "見送りに来てくれた彼に精一杯の笑顔で応えて。\n
いよいよ私は塔の外へと歩き出した。"

$ hi_mes()

scene map_bg_winter_day
with stripe_l_medium


play music map_winter_jok

scene bg_gen_sky_win_day
with stripe_l_long
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「さて、どこに行こうかしら」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界に住む友人は何人もいるが、しばらく滞在させてもらうことを考えると……。"

$ hi_mes()
$ routechara = "Gray"
scene map_gen_bg with fade
$ show_mes("frame_gen_togaki")
T "Where do I want to visit?"
$ hi_mes()
show screen fushigi_map1
$ ui.interact()
