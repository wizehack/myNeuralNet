import numpy
import neural
import scipy.special
import scipy.misc
# import scipy.ndimage

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

		#	curv_plus_ten_degree_inputs = scipy.ndimage.interpolation.rotate(inputs.reshape(28,28), 10, cval=0.01, order=1, reshape=False)
		#	neuralNetwork.learn(curv_plus_ten_degree_inputs.reshape(784), targets)

		#	curv_minus_ten_degree_inputs = scipy.ndimage.interpolation.rotate(inputs.reshape(28,28), -10, cval=0.01, order=1, reshape=False)
		#	neuralNetwork.learn(curv_minus_ten_degree_inputs.reshape(784), targets)
			pass
		pass
	pass


def query(neuralNetwork, data_path, correct_label):

	img_array = scipy.misc.imread(data_path, flatten=True)
	img_data = 255.0 - img_array.reshape(784)
	inputs = (img_data / 255.0 * 0.99) + 0.01
	outputs = neuralNetwork.reason(inputs)

	label = numpy.argmax(outputs)

	return label


def evaluate(results):
	result_array = numpy.asarray(results)
	score = result_array.sum() / result_array.size
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

	results = []

	for correct_label in range(2, 7):
		data_path = "./img/" + str(correct_label) + ".png"
		label = query(n, data_path, correct_label)

		print(" ############ reasoning ############ ")
		print("correct label: ", correct_label)
		print("output: ", label)
		if (label == correct_label) :
			results.append(1)
		else:
			results.append(0)
		pass

	print(" ############ evaluation ############ ")

	print("score: ", evaluate(results))
