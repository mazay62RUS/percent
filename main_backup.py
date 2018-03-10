import matplotlib.pyplot as plt
import os

class Percent:

	### __ ������ ��業�� __ ###

	os.system("color 02")

	def initHardPercent(self):
		self.sumForHardPercent 	   = float(input("������ �㬬� ������: "))
		self.percentForHardPercent = float(input("������ ��業�: "))
		self.timeForHardPercent	   = int(input("������ �६� (� ������): "))
		print("�㬬� ������ = " + str(round(self.hardPercent(self.sumForHardPercent, self.percentForHardPercent, self.timeForHardPercent), 2)) + " RUR")
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
		plt.xlabel("�६� (� ������)")
		plt.ylabel("�������訥�� �㬬� (� �㡫��)")
		plt.show()

	### __ ����� ��業�� __ ###

	def initSimplePercent(self):
		self.sumForSimplePercent	 = float(input("������ �㬬� ������: "))
		self.percentForSimplePercent = float(input("������ ��業�: "))
		self.timeForSimplePercent    = int(input("������ �६� (� ������): "))
		print("�㬬� ������ = " + str(round(self.simplePercent(self.sumForSimplePercent, self.percentForSimplePercent, self.timeForSimplePercent), 2)) + " RUR")
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
		plt.xlabel("�६� (� ������)")
		plt.ylabel("�������訥�� �㬬� (� �㡫��)")
		plt.title("��䨪 ���祭�� ������ � ��।������ �����")
		plt.show()

def main():
	percent = Percent()
	
	try:
		state = str(input("�롥�� ᫮��� ��業�� (h) ��� ����� ��業�� (s) (h or s): "))

		if state == 'h':
			percent.initHardPercent()
		if state == 's':
			percent.initSimplePercent()
		else:
			print("�������� �������⨬�� ���祭��!")
			main()
	except KeyboardInterrupt:
		print("\n��室 �� �ணࠬ��.")
	except OverflowError:
		print("�������� ᫨誮� ����讥 ���祭��!")
		main()
	except ValueError:
		print("�������� �᫮!")
		main()

if __name__ == "__main__":
	main()
