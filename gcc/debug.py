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
		"-ggdb3",
                "-DDEBUG"
	    ]
	}
    }
]
''')

def configure(confCtx):
    return __template.substitute()
