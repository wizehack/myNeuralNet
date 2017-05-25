import numpy
import neural
import scipy.special
import scipy.ndimage
import scipy.misc
import os.path

def train(neuralNetwork, epochs, data_path):
	train_data_file = open(data_path, 'r')
	train_data_list = train_data_file.readlines()
	train_data_file.close()

	for e in range(epochs):
		for record in train_data_list:
			all_values = record.split(",")

			targets = numpy.zeros(o) + 0.01
			targets[int(all_values[0])] = 0.99

			inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
			neuralNetwork.learn(inputs, targets)
			pass
		pass
	pass

def query(neuralNetwork, correct_label):

	basic_path = "./mnist/mnist_png/testing/"
	results = []

	for n in range(0, 10000):
		full_path = basic_path + str(correct_label) + "/" + str(n) + ".png"
		while os.path.isfile(full_path):
			img_array = scipy.misc.imread(full_path, flatten=True)
			img_data = img_array.reshape(784)
			inputs = (img_data / 255.0 * 0.99) + 0.01
			outputs = neuralNetwork.reason(inputs)
			label = numpy.argmax(outputs)

#			print("path: ", full_path)
#			print("correct label", correct_label)
#			print("result: ", label)

			if (label == correct_label) :
				results.append(1)
			else:
				results.append(0)
			break
		pass
	return results;


def evaluate(results):
	result_array = numpy.asarray(results)
	score = result_array.sum() / result_array.size
	print("total: ", result_array.size)
	print("success: ", result_array.sum())
	print("failure: ", result_array.size - result_array.sum())
	return score


if __name__ == "__main__":
	i = 784
	h = 200
	o = 10
	r = 0.1

	n = neural.NeuralNetwrok(i, h, o, r)

	print(" ############ learning ############ ")
	# availalbe at https://pjreddie.com/media/files/mnist_train.csv
	train(n, 5, "./csv/mnist_train.csv")

	for num in range(1, 10):
		results = query(n, num)
		print(" ############ evaluation ############ ")
		print("label: ", num)
		print("score: ", evaluate(results))
