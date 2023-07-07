# pyraxis
subset of python3 with extensions, transpiles to C <br>

## file types
.pyr - pyraxis code <br>
.pyh - pyraxis header <br>

## command line arguments

-o 'x'          - filename/path to output resulting code/binary (this is fed to the C compiler) <br>
-cc 'x'         - c compiler to be invoked <br>
-cc_flags='x'   - flags to parse to the C compiler <br>
-c              - tells the C compiler to output an object and not a final executable <br>
-nstdlib        - disable the stdlib (non existent currently, arg implemented so freestanding code can be built by future versions) <br>
-i              - tells pyraxis where to look for .pyh (can be defined multiple times)<br>

## provided freestanding types

int - (translates to i32) <br>
i8 <br>
u8 <br>
i16 <br>
u16 <br>
i32 <br>
u32 <br>
i64 <br>
u64 <br>

const   - cannot be changed after definition <br>
*'type' - pointer to another object with 'type' as its type <br>
void    - no explicit type <br>
[]      - array <br>

## new keywords

c_attribute('x') - can be put before object definiton to add an attribute (x) to the created C file. ("packed", etc) <br>
& - can be used to get the location in memory of an object <br>
extern - used to define an externally defined objecy, can be used to create a binding with C code or act as a header for a library (C or pyraxis) <br>

## differences from python, synatax/function wise
pointers and pointer arithmetic <br>
variable must define type on definition <br>
functions must define return type and arguement types on definition (excluding '...', this will directly translated to C) <br>
functions cannot be defined in classes <br>

## stdlib
pyraxis currently does not have stdlib (keyword being currently) <br>
you can use the C library and extern to achieve a sort of stdlib <br>

## intergration with C
you can make a pyraxis header (.pyh) with extern definitons to bind to C <br>
to bind pyraxis code to C, you can make a C header file with defintions of the .pyr file <br>