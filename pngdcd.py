import sys
if __name__ == "__main__":
    try:
        name = sys.argv[1]
    except:
        print "Usage: pngdcd.py [filename] [verbose(optional)]"
        sys.exit(1)
    try:
        verbose = sys.argv[2]
    except:
        verbose = 0
    ifile = open(name+'.png','rb')
    data = ifile.read(32*32)
    picraw = []
    while data:
        #print data.encode('hex')
        picraw.append(data.encode('hex'))
        data = ifile.read(32*32)

    ifile.close()
    '''
    png file signature
    137 80 78 71 13 10 26 10
    89 50 4e 47 0d 0a 1a 0a

    ihdr
    49 48 44 52
    73 72 68 82
    plte
    80 76 84 69
    50 4c 54 45
    idat
    73 68 65 84
    49 44 41s 54
    iend
    73 69 78 68
    49 45 4e 44
    '''

    pictot = ''.join(picraw)

    '''pic = {}
    pic.update({'sig': pictot[:16]})
    print pic['sig']
    was going to make dict but, i have multiple idats'''
    pic = [pictot[:16]]
    pic.append(pictot[16:24])
    print pic[0]
    q=8*2
    r=4*2
    z=0
    size=8
    if (verbose):
        ofile = open(name+'VERBOSE.txt', 'w')
    else:
        ofile = open(name+'.txt', 'w')
    ofile.write(pic[0])
    for i in range(len(pictot)):
              temp = []
              i=q
              temp.append(pictot[q:q+r])#length
              try:
                  z=int(temp[0],16)*2
              except:
                  break;
              temp.append(pictot[q+r:q+(2*r)])#type
              temp.append(pictot[q+(2*r):q+(2*r)+z])#data
              temp.append(pictot[q+(2*r)+z:q+(3*r)+z])#CRC
              q=q+(3*r)+z
              size += (z/2)+12
              pic.append(temp)
              print '{}, {}, {}||{}+12'.format(temp[0], temp[1], temp[3],(z/2))
              ofile.write('\n{}, {}, {}||{}+12'.format(temp[0], temp[1], temp[3],(z/2)))
              if (verbose):
                  ofile.write('\n'+temp[2])
              if (temp[1]=='49454e44'):#iEND
                  print size
                  ofile.write('\n{}'.format(size))
                  print pictot[q:]
                  ofile.write('\n'+pictot[q:])
                  size += len(pictot[q:])
                  break;
    print size
    ofile.write('\n{}'.format(size))
    ofile.close()
