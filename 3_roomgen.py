


header = ''
lsroom = []
scale = 1

def linkrgt(id0, id1, a, b, c, d, z, y):
	
	a *= scale
	b *= scale
	c *= scale
	d *= scale
	z *= scale
	y *= scale
	
	r = lsroom[id0]
	s = ', '.join(map(lambda x: "%ff" % x, (a, b, c, d)))
	
	r[0] += '\tif(+v.px < room%d.w) {\n' % id0
	r[0] += '\t\tView door = View_through_rgt(v, room%d.w, %s);\n' % (id0, s)
	r[0] += '\t\tdoor.px -= room%d.w + room%d.w;\n' % (id0, id1)
	r[0] += '\t\tdoor.py -= %ff;\n' % y
	r[0] += '\t\tdoor.pz -= %ff;\n' % z
	r[0] += '\t\tif(--depth) room%d_render(door);\n' % id1
	r[0] += '\t\tdepth++;\n'
	r[0] += '\t}\n'
	
	r[1] += '\tif(v.pz >= %ff+d)\n' % a
	r[1] += '\tif(v.pz <= %ff-d)\n' % b
	r[1] += '\tif(v.py >= %ff+d)\n' % c
	r[1] += '\tif(v.py <= %ff-d)\n' % d
	r[1] += '\tif(v.px + x > room%d.w - w) {\n' % id0
	r[1] += '\t\tif(v.px + x > room%d.w) {\n' % id0
	r[1] += '\t\t\t*r = &room%d;\n' % id1
	r[1] += '\t\t\tv.px -= room%d.w + room%d.w;\n' % (id0, id1)
	r[1] += '\t\t\tv.py -= %ff;\n' % y
	r[1] += '\t\t\tv.pz -= %ff;\n' % z
	r[1] += '\t\t\treturn room%d_update(v, r, w, d, dt);\n' % id1
	r[1] += '\t\t}\n'
	r[1] += '\t\tv.px += x;\n'
	r[1] += '\t\tv.py += y;\n'
	r[1] += '\t\tv.pz += z;\n'
	
	r[1] += '\t\tif(v.pz < %ff+d) v.pz = %ff+d, v.vz = 0;\n' % (a, a)
	r[1] += '\t\tif(v.pz > %ff-d) v.pz = %ff-d, v.vz = 0;\n' % (b, b)
	r[1] += '\t\tif(v.py < %ff+d) v.py = %ff+d, v.vy = 0;\n' % (c, c)
	r[1] += '\t\tif(v.py > %ff-d) v.py = %ff-d, v.vy = 0;\n' % (d, d)
	
	r[1] += '\t\treturn v;\n'
	r[1] += '\t}\n'

def linklft(id0, id1, a, b, c, d, z, y):
	
	a *= scale
	b *= scale
	c *= scale
	d *= scale
	z *= scale
	y *= scale
	
	r = lsroom[id0]
	s = ', '.join(map(lambda x: "%ff" % x, (a, b, c, d)))
	
	r[0] += '\tif(-v.px < room%d.w) {\n' % id0
	r[0] += '\t\tView door = View_through_lft(v, -room%d.w, %s);\n' % (id0, s)
	r[0] += '\t\tdoor.px += room%d.w + room%d.w;\n' % (id0, id1)
	r[0] += '\t\tdoor.py -= %ff;\n' % y
	r[0] += '\t\tdoor.pz -= %ff;\n' % z
	r[0] += '\t\tif(--depth) room%d_render(door);\n' % id1
	r[0] += '\t\tdepth++;\n'
	r[0] += '\t}\n'
	
	r[1] += '\tif(v.pz >= %ff+d)\n' % a
	r[1] += '\tif(v.pz <= %ff-d)\n' % b
	r[1] += '\tif(v.py >= %ff+d)\n' % c
	r[1] += '\tif(v.py <= %ff-d)\n' % d
	r[1] += '\tif(v.px + x < -room%d.w + w) {\n' % id0
	r[1] += '\t\tif(v.px + x < -room%d.w) {\n' % id0
	r[1] += '\t\t\t*r = &room%d;\n' % id1
	r[1] += '\t\t\tv.px += room%d.w + room%d.w;\n' % (id0, id1)
	r[1] += '\t\t\tv.py -= %ff;\n' % y
	r[1] += '\t\t\tv.pz -= %ff;\n' % z
	r[1] += '\t\t\treturn room%d_update(v, r, w, d, dt);\n' % id1
	r[1] += '\t\t}\n'
	r[1] += '\t\tv.px += x;\n'
	r[1] += '\t\tv.py += y;\n'
	r[1] += '\t\tv.pz += z;\n'
	
	r[1] += '\t\tif(v.pz < %ff+d) v.pz = %ff+d, v.vz = 0;\n' % (a, a)
	r[1] += '\t\tif(v.pz > %ff-d) v.pz = %ff-d, v.vz = 0;\n' % (b, b)
	r[1] += '\t\tif(v.py < %ff+d) v.py = %ff+d, v.vy = 0;\n' % (c, c)
	r[1] += '\t\tif(v.py > %ff-d) v.py = %ff-d, v.vy = 0;\n' % (d, d)
	
	r[1] += '\t\treturn v;\n'
	r[1] += '\t}\n'

