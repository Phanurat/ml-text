import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.models import Sequential

# ข้อมูลตัวอย่าง
texts = ["ดีใจด้วย", "เป็นกำลังใจ"]

# แปลงข้อความเป็นตัวเลข
tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)
max_sequence_length = max([len(seq) for seq in sequences])
padded_sequences = pad_sequences(sequences, maxlen=max_sequence_length, padding='post')

# สร้างโมเดล RNN
model = Sequential([
    Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=64, input_length=max_sequence_length),
    LSTM(64),
    Dense(len(tokenizer.word_index) + 1, activation='softmax')
])

# คอมไพล์และฝึกโมเดล
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(padded_sequences, np.array([0, 1]), epochs=10)

# บันทึกโมเดล
model.save('my_model.h5')

# ทดสอบโมเดล
test_texts = ["ดีใจ", "เป็นกำลังใจ", "ยินดี", "สุขใจ"]
test_sequences = tokenizer.texts_to_sequences(test_texts)
test_padded_sequences = pad_sequences(test_sequences, maxlen=max_sequence_length, padding='post')

# โหลดโมเดล
from tensorflow.keras.models import load_model
loaded_model = load_model('my_model.h5')

# ทำการทดสอบโมเดลที่โหลด
predictions = loaded_model.predict(test_padded_sequences)
predicted_labels = np.argmax(predictions, axis=1)
print("Predicted Labels:", predicted_labels)
