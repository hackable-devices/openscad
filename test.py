
from cffi import FFI

ffi = FFI()

ffi.cdef("""
	int buildSTLFromSCAD(char *filename, char *output_file, unsigned int isText);
	int main(int argc, char **argv);
""")
arguments = [ffi.new("char[]", "openscad"), ffi.new("char[]", "-otest.stl"), ffi.new("char[]", "test.scad")]

#lib.main(3, arguments)

for i in range(1, 23):
	filename = ""
	if i < 10:
		filename = "/home/vagrant/openscad/examples/example00" + str(i) + ".scad"
	else:
		filename = "/home/vagrant/openscad/examples/example0" + str(i) + ".scad"
	
	output = "-o" + filename.replace(".scad", ".stl")
	output = output.replace("/home/vagrant/openscad/examples/", "./")

	arguments = [ffi.new("char[]", "openscad"), ffi.new("char[]", str(output)), ffi.new("char[]", str(filename))]
	
	lib = ffi.dlopen("./libopenscad.so")
	#lib.main(3, arguments)
	lib.buildSTLFromSCAD(ffi.new("char[]", str(filename)), ffi.new("char[]", str(output)), 0)

#lib.buildSTLFromSCAD(filename_arg, outputfile_arg)