def linkuwd(id0, id1, a, b, c, d, x, z):
	
	a *= scale
	b *= scale
	c *= scale
	d *= scale
	x *= scale
	z *= scale
	
	r = lsroom[id0]
	s = ', '.join(map(lambda x: "%ff" % x, (a, b, c, d)))
	
	r[0] += '\tif(+v.py < room%d.h) {\n' % id0
	r[0] += '\t\tView door = View_through_uwd(v, room%d.h, %s);\n' % (id0, s)
	r[0] += '\t\tdoor.px -= %ff;\n' % x
	r[0] += '\t\tdoor.py -= room%d.h + room%d.h;\n' % (id0, id1)
	r[0] += '\t\tdoor.pz -= %ff;\n' % z
	r[0] += '\t\tif(--depth) room%d_render(door);\n' % id1
	r[0] += '\t\tdepth++;\n'
	r[0] += '\t}\n'
	
	r[1] += '\tif(v.px >= %ff+d)\n' % a
	r[1] += '\tif(v.px <= %ff-d)\n' % b
	r[1] += '\tif(v.pz >= %ff+d)\n' % c
	r[1] += '\tif(v.pz <= %ff-d)\n' % d
	r[1] += '\tif(v.py + y > room%d.h - w) {\n' % id0
	r[1] += '\t\tif(v.py + y > room%d.h) {\n' % id0
	r[1] += '\t\t\t*r = &room%d;\n' % id1
	r[1] += '\t\t\tv.px -= %ff;\n' % x
	r[1] += '\t\t\tv.py -= room%d.h + room%d.h;\n' % (id0, id1)
	r[1] += '\t\t\tv.pz -= %ff;\n' % z
	r[1] += '\t\t\treturn room%d_update(v, r, w, d, dt);\n' % id1
	r[1] += '\t\t}\n'
	r[1] += '\t\tv.px += x;\n'
	r[1] += '\t\tv.py += y;\n'
	r[1] += '\t\tv.pz += z;\n'
	
	r[1] += '\t\tif(v.px < %ff+d) v.px = %ff+d, v.vx = 0;\n' % (a, a)
	r[1] += '\t\tif(v.px > %ff-d) v.px = %ff-d, v.vx = 0;\n' % (b, b)
	r[1] += '\t\tif(v.pz < %ff+d) v.pz = %ff+d, v.vz = 0;\n' % (c, c)
	r[1] += '\t\tif(v.pz > %ff-d) v.pz = %ff-d, v.vz = 0;\n' % (d, d)
	
	r[1] += '\t\treturn v;\n'
	r[1] += '\t}\n'

