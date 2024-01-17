import sys
import os

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python3 newClass.py <class_name>")
		sys.exit(1)

	class_name = sys.argv[1]
	includesDir = "includes"
	srcDir = "src"

	os.makedirs(includesDir, exist_ok=True)
	os.makedirs(srcDir, exist_ok=True)

	hppPath = os.path.join(includesDir, f"{class_name}.hpp")
	cppPath = os.path.join(srcDir, f"{class_name}.cpp")

	with open(hppPath, "w") as file:
		file.write(f"#ifndef {class_name.upper()}_HPP\n")
		file.write(f"# define {class_name.upper()}_HPP\n\n")
		file.write(f"# include <iostream>\n\n")
		file.write(f"class {class_name}\n")
		file.write("{\n")
		file.write(f"	private:\n\n")
		file.write(f"	public:\n\n")
		file.write(f"		{class_name}();\n")
		file.write(f"		~{class_name}();\n")
		file.write(f"		{class_name}({class_name} const &original);\n")
		file.write(f"		{class_name} &operator=({class_name} const &other);\n\n")
		file.write("};\n\n")
		file.write(f"#endif\n")
	
	with open(cppPath, "w") as file:
		file.write(f"#include \"../includes/{class_name}.hpp\"\n\n")
		file.write(f"{class_name}::{class_name}()\n")
		file.write("{}\n\n")
		file.write(f"{class_name}::~{class_name}()\n")
		file.write("{}\n\n")
		file.write(f"{class_name}::{class_name}({class_name} const &original)\n")
		file.write("{\n		*this = original;\n}\n\n")
		file.write(f"{class_name} &{class_name}::operator=({class_name} const &other)\n")
		file.write("{\n")
		file.write("	if (this != &other)\n")
		file.write("	{}\n")
		file.write("	return (*this);\n")
		file.write("}\n")
	
	print(f"{class_name}.hpp and {class_name}.cpp created")
		