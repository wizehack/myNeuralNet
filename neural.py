import numpy
import math
import scipy.special as mathEx

class NeuralNetwrok:

	def __init__(self, iNodes, hNodes, oNodes, lRate):
		self.inputNodes = iNodes
		self.hiddenNodes = hNodes
		self.outputNodes = oNodes
		self.learningRate = lRate
		self.wih = numpy.random.normal(0.0, 1/math.sqrt(self.hiddenNodes), (self.hiddenNodes, self.inputNodes))
		self.who = numpy.random.normal(0.0, 1/math.sqrt(self.outputNodes), (self.outputNodes, self.hiddenNodes))

		self.activationFunction = lambda x: mathEx.expit(x) # sigmoid function
		pass


	def learn(self, inp, tar):
		inputs = numpy.array(inp, ndmin=2).T
		targets = numpy.array(tar, ndmin=2).T

		outputs = self.reason(inp)

		outErrors = targets - outputs
		hiddenErrors = numpy.dot(self.who.T, outErrors)

		d_outError = numpy.dot((-1) * outErrors * outputs * (1-outputs), self.hidden_outputs.T)
		d_hiddenError = numpy.dot( (-1) * hiddenErrors * self.hidden_outputs * (1-self.hidden_outputs), inputs.T)

		self.who = self.who - (self.learningRate * d_outError);
		self.wih = self.wih - (self.learningRate * d_hiddenError);

		pass


	def reason(self, q):
		inputs = numpy.array(q, ndmin=2).T
		hidden_inputs = numpy.dot(self.wih, inputs)
		self.hidden_outputs = self.activationFunction(hidden_inputs)
		outputs_tmp = numpy.dot(self.who, self.hidden_outputs)
		outputs = self.activationFunction(outputs_tmp)

		return outputs
