import sys
import os

'''Try to delete a file until success.
'''
def main():
  while True:
    try:
      os.remove(sys.argv[1])
      break
    except:
      pass

if __name__ == '__main__':
  main()