def linkdwn(id0, id1, a, b, c, d, x, z):
	
	a *= scale
	b *= scale
	c *= scale
	d *= scale
	x *= scale
	z *= scale
	
	r = lsroom[id0]
	s = ', '.join(map(lambda x: "%ff" % x, (a, b, c, d)))
	
	r[0] += '\tif(-v.py < room%d.h) {\n' % id0
	r[0] += '\t\tView door = View_through_dwn(v, -room%d.h, %s);\n' % (id0, s)
	r[0] += '\t\tdoor.px -= %ff;\n' % x
	r[0] += '\t\tdoor.py += room%d.h + room%d.h;\n' % (id0, id1)
	r[0] += '\t\tdoor.pz -= %ff;\n' % z
	r[0] += '\t\tif(--depth) room%d_render(door);\n' % id1
	r[0] += '\t\tdepth++;\n'
	r[0] += '\t}\n'
	
	r[1] += '\tif(v.px >= %ff+d)\n' % a
	r[1] += '\tif(v.px <= %ff-d)\n' % b
	r[1] += '\tif(v.pz >= %ff+d)\n' % c
	r[1] += '\tif(v.pz <= %ff-d)\n' % d
	r[1] += '\tif(v.py + y < -room%d.h + w) {\n' % id0
	r[1] += '\t\tif(v.py + y < -room%d.h) {\n' % id0
	r[1] += '\t\t\t*r = &room%d;\n' % id1
	r[1] += '\t\t\tv.px -= %ff;\n' % x
	r[1] += '\t\t\tv.py += room%d.h + room%d.h;\n' % (id0, id1)
	r[1] += '\t\t\tv.pz -= %ff;\n' % z
	r[1] += '\t\t\treturn room%d_update(v, r, w, d, dt);\n' % id1
	r[1] += '\t\t}\n'
	r[1] += '\t\tv.px += x;\n'
	r[1] += '\t\tv.py += y;\n'
	r[1] += '\t\tv.pz += z;\n'
	
	r[1] += '\t\tif(v.px < %ff+d) v.px = %ff+d, v.vx = 0;\n' % (a, a)
	r[1] += '\t\tif(v.px > %ff-d) v.px = %ff-d, v.vx = 0;\n' % (b, b)
	r[1] += '\t\tif(v.pz < %ff+d) v.pz = %ff+d, v.vz = 0;\n' % (c, c)
	r[1] += '\t\tif(v.pz > %ff-d) v.pz = %ff-d, v.vz = 0;\n' % (d, d)
	
	r[1] += '\t\treturn v;\n'
	r[1] += '\t}\n'
	
	r[2] += '\tif(v.px >= %ff)\n' % a
	r[2] += '\tif(v.px <= %ff)\n' % b
	r[2] += '\tif(v.pz >= %ff)\n' % c
	r[2] += '\tif(v.pz <= %ff) {\n' % d
	r[2] += '\t\tv.px -= %ff;\n' % x
	r[2] += '\t\tv.py += room%d.h + room%d.h;\n' % (id0, id1)
	r[2] += '\t\tv.pz -= %ff;\n' % z
	r[2] += '\t\treturn room%d_cast_down(v, d);\n' % id1
	r[2] += '\t}\n'

