import random
import pandas as pd
import os

null = ""
# อ่านข้อมูล Sub
with open('data/sub.txt', 'r', encoding='utf-8') as f:
    Sub = f.readlines()

# อ่านข้อมูล Vis
with open('data/vis.txt', 'r', encoding='utf-8') as f:
    Vis = f.readlines()

# ลบช่องว่างหรือ newline character ออกจากแต่ละบรรทัด
Sub = [line.strip() for line in Sub]
Vis = [line.strip() for line in Vis]

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
