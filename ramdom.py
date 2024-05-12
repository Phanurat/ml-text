import random
import pandas as pd
import os

null = ""
Sub = ["นายก", "คุณเศรษฐา", "นายกนิด", "นายกเศรษฐา", 'คุณนิด', 'ท่านนายก', 'เพื่อไทย']
Vis = ["เก่งจังเลย", "เยี่ยมมากเลย", "ทำดีตลอด", "มีความผู้นำจริงๆ", "เหนื่อยแทนประชาชนตลอด", "ดูแลตัวเองด้วยนะ", "เก่งๆ ยอมเลย", "โคตะระเป็นทุกอย่างเลย"]
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

data = []
for i in range(len(random_Sub)):
    if random_Sub[i] != null:
        if random_Vis and random_Vis[i] != null:
            data.append([random_Sub[i] + random_Vis[i]])
        else:
            data.append([random_Sub[i]])

# ตรวจสอบว่าไฟล์ 'output.xlsx' มีอยู่หรือไม่
if os.path.isfile("output.xlsx"):
    existing_data = pd.read_excel("output.xlsx")
else:
    existing_data = pd.DataFrame()

new_data = pd.DataFrame(data, columns=["Combined"])
combined_data = pd.concat([existing_data, new_data])

combined_data.to_excel("output.xlsx", index=False)
