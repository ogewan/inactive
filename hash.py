import sys
import hashlib
if __name__ == "__main__":
    f = open(sys.argv[1], 'r')
    a = hashlib.md5()
    a.update(f.read())
    print a.hexdigest()
    f.close()
