#!/usr/bin/env python
# encoding: utf-8

from string import Template

__template = Template('''
[
    {
	"append_env_var":
	{
	    "env_var" : "CXXFLAGS",
	    "value_list":
	    [
		"-Wall",
		"-Wextra",
		"-pthread",
		"-Wl,rpath=$$ORIGIN",
		"-Wl,-z,origin",
		"-Wl,--eh-frame-hdr",
		"-std=c++11",
		"-Wno-unused-local-typedefs",
		"-Wno-unused-but-set-parameter",
		"-Wno-maybe-uninitialized",
		"-pipe",
		"-DLEVEL1_DCACHE_LINESIZE=$dcache_line_size",
		"-fstack-protector-all",
		"-fno-builtin-malloc",
		"-fno-builtin-calloc",
		"-fno-builtin-realloc",
		"-fno-builtin-free"
	    ]
	}
    },
    {
	"append_env_var":
	{
	    "env_var" : "LDFLAGS",
	    "value_list":
	    [
		"-lrt",
		"-lpthread"
	    ]
	}
    }

]
''')

def configure(confCtx):
    return __template.substitute(
	    dcache_line_size=confCtx.env.dcache_line_size)
