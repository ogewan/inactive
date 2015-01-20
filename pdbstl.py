#pdbstl - generate stl file from PDB and scale
#Seun Ogedengbe
#Digital Fabrication
#Lab 2
import sys
import math

def dodca(x,y,z,sc):
        #translate to x y z scale to sc
        p=((1 + math.sqrt(5))/2)
        asc = int(p*int(sc))
        bsc = int(int(sc)/p)
        csc = int(2*int(sc))
        return "  facet normal 1.73121e-008 -0.850651 0.525731\n    outer loop\n      vertex "+str(0+x)+" "+str(-bsc+y)+" "+str(asc+z)+"\n      vertex "+str(bsc+x)+" "+str(-asc+y)+" "+str(0+z)+"\n      vertex "+str(sc+x)+" "+str(-sc+y)+" "+str(sc+z)+"\n    endloop\n  endfacet\n  facet normal 0.525731 -1.73121e-008 0.850651\n    outer loop\n      vertex "+str(0+x)+" "+str(-bsc+y)+" "+str(asc+z)+"\n      vertex "+str(sc+x)+" "+str(-sc+y)+" "+str(sc+z)+"\n      vertex "+str(asc+x)+" "+str(0+y)+" "+str(bsc+z)+"\n    endloop\n  endfacet\n  facet normal 0.850651 -0.525731 1.73121e-008\n    outer loop\n      vertex "+str(bsc+x)+" "+str(-asc+y)+" "+str(0+z)+"\n      vertex "+str(asc+x)+" "+str(0+y)+" "+str(bsc+z)+"\n      vertex "+str(sc+x)+" "+str(-sc+y)+" "+str(sc+z)+"\n    endloop\n  endfacet\n  facet normal -0.525731 0 0.850651\n    outer loop\n      vertex "+str(-asc+x)+" "+str(0+y)+" "+str(bsc+z)+"\n      vertex "+str(0+x)+" "+str(-bsc+y)+" "+str(asc+z)+"\n      vertex "+str(0+x)+" "+str(bsc+y)+" "+str(asc+z)+"\n    endloop\n  endfacet\n  facet normal 0.525731 0 0.850651\n    outer loop\n      vertex "+str(0+x)+" "+str(-bsc+y)+" "+str(asc+z)+"\n      vertex "+str(asc+x)+" "+str(0+y)+" "+str(bsc+z)+"\n      vertex "+str(0+x)+" "+str(bsc+y)+" "+str(asc+z)+"\n    endloop\n  endfacet\n  facet normal 0 -0.850651 0.525731\n    outer loop\n      vertex "+str(-bsc+x)+" "+str(-asc+y)+" "+str(0+z)+"\n      vertex "+str(bsc+x)+" "+str(-asc+y)+" "+str(0+z)+"\n      vertex "+str(0+x)+" "+str(-bsc+y)+" "+str(asc+z)+"\n    endloop\n  endfacet\n  facet normal -1.73121e-008 -0.850651 0.525731\n    outer loop\n      vertex "+str(-sc+x)+" "+str(-sc+y)+" "+str(sc+z)+"\n      vertex "+str(-bsc+x)+" "+str(-asc+y)+" "+str(0+z)+"\n      vertex "+str(0+x)+" "+str(-bsc+y)+" "+str(asc+z)+"\n    endloop\n  endfacet\n  facet normal -0.525731 -1.73121e-008 0.850651\n    outer loop\n      vertex "+str(-asc+x)+" "+str(0+y)+" "+str(bsc+z)+"\n      vertex "+str(-sc+x)+" "+str(-sc+y)+" "+str(sc+z)+"\n      vertex "+str(0+x)+" "+str(-bsc+y)+" "+str(asc+z)+"\n    endloop\n  endfacet\n  facet normal 0 -0.850651 -0.525731\n    outer loop\n      vertex "+str(-bsc+x)+" "+str(-asc+y)+" "+str(0+z)+"\n      vertex "+str(0+x)+" "+str(-bsc+y)+" "+str(-asc+z)+"\n      vertex "+str(bsc+x)+" "+str(-asc+y)+" "+str(0+z)+"\n    endloop\n  endfacet\n  facet normal 0.850651 -0.525731 0\n    outer loop\n      vertex "+str(bsc+x)+" "+str(-asc+y)+" "+str(0+z)+"\n      vertex "+str(asc+x)+" "+str(0+y)+" "+str(-bsc+z)+"\n      vertex "+str(asc+x)+" "+str(0+y)+" "+str(bsc+z)+"\n    endloop\n  endfacet\n  facet normal 0.850651 -0.525731 -1.73121e-008\n    outer loop\n      vertex "+str(bsc+x)+" "+str(-asc+y)+" "+str(0+z)+"\n      vertex "+str(sc+x)+" "+str(-sc+y)+" "+str(-sc+z)+"\n      vertex "+str(asc+x)+" "+str(0+y)+" "+str(-bsc+z)+"\n    endloop\n  endfacet\n  facet normal 1.73121e-008 -0.850651 -0.525731\n    outer loop\n      vertex "+str(0+x)+" "+str(-bsc+y)+" "+str(-asc+z)+"\n      vertex "+str(sc+x)+" "+str(-sc+y)+" "+str(-sc+z)+"\n      vertex "+str(bsc+x)+" "+str(-asc+y)+" "+str(0+z)+"\n    endloop\n  endfacet\n  facet normal 0.525731 1.73121e-008 0.850651\n    outer loop\n      vertex "+str(0+x)+" "+str(bsc+y)+" "+str(asc+z)+"\n      vertex "+str(asc+x)+" "+str(0+y)+" "+str(bsc+z)+"\n      vertex "+str(sc+x)+" "+str(sc+y)+" "+str(sc+z)+"\n    endloop\n  endfacet\n  facet normal 0.850651 0.525731 1.73121e-008\n    outer loop\n      vertex "+str(bsc+x)+" "+str(asc+y)+" "+str(0+z)+"\n      vertex "+str(sc+x)+" "+str(sc+y)+" "+str(sc+z)+"\n      vertex "+str(asc+x)+" "+str(0+y)+" "+str(bsc+z)+"\n    endloop\n  endfacet\n  facet normal 0.850651 0.525731 0\n    outer loop\n      vertex "+str(bsc+x)+" "+str(asc+y)+" "+str(0+z)+"\n      vertex "+str(asc+x)+" "+str(0+y)+" "+str(bsc+z)+"\n      vertex "+str(asc+x)+" "+str(0+y)+" "+str(-bsc+z)+"\n    endloop\n  endfacet\n  facet normal -0.850651 0.525731 0\n    outer loop\n      vertex "+str(-asc+x)+" "+str(0+y)+" "+str(-bsc+z)+"\n      vertex "+str(-asc+x)+" "+str(0+y)+" "+str(bsc+z)+"\n      vertex "+str(-bsc+x)+" "+str(asc+y)+" "+str(0+z)+"\n    endloop\n  endfacet\n  facet normal -0.850651 0.525731 1.73121e-008\n    outer loop\n      vertex "+str(-asc+x)+" "+str(0+y)+" "+str(bsc+z)+"\n      vertex "+str(-sc+x)+" "+str(sc+y)+" "+str(sc+z)+"\n      vertex "+str(-bsc+x)+" "+str(asc+y)+" "+str(0+z)+"\n    endloop\n  endfacet\n  facet normal -0.525731 1.73121e-008 0.850651\n    outer loop\n      vertex "+str(-asc+x)+" "+str(0+y)+" "+str(bsc+z)+"\n      vertex "+str(0+x)+" "+str(bsc+y)+" "+str(asc+z)+"\n      vertex "+str(-sc+x)+" "+str(sc+y)+" "+str(sc+z)+"\n    endloop\n  endfacet\n  facet normal -0.850651 -0.525731 1.73121e-008\n    outer loop\n      vertex "+str(-asc+x)+" "+str(0+y)+" "+str(bsc+z)+"\n      vertex "+str(-bsc+x)+" "+str(-asc+y)+" "+str(0+z)+"\n      vertex "+str(-sc+x)+" "+str(-sc+y)+" "+str(sc+z)+"\n    endloop\n  endfacet\n  facet normal -0.850651 -0.525731 0\n    outer loop\n      vertex "+str(-asc+x)+" "+str(0+y)+" "+str(-bsc+z)+"\n      vertex "+str(-bsc+x)+" "+str(-asc+y)+" "+str(0+z)+"\n      vertex "+str(-asc+x)+" "+str(0+y)+" "+str(bsc+z)+"\n    endloop\n  endfacet\n  facet normal -1.73121e-008 0.850651 0.525731\n    outer loop\n      vertex "+str(-sc+x)+" "+str(sc+y)+" "+str(sc+z)+"\n      vertex "+str(0+x)+" "+str(bsc+y)+" "+str(asc+z)+"\n      vertex "+str(-bsc+x)+" "+str(asc+y)+" "+str(0+z)+"\n    endloop\n  endfacet\n  facet normal 0 0.850651 0.525731\n    outer loop\n      vertex "+str(-bsc+x)+" "+str(asc+y)+" "+str(0+z)+"\n      vertex "+str(0+x)+" "+str(bsc+y)+" "+str(asc+z)+"\n      vertex "+str(bsc+x)+" "+str(asc+y)+" "+str(0+z)+"\n    endloop\n  endfacet\n  facet normal 1.73121e-008 0.850651 0.525731\n    outer loop\n      vertex "+str(0+x)+" "+str(bsc+y)+" "+str(asc+z)+"\n      vertex "+str(sc+x)+" "+str(sc+y)+" "+str(sc+z)+"\n      vertex "+str(bsc+x)+" "+str(asc+y)+" "+str(0+z)+"\n    endloop\n  endfacet\n  facet normal -1.73121e-008 -0.850651 -0.525731\n    outer loop\n      vertex "+str(-sc+x)+" "+str(-sc+y)+" "+str(-sc+z)+"\n      vertex "+str(0+x)+" "+str(-bsc+y)+" "+str(-asc+z)+"\n      vertex "+str(-bsc+x)+" "+str(-asc+y)+" "+str(0+z)+"\n    endloop\n  endfacet\n  facet normal -0.850651 -0.525731 -1.73121e-008\n    outer loop\n      vertex "+str(-asc+x)+" "+str(0+y)+" "+str(-bsc+z)+"\n      vertex "+str(-sc+x)+" "+str(-sc+y)+" "+str(-sc+z)+"\n      vertex "+str(-bsc+x)+" "+str(-asc+y)+" "+str(0+z)+"\n    endloop\n  endfacet\n  facet normal 0.525731 -1.73121e-008 -0.850651\n    outer loop\n      vertex "+str(0+x)+" "+str(-bsc+y)+" "+str(-asc+z)+"\n      vertex "+str(asc+x)+" "+str(0+y)+" "+str(-bsc+z)+"\n      vertex "+str(sc+x)+" "+str(-sc+y)+" "+str(-sc+z)+"\n    endloop\n  endfacet\n  facet normal 0.525731 0 -0.850651\n    outer loop\n      vertex "+str(0+x)+" "+str(-bsc+y)+" "+str(-asc+z)+"\n      vertex "+str(0+x)+" "+str(bsc+y)+" "+str(-asc+z)+"\n      vertex "+str(asc+x)+" "+str(0+y)+" "+str(-bsc+z)+"\n    endloop\n  endfacet\n  facet normal -0.525731 0 -0.850651\n    outer loop\n      vertex "+str(-asc+x)+" "+str(0+y)+" "+str(-bsc+z)+"\n      vertex "+str(0+x)+" "+str(bsc+y)+" "+str(-asc+z)+"\n      vertex "+str(0+x)+" "+str(-bsc+y)+" "+str(-asc+z)+"\n    endloop\n  endfacet\n  facet normal -0.525731 -1.73121e-008 -0.850651\n    outer loop\n      vertex "+str(-asc+x)+" "+str(0+y)+" "+str(-bsc+z)+"\n      vertex "+str(0+x)+" "+str(-bsc+y)+" "+str(-asc+z)+"\n      vertex "+str(-sc+x)+" "+str(-sc+y)+" "+str(-sc+z)+"\n    endloop\n  endfacet\n  facet normal 0.850651 0.525731 -1.73121e-008\n    outer loop\n      vertex "+str(bsc+x)+" "+str(asc+y)+" "+str(0+z)+"\n      vertex "+str(asc+x)+" "+str(0+y)+" "+str(-bsc+z)+"\n      vertex "+str(sc+x)+" "+str(sc+y)+" "+str(-sc+z)+"\n    endloop\n  endfacet\n  facet normal 0.525731 1.73121e-008 -0.850651\n    outer loop\n      vertex "+str(0+x)+" "+str(bsc+y)+" "+str(-asc+z)+"\n      vertex "+str(sc+x)+" "+str(sc+y)+" "+str(-sc+z)+"\n      vertex "+str(asc+x)+" "+str(0+y)+" "+str(-bsc+z)+"\n    endloop\n  endfacet\n  facet normal 0 0.850651 -0.525731\n    outer loop\n      vertex "+str(-bsc+x)+" "+str(asc+y)+" "+str(0+z)+"\n      vertex "+str(bsc+x)+" "+str(asc+y)+" "+str(0+z)+"\n      vertex "+str(0+x)+" "+str(bsc+y)+" "+str(-asc+z)+"\n    endloop\n  endfacet\n  facet normal 1.73121e-008 0.850651 -0.525731\n    outer loop\n      vertex "+str(0+x)+" "+str(bsc+y)+" "+str(-asc+z)+"\n      vertex "+str(bsc+x)+" "+str(asc+y)+" "+str(0+z)+"\n      vertex "+str(sc+x)+" "+str(sc+y)+" "+str(-sc+z)+"\n    endloop\n  endfacet\n  facet normal -0.525731 1.73121e-008 -0.850651\n    outer loop\n      vertex "+str(-asc+x)+" "+str(0+y)+" "+str(-bsc+z)+"\n      vertex "+str(-sc+x)+" "+str(sc+y)+" "+str(-sc+z)+"\n      vertex "+str(0+x)+" "+str(bsc+y)+" "+str(-asc+z)+"\n    endloop\n  endfacet\n  facet normal -0.850651 0.525731 -1.73121e-008\n    outer loop\n      vertex "+str(-asc+x)+" "+str(0+y)+" "+str(-bsc+z)+"\n      vertex "+str(-bsc+x)+" "+str(asc+y)+" "+str(0+z)+"\n      vertex "+str(-sc+x)+" "+str(sc+y)+" "+str(-sc+z)+"\n    endloop\n  endfacet\n  facet normal -1.73121e-008 0.850651 -0.525731\n    outer loop\n      vertex "+str(-sc+x)+" "+str(sc+y)+" "+str(-sc+z)+"\n      vertex "+str(-bsc+x)+" "+str(asc+y)+" "+str(0+z)+"\n      vertex "+str(0+x)+" "+str(bsc+y)+" "+str(-asc+z)+"\n    endloop\n  endfacet\n"

