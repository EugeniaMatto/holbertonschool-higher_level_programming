#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(args)
    except Exception as te:
        print("Exception: {}".format(te), file=sys.stderr)
        return None
