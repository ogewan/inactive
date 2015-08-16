#Earth to NML Cygni project
"""
Measurements
Earth = 1 Pixel
Sun = 109 Earths
NML Cygni = 1650 Solar Radii = 179850 Earth Radii
NML Cygni = 179850 Earths
NML Cygni = 179850 * 179850 pixels
Earth = 1 * 1 pixels
Total Pixels = 32346022500
"""

#1. make array of size 179850 where each element is an array of size 179850
imgmap = [0]*179850
rmap = [imgmap]*179850

"""
pixel can be 0,1,2
where:
0 is a point not contained within our sphere, is black
1 is a point within our sphere, is orange-red
2 is a point that represents earth, it is outside the circle and blue

[0,0,1,0,0]
[0,1,1,1,0]
[1,1,1,1LO,1]
[0,1,1,1,0]
[0,0,1,0,0]
