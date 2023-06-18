def readfiles(fname):
    data = None
    with open(fname, "r") as fb:
        data = fb.read()
    print(f"read {fname} file")


def writelines(fname, lines):
    with open(fname,"w") as fb:
        fb.writelines(lines)
    print(f'Write lines to the {fname}')

