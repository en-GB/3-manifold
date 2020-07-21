header = ""
lsroom = []
scale = 1
from string import Template

def linkrgt(id0, id1, a, b, c, d, z, y):

    a = a*float(scale)
    b = b*float(scale)
    c = c*float(scale)
    d = d*float(scale)
    z = z*float(scale)
    y = y*float(scale)

    r = lsroom[id0]
    s = ", ".join(map(lambda x: "%ff" % x, (a, b, c, d)))

    # based on linkrgt
    r[0] += Template("""
        if(+v.px < room${id0}.w) {
            View door = View_through_rgt(v, room${id0}.w, ${s});
            door.px -= room${id0}.w + room${id1}.w;
            door.py -= ${y}f;
            door.pz -= ${z}f;
            if (--depth) room${id1}_render(door);
            depth++;
        }
    """).substitute(locals())

    r[1] += Template("""
        if(v.pz >= ${a}f+d &&
            v.pz <= ${b}f-d &&
            v.py >= ${c}f-d &&
            v.py <= ${d}f-d &&
            v.px + x > room${id0}.w - w) {
                if (v.px + x > room${id0}.w) {
                    *r = &room${id1};
                    v.px -= room${id0}.w + room${id1}.w;
                    v.py -= ${y}f;
                    v.pz -= ${z}f;
                    return room${id1}_update(v, r, w, d, dt);
                }
                v.px += x;
                v.py += y;
                v.pz += z;

                //clamp defined in 3_less.c, like the glsl func
                v.pz = clamp(v.pz, ${a}f+d, ${b}f-d);
                v.py = clamp(v.py, ${c}f+d, ${d}f-d);

                // when v.pz and v.py are equal to some boundary,
                // v.vz and v.vy would not be set to 0 before.
                // now it always sets to 0

                //if (v.pz == ${a}f+d || v.pz == ${b}f-d)
                v.vz = 0;
                //if(v.py == ${c}f+d || v.py == ${d}f-d)
                v.vy = 0;

                return v;
            }

    """).substitute(locals())

def linklft(id0, id1, a, b, c, d, z, y):

    a = a*float(scale)
    b = b*float(scale)
    c = c*float(scale)
    d = d*float(scale)
    z = z*float(scale)
    y = y*float(scale)

    r = lsroom[id0]
    s = ", ".join(map(lambda x: "%ff" % x, (a, b, c, d)))

    r[0] += Template("""
        if(-v.px < room${id0}.w) {
            View door = View_through_lft(v, -room${id0}.w, ${s});
            door.px += room${id0}.w + room${id1}.w;
            door.py -= ${y}f;
            door.pz -= ${z}f;
            if (--depth) room${id1}_render(door);
            depth++;
        }
    """).substitute(locals())

    r[1] += Template("""
        if(v.pz >= ${a}f+d &&
           v.pz <= ${b}f-d &&
           v.py >= ${c}f+d &&
           v.py <= ${d}f-d &&
           v.px + x < -room${id0}.w + w) {
                if(v.px + x < -room${id0}.w) {
                    *r = &room${id1};
                    v.px += room${id0}.w + room${id1}.w;
                    v.py -= ${y}f;
                    v.pz -= ${z}f;
                    return room${id1}_update(v,r,w,d,dt);
                }

                v.px += x;
                v.py += y;
                v.pz += z;
            
                v.pz = clamp(v.pz, ${a}f+d, ${b}f-d);
                v.py = clamp(v.py, ${c}f+d, ${d}f-d);

                v.vz = 0;
                v.vy = 0;

                return v;
            }
    """).substitute(locals())


def linkuwd(id0, id1, a, b, c, d, x, z):

    a = a*float(scale)
    b = b*float(scale)
    c = c*float(scale)
    d = d*float(scale)
    x = x*float(scale)
    z = z*float(scale)

    r = lsroom[id0]
    s = ", ".join(map(lambda x: "%ff" % x, (a, b, c, d)))

    r[0] += Template("""
        if(+v.py < room${id0}.h) {
            View door = View_through_uwd(v, room${id0}.h, ${s});
            door.px -= ${x}f;
            door.py -= room${id0}.h + room${id1}.h;
            door.pz -= ${z}f;
            if(--depth) room${id1}_render(door);
            depth++;
        }
    """).substitute(locals())

    r[1] += Template("""
        if(v.px >= ${a}f+d &&
           v.px <= ${b}f-d &&
           v.pz >= ${c}f+d &&
           v.pz <= ${d}f-d &&
           v.py + y > room${id0}.h - w) {
                if(v.py + y > room${id0}.h) {
                    *r = &room${id1};
                    v.px -= ${x}f;
                    v.py -= room${id0}.h + room${id1}.h;
                    v.pz -= ${z}f;
                    return room${id1}_update(v,r,w,d,dt);
                }
                v.px += x;
                v.py += y;
                v.pz += z;

                v.px = clamp(v.px, ${a}f+d, ${b}f-d);
                v.pz = clamp(v.pz, ${c}f+d, ${d}f-d);

                v.vx = 0;
                v.vz = 0;

                return v;
           }
    """).substitute(locals())

