
class TF:
	def __init__(self, K, I):
		self.K_gain = K
		self.I_gain = I
		self.Integral_sum = 0
		
	
	def transfer(self, error):
		output = self.K_gain * error
		output = output + self.I_gain * self.Integral_sum
		self.Integral_sum += output
		return output
