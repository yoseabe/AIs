import tensorflow as tf
import pandas as pd

dataset = pd.read_csv("cancer.csv")
test_data = dataset.drop(columns=["diagnosis(1=m, 0=b)"])

model = tf.keras.models.load_model("cancerChecker.h5")
predictions = model.predict(test_data)

print(len(predictions))
l = 1
for i in range(0, len(predictions)):
	l = l+1
	if(predictions[i] < 0.5):
		print(f"{l} Prediction: Does not Spread")
	else:
		print(f"{l} Prediction: Spread")
	
	