def linkdwn(id0, id1, a, b, c, d, x, z):

    a = a*float(scale)
    b = b*float(scale)
    c = c*float(scale)
    d = d*float(scale)
    x = x*float(scale)
    z = z*float(scale)

    r = lsroom[id0]
    s = ", ".join(map(lambda x: "%ff" % x, (a, b, c, d)))

    r[0] += Template("""
        if(-v.py < room${id0}.h) {
            View door = View_through_dwn(v, -room${id0}.h, ${s});
            door.px -= ${x}f;
            door.py += room${id0}.h + room${id1}.h;
            door.pz -= ${z}f;
            if(--depth) room${id1}_render(door);
            depth++;
        }""").substitute(locals())

    r[1] += Template("""
        if(v.px >= ${a}f+d &&
           v.px <= ${b}f-d &&
           v.pz >= ${c}f+d &&
           v.pz <= ${d}f-d &&
           v.py + y < -room${id0}.h + w) {
                if (v.py + y < -room${id0}.h) {
                    *r = &room${id1};
                    v.px -= ${x}f;
                    v.py += room${id0}.h + room${id1}.h;
                    v.pz -= ${z}f;
                    return room${id1}_update(v,r,w,d,dt);
                }

            v.px += x;
            v.py += y;
            v.pz += z;

            v.px = clamp(v.px, ${a}f+d, ${b}f-d);
            v.pz = clamp(v.pz, ${c}f+d, ${d}f-d);

            v.vx = 0;
            v.vz = 0;

            return v;
        }""").substitute(locals())

    r[2] += Template("""
        if (v.px >= ${a}f &&
            v.px <= ${b}f &&
            v.pz >= ${c}f &&
            v.pz <= ${d}f) {
                v.px -= ${x}f;
                v.py += room${id0}.h + room${id1}.h;
                v.pz -= ${z}f;
                return room${id1}_cast_down(v, d);
        }
    """).substitute(locals())

def linkfwd(id0, id1, a, b, c, d, x, y):

    a = a*float(scale)
    b = b*float(scale)
    c = c*float(scale)
    d = d*float(scale)
    x = x*float(scale)
    y = y*float(scale)

    r = lsroom[id0]
    s = ", ".join(map(lambda x: "%ff" % x, (a, b, c, d)))

    r[0] += Template("""
        if(+v.pz < room${id0}.d) {
            View door = View_through_fwd(v, room${id0}.d, ${s});
            door.px -= ${x}f;
            door.py -= ${y}f;
            door.pz -= room${id0}.d + room${id1}.d;
            if(--depth) room${id1}_render(door);
            depth++;
        }
    """).substitute(locals())

    r[1] += Template("""
        if(v.px >= ${a}f+d &&
           v.px <= ${b}f-d &&
           v.py >= ${c}f+d &&
           v.py <= ${d}f-d &&
           v.pz + z > room${id0}.d - w) {
                if(v.pz + z > room${id0}.d) {
                    *r = &room${id1};
                    v.px -= ${x}f;
                    v.py -= ${y}f;
                    v.pz -= room${id0}.d + room${id1}.d;
                    v = room${id1}_update(v,r,w,d,dt);
                    v.vz -= room${id0}._d + room${id1}._d; //velocity
                    return v;
                }

                v.px += x;
                v.py += y;
                v.pz += z;

                v.px = clamp(v.px, ${a}f+d, ${b}f-d);
                v.py = clamp(v.py, ${c}f+d, ${d}f-d);

                v.vx = 0;
                v.vy = 0;

                return v;
           }
    """).substitute(locals())

