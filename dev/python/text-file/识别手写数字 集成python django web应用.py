
# import the necessary packages
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report
from sklearn import datasets
from sklearn.decomposition import PCA as pca
from nolearn.dbn import DBN
from matplotlib import pyplot
from PIL import Image
import numpy as np
import scipy

STANDARD_SIZE = (28, 28)

class DigitProphet(object):
	def __init__(self):
		# load train.csv
		# train = pd.read_csv("data/train.csv")
		# data_train=train.as_matrix()
		# values_train=data_train[:,0]
		# images_train=data_train[:,1:]
		# trainX, _trainX, trainY, _trainY = train_test_split(images_train/255.,values_train,test_size=0.5)

		# #load test.csv
		# test = pd.read_csv("data/test.csv")
		# data_test=test.as_matrix()
		# testX, _testX = train_test_split(data_test/255.,test_size=0.99)
		
		# Random Forest
		# self.clf = RandomForestClassifier()
		
		# Stochastic Gradient Descent
		# self.clf = SGDClassifier()
		
		# Support Vector Machine
		# self.clf = LinearSVC()
		
		# Nearest Neighbors
		# self.clf = KNeighborsClassifier(n_neighbors=13)
		
		
		train = pd.read_csv("data/train.csv")
		data_train=train.as_matrix()
		values_train=data_train[:,0]
		images_train=data_train[:,1:]
		trainX, _trainX, trainY, _trainY = train_test_split(images_train/255.,values_train,test_size=0.995)
		
		# Neural Network
		self.clf = DBN([trainX.shape[1], 300, 10],learn_rates=0.3,learn_rate_decays=0.9,epochs=10,verbose = 1)
		
		#Training
		self.clf.fit(trainX, trainY)
		
		pass

	def predictImage(self,array):
		image=np.atleast_2d(array)
		return self.clf.predict(image)[0]


def trim(image):
	image_data = np.array(image)
	image_data_bw = image_data.min(axis=2)
	row_min = np.where(image_data_bw.min(axis=1)<255)[0].min()
	row_max = np.where(image_data_bw.min(axis=1)<255)[0].max()
	col_min = np.where(image_data_bw.min(axis=0)<255)[0].min()
	col_max = np.where(image_data_bw.min(axis=0)<255)[0].max()
	size=int((max(row_max-row_min,col_max-col_min))*1.3)
	cropBox = (row_min, row_max, col_min, col_max)
	image_data_new = image_data[cropBox[0]:cropBox[1]+1, cropBox[2]:cropBox[3]+1 , :]
	new_image = Image.fromarray(image_data_new)
	
	img_w, img_h = new_image.size
	background = Image.new('RGBA', (size, size), (255, 255, 255, 255))
	bg_w, bg_h = background.size
	offset = ((bg_w-img_w)/2,(bg_h-img_h)/2)
	background.paste(new_image, offset)
	return background

def getimgdata(filename):
	img = Image.open(filename)
	img=alpha_to_color(img)
	img = trim(img)
	img = img.convert('L')
	img = img.getdata()
	img = img.resize(STANDARD_SIZE)
	img = np.array(img)/255.
	img = [1-i for i in img]
	return img
	
def alpha_to_color(image, color=(255, 255, 255)):
    x = np.array(image)
    r, g, b, a = np.rollaxis(x, axis=-1)
    r[a == 0] = color[0]
    g[a == 0] = color[1]
    b[a == 0] = color[2] 
    x = np.dstack([r, g, b, a])
    return Image.fromarray(x, 'RGBA')
		
def saveImage(array,path='outfile.jpg'):
	# Get the training data back to its original form.
	matrix = np.reshape(array, (STANDARD_SIZE))
	# Get the original pixel values.
	matrix = matrix*255. 
	# pyplot.imshow(sample, cmap = pyplot.cm.gray)
	# result=predictImg(clf,image)
	scipy.misc.imsave(path, matrix)
		

dp=DigitProphet()
pointer=0

def main():
	# filename="imageToSave.png"
	# data=getimgdata(filename)
	# saveImage(data)
	# preds=dp.predictImage(data)
	# print preds
	pass
	
	
if __name__ == '__main__':
	main()