def linkfwd(id0, id1, a, b, c, d, x, y):
	
	a *= scale
	b *= scale
	c *= scale
	d *= scale
	x *= scale
	y *= scale
	
	r = lsroom[id0]
	s = ', '.join(map(lambda x: "%ff" % x, (a, b, c, d)))
	
	r[0] += '\tif(+v.pz < room%d.d) {\n' % id0
	r[0] += '\t\tView door = View_through_fwd(v, room%d.d, %s);\n' % (id0, s)
	r[0] += '\t\tdoor.px -= %ff;\n' % x
	r[0] += '\t\tdoor.py -= %ff;\n' % y
	r[0] += '\t\tdoor.pz -= room%d.d + room%d.d;\n' % (id0, id1)
	r[0] += '\t\tif(--depth) room%d_render(door);\n' % id1
	r[0] += '\t\tdepth++;\n'
	r[0] += '\t}\n'
	
	r[1] += '\tif(v.px >= %ff+d)\n' % a
	r[1] += '\tif(v.px <= %ff-d)\n' % b
	r[1] += '\tif(v.py >= %ff+d)\n' % c
	r[1] += '\tif(v.py <= %ff-d)\n' % d
	r[1] += '\tif(v.pz + z > room%d.d - w) {\n' % id0
	r[1] += '\t\tif(v.pz + z > room%d.d) {\n' % id0
	r[1] += '\t\t\t*r = &room%d;\n' % id1
	r[1] += '\t\t\tv.px -= %ff;\n' % x
	r[1] += '\t\t\tv.py -= %ff;\n' % y
	r[1] += '\t\t\tv.pz -= room%d.d + room%d.d;\n' % (id0, id1)
	r[1] += '\t\t\tv = room%d_update(v, r, w, d, dt);\n' % id1
	r[1] += '\t\t\tv.vz -= room%d._d + room%d._d;\n' % (id0, id1) # velocity
	r[1] += '\t\t\treturn v;\n'
	r[1] += '\t\t}\n'
	r[1] += '\t\tv.px += x;\n'
	r[1] += '\t\tv.py += y;\n'
	r[1] += '\t\tv.pz += z;\n'
	
	r[1] += '\t\tif(v.px < %ff+d) v.px = %ff+d, v.vx = 0;\n' % (a, a)
	r[1] += '\t\tif(v.px > %ff-d) v.px = %ff-d, v.vx = 0;\n' % (b, b)
	r[1] += '\t\tif(v.py < %ff+d) v.py = %ff+d, v.vy = 0;\n' % (c, c)
	r[1] += '\t\tif(v.py > %ff-d) v.py = %ff-d, v.vy = 0;\n' % (d, d)
	
	r[1] += '\t\treturn v;\n'
	r[1] += '\t}\n'

def linkbwd(id0, id1, a, b, c, d, x, y):
	
	a *= scale
	b *= scale
	c *= scale
	d *= scale
	x *= scale
	y *= scale
	
	r = lsroom[id0]
	s = ', '.join(map(lambda x: "%ff" % x, (a, b, c, d)))
	
	r[0] += '\tif(-v.pz < room%d.d) {\n' % id0
	r[0] += '\t\tView door = View_through_bwd(v, -room%d.d, %s);\n' % (id0, s)
	r[0] += '\t\tdoor.px -= %ff;\n' % x
	r[0] += '\t\tdoor.py -= %ff;\n' % y
	r[0] += '\t\tdoor.pz += room%d.d + room%d.d;\n' % (id0, id1)
	r[0] += '\t\tif(--depth) room%d_render(door);\n' % id1
	r[0] += '\t\tdepth++;\n'
	r[0] += '\t}\n'
	
	r[1] += '\tif(v.px >= %ff+d)\n' % a
	r[1] += '\tif(v.px <= %ff-d)\n' % b
	r[1] += '\tif(v.py >= %ff+d)\n' % c
	r[1] += '\tif(v.py <= %ff-d)\n' % d
	r[1] += '\tif(v.pz + z < -room%d.d + w) {\n' % id0
	r[1] += '\t\tif(v.pz + z < -room%d.d) {\n' % id0
	r[1] += '\t\t\t*r = &room%d;\n' % id1
	r[1] += '\t\t\tv.px -= %ff;\n' % x
	r[1] += '\t\t\tv.py -= %ff;\n' % y
	r[1] += '\t\t\tv.pz += room%d.d + room%d.d;\n' % (id0, id1)
	r[1] += '\t\t\tv = room%d_update(v, r, w, d, dt);\n' % id1
	r[1] += '\t\t\tv.vz += room%d._d + room%d._d;\n' % (id0, id1) # velocity
	r[1] += '\t\t\treturn v;\n'
	r[1] += '\t\t}\n'
	r[1] += '\t\tv.px += x;\n'
	r[1] += '\t\tv.py += y;\n'
	r[1] += '\t\tv.pz += z;\n'
	
	r[1] += '\t\tif(v.px < %ff+d) v.px = %ff+d, v.vx = 0;\n' % (a, a)
	r[1] += '\t\tif(v.px > %ff-d) v.px = %ff-d, v.vx = 0;\n' % (b, b)
	r[1] += '\t\tif(v.py < %ff+d) v.py = %ff+d, v.vy = 0;\n' % (c, c)
	r[1] += '\t\tif(v.py > %ff-d) v.py = %ff-d, v.vy = 0;\n' % (d, d)
	
	r[1] += '\t\treturn v;\n'
	r[1] += '\t}\n'

