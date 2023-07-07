#!/usr/bin/python3
import sys
import uuid
import os

is_object_file = False
output_filename = ""
c_compiler = "cc"
cc_flags = "-O2"
pyh_path = ["."]
source_file = ""

next_arg_is_output_filename = False
next_arg_is_cc = False
next_arg_append_to_pyh_path = False
for sys_arg in sys.argv:
    if sys_arg == sys.argv[0]: continue

    if next_arg_is_output_filename: output_filename = sys_arg; next_arg_is_output_filename = False; continue
    if next_arg_is_cc: c_compiler = sys_arg; next_arg_is_cc = False; continue
    if next_arg_append_to_pyh_path: pyh_path.append(sys_arg); next_arg_append_to_pyh_path = False; continue
    
    if sys_arg == "-c": is_object_file = True; continue
    if sys_arg == "-o": next_arg_is_output_filename = True; continue
    if sys_arg == "-cc": next_arg_is_cc = True; continue
    if sys_arg.split("=")[0] == "-cc_flags": cc_flags = sys_arg.split("=")[1]; continue
    if sys_arg == "-nstdlib": continue
    if sys_arg == "-i": next_arg_append_to_pyh_path = True; continue
    if source_file == "": source_file = sys_arg; continue

if source_file == "": print("PYRAXIS ERROR: Source file not parsed"); exit(-1)
if output_filename == "":
    if is_object_file == True: output_filename = f"{source_file}.o";
    else: output_filename = source_file.replace("."+source_file.split(".")[-1], "")

print(f"source_file: {source_file}")
print(f"is_object_file: {is_object_file}")
print(f"output_filename: {output_filename}")
print(f"pyh_path: {pyh_path}")
print(f"cc: {c_compiler}")
print(f"cc_clags: {cc_flags}")

c_string = "" #write to this str to have it written to the final C file
#with open(source_file) as f:
#    for line in f:



print(c_string)
if os.path.isdir("/tmp") == False:
    print("PYRAXIS ERROR: /tmp is does not exist")
    exit(-1)
#c_file_path = f"/tmp/{str(uuid.uuid4().hex)}.c"
#c_file = open(c_file_path, "wb")