bstr = ""
coro = {
    "1": "001",
    "2": "010",
    "3": "011",
    "4": "100",
    "5": "101",
    "6": "110",
    "7": "111",
    "8": "0011",
    "9": "1100",
    "0": "000",
    " ": "",
    ".": ""
}
while True:
    inp = input ("8=D  ")
    for n in inp:
        bstr += coro[n]
    print (f"{bin(int(bstr))}")
