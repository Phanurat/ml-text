import random

name = "นักเรียน"
Sub = ["", "นักเรียน", "ทหาร", "นักเรียน"]
Vis = ""
Noun = "ชาติ"
Pnoun = "เรา"
Act = "ตก"

def random_box(Sub):
    random_Sub = random.choice(Sub)
    return random_Sub

random_Sub = random_box(Sub)
print("Random word:", random_Sub)
