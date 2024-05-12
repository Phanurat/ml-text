import random

null = ""
Sub = ["นายก", "คุณเศรษฐา", "นายกนิด", "นายกเศรษฐา", 'คุณนิด', 'ท่านนายก', 'เพื่อไทย']
Vis = ["เก่งจังเลย", "เยื่อมมากเลย", "ทำดีตลอด", "มีความผู้นำจริงๆ", "เหนื่อยแทนประชาชน", "ดูแลตัวเองด้วยนะ", "เก่งๆ ยอมเลย"]
Noun = "ชาติ"
Pnoun = "เรา"
Act = "ตก"

def random_Box_Sub(Sub):
    random_Sub = random.sample(Sub, len(Sub))
    return random_Sub

def random_Box_Vis(Vis, length):
    min_length = min(len(Vis), length)
    random_Vis = random.sample(Vis, min_length)
    return random_Vis

random_Sub = random_Box_Sub(Sub)
random_Vis = random_Box_Vis(Vis, len(random_Sub))

for i in range(len(random_Sub)):
    if random_Sub[i] != null:
        if random_Vis and random_Vis[i] != null:
            print(random_Sub[i], random_Vis[i])
        else:
            print(random_Sub[i])
