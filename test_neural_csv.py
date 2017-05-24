import numpy
import neural


def train(neuralNetwork, epochs, data_path):
	train_data_file = open(data_path, 'r')
	train_data_list = train_data_file.readlines()
	train_data_file.close()

	for e in range(epochs):
		for record in train_data_list:
			all_values = record.split(",")
			inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
			targets = numpy.zeros(o) + 0.01
			targets[int(all_values[0])] = 0.99
			neuralNetwork.learn(inputs, targets)
			pass
		pass
	pass


def test(neuralNetwork, data_path):
	data_file = open(data_path, 'r')
	data_list = data_file.readlines()
	data_file.close()

	results = []

	for record in data_list:
		all_values = record.split(",")
		target = int(all_values[0])
		inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
		outputs = neuralNetwork.reason(inputs)

		label = numpy.argmax(outputs)

		if (label == target) :
			results.append(1)
		else:
			results.append(0)
	return results


def evaluate(results):
	result_array = numpy.asarray(results)
	score = result_array.sum() / result_array.size

	print(" ############ evaluation ############ ")
	print("Total: ", result_array.size)
	print("Success: ", result_array.sum())
	print("Failure: ", result_array.size - result_array.sum())
	return score


if __name__ == "__main__":
	i = 784
	h = 200
	o = 10
	r = 0.1

	n = neural.NeuralNetwrok(i, h, o, r)

	print(" ############ initial setting ############ ")
	print("weight of input_hidden: ")
	print(n.wih)
	print("weight of hidden_output: ")
	print(n.who)

	print(" ############ learning ############ ")

	# availalbe at https://pjreddie.com/media/files/mnist_train.csv
	train(n, 5, "./csv/mnist_train.csv")

	print("weight of input_hidden: ")
	print(n.wih)
	print("weight of hidden_output: ")
	print(n.who)

	print(" ############ reasoning ############ ")

	# availalbe at https://pjreddie.com/media/files/mnist_test.csv
	results = test(n, "./csv/mnist_test.csv")

	print("score: ", evaluate(results))
