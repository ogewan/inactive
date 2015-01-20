#scadr - generate scad file from shape and scale
#Seun Ogedengbe
#Digital Fabrication
#Lab 2
import sys
if __name__ == "__main__":
    try:
        sh = sys.argv[1].lower()
        sc = sys.argv[2]
    except:
        print "Usage: scadr.py [shape] [scale]"
        sys.exit(1)
    if int(sc) <= 0:
        print "scale must be greater than zero"
        sc = 1
    sc = str(sc)
    gold = "p = ((1 + sqrt(5))/2);\n"
    sfac = "a = "+sc+";\nscale([a,a,a]) polyhedron(points=["
    if sh == "icosahedron":
        f = open('icosa.scad', 'w')
        f.write(gold+sfac+"[p,1,0], [-p,1,0], [-p,-1,0], [p,-1,0], [0,-p,1], [0,p,1], [0,p,-1], [0,-p,-1], [1,0,p], [-1,0,p], [-1,0,-p], [1,0,-p] ], faces=[ [0,8,5], [0,5,6], [0,6,11], [0,11,3], [0,3,8], [3,4,8], [3,11,7], [3,7,4], [9,8,4], [9,4,2], [7,2,4], [7,11,10], [7,10,2], [11,6,10], [1,10,6], [1,2,10], [1,9,2], [1,6,5], [5,8,9], [5,9,1] ]);")
    elif sh == "dodecahedron":
        f = open('dodeca.scad', 'w')
        f.write(gold+sfac+"[1,1,1], [1,-1,1], [-1,-1,1], [-1,1,1], [-1,1,-1], [1,1,-1], [1,-1,-1], [-1,-1,-1], [p,0,(1/p)], [-p,0,(1/p)], [-p,0,(-1/p)], [p,0,(-1/p)], [(1/p),p,0], [(1/p),-p,0], [(-1/p),-p,0], [(-1/p),p,0], [0,(1/p),p], [0,(1/p),-p], [0,(-1/p),-p], [0,(-1/p),p]], faces=[ [8,1,19,16,0], [8,0,12,5,11], [8,11,6,13,1], [6,11,5,17,18], [5,12,15,4,17], [17,4,10,7,18], [2,14,7,10,9], [14,2,19,1,13], [6,18,7,14,13], [16,19,2,9,3], [16,3,15,12,0], [9,10,4,15,3] ]);")
    elif sh == "octahedron":
        f = open('octa.scad', 'w')
        f.write(sfac+"[0,0,2], [2,0,0], [0,2,0], [0,-2,0], [-2,0,0], [0,0,-2] ], faces=[ [0,4,2], [5,2,4], [0,2,1], [5,1,2], [0,1,3], [5,3,1], [0,3,4], [5,4,3] ]);")
    elif sh == "cube":
        f = open('cube.scad', 'w')
        f.write(sfac+"[1,1,1], [1,-1,1], [-1,-1,1], [-1,1,1], [-1,1,-1], [1,1,-1], [1,-1,-1], [-1,-1,-1] ], faces=[ [0,1,2,3], [4,7,6,5], [0,5,6,1], [4,5,0,3], [2,7,4,3], [6,7,2,1], ]);")
    else:
        if sh != "tetrahedron":
            print "shape must be a platonic solid: Tetrahedron, Cube, Octahedron, Dodecahedron, or Icosahedron"
        f = open('tetra.scad', 'w')
        f.write(sfac+"[1,1,1], [-1,-1,1], [-1,1,-1], [1,-1,-1] ], faces=[ [0,3,1], [0,1,2], [0,2,3], [1,3,2] ]);")
    f.close()