if __name__ == "__main__":
        try:
                pdb = sys.argv[1]
        except:
                print "Usage: pdbstl.py [PDB filename] *[scale=100] *[portion=1000]"
                sys.exit(1)
        try:
                res = int(sys.argv[2])
                if res <= 0:
                        res = 100#resolution - scale of atom size
        except:
                res = 1
        try:
                atl = int(sys.argv[3])
                if atl <= 0:
                        atl = 1000#atom limit - render every nth atom
        except:
                atl = 1000
        ddec = "polyhedron(points=[[1,1,1], [1,-1,1], [-1,-1,1], [-1,1,1], [-1,1,-1], [1,1,-1], [1,-1,-1], [-1,-1,-1], [p,0,(1/p)], [-p,0,(1/p)], [-p,0,(-1/p)], [p,0,(-1/p)], [(1/p),p,0], [(1/p),-p,0], [(-1/p),-p,0], [(-1/p),p,0], [0,(1/p),p], [0,(1/p),-p], [0,(-1/p),-p], [0,(-1/p),p]], faces=[ [8,1,19,16,0], [8,0,12,5,11], [8,11,6,13,1], [6,11,5,17,18], [5,12,15,4,17], [17,4,10,7,18], [2,14,7,10,9], [14,2,19,1,13], [6,18,7,14,13], [16,19,2,9,3], [16,3,15,12,0], [9,10,4,15,3] ]);"
        e = open(pdb, 'r')
        f = open(pdb.replace('.pdb', '.stl'), 'w')
        q = open(pdb.replace('.pdb', '.scad'), 'w')
        f.write("solid OpenSCAD_Model\n")#stl header
        q.write("p = ((1 + sqrt(5))/2);\na = "+str(res)+";\n")#scad header
        '''
        pdb format descriptions
        ftp://ftp.wwpdb.org/pub/pdb/doc/format_descriptions/Format_v33_Letter.pdf
        atom
        31 - 38 Real(8.3) x Orthogonal coordinates for X in Angstroms.
        39 - 46 Real(8.3) y Orthogonal coordinates for Y in Angstroms.
        47 - 54 Real(8.3) z Orthogonal coordinates for Z in Angstroms.
        '''
        count = 0;
        for line in e:
                if line[:4] == "ATOM":
                        if count == atl:
                                q.write("translate(["+line[30:37]+","+line[30:37]+","+line[46:53]+"]) scale([a,a,a]) "+ddec+"\n")
                                f.write(dodca(float(line[30:37]),float(line[30:37]),float(line[46:53]),res))
                                count=0
                        else:
                                count=count+1
        f.write("endsolid OpenSCAD_Model")#stl footer
        f.close()
        q.close()
        e.close()
        print pdb.replace('.pdb', '.stl')
        print pdb.replace('.pdb', '.scad')