def rgt(id0,z0,y0, id1,z1,y1, d,h):
	linkrgt(id0, id1, z0-d, z0+d, y0-h, y0+h, z0-z1, y0-y1)
	linklft(id1, id0, z1-d, z1+d, y1-h, y1+h, z1-z0, y1-y0)

def lft(id0,z0,y0, id1,z1,y1, d,h):
	linklft(id0, id1, z0-d, z0+d, y0-h, y0+h, z0-z1, y0-y1)
	linkrgt(id1, id0, z1-d, z1+d, y1-h, y1+h, z1-z0, y1-y0)

def uwd(id0,x0,z0, id1,x1,z1, w,h):
	linkuwd(id0, id1, x0-w, x0+w, z0-h, z0+h, x0-x1, z0-z1)
	linkdwn(id1, id0, x1-w, x1+w, z1-h, z1+h, x1-x0, z1-z0)

def dwn(id0,x0,z0, id1,x1,z1, w,h):
	linkdwn(id0, id1, x0-w, x0+w, z0-h, z0+h, x0-x1, z0-z1)
	linkuwd(id1, id0, x1-w, x1+w, z1-h, z1+h, x1-x0, z1-z0)

def fwd(id0,x0,y0, id1,x1,y1, w,h):
	linkfwd(id0, id1, x0-w, x0+w, y0-h, y0+h, x0-x1, y0-y1)
	linkbwd(id1, id0, x1-w, x1+w, y1-h, y1+h, x1-x0, y1-y0)

def bwd(id0,x0,y0, id1,x1,y1, w,h):
	linkbwd(id0, id1, x0-w, x0+w, y0-h, y0+h, x0-x1, y0-y1)
	linkfwd(id1, id0, x1-w, x1+w, y1-h, y1+h, x1-x0, y1-y0)

def room(w, h, d):
	
	w *= scale
	h *= scale
	d *= scale
	
	global header, lsroom
	index = len(lsroom)
	
	header+='fn void room%d_render(View v);\n' % index
	header+='fn View room%d_update(View v, Room **r'\
	', float w, float d, float dt);\n' % index
	header+='fn float room%d_cast_down(View v, float d);\n' % index
	header+='vr Room room%d =\n' %index
	header+='{ %f,%f,%f\n' % (w, h, d)
	header+=', 0, 0, 0\n'
	header+=', room%d_render\n' % index
	header+=', room%d_update\n' % index
	header+=', room%d_cast_down\n' % index
	header+='};\n'
	header+='\n'
	
	lsroom += [['', '', '']]
	return index