def linkbwd(id0, id1, a, b, c, d, x, y):

    a = a*float(scale)
    b = b*float(scale)
    c = c*float(scale)
    d = d*float(scale)
    x = x*float(scale)
    y = y*float(scale)

    r = lsroom[id0]
    s = ", ".join(map(lambda x: "%ff" % x, (a, b, c, d)))

    r[0] += Template("""
        if (-v.pz < room${id0}.d) {
            View door = View_through_bwd(v, -room${id0}.d, ${s});
            door.px -= ${x}f;
            door.py -= ${y}f;
            door.pz += room${id0}.d + room${id1}.d;
            if (--depth) room${id1}_render(door);
            depth++;
        }
    """).substitute(locals())

    r[1] += Template("""
        if(v.px >= ${a}f+d &&
           v.px <= ${b}f-d &&
           v.py >= ${c}f+d &&
           v.py <= ${d}f-d &&
           v.pz + z < -room${id0}.d + w) {
               if (v.pz + z < -room${id0}.d){
                   *r = &room${id1};
                   v.px -= ${x}f;
                   v.py -= ${y}f;
                   v.pz += room${id0}.d + room${id1}.d;
                   v = room${id1}_update(v,r,w,d,dt);
                   v.vz += room${id0}._d + room${id1}._d; //velocity
                   return v;
               }

               v.px += x;
               v.py += y;
               v.pz += z;

               v.px = clamp(v.px, ${a}f+d, ${b}f-d);
               v.py = clamp(v.py, ${c}f+d, ${d}f-d);
               
               v.vx = 0;
               v.vy = 0;

               return v;
           }
    """).substitute(locals())


def rgt(id0, z0, y0, id1, z1, y1, d, h):
    linkrgt(id0, id1, z0 - d, z0 + d, y0 - h, y0 + h, z0 - z1, y0 - y1)
    linklft(id1, id0, z1 - d, z1 + d, y1 - h, y1 + h, z1 - z0, y1 - y0)


def lft(id0, z0, y0, id1, z1, y1, d, h):
    linklft(id0, id1, z0 - d, z0 + d, y0 - h, y0 + h, z0 - z1, y0 - y1)
    linkrgt(id1, id0, z1 - d, z1 + d, y1 - h, y1 + h, z1 - z0, y1 - y0)


def uwd(id0, x0, z0, id1, x1, z1, w, h):
    linkuwd(id0, id1, x0 - w, x0 + w, z0 - h, z0 + h, x0 - x1, z0 - z1)
    linkdwn(id1, id0, x1 - w, x1 + w, z1 - h, z1 + h, x1 - x0, z1 - z0)


def dwn(id0, x0, z0, id1, x1, z1, w, h):
    linkdwn(id0, id1, x0 - w, x0 + w, z0 - h, z0 + h, x0 - x1, z0 - z1)
    linkuwd(id1, id0, x1 - w, x1 + w, z1 - h, z1 + h, x1 - x0, z1 - z0)


def fwd(id0, x0, y0, id1, x1, y1, w, h):
    linkfwd(id0, id1, x0 - w, x0 + w, y0 - h, y0 + h, x0 - x1, y0 - y1)
    linkbwd(id1, id0, x1 - w, x1 + w, y1 - h, y1 + h, x1 - x0, y1 - y0)


def bwd(id0, x0, y0, id1, x1, y1, w, h):
    linkbwd(id0, id1, x0 - w, x0 + w, y0 - h, y0 + h, x0 - x1, y0 - y1)
    linkfwd(id1, id0, x1 - w, x1 + w, y1 - h, y1 + h, x1 - x0, y1 - y0)


def room(w, h, d):

    w *= scale
    h *= scale
    d *= scale

    global header, lsroom
    index = len(lsroom)

    header += Template("""
        fn void room${index}_render(View v);
        fn View room${index}_update(View v, Room **r, float w, float d, float dt);
        fn float room${index}_cast_down(View v, float d);
        vr Room room${index} = {
            ${w}, ${h}, ${d},
            0,0,0,
            room${index}_render,
            room${index}_update,
            room${index}_cast_down
        };
    """).substitute(locals())

    lsroom += [["", "", ""]]
    return index


