from pythainlp.tokenize import word_tokenize

# ประโยคที่ต้องการตัดคำ
sentence = "สวัสดีครับ ยินดีที่ได้พบคุณ"

# ใช้ฟังก์ชัน word_tokenize เพื่อตัดคำ
tokens = word_tokenize(sentence, engine='newmm')

test_arr = tokens[:]

# พิมพ์ผลลัพธ์
print(test_arr[0],test_arr[1])
