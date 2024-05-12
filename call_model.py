import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

# โหลดโมเดล
model = load_model('my_model.h5')

# โหลด tokenizer จากไฟล์ pickle
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

# เตรียมข้อความที่ต้องการทำนาย
texts = ["ยกระดับอาหารไทย", "ส่งเสริมๆ"]

# แปลงข้อความเป็นลิสต์ของตัวเลข (sequences)
sequences = tokenizer.texts_to_sequences(texts)

# กำหนดความยาวของ sequences เท่ากับความยาวที่ใช้ในการฝึกโมเดล
max_sequence_length = 100


# ทำ padding ข้อมูล
padded_sequences = pad_sequences(sequences, maxlen=max_sequence_length, padding='post')

# ทำการทำนาย
predictions = model.predict(padded_sequences)

# แปลงผลลัพธ์ที่ได้ให้อ่านง่ายขึ้น
predicted_label = np.argmax(predictions[0])

# แสดงผลลัพธ์
print("Predicted Label:", predicted_label)
