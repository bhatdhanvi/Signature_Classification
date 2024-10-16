import tensorflow as tf
import numpy as np
from google.colab import drive
drive.mount('/content/gdrive')
train_path='/content/gdrive/MyDrive/dataset/train'
test_path='/content/gdrive/MyDrive/dataset/test'
val_ds=tf.keras.utils.image_dataset_from_directory(test_path,image_size=(100,100),batch_size=20)
train_ds=tf.keras.utils.image_dataset_from_directory(train_path,image_size=(100,100),batch_size=20)
train_ds.prefetch(1)
class_names=train_ds.class_names
num_classes=len(class_names)
print(class_names)
print(num_classes)
import matplotlib.pyplot as plt
plt.figure(figsize=(10,10))
for img,label in val_ds.take(1):
for i in range(4):
ax=plt.subplot(2,2,i+1)
plt.imshow(img[i].numpy().astype("uint8"))
plt.title(class_names[label[i]])
plt.axis("off")
norm_layer=tf.keras.layers.experimental.preprocessing.Rescaling(1./255)
zoom_layer=tf.keras.layers.experimental.preprocessing.RandomZoom(height_factor=(0.1,0.3))rot_layer=tf.keras.layers.experimental.preprocessing.RandomRotation(factor=0.2)
from keras.layers import
Conv2D,MaxPooling2D,Input,Flatten,Dense,BatchNormalization,Dropout
from keras.models import Sequential



def get_model(num_classes):
model = Sequential([norm_layer,zoom_layer,rot_layer,Conv2D(16, (5, 5), padding='same', activation='relu'),MaxPooling2D((2,2)),BatchNormalization(),Dropout(0.3),
Conv2D(16, (3, 3), padding='same', activation='relu'),MaxPooling2D((2,2), strides=(2,2)),Dropout(0.3),Flatten(),Dense(256, activation='relu'),Dropout(0.5),Dense(num_classes, activation='softmax')])
model.compile(optimizer=tf.keras.optimizers.Adam(1e-4),
loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=
False, reduction='auto'),
metrics=['accuracy'])

return model
model = get_model(num_classes)
history=model.fit(train_ds,validation_data=val_ds,epochs=50)
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(12,5))
fig.add_subplot(121)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Loss vs.epochs')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Training','Validation'],loc='best')
fig.add_subplot(122)
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Accuracy vs.epochs')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Training','Validation'],loc='best')
plt.show()
from keras.utils.np_utils import to_categorical
from tensorflow.keras.preprocessing.image import
ImageDataGenerator
test_datagen = ImageDataGenerator()



test_ds = test_datagen.flow_from_directory(
test_path,
target_size=(100,100),
batch_size =1,class_mode ='categorical',
color_mode ="rgb",
shuffle=False,
)
test_ds.reset()
predictions=model.predict(test_ds,steps=len(test_ds.filenames),v
erbose=1)
import pandas as pd
predicted_class_indices=np.argmax(predictions,axis=1)
labels=(test_ds.class_indices)
labels=dict((v,k) for k,v in labels.items())
pred_labels=[labels[k] for k in predicted_class_indices]
filenames=test_ds.filenames
results=pd.DataFrame({"Filename":filenames,"Predictions":pred_la
bels})
results.tail(110)
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import seaborn as sns

Y_pred = model.predict_generator(test_ds,120)
y_pred = np.argmax(Y_pred, axis=1)
target_names = ['Abdul','Alisha','Bhamini','Dhanvi']
cm = confusion_matrix(test_ds.classes, y_pred )
sns.heatmap(cm, annot=True, cmap='Blues',
xticklabels=target_names, yticklabels=target_names)
plt.xlabel('Predicted labels')
plt.ylabel('True labels')
plt.show()
print('Classification Report')
print(classification_report(test_ds.classes, y_pred,
target_names=target_names))