def out():
    index = 0
    print("// AUTOGEN //")
    print(header)
    for r, u, c in lsroom:
        s = "room%d.w, room%d.h, room%d.d" % (index, index, index)
        print(Template("""
            fn void room${index}_render(View v) {
                if(v.xy[0] * v.xy[3] - v.xy[1] * v.xy[2] < 0) return;
                if(v.yz[0] * v.yz[3] - v.yz[1] * v.yz[2] < 0) return;
                if(v.zx[0] * v.zx[3] - v.zx[1] * v.zx[2] < 0) return;
                glUniform4f(u_xy_id, v.xy[0], v.xy[1], v.xy[2], v.xy[3]);
                glUniform4f(u_yz_id, v.yz[0], v.yz[1], v.yz[2], v.yz[3]);
                glUniform4f(u_zx_id, v.zx[0], v.zx[1], v.zx[2], v.zx[3]);
                glUniform4f(u_pos_id, v.px, v.py, v.pz, ${index});
                glUniform3f(u_scale_id, ${s});
                glDrawArrays(GL_QUADS, 0, 4 * 6);
                test_counter++;
                ${r}
            }

            fn View room${index}_update(View v, Room **r, float w, float d, float dt) {
                float x = v.vx * dt, y = v.vy * dt, z = v.vz * dt;
                if(-room${index}.w < v.px && v.px < room${index}.w
                && -room${index}.h < v.py && v.py < room${index}.h
                && -room${index}.d < v.pz && v.pz < room${index}.d);
                ${u}
            
                v.px += x;
                v.py += y;
                v.pz += z;
                if(v.px > room${index}.w-w) v.px=room${index}.w-w, v.vx*=0;
                if(v.py > room${index}.h-w) v.py=room${index}.h-w, v.vy*=-1;
                if(v.pz > room${index}.d-w) v.pz=room${index}.d-w, v.vz*=0;
                if(v.px < w-room${index}.w) v.px=w-room${index}.w, v.vx*=0;
                if(v.py < w-room${index}.h) v.py=w-room${index}.h, v.vy*=0;
                if(v.pz < w-room${index}.d) v.pz=w-room${index}.d, v.vz*=0;

                return v;
            }
            fn float room${index}_cast_down(View v, float d) {
                if(d < v.py + room${index}.h)
                    return d;
            
                return v.py + room${index}.h;
            }
        """).substitute(locals()))
        index += 1


# a = room(1, 2, 2)
# b = room(4, 2, 2)
# fwd(a,0,0, b,0,0, 1, 2)


scale = 1

a = room(4, 2, 8)
b = room(4, 6, 4)
c = room(4, 6, 4)
d = room(4, 2, 6)
e = room(4, 2, 1)

uwd(a, 0, +4, b, 0, 0, 4, 2)
uwd(a, 0, -4, c, 0, 0, 4, 2)

fwd(d, 0, 0, b, 0, 4, 4, 2)
bwd(d, 0, 0, c, 0, 4, 4, 2)

# rgt(a,7,0, b,1,4, 1, 2)
# fwd(a,3,0, b,+1,0, 1, 2)
# fwd(b,0,4, b,-1,0, 1, 2)
fwd(b, 0, 4, e, 0, 0, 4, 2)

fwd(e, +2.5, 0, a, +2.5, 0, 1.5, 2)
# fwd(e,-2.5,0, a,-2.5,0, 1.5,2)
# fwd(e,-2,0, c,0,10, 1, 2)

col = room(8, 12, 8)
cll = room(2, 4, 8)
clr = room(2, 4, 8)
clf = room(2, 4, 6)
clb = room(2, 4, 6)

clu = room(2, 1, 2)
cld = room(2, 1, 2)

uwd(col, +4, 0, clr, 0, 0, 2, 6)
uwd(col, -4, 0, cll, 0, 0, 2, 6)
uwd(clr, 0, 0, col, +4, 0, 2, 6)
uwd(cll, 0, 0, col, -4, 0, 2, 6)

lft(clr, +4, 0, clf, 0, 0, 4, 4)
lft(clr, -4, 0, clb, 0, 0, 4, 4)
rgt(cll, +4, 0, clf, 0, 0, 4, 4)
rgt(cll, -4, 0, clb, 0, 0, 4, 4)

uwd(col, 0, +4, clf, 0, 0, 2, 2)
uwd(col, 0, -4, clb, 0, 0, 2, 2)
dwn(col, 0, +4, clf, 0, 0, 2, 2)
dwn(col, 0, -4, clb, 0, 0, 2, 2)

# fwd(clb,0, 0, clf,0,0, 2, 4)
fwd(col, 0, 0, clb, 0, 0, 2, 4)
fwd(clf, 0, 0, col, 0, 0, 2, 4)

uwd(cld, 0, 0, col, 0, 0, 2, 2)
uwd(col, 0, 0, clu, 0, 0, 2, 2)

