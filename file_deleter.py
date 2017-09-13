import sys
import os


def main():
	while True:
		try:
			os.remove(sys.argv[1])
			break
		except:
			pass


if __name__ == '__main__':
	main()
