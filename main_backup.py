﻿from percent_backup import * 

def main():
	os.system("color 02")
	
	try:
		state = str(input("Выберите сложные проценты (1) или простые проценты (0) (1 or 0): "))
		isBuildGraphic = int(input("строить график ? (1 or 0): "))
		percent = Percent()
		if state == '1':
			if isBuildGraphic == 1:
				percent.initHardPercent(1)
			else:
				percent.initHardPercent(0)
		elif state == '0':
			if isBuildGraphic == 1:
				percent.initSimplePercent(1)
			else:
				percent.initSimplePercent(0)
		else:
			print("Введенно недопустимое значение!")
			main()
	except SystemExit:
		main()
	except KeyboardInterrupt:
		print("\nВыход из программы.")
	except OverflowError:
		print("Введенно слишком большое значение!")
		main()
	except ValueError:
		print("Введенна строка!")
		main()

if __name__ == "__main__":
	main()