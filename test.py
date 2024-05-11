import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
import pickle
import os

# โหลดโมเดล
model = load_model('my_model.h5')

# ตรวจสอบว่าไฟล์ tokenizer.pickle มีอยู่หรือไม่
if os.path.exists('tokenizer.pickle'):
    # โหลด tokenizer
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
else:
    # ข้อมูลตัวอย่าง
    texts = ["ดีใจด้วย", "เป็นกำลังใจ"]

    # สร้าง tokenizer
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(texts)

    # บันทึก tokenizer เป็นไฟล์
    with open('tokenizer.pickle', 'wb') as handle:
        pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

# เพิ่มข้อความภาษาไทยที่ต้องการทดสอบ
test_texts = ["ดีใจ"]

# แปลงข้อความเป็นตัวเลข
test_sequences = tokenizer.texts_to_sequences(test_texts)
max_sequence_length = max([len(seq) for seq in test_sequences])
test_padded_sequences = pad_sequences(test_sequences, maxlen=max_sequence_length, padding='post')
# ตรวจสอบข้อมูล test_texts
print(tokenizer.texts_to_sequences(test_texts))


# ทำการทำนาย
predictions = model.predict(test_padded_sequences)
predicted_label = np.argmax(predictions[0])

# แสดงผลลัพธ์
print("Predicted Label:", predicted_label)
