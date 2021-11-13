label gakuen_friend_check_castle:
    if gakuen_dormitory_tower_not2a_seen == True:
        jump gakuen_friend_tower
    if gakuen_dormitory_hatter_not5a_seen == True:
        jump gakuen_friend_hatter
    if gakuen_dormitory_amuse_not4a_seen == True:
        jump gakuen_friend_amuse
    if routechara == "Vivaldi":
        jump gakuen_vivaldi2
    if routechara == "Peter":
        jump gakuen_peter2
    if routechara == "Ace":
        jump gakuen_ace2
label gakuen_friend_check_hatter:
    if gakuen_dormitory_tower_not2a_seen == True:
        jump gakuen_friend_tower
    if gakuen_dormitory_amuse_not4a_seen == True:
        jump gakuen_friend_amuse
    if gakuen_dormitory_castle_not2a_seen == True:
        jump gakuen_friend_castle
    if routechara == "Blood":
        jump gakuen_blood2
    if routechara == "Elliot":
        jump gakuen_elliot2
    if routechara == "Deedam":
        jump gakuen_dad2
label gakuen_friend_check_amuse:
    if gakuen_dormitory_tower_not2a_seen == True:
        jump gakuen_friend_tower
    if gakuen_dormitory_hatter_not5a_seen == True:
        jump gakuen_friend_hatter
    if gakuen_dormitory_castle_not2a_seen == True:
        jump gakuen_friend_castle
    if routechara == "Gowland":
        jump gakuen_gowland2
    if routechara == "Boris":
        jump gakuen_boris2
    if routechara == "Pierce":
        jump gakuen_pierce2

label gakuen_friend_check_tower:
    if gakuen_dormitory_amuse_not4a_seen == True:
        jump gakuen_friend_amuse
    if gakuen_dormitory_hatter_not5a_seen == True:
        jump gakuen_friend_hatter
    if gakuen_dormitory_castle_not2a_seen == True:
        jump gakuen_friend_castle
    if routechara == "Nightmare":
        jump gakuen_nightmare2
    if routechara == "Gray":
        jump gakuen_gray2
    if routechara == "Julius":
        jump gakuen_julius2
    if routechara == "Joker":
        jump gakuen_joker2
