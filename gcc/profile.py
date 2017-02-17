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
		"-O2",
		"-ggdb",
		"-pg",
                "-DNDEBUG"
	    ]
	}
    },
    {
	"append_env_var":
	{
	    "env_var" : "LDFLAGS",
	    "value_list":
	    [
		"-pg"
	    ]
	}
    }
]
''')

def configure(confCtx):
    return __template.substitute()