def out():
	index = 0
	print('// AUTOGEN //')
	print(header)
	for r, u, c in lsroom:
		s = "room%d.w, room%d.h, room%d.d" % (index, index, index)
		print('fn void room%d_render(View v) {' % index)
		print('\tif(v.xy[0] * v.xy[3] - v.xy[1] * v.xy[2] < 0) return;')
		print('\tif(v.yz[0] * v.yz[3] - v.yz[1] * v.yz[2] < 0) return;')
		print('\tif(v.zx[0] * v.zx[3] - v.zx[1] * v.zx[2] < 0) return;')
		print('\tglUniform4f(u_xy_id, v.xy[0], v.xy[1], v.xy[2], v.xy[3]);')
		print('\tglUniform4f(u_yz_id, v.yz[0], v.yz[1], v.yz[2], v.yz[3]);')
		print('\tglUniform4f(u_zx_id, v.zx[0], v.zx[1], v.zx[2], v.zx[3]);')
		print('\tglUniform4f(u_pos_id, v.px, v.py, v.pz, %d);' % index)
		print('\tglUniform3f(u_scale_id, %s);' % s)
		print('\tglDrawArrays(GL_QUADS, 0, 4 * 6);')
		print('\ttest_counter++;')
		print(r)
		print('}')
		print('fn View room%d_update(View v, Room **r'
		', float w, float d, float dt) {' % index)
		print('float x = v.vx * dt, y = v.vy * dt, z = v.vz * dt;')
		print('\tif(-room%d.w < v.px && v.px < room%d.w' % (index, index))
		print('\t&& -room%d.h < v.py && v.py < room%d.h' % (index, index))
		print('\t&& -room%d.d < v.pz && v.pz < room%d.d' % (index, index))
		print('\t);')
		print(u)
		print('\tv.px += x;')
		print('\tv.py += y;')
		print('\tv.pz += z;')
		print('\tif(v.px > room%d.w-w) v.px=room%d.w-w, v.vx*=0;' % (index, index))
		print('\tif(v.py > room%d.h-w) v.py=room%d.h-w, v.vy*=-1;' % (index, index))
		print('\tif(v.pz > room%d.d-w) v.pz=room%d.d-w, v.vz*=0;' % (index, index))
		print('\tif(v.px < w-room%d.w) v.px=w-room%d.w, v.vx*=0;' % (index, index))
		print('\tif(v.py < w-room%d.h) v.py=w-room%d.h, v.vy*=0;' % (index, index))
		print('\tif(v.pz < w-room%d.d) v.pz=w-room%d.d, v.vz*=0;' % (index, index))
		print('\treturn v;')
		print('}')
		print('fn float room%d_cast_down(View v, float d) {' % index)
		print('\tif(d < v.py + room%d.h) return d;' % index)
		print(c)
		print('\treturn v.py + room%d.h;' % index)
		print('}')
		index += 1

# RANDOMIZER SCRIPT V3
# I was too lazy to describe this mess
# And I was also too lazy to remove all my test and useless things like this alphabet thing
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
scale = 1.5
import random as r

rooms = []
rooms_codes = []
rooms_linked = []
rooms_linked_b = []

# generates rooms
#total_rooms = r.randint(10,20)
total_rooms = 15
for i in range(total_rooms):
	#code = alphabet[r.randint(0,25)] + str(i)
	#rooms_codes.append(code)
	s1 = r.randint(2, 15)
	s2 = r.randint(2, 15)
	s3 = r.randint(2, 15)
	n = room(s1,s2,s3)
	rooms.append(n)
	#rooms[-1] = room(4,4,4)

#links = r.randint(total_rooms, (total_rooms * 6))
links = total_rooms
#print(links)
#links = 0
for i in range(2):
	for i in range(links):
		side = r.randint(1,4)
		#start_room = r.randint(0,total_rooms-1)
		end_room = r.randint(0,total_rooms-1)
		#if start_room==end_room:
			#if end_room==0:
				#end_room += 1
			#else:
				#end_room -= 1

		#if not (start_room, side) in rooms_linked or not (end_room, side) in rooms_linked:
		size1 = r.randint(1,5)
		size2 = r.randint(1,5)
		offset_start_x = r.randint(-5,5)
		offset_start_y = r.randint(-5,5)
		offset_end_x = r.randint(-5,5)
		offset_end_y = r.randint(-5,5)
		if side==1:
			rgt(i,offset_start_x,offset_start_y, end_room,offset_end_x,offset_end_y, size1, size2)
		elif side==2:
			lft(i,offset_start_x,offset_start_y, end_room,offset_end_x,offset_end_y, size1, size2)
		elif side==3:
			fwd(i,offset_start_x,offset_start_y, end_room,offset_end_x,offset_end_y, size1, size2)
		elif side==4:
			bwd(i,offset_start_x,offset_start_y, end_room,offset_end_x,offset_end_y, size1, size2)
		elif side==5:
			uwd(i,offset_start_x,offset_start_y, end_room,offset_end_x,offset_end_y, size1, size2)
		elif side==6:
			dwn(i,offset_start_x,offset_start_y, end_room,offset_end_x,offset_end_y, size1, size2)

			#rooms_linked.append((start_room, side))
			#rooms_linked_b.append((end_room, side))

#room1 = room(4, 4, 4)
#room2 = room(4, 4, 4)
#room3 = room(4, 4, 4)

