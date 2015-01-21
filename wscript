from waflib.ConfigSet import ConfigSet

def options(optCtx):
    optCtx.recurse('gcc')

def configure(confCtx):
    confCtx.recurse('gcc')
