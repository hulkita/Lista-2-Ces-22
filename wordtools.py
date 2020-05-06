import sys

def test(did_pass):
    lineum = sys._getframe(1).f_lineno
    if did_pass:
        msg = ("Test at line {0} ok".format(lineum))
    else:
        msg = ("Test at line {0} FAILED".format(lineum))
    print(msg)