#rgt(room1,0,0, room2,0,0, 2, 2)
#rgt(room1,0,0, room3,0,0, 2, 2)

#a = room(4, 2, 8)
#b = room(4, 6, 4)
#c = room(4, 6, 4)
#d = room(4, 2, 6)
#e = room(4, 2, 1)

#uwd(a,0,+4, b,0,0, 4, 2)
#uwd(a,0,-4, c,0,0, 4, 2)

#fwd(d,0,0, b,0,4, 4, 2)
#bwd(d,0,0, c,0,4, 4, 2)

#fwd(b,0,4, e,0,0, 4, 2)

#fwd(e,+2.5,0, a,+2.5,0, 1.5,2)

#col = room(8, 12, 8)
#cll = room(2, 4, 8)
#clr = room(2, 4, 8)
#clf = room(2, 4, 6)
#clb = room(2, 4, 6)

#clu = room(2, 1, 2)
#cld = room(2, 1, 2)

#uwd(col,+4,0, clr, 0,0, 2, 6)
#uwd(col,-4,0, cll, 0,0, 2, 6)
#uwd(clr, 0,0, col,+4,0, 2, 6)
#uwd(cll, 0,0, col,-4,0, 2, 6)

#lft(clr,+4,0, clf,0,0, 4, 4)
#lft(clr,-4,0, clb,0,0, 4, 4)
#rgt(cll,+4,0, clf,0,0, 4, 4)
#rgt(cll,-4,0, clb,0,0, 4, 4)

#uwd(col,0,+4, clf,0,0, 2, 2)
#uwd(col,0,-4, clb,0,0, 2, 2)
#dwn(col,0,+4, clf,0,0, 2, 2)
#dwn(col,0,-4, clb,0,0, 2, 2)

#fwd(col,0, 0, clb,0,0, 2, 4)
#fwd(clf,0, 0, col,0,0, 2, 4)

#uwd(cld,0,0, col,0,0, 2,2)
#uwd(col,0,0, clu,0,0, 2,2)

#uwd(a,2,0, cld,0,0, 2,2)
#uwd(clu,0,0, d,2,0, 2,2)
#uwd(a,-2,0, d,-2,0, 2,2)

#hall1 = room(1, 2, 33)
#hall2 = room(1, 2, 33)
#front = room(12, 12, 6)
#back = room(12, 12, 6)

#fwd(hall2,0,0, a,0,0, 1,2)
#bwd(hall2,0,0, back,0,-10, 1, 2)

#fwd(e,+2.5,0, a,+2.5,0, 1.5,2)
#fwd(front,-2.5,0, a,-2.5,0, 1.5,2)
#fwd(a,-2.5,0, back,-2.5,0, 1.5,2)


#fwd(e,0,0, hall1,0,0, 1, 2)
#fwd(hall1,0,0, front,0,-10, 1, 2)
#fwd(back,+6.5,0, front,+6.5,0, 5.5, 12)
#fwd(back,-6.5,0, front,-6.5,0, 5.5, 12)
#fwd(back, 0,2, front, 0,2, 1, 10)

#a = room(6, 2, 2)
#b = room(6, 2, 2)
#c = room(4, 4, 4)
#d = room(10, 6, 10)

#e = room(2, 4, 4)
#f = room(2, 4, 4)
#g = room(8, 6, 2)
#h = room(8, 6, 2)

#i = room(8, 4, 8)

#fwd(front,0,-10, a,0,0, 6, 2)
#bwd(back,0,-10, b,0,0, 6, 2)

#lft(a,+.5,-.5, b,+.5,-.5, 0.5,1.5)
#lft(b,+.5,-.5, a,+.5,-.5, 0.5,1.5)
#lft(a,-.5,-.5, a,-.5,-.5, 0.5,1.5)
#lft(b,-.5,-.5, b,-.5,-.5, 0.5,1.5)


#fwd(a,+2,0, b,+2, 0, 2,2)
#bwd(b,-2,0, c,-2,+2, 2,2)
#fwd(a,-2,0, c,-2,-2, 2,2)
#fwd(c,+2,0, c,+2, -2, 2,2)



