from waflib.ConfigSet import ConfigSet

def options(optCtx):
    optCtx.recurse('cxx')

def configure(confCtx):
    confCtx.recurse('cxx')
