from waflib.ConfigSet import ConfigSet

def options(optCtx):
    optCtx.recurse('gcc')

def prepare(prepCtx):
    pass

def configure(confCtx):
    confCtx.recurse('gcc')