'''miscellaneous - python code here parses dodecahedron code from stler
line = """  facet normal 1.73121e-008 -0.850651 0.525731\n    outer loop\n      vertex 0 -"+bsc+" "+asc+"\n      vertex "+bsc+" -"+asc+" 0\n      vertex "+sc+" -"+sc+" "+sc+"\n    endloop\n  endfacet\n  facet normal 0.525731 -1.73121e-008 0.850651\n    outer loop\n      vertex 0 -"+bsc+" "+asc+"\n      vertex "+sc+" -"+sc+" "+sc+"\n      vertex "+asc+" 0 "+bsc+"\n    endloop\n  endfacet\n  facet normal 0.850651 -0.525731 1.73121e-008\n    outer loop\n      vertex "+bsc+" -"+asc+" 0\n      vertex "+asc+" 0 "+bsc+"\n      vertex "+sc+" -"+sc+" "+sc+"\n    endloop\n  endfacet\n  facet normal -0.525731 0 0.850651\n    outer loop\n      vertex -"+asc+" 0 "+bsc+"\n      vertex 0 -"+bsc+" "+asc+"\n      vertex 0 "+bsc+" "+asc+"\n    endloop\n  endfacet\n  facet normal 0.525731 0 0.850651\n    outer loop\n      vertex 0 -"+bsc+" "+asc+"\n      vertex "+asc+" 0 "+bsc+"\n      vertex 0 "+bsc+" "+asc+"\n    endloop\n  endfacet\n  facet normal 0 -0.850651 0.525731\n    outer loop\n      vertex -"+bsc+" -"+asc+" 0\n      vertex "+bsc+" -"+asc+" 0\n      vertex 0 -"+bsc+" "+asc+"\n    endloop\n  endfacet\n  facet normal -1.73121e-008 -0.850651 0.525731\n    outer loop\n      vertex -"+sc+" -"+sc+" "+sc+"\n      vertex -"+bsc+" -"+asc+" 0\n      vertex 0 -"+bsc+" "+asc+"\n    endloop\n  endfacet\n  facet normal -0.525731 -1.73121e-008 0.850651\n    outer loop\n      vertex -"+asc+" 0 "+bsc+"\n      vertex -"+sc+" -"+sc+" "+sc+"\n      vertex 0 -"+bsc+" "+asc+"\n    endloop\n  endfacet\n  facet normal 0 -0.850651 -0.525731\n    outer loop\n      vertex -"+bsc+" -"+asc+" 0\n      vertex 0 -"+bsc+" -"+asc+"\n      vertex "+bsc+" -"+asc+" 0\n    endloop\n  endfacet\n  facet normal 0.850651 -0.525731 0\n    outer loop\n      vertex "+bsc+" -"+asc+" 0\n      vertex "+asc+" 0 -"+bsc+"\n      vertex "+asc+" 0 "+bsc+"\n    endloop\n  endfacet\n  facet normal 0.850651 -0.525731 -1.73121e-008\n    outer loop\n      vertex "+bsc+" -"+asc+" 0\n      vertex "+sc+" -"+sc+" -"+sc+"\n      vertex "+asc+" 0 -"+bsc+"\n    endloop\n  endfacet\n  facet normal 1.73121e-008 -0.850651 -0.525731\n    outer loop\n      vertex 0 -"+bsc+" -"+asc+"\n      vertex "+sc+" -"+sc+" -"+sc+"\n      vertex "+bsc+" -"+asc+" 0\n    endloop\n  endfacet\n  facet normal 0.525731 1.73121e-008 0.850651\n    outer loop\n      vertex 0 "+bsc+" "+asc+"\n      vertex "+asc+" 0 "+bsc+"\n      vertex "+sc+" "+sc+" "+sc+"\n    endloop\n  endfacet\n  facet normal 0.850651 0.525731 1.73121e-008\n    outer loop\n      vertex "+bsc+" "+asc+" 0\n      vertex "+sc+" "+sc+" "+sc+"\n      vertex "+asc+" 0 "+bsc+"\n    endloop\n  endfacet\n  facet normal 0.850651 0.525731 0\n    outer loop\n      vertex "+bsc+" "+asc+" 0\n      vertex "+asc+" 0 "+bsc+"\n      vertex "+asc+" 0 -"+bsc+"\n    endloop\n  endfacet\n  facet normal -0.850651 0.525731 0\n    outer loop\n      vertex -"+asc+" 0 -"+bsc+"\n      vertex -"+asc+" 0 "+bsc+"\n      vertex -"+bsc+" "+asc+" 0\n    endloop\n  endfacet\n  facet normal -0.850651 0.525731 1.73121e-008\n    outer loop\n      vertex -"+asc+" 0 "+bsc+"\n      vertex -"+sc+" "+sc+" "+sc+"\n      vertex -"+bsc+" "+asc+" 0\n    endloop\n  endfacet\n  facet normal -0.525731 1.73121e-008 0.850651\n    outer loop\n      vertex -"+asc+" 0 "+bsc+"\n      vertex 0 "+bsc+" "+asc+"\n      vertex -"+sc+" "+sc+" "+sc+"\n    endloop\n  endfacet\n  facet normal -0.850651 -0.525731 1.73121e-008\n    outer loop\n      vertex -"+asc+" 0 "+bsc+"\n      vertex -"+bsc+" -"+asc+" 0\n      vertex -"+sc+" -"+sc+" "+sc+"\n    endloop\n  endfacet\n  facet normal -0.850651 -0.525731 0\n    outer loop\n      vertex -"+asc+" 0 -"+bsc+"\n      vertex -"+bsc+" -"+asc+" 0\n      vertex -"+asc+" 0 "+bsc+"\n    endloop\n  endfacet\n  facet normal -1.73121e-008 0.850651 0.525731\n    outer loop\n      vertex -"+sc+" "+sc+" "+sc+"\n      vertex 0 "+bsc+" "+asc+"\n      vertex -"+bsc+" "+asc+" 0\n    endloop\n  endfacet\n  facet normal 0 0.850651 0.525731\n    outer loop\n      vertex -"+bsc+" "+asc+" 0\n      vertex 0 "+bsc+" "+asc+"\n      vertex "+bsc+" "+asc+" 0\n    endloop\n  endfacet\n  facet normal 1.73121e-008 0.850651 0.525731\n    outer loop\n      vertex 0 "+bsc+" "+asc+"\n      vertex "+sc+" "+sc+" "+sc+"\n      vertex "+bsc+" "+asc+" 0\n    endloop\n  endfacet\n  facet normal -1.73121e-008 -0.850651 -0.525731\n    outer loop\n      vertex -"+sc+" -"+sc+" -"+sc+"\n      vertex 0 -"+bsc+" -"+asc+"\n      vertex -"+bsc+" -"+asc+" 0\n    endloop\n  endfacet\n  facet normal -0.850651 -0.525731 -1.73121e-008\n    outer loop\n      vertex -"+asc+" 0 -"+bsc+"\n      vertex -"+sc+" -"+sc+" -"+sc+"\n      vertex -"+bsc+" -"+asc+" 0\n    endloop\n  endfacet\n  facet normal 0.525731 -1.73121e-008 -0.850651\n    outer loop\n      vertex 0 -"+bsc+" -"+asc+"\n      vertex "+asc+" 0 -"+bsc+"\n      vertex "+sc+" -"+sc+" -"+sc+"\n    endloop\n  endfacet\n  facet normal 0.525731 0 -0.850651\n    outer loop\n      vertex 0 -"+bsc+" -"+asc+"\n      vertex 0 "+bsc+" -"+asc+"\n      vertex "+asc+" 0 -"+bsc+"\n    endloop\n  endfacet\n  facet normal -0.525731 0 -0.850651\n    outer loop\n      vertex -"+asc+" 0 -"+bsc+"\n      vertex 0 "+bsc+" -"+asc+"\n      vertex 0 -"+bsc+" -"+asc+"\n    endloop\n  endfacet\n  facet normal -0.525731 -1.73121e-008 -0.850651\n    outer loop\n      vertex -"+asc+" 0 -"+bsc+"\n      vertex 0 -"+bsc+" -"+asc+"\n      vertex -"+sc+" -"+sc+" -"+sc+"\n    endloop\n  endfacet\n  facet normal 0.850651 0.525731 -1.73121e-008\n    outer loop\n      vertex "+bsc+" "+asc+" 0\n      vertex "+asc+" 0 -"+bsc+"\n      vertex "+sc+" "+sc+" -"+sc+"\n    endloop\n  endfacet\n  facet normal 0.525731 1.73121e-008 -0.850651\n    outer loop\n      vertex 0 "+bsc+" -"+asc+"\n      vertex "+sc+" "+sc+" -"+sc+"\n      vertex "+asc+" 0 -"+bsc+"\n    endloop\n  endfacet\n  facet normal 0 0.850651 -0.525731\n    outer loop\n      vertex -"+bsc+" "+asc+" 0\n      vertex "+bsc+" "+asc+" 0\n      vertex 0 "+bsc+" -"+asc+"\n    endloop\n  endfacet\n  facet normal 1.73121e-008 0.850651 -0.525731\n    outer loop\n      vertex 0 "+bsc+" -"+asc+"\n      vertex "+bsc+" "+asc+" 0\n      vertex "+sc+" "+sc+" -"+sc+"\n    endloop\n  endfacet\n  facet normal -0.525731 1.73121e-008 -0.850651\n    outer loop\n      vertex -"+asc+" 0 -"+bsc+"\n      vertex -"+sc+" "+sc+" -"+sc+"\n      vertex 0 "+bsc+" -"+asc+"\n    endloop\n  endfacet\n  facet normal -0.850651 0.525731 -1.73121e-008\n    outer loop\n      vertex -"+asc+" 0 -"+bsc+"\n      vertex -"+bsc+" "+asc+" 0\n      vertex -"+sc+" "+sc+" -"+sc+"\n    endloop\n  endfacet\n  facet normal -1.73121e-008 0.850651 -0.525731\n    outer loop\n      vertex -"+sc+" "+sc+" -"+sc+"\n      vertex -"+bsc+" "+asc+" 0\n      vertex 0 "+bsc+" -"+asc+"\n    endloop\n  endfacet\n"""
line = line.replace("\n"," _x")//preserves new line while keeping it as a seperate element
print line
parseme = line.split(" ")//split elements
#print parseme
for o in range(len(parseme)):
    #corrections to stler code
    if parseme[o] == '"+bsc+"':
        parseme[o] = "bsc"
    if parseme[o] == '"+sc+"':
        parseme[o] = "sc"
    if parseme[o] == '-"+sc+"':
        parseme[o] = "-sc"
    if parseme[o] == '"+sc+"\n':
        parseme[o] = "sc\n"
    if parseme[o] == '-"+sc+"\n':
        parseme[o] = "-sc\n"
    if parseme[o] == '"+asc+"':
        parseme[o] = "asc"
    if parseme[o] == '"+csc+"':
        parseme[o] = "csc"
    if parseme[o] == '-"+bsc+"':
        parseme[o] = "-bsc"
    if parseme[o] == '-"+asc+"':
        parseme[o] = "-asc"
    if parseme[o] == '-"+csc+"':
        parseme[o] = "-csc"
    if parseme[o] == '-"+bsc+"\n':
        parseme[o] = "-bsc\n"
    if parseme[o] == '-"+asc+"\n':
        parseme[o] = "-asc\n"
    if parseme[o] == '-"+csc+"\n':
        parseme[o] = "-csc\n"
    if parseme[o] == '"+bsc+"\n':
        parseme[o] = "bsc\n"
    if parseme[o] == '"+asc+"\n':
        parseme[o] = "asc\n"
    if parseme[o] == '"+csc+"\n':
        parseme[o] = "csc\n"
print parseme
for o in range(len(parseme)):
    if parseme[o] == "vertex"://modification to persist scalar while adding translate coords for specific axis
        parseme[o+1] = '"'+"+str("+parseme[o+1]+"+x)+"+'"'
        parseme[o+2] = '"'+"+str("+parseme[o+2]+"+y)+"+'"'
        parseme[o+3] = '"'+"+str("+parseme[o+3]+"+z)+"+'"'
print parseme
mydoca = " ".join(parseme)
mydoca = mydoca.replace(" _x","\n")
print mydoca

'''
