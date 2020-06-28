
#if 0


python 3_roomgen.py && clang -m64 $0 -std=c99 -Wall -Werror -Wno-unused -Wno-string-plus-int -Os -o ${0%.*}.exe -static -lglfw3 -lGdi32 &&

exec ${0%.*}.exe "$@"
exit 0

#endif

#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>
#include <math.h>
#include "glad/glad.h"
#include <GLFW/glfw3.h>

#define vr static
#define fn static
#define string(...) #__VA_ARGS__

#define assert(c, ...) \
do { \
	if(__builtin_expect(!(c), 0)) { \
		printf("\n <CRASH> %s:%d: %s\n  ", __FILE__, __LINE__, #c); \
		printf(__VA_ARGS__); \
		putchar('\n'); \
		putchar('\n'); \
		fflush(stdout); \
		exit(-1); \
	} \
} while(0);

typedef struct View View;
typedef struct Room Room;

struct View {
	float xy[4];
	float yz[4];
	float zx[4];
	float px, py, pz;
	float vx, vy, vz;
};

struct Room {
	float w, h, d;
	float _w, _h, _d;
	void (*render)(View v);
	View (*update)(View v, Room **r, float w, float d, float dt);
	float (*cast_down)(View v, float d);
};

fn View View_through_rgt(View v, float x, float a, float b, float c, float d) {
	
	x -= v.px;
	c -= v.py;
	d -= v.py;
	a -= v.pz;
	b -= v.pz;
	
	if(x * v.xy[0] + d * v.xy[1] >= 0) v.xy[0] = +d, v.xy[1] = -x;
	if(x * v.xy[2] + c * v.xy[3] >= 0) v.xy[2] = -c, v.xy[3] = +x;
	if(a * v.zx[0] + x * v.zx[1] >= 0) v.zx[0] = +x, v.zx[1] = -a;
	if(b * v.zx[2] + x * v.zx[3] >= 0) v.zx[2] = -x, v.zx[3] = +b;
	
	return v;
}

fn View View_through_lft(View v, float x, float a, float b, float c, float d) {
	
	x -= v.px;
	c -= v.py;
	d -= v.py;
	a -= v.pz;
	b -= v.pz;
	
	if(x * v.xy[0] + c * v.xy[1] >= 0) v.xy[0] = +c, v.xy[1] = -x;
	if(x * v.xy[2] + d * v.xy[3] >= 0) v.xy[2] = -d, v.xy[3] = +x;
	if(b * v.zx[0] + x * v.zx[1] >= 0) v.zx[0] = +x, v.zx[1] = -b;
	if(a * v.zx[2] + x * v.zx[3] >= 0) v.zx[2] = -x, v.zx[3] = +a;
	
	return v;
}

fn View View_through_uwd(View v, float y, float a, float b, float c, float d) {
	
	a -= v.px;
	b -= v.px;
	y -= v.py;
	c -= v.pz;
	d -= v.pz;
	
	if(a * v.xy[0] + y * v.xy[1] >= 0) v.xy[0] = +y, v.xy[1] = -a;
	if(b * v.xy[2] + y * v.xy[3] >= 0) v.xy[2] = -y, v.xy[3] = +b;
	if(y * v.yz[0] + d * v.yz[1] >= 0) v.yz[0] = +d, v.yz[1] = -y;
	if(y * v.yz[2] + c * v.yz[3] >= 0) v.yz[2] = -c, v.yz[3] = +y;
	
	return v;
}

fn View View_through_dwn(View v, float y, float a, float b, float c, float d) {
	
	a -= v.px;
	b -= v.px;
	y -= v.py;
	c -= v.pz;
	d -= v.pz;
	
	if(b * v.xy[0] + y * v.xy[1] >= 0) v.xy[0] = +y, v.xy[1] = -b;
	if(a * v.xy[2] + y * v.xy[3] >= 0) v.xy[2] = -y, v.xy[3] = +a;
	if(y * v.yz[0] + c * v.yz[1] >= 0) v.yz[0] = +c, v.yz[1] = -y;
	if(y * v.yz[2] + d * v.yz[3] >= 0) v.yz[2] = -d, v.yz[3] = +y;
	
	return v;
}

fn View View_through_fwd(View v, float z, float a, float b, float c, float d) {
	
	a -= v.px;
	b -= v.px;
	c -= v.py;
	d -= v.py;
	z -= v.pz;
	
	if(c * v.yz[0] + z * v.yz[1] >= 0) v.yz[0] = +z, v.yz[1] = -c;
	if(d * v.yz[2] + z * v.yz[3] >= 0) v.yz[2] = -z, v.yz[3] = +d;
	if(z * v.zx[0] + b * v.zx[1] >= 0) v.zx[0] = +b, v.zx[1] = -z;
	if(z * v.zx[2] + a * v.zx[3] >= 0) v.zx[2] = -a, v.zx[3] = +z;
	
	return v;
}

fn View View_through_bwd(View v, float z, float a, float b, float c, float d) {
	
	a -= v.px;
	b -= v.px;
	c -= v.py;
	d -= v.py;
	z -= v.pz;
	
	if(d * v.yz[0] + z * v.yz[1] >= 0) v.yz[0] = +z, v.yz[1] = -d;
	if(c * v.yz[2] + z * v.yz[3] >= 0) v.yz[2] = -z, v.yz[3] = +c;
	if(z * v.zx[0] + a * v.zx[1] >= 0) v.zx[0] = +a, v.zx[1] = -z;
	if(z * v.zx[2] + b * v.zx[3] >= 0) v.zx[2] = -b, v.zx[3] = +z;
	
	return v;
}

vr float player_speed;
vr float player_x, player_y, player_z;
vr void *player_room;
vr int u_xy_id;
vr int u_yz_id;
vr int u_zx_id;
vr int u_pos_id;
vr int u_scale_id;
vr double gtime;
vr int depth = 25;
vr int test_counter = 0;

#undef fn
#define fn static __attribute__((noinline))
#include "3_roomgen_output.h"
#undef fn
#define fn static

fn char *shader_error_log(unsigned shader) {
	
	int length;
	glGetShaderiv(shader, GL_INFO_LOG_LENGTH, &length);
	
	char *log = malloc(length);
	glGetShaderInfoLog(shader, length, &length, log);
	return log;
}

fn char *program_error_log(unsigned program) {
	
	int length;
	glGetProgramiv(program, GL_INFO_LOG_LENGTH, &length);
	
	char *log = malloc(length);
	glGetProgramInfoLog(program, length, &length, log);
	return log;
}

fn unsigned create_shader(unsigned prog, GLenum type, char *src) {
	
	int error = 0;
	unsigned r = glCreateShader(type);
	
	glShaderSource(r, 1, (void *)&src, 0);
	glCompileShader(r);
	
	glGetShaderiv(r, GL_COMPILE_STATUS, &error);
	assert(error, "Compiler error in shader\n%s", shader_error_log(r));
	
	glAttachShader(prog, r);
	return r;
}

fn unsigned create_program(char *vert_src, char *frag_src) {
	
	int error = 0;
	unsigned prog = glCreateProgram();
	unsigned vert = create_shader(prog, GL_VERTEX_SHADER, vert_src);
	unsigned frag = create_shader(prog, GL_FRAGMENT_SHADER, frag_src);
	
	glLinkProgram(prog);
	glGetProgramiv(prog, GL_LINK_STATUS, &error);
	assert(error, "Linker error in program\n%s", program_error_log(prog));
	
	glDetachShader(prog, vert);
	glDetachShader(prog, frag);
	glDeleteShader(vert);
	glDeleteShader(frag);
	
	glValidateProgram(prog);
	glGetProgramiv(prog, GL_VALIDATE_STATUS, &error);
	assert(error, "Linker error in program\n%s", program_error_log(prog));
	
	return prog;
}

fn void loop(GLFWwindow *window) {
	
	glfwSetInputMode(window, GLFW_CURSOR, GLFW_CURSOR_DISABLED);
	
	glEnable(GL_CLIP_PLANE0);
	glEnable(GL_CLIP_PLANE1);
	glEnable(GL_CLIP_PLANE2);
	glEnable(GL_CLIP_PLANE3);
	glEnable(GL_CLIP_PLANE4);
	glEnable(GL_CLIP_PLANE5);
	
	unsigned prog = create_program("#version 150\n" string(
		
		vec2 I(vec2 v) {
			return vec2(-v.y, v.x);
		}
		
		uniform vec4 u_xy;
		uniform vec4 u_yz;
		uniform vec4 u_zx;
		uniform vec4 u_pos;
		uniform vec3 u_scale;
		uniform vec3 u_rgt;
		uniform vec3 u_uwd;
		uniform vec3 u_fwd;
		uniform float u_t;
		
		centroid out vec3 v_vert;
		out vec3 v_nor;
		out vec3 v_pos;
		
		const vec3 vert[6 * 4] = vec3[]
		( vec3(-1.,-1.,-1.),vec3(-1.,-1.,+1.),vec3(-1.,+1.,+1.),vec3(-1.,+1.,-1.)
		, vec3(-1.,-1.,-1.),vec3(+1.,-1.,-1.),vec3(+1.,-1.,+1.),vec3(-1.,-1.,+1.)
		, vec3(-1.,-1.,-1.),vec3(-1.,+1.,-1.),vec3(+1.,+1.,-1.),vec3(+1.,-1.,-1.)
		
		, vec3(+1.,-1.,-1.),vec3(+1.,+1.,-1.),vec3(+1.,+1.,+1.),vec3(+1.,-1.,+1.)
		, vec3(-1.,+1.,-1.),vec3(-1.,+1.,+1.),vec3(+1.,+1.,+1.),vec3(+1.,+1.,-1.)
		, vec3(-1.,-1.,+1.),vec3(+1.,-1.,+1.),vec3(+1.,+1.,+1.),vec3(-1.,+1.,+1.)
		);
		
		const vec3 nor[6] = vec3[]
		( vec3(+1., 0., 0.)
		, vec3( 0.,+1., 0.)
		, vec3( 0., 0.,+1.)
		
		, vec3(-1., 0., 0.)
		, vec3( 0.,-1., 0.)
		, vec3( 0., 0.,-1.)
		);
		
		vec2 r90(vec2 z) {
			return vec2(-z.y, z.x);
		}
		
		void main() {
			v_vert = vert[gl_VertexID] * u_scale;
			v_nor = nor[gl_VertexID / 4];
			v_pos = v_vert - u_pos.xyz;
			
			gl_ClipDistance[0] = dot(v_pos.xy, u_xy.xy);
			gl_ClipDistance[1] = dot(v_pos.xy, u_xy.zw);
			gl_ClipDistance[2] = dot(v_pos.yz, u_yz.xy);
			gl_ClipDistance[3] = dot(v_pos.yz, u_yz.zw);
			gl_ClipDistance[4] = dot(v_pos.zx, u_zx.xy);
			gl_ClipDistance[5] = dot(v_pos.zx, u_zx.zw);
			
			gl_Position = vec4
			( dot(v_pos, u_rgt)
			, dot(v_pos, u_uwd)
			, dot(v_pos, u_fwd)
			, dot(v_pos, u_fwd) * 2.0);
		}
	), "#version 150\n" string(
		uniform vec4 u_xy;
		uniform vec4 u_yz;
		uniform vec4 u_zx;
		uniform vec4 u_pos;
		uniform vec3 u_scale;
		uniform vec3 u_rgt;
		uniform vec3 u_uwd;
		uniform vec3 u_fwd;
		uniform float u_asd;
		uniform int u_frame;
		uniform float u_t;
		
		centroid in vec3 v_vert;
		in vec3 v_nor;
		in vec3 v_pos;
		
		out vec4 o_color;
		
		vec3 hash23(vec2 p) {
			vec3 p3 = fract(p.xyx * vec3(.1031, .1030, .0973));
			p3 += dot(p3, p3.yxz+19.19);
			return fract((p3.xxy + p3.yzz)*(p3.zyx + u_t * 1e-2));
		}
		
		void main() {
			vec3 H = fwidth(hash23(floor(gl_FragCoord.xy * .75)));
			vec3 w = u_scale - abs(v_vert);
			vec3 a = vec3(101.1234, 132.534, 647.12);
			float t = step(0., floor(dot(sin(v_vert + H*fwidth(v_vert)), u_scale))) * .1;
			vec3 c = fract(1. / cos(u_pos.w) * a + t + v_nor * .1);
			c = c / (c + dot(1. / (1. + w*w), vec3(.2)) + H * .1);
			o_color = vec4(pow(c, vec3(.5)), 1.0);
		}
	));
	
	glUseProgram(prog);
	u_xy_id = glGetUniformLocation(prog, "u_xy");
	u_yz_id = glGetUniformLocation(prog, "u_yz");
	u_zx_id = glGetUniformLocation(prog, "u_zx");
	u_pos_id = glGetUniformLocation(prog, "u_pos");
	u_scale_id = glGetUniformLocation(prog, "u_scale");
	int u_rgt_id = glGetUniformLocation(prog, "u_rgt");
	int u_uwd_id = glGetUniformLocation(prog, "u_uwd");
	int u_fwd_id = glGetUniformLocation(prog, "u_fwd");
	int u_asd_id = glGetUniformLocation(prog, "u_asd");
	int u_frame_id = glGetUniformLocation(prog, "u_frame");
	int u_t_id = glGetUniformLocation(prog, "u_t");
	
	View v;
	Room *r = &room0;
	memset(&v, 0, sizeof v);
	
	float P = 0, H = 0;
	double mx = 0, my = 0;
	double _mx, _my;
	gtime = glfwGetTime();
	glfwGetCursorPos(window, &mx, &my);
	glClearColor(0, 0, 0, 0);
	glEnable(GL_CULL_FACE);
	glDisable(GL_DEPTH_TEST);
	glfwSwapInterval(0);
	
	if(glfwRawMouseMotionSupported())
		glfwSetInputMode(window, GLFW_RAW_MOUSE_MOTION, GLFW_TRUE);
	
	while(!glfwWindowShouldClose(window)) {
		double time = glfwGetTime();
		
		{
			float g = 2;
			room12.d = 10.1 - 10*sin(g*gtime);
			room13.d = 10.1 + 10*sin(g*gtime);
			room12._d = -10*g*cos(g*gtime);
			room13._d = +10*g*cos(g*gtime);
		}
		
		vr double vblank = 0;
		vr double next = 0;
		
		float dt = time - gtime;
		gtime = time;
		
		glfwPollEvents();
		glfwGetCursorPos(window, &_mx, &_my);
		_mx -= mx;
		_my -= my;
		mx += _mx;
		my += _my;
		
		P -= _my * 0.001f;
		H -= _mx * 0.001f;
		
		if(P > +1.5707963f) P = +1.5707963f;
		if(P < -1.5707963f) P = -1.5707963f;
		if(H > +3.1415926f) H -= 6.2831852f;
		if(H < -3.1415926f) H += 6.2831852f;
		
		float bhop_limit = 150;
		float speed = 8 - 4 * glfwGetKey(window, GLFW_KEY_LEFT_SHIFT);
		float accel = 100;
		float friction = 50;
		float air_speed = 1;
		float air_accel = 150;
		
		{
			vr int jump = 0;
			
			int ix = glfwGetKey(window, GLFW_KEY_D) - glfwGetKey(window, GLFW_KEY_A);
			int iy = glfwGetKey(window, GLFW_KEY_E) - glfwGetKey(window, GLFW_KEY_Q);
			int iz = glfwGetKey(window, GLFW_KEY_W) - glfwGetKey(window, GLFW_KEY_S);
			int ij = glfwGetMouseButton(window, GLFW_MOUSE_BUTTON_RIGHT);
			ij |= glfwGetKey(window, GLFW_KEY_SPACE);
			
			vr int _ix = 0;
			vr int _iy = 0;
			vr int _iz = 0;
			vr int _ij = 0;
			
			float gspeed = 1;
			if(ix && iz) gspeed = 1.0 / sqrt(2.0);
			
			float rx = cosf(H);
			float ry = 0;
			float rz = sinf(H);
			
			float ux = 0;
			float uy = 1;
			float uz = 0;
			
			float fx = -sinf(H);
			float fy = 0;
			float fz = cosf(H);
			
			float dx = (ix*rx + iz*fx) * gspeed;
			float dz = (ix*rz + iz*fz) * gspeed;
			
			float dist = 1e20f;
			for(int a = 0; a < 20; a++)
			for(int b = 0; b < 20; b++) {
				
				Room *rrr = r;
				View vvv = v;
				
				float radius = 0.5f;
				
				float x = (a/(20.0f-1)-0.5f) * radius;
				float y = (b/(20.0f-1)-0.5f) * radius;
				
				vvv.vx = x;
				vvv.vy = 0;
				vvv.vz = y;
				
				vvv = rrr->update(vvv, &rrr, 0, 0, 1);
				float d = rrr->cast_down(vvv, 2);
				
				if(d < dist)
					dist = d;
			}
			
			if(dist < 1.1f) {
				
				if(!jump) {
					jump |= (player_speed < bhop_limit) & ij & ~_ij;
					v.vy += dt * ((1 - dist) * 24 - v.vy) * 24;
				}
				
				if(jump) {
					v.vy = 10;
				} else
				{
					
					if(v.vx*v.vx + v.vz*v.vz > 0) {
						float l = sqrtf(v.vx*v.vx + v.vz*v.vz);
						if(l < dt * friction) {
							v.vx = 0;
							v.vz = 0;
						} else {
							v.vx -= v.vx/l * dt * friction;
							v.vz -= v.vz/l * dt * friction;
						}
					}
					
					
					float slide = dx*v.vz - dz*v.vx;
					float slide2 = slide*slide;
					float speed2 = speed*speed;
					
					float ground_speed = speed;
					// if(v.vx*v.vx + v.vz*v.vz < ground_speed*ground_speed) 	{
					// float ground_speed = speed2 < slide2 ? 0 : sqrtf(speed2 - slide2);
					if(dx*v.vx + dz*v.vz < ground_speed) {
						v.vx += dx * dt * accel;
						v.vz += dz * dt * accel;
						float t = dx*v.vx + dz*v.vz;
						if(t > ground_speed) {
							t -= ground_speed;
							v.vx -= dx * t;
							v.vz -= dz * t;
						}
					}
				}
				
			} else
			{
				jump = 0;
				
				v.vy += dt * -40;
				
				if(dx*v.vx + dz*v.vz < air_speed) {
					v.vx += dx * dt * air_accel;
					v.vz += dz * dt * air_accel;
					
					float t = dx*v.vx + dz*v.vz;
					if(t > air_speed) {
						t -= air_speed;
						v.vx -= dx * t;
						v.vz -= dz * t;
					}
				}
			}
			
			v = r->update(v, &r, 0.1f, 0.1f, dt);
			
			_ij = ij;
			_ix = ix;
			_iy = iy;
			_iz = iz;
		}
		
		player_x = v.px;
		player_y = v.py;
		player_z = v.pz;
		player_room = r;
		player_speed = sqrtf(v.vx*v.vx + v.vz*v.vz);
		
		float rx = cosf(H);
		float ry = 0;
		float rz = sinf(H);
		
		float ux = sinf(P) * +sinf(H);
		float uy = cosf(P);
		float uz = sinf(P) * -cosf(H);
		
		float fx = ry*uz - uy*rz;
		float fy = ux*rz - rx*uz;
		float fz = rx*uy - ux*ry;
		
		int width, height;
		glfwGetWindowSize(window, &width, &height);
		
		ux *= 1.f * width / height;
		uy *= 1.f * width / height;
		uz *= 1.f * width / height;
		
		glUniform3f(u_rgt_id, rx, ry, rz);
		glUniform3f(u_uwd_id, ux, uy, uz);
		glUniform3f(u_fwd_id, fx, fy, fz);
		glUniform1f(u_t_id, gtime);
		
		r->render(v);
		glfwSwapBuffers(window);
		glClear(GL_COLOR_BUFFER_BIT);
	}
}

int main(int argc, char *args[]) {
	
	if(!glfwInit())
		return -1;
	
	glfwWindowHint(GLFW_SAMPLES, 4);
	
	GLFWmonitor *monitor = glfwGetPrimaryMonitor();
	const GLFWvidmode *mode = glfwGetVideoMode(monitor);
	GLFWwindow *W = glfwCreateWindow(mode->width, mode->height, "", monitor, 0);
	
	if(W == 0) {
		printf("Failed to open Window");
		glfwTerminate();
		return -1;
	}
	
	glfwMakeContextCurrent(W);
	
	if(!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress)) {
		printf("Failed to initialize OpenGL context");
		return -1;
	}
	
	loop(W);
	
	glfwTerminate();
	return 0;
}
