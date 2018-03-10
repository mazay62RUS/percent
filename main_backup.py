import matplotlib.pyplot as plt
import os

class Percent:

	### __ Сложные проценты __ ###

	os.system("color 02")

	def initHardPercent(self):
		self.sumForHardPercent 	   = float(input("Введите сумму вклада: "))
		self.percentForHardPercent = float(input("Введите процент: "))
		self.timeForHardPercent	   = int(input("Введите время (в месяцах): "))
		print("Сумма вклада = " + str(round(self.hardPercent(self.sumForHardPercent, self.percentForHardPercent, self.timeForHardPercent), 2)) + " RUR")
		self.buildGraphicForHardPercent(self.sumForHardPercent, self.percentForHardPercent, self.timeForHardPercent)

	def hardPercent(self, sumForHardPercent, percentForHardPercent, timeForHardPercent):
		k = sumForHardPercent * (1 + percentForHardPercent / 100) ** (timeForHardPercent)
		return k

	def buildGraphicForHardPercent(self, sumForHardPercent, percentForHardPercent, timeForHardPercent):
		x = []
		y = []

		for i in range(timeForHardPercent + 1):
			x.append(i)
			k = self.hardPercent(sumForHardPercent, percentForHardPercent, i)
			y.append(k)

		plt.plot(x,y)
		plt.xlabel("Время (в месяцах)")
		plt.ylabel("Накопившиеся сумма (в рублях)")
		plt.show()

	### __ Простые проценты __ ###

	def initSimplePercent(self):
		self.sumForSimplePercent	 = float(input("Введите сумму вклада: "))
		self.percentForSimplePercent = float(input("Введите процент: "))
		self.timeForSimplePercent    = int(input("Введите время (в месяцах): "))
		print("Сумма вклада = " + str(round(self.simplePercent(self.sumForSimplePercent, self.percentForSimplePercent, self.timeForSimplePercent), 2)) + " RUR")
		self.buildGraphicForSimplePercent(self.sumForSimplePercent, self.percentForSimplePercent, self.timeForSimplePercent)

	def simplePercent(self, sumForSimplePercent, percentForSimplePercent, timeForSimplePercent):
		k = sumForSimplePercent * (1 + (percentForSimplePercent / 100) * (timeForSimplePercent / 12))
		return k

	#def buildGraphic(self,)

	def buildGraphicForSimplePercent(self, sumForSimplePercent, percentForSimplePercent, timeForSimplePercent):
		x = []
		y = []

		for i in range(timeForSimplePercent + 1):
			x.append(i)
			Sum = self.simplePercent(sumForSimplePercent, percentForSimplePercent, i)
			y.append(Sum)

		plt.plot(x,y)
		plt.xlabel("Время (в месяцах)")
		plt.ylabel("Накопившиеся сумма (в рублях)")
		plt.title("График значения вклада в определенный месяц")
		plt.show()

def main():
	percent = Percent()
	
	try:
		state = str(input("Выберите сложные проценты (h) или простые проценты (s) (h or s): "))

		if state == 'h':
			percent.initHardPercent()
		if state == 's':
			percent.initSimplePercent()
		else:
			print("Введенно недопустимое значение!")
			main()
	except KeyboardInterrupt:
		print("\nВыход из программы.")
	except OverflowError:
		print("Введенно слишком большое значение!")
		main()
	except ValueError:
		print("Введенно число!")
		main()

if __name__ == "__main__":
	main()
