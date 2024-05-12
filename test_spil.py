from pythainlp.tokenize import word_tokenize

# ประโยคที่ต้องการตัดคำ
sentence = "ไทยเพื่อนี้ทำอะไรให้ประเทศไทยเยอะมาก พัฒณาต่อไปนะ"

# ใช้ฟังก์ชัน word_tokenize เพื่อตัดคำ
tokens = word_tokenize(sentence, engine='newmm')

test_arr = tokens[:]

# พิมพ์ผลลัพธ์
print(test_arr[0],test_arr[1])
     