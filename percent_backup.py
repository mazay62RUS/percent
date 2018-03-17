import matplotlib.pyplot as plt
import os

class Percent:

		def __init__(self):
			self.Sum 	= float(input("Введите сумму вклада: "))
			self.percent = float(input("Введите процент: "))
			self.time	= int(input("Введите время (в годах): "))

	### === PRIVATE === ###

		### __ Вспомогательные функции __ ###

		def __checkValue(self, summ, percent, time): 
			if summ or percent or time < 0:
				return 0
			else:
				return 1

		def __init(self, Sum, percent, time, typeOfPercent):

			check = self.__checkValue(Sum, percent, time)
			if check == 0: 
				print("значения должны быть больше нуля") 
				raise SystemExit(1)
			if typeOfPercent == 0:
				print("Сумма вклада = " + str(round(self.__hardPercent(Sum, percent, time), 2)) + " RUR")
			elif typeOfPercent == 1:
				print("Сумма вклада = " + str(round(self.__simplePercent(Sum, percent, time), 2)) + " RUR")

		### __ Вспомогательные функции для сложных процентов __ ###

		def __hardPercent(self, sumForHardPercent, percentForHardPercent, timeForHardPercent):
			Sum = sumForHardPercent * (1 + percentForHardPercent / 100) ** (timeForHardPercent)
			return Sum

		def __buildGraphicForHardPercent(self, sumForHardPercent, percentForHardPercent, timeForHardPercent):
			x = []
			y = []

			for i in range(timeForHardPercent + 1):
				x.append(i)
				Sum = self.__hardPercent(sumForHardPercent, percentForHardPercent, i)
				y.append(Sum)

			plt.plot(x,y)
			plt.xlabel("Время (в годах)")
			plt.ylabel("Накопившиеся сумма (в рублях)")
			plt.show()

		### __ Вспомогательные функции для простых процентов __ ###

		def __simplePercent(self, sumForSimplePercent, percentForSimplePercent, timeForSimplePercent):
			Sum = sumForSimplePercent * (1 + (percentForSimplePercent / 100) * (timeForSimplePercent / 12))
			return Sum

		def __buildGraphicForSimplePercent(self, sumForSimplePercent, percentForSimplePercent, timeForSimplePercent):
			x = []
			y = []

			for i in range(timeForSimplePercent + 1):
				x.append(i)
				Sum = self.__simplePercent(sumForSimplePercent, percentForSimplePercent, i)
				y.append(Sum)

			plt.plot(x,y)
			plt.xlabel("Время (в годах)")
			plt.ylabel("Накопившиеся сумма (в рублях)")
			plt.title("График значения вклада в определенный год")
			plt.show()

	### === PRIVATE END === ###

	### === PUBLIC === ###

		### __ Сложные проценты __ ###

		def initHardPercent(self, state):
			self.__init(self.Sum, self.percent, self.time, 0)
			if state == 1:
				self.__buildGraphicForHardPercent(self.Sum, self.percent, self.time)
			else:
				print("Завершение программы.")

		### __ Простые проценты __ ###

		def initSimplePercent(self, state):
			self.__init(self.Sum, self.percent, self.time, 1)
			if state == 1: 
				self.__buildGraphicForSimplePercent(self.Sum, self.percent, self.time)
			else:
				print("Завершение программы.")

	### === PUBLIC END === ###