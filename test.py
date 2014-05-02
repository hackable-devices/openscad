
from cffi import FFI

ffi = FFI()

ffi.cdef("""
	int main(int argc, char **argv);
	int buildSTLFromSCAD(const char *filename, const char *output_file);
""")
arguments = [ffi.new("char[]", "openscad"), ffi.new("char[]", "-otest.stl"), ffi.new("char[]", "test.scad")]
filename = ffi.new("char[]", "test.scad")
output_file_name = ffi.new("char[]", "test.stl")

lib = ffi.dlopen("./libopenscad.so")
lib.main(3, arguments)
#print(lib.main(0, ffi.new("char[]", "")))
#lib.buildSTLFromSCAD(filename, output_file_name)