uwd(a, 2, 0, cld, 0, 0, 2, 2)
uwd(clu, 0, 0, d, 2, 0, 2, 2)
uwd(a, -2, 0, d, -2, 0, 2, 2)

hall1 = room(1, 2, 33)
hall2 = room(1, 2, 33)
front = room(12, 12, 6)
back = room(12, 12, 6)

fwd(hall2, 0, 0, a, 0, 0, 1, 2)
bwd(hall2, 0, 0, back, 0, -10, 1, 2)

fwd(e, +2.5, 0, a, +2.5, 0, 1.5, 2)
fwd(front, -2.5, 0, a, -2.5, 0, 1.5, 2)
fwd(a, -2.5, 0, back, -2.5, 0, 1.5, 2)


fwd(e, 0, 0, hall1, 0, 0, 1, 2)
fwd(hall1, 0, 0, front, 0, -10, 1, 2)
fwd(back, +6.5, 0, front, +6.5, 0, 5.5, 12)
fwd(back, -6.5, 0, front, -6.5, 0, 5.5, 12)
# fwd(back, 0,2, back, 0,2, 1, 10)
# fwd(front, 0,2, front, 0,2, 1, 10)
fwd(back, 0, 2, front, 0, 2, 1, 10)

a = room(6, 2, 2)
b = room(6, 2, 2)
c = room(4, 4, 4)
d = room(10, 6, 10)

e = room(2, 4, 4)
f = room(2, 4, 4)
g = room(8, 6, 2)
h = room(8, 6, 2)

i = room(8, 4, 8)

fwd(front, 0, -10, a, 0, 0, 6, 2)
bwd(back, 0, -10, b, 0, 0, 6, 2)

lft(a, +0.5, -0.5, b, +0.5, -0.5, 0.5, 1.5)
lft(b, +0.5, -0.5, a, +0.5, -0.5, 0.5, 1.5)
lft(a, -0.5, -0.5, a, -0.5, -0.5, 0.5, 1.5)
lft(b, -0.5, -0.5, b, -0.5, -0.5, 0.5, 1.5)

# lft(a,0,0, a,0,0, 0.5,1)
# lft(b,0,0, b,0,0, 0.5,1)

fwd(a, +2, 0, b, +2, 0, 2, 2)
bwd(b, -2, 0, c, -2, +2, 2, 2)
fwd(a, -2, 0, c, -2, -2, 2, 2)
fwd(c, +2, 0, c, +2, -2, 2, 2)

# uwd(c,0,0, d,0,0, 2,2)
# uwd(i,0,0, c,0,0, 2,2)


uwd(c, +2, 0, d, +3, +1, 2, 2)
uwd(c, -2, 0, d, -3, -1, 2, 2)

rgt(d, 0, -4, c, 0, -2, 4, 2)

rgt(i, 0, -2, e, 0, -2, 4, 2)
lft(i, 0, -2, f, 0, -2, 4, 2)
fwd(d, 0, -4, g, 0, -4, 4, 2)
bwd(d, 0, -4, h, 0, -4, 4, 2)

fwd(e, 0, 0, g, +6, -2, 2, 4)
fwd(f, 0, 0, g, -6, -2, 2, 4)
bwd(e, 0, 0, h, +6, -2, 2, 4)
bwd(f, 0, 0, h, -6, -2, 2, 4)

uwd(d, 0, 0, i, 0, 0, 4, 4)
uwd(d, +4.5, 0, i, +4.5, 0, 0.5, 2)
uwd(d, -4.5, 0, i, -4.5, 0, 0.5, 2)
uwd(d, 0, +4.5, i, 0, +4.5, 2, 0.5)
uwd(d, 0, -4.5, i, 0, -4.5, 2, 0.5)


cla = room(2, 6, 1)
clb = room(2, 6, 1)

fwd(col, +5, 0, cla, 0, 0, 2, 6)
fwd(col, -5, 0, clb, 0, 0, 2, 6)


n0 = room(1000, 4, 300)

fwd(n0, -0.5, -3, 2, -0.5, -0.5, 0.5, 0.5)
rgt(n0, 0, 0, n0, 0, 0, 3, 4)
# fwd(n0, 0, -3, n0, 0, -3, 1, 1)
fwd(n0, +0.5, -3, n0, -0.5, -3, 0.5, 0.5)

out()
import sys

sys.stdout = open("3_roomgen_output.h", "w")
out()

