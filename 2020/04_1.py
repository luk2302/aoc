import re
from time import time

start_time = time()
passports = []
with open("04_input.txt") as f:
    eof = False
    while True:
        data = ""
        while True:
            d = f.readline()
            if d == "":  # eof
                eof = True
                break
            d = d[:-1]
            if d == "":  # newline
                break
            data = data + d + " "
        print(data)
        data = data[:-1].split(" ")
        data = [d.split(":") for d in data]
        passport = {d[0]: d[1] for d in data}
        try:
            if "byr" in passport and "iyr" in passport and "eyr" in passport and "hgt" in passport and "hcl" in passport and "ecl" in passport and "pid" in passport:
                if 1920 <= int(passport["byr"]) <= 2002:
                    if 2010 <= int(passport["iyr"]) <= 2020:
                        if 2020 <= int(passport["eyr"]) <= 2030:
                            h = int(passport["hgt"][:-2])
                            a = passport["hgt"][-2:]
                            if (a == "cm" and 150 <= h <= 193) or (a == "in" and 59 <= h <= 76):
                                if re.match("^#[0-9abcdef]{6}$", passport["hcl"]):
                                    if passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                                        if re.match("^[0-9]{9}$", passport["pid"]):
                                            passports.append(passport)
        except:
            print("nothing")
        if eof:
            break

print(len(passports))

end_time = time()
print((end_time - start_time))