#uwd(c,+2,0, d,+3,+1, 2,2)
#uwd(c,-2,0, d,-3,-1, 2,2)

#rgt(d,0,-4, c,0,-2, 4,2)

#rgt(i,0,-2, e,0,-2, 4,2)
#lft(i,0,-2, f,0,-2, 4,2)
#fwd(d,0,-4, g,0,-4, 4,2)
#bwd(d,0,-4, h,0,-4, 4,2)

#fwd(e,0,0, g,+6,-2, 2,4)
#fwd(f,0,0, g,-6,-2, 2,4)
#bwd(e,0,0, h,+6,-2, 2,4)
#bwd(f,0,0, h,-6,-2, 2,4)

#uwd(d,0,0, i,0,0, 4,4)
#uwd(d,+4.5,0, i,+4.5,0, 0.5,2)
#uwd(d,-4.5,0, i,-4.5,0, 0.5,2)
#uwd(d,0,+4.5, i,0,+4.5, 2,0.5)
#uwd(d,0,-4.5, i,0,-4.5, 2,0.5)


#cla = room(2, 6, 1)
#clb = room(2, 6, 1)

#fwd(col,+5,0, cla,0,0, 2,6)
#fwd(col,-5,0, clb,0,0, 2,6)



#n0 = room(1000, 4, 300)

#fwd(n0,-.5,-3, 2,-.5,-.5, .5, .5)
#rgt(n0, 0, 0, n0, 0, 0, 3, 4)
#fwd(n0,+.5,-3, n0,-.5,-3, .5, .5)

# test script 1:
#links = r.randint(total_rooms, (total_rooms * 6))
#print(links)
#links = 0
#for i in range(links):
	#side = r.randint(1,6)
	#start_room = r.randint(0,total_rooms-1)
	#end_room = r.randint(0,total_rooms-1)
	#if start_room==end_room:
		#if end_room==0:
			#end_room += 1
		#else:
			#end_room -= 1

	#if not (start_room, side) in rooms_linked or not (end_room, side) in rooms_linked:
		#if side==1:
			#rgt(start_room,0,0, end_room,0,0, 4, 4)
		#elif side==2:
			#lft(start_room,0,0, end_room,0,0, 4, 4)
		#elif side==3:
			#uwd(start_room,0,0, end_room,0,0, 4, 4)
		#elif side==4:
			#dwn(start_room,0,0, end_room,0,0, 4, 4)
		#elif side==5:
			#fwd(start_room,0,0, end_room,0,0, 4, 4)
		#elif side==6:
			#bwd(start_room,0,0, end_room,0,0, 4, 4)

		#rooms_linked.append((start_room, side))
		#rooms_linked_b.append((end_room, side))

# test script 2:
#print(rooms_left)
#r2 = rooms_left
# links rooms

#for i in range(6):
	#while len(rooms_left) > 1:
		#start = rooms_left[r.randint(0, len(rooms_left)-1)]
		#end = rooms_left[r.randint(0, len(rooms_left)-1)]
		#if start==end:
			#if end==0:
				#end = rooms_left[r.randint(0, len(rooms_left)-1)]
			#else:
				#end = rooms_left[r.randint(0, len(rooms_left)-1)]

		#if i==1:
			#rgt(start,0,0, end,0,0, 4, 4)
		#elif i==2:
			#lft(start,0,0, end,0,0, 4, 4)
		#elif i==3:
			#uwd(start,0,0, end,0,0, 4, 4)
		#elif i==4:
			#dwn(start,0,0, end,0,0, 4, 4)
		#elif i==5:
			#fwd(start,0,0, end,0,0, 4, 4)
		#elif i==6:
			#bwd(start,0,0, end,0,0, 4, 4)

		#print(start)
		#print(end)
		#print(rooms_left)
		#rooms_left.remove(start)
		#print(rooms_left)
		#rooms_left.remove(end)
	#rooms_left.clear()
	#rooms_left.extend(r2)

out()
import sys
sys.stdout = open('3_roomgen_output.h', 'w')
out()
