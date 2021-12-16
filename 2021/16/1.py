from functools import reduce


def parse(packet: str, indent: str):
    print(f"{indent}parsing packet '{packet}'")
    v = int(packet[:3], 2)
    t = int(packet[3:6], 2)
    print(f"{indent}version {v}")
    if t == 4:
        print(f"{indent}literal")
        bits = ""
        for i in range(6, len(packet), 5):
            pp = packet[i:i+5]
            bits += pp[1:]
            if pp[0] == "0":
                break
        o = int(bits, 2)
        print(f"{indent}consumed {i+5} - lit {o}")
        return o, i + 5, v
    else:
        print(f"{indent}operator {t}")
        i = packet[6]
        pvs = []
        if i == "0":
            print(f"{indent}i0")
            length = int(packet[7:22], 2)
            print(f"{indent}length {length}")
            s = 22
            max_s = s + length
            while s < max_s:
                o2, i2, v2 = parse(packet[s:], indent+"    ")
                s += i2
                v += v2
                pvs.append(o2)
        else:
            print(f"{indent}i1")
            num = int(packet[7:18], 2)

            print(f"{indent}num packets {num}")
            s = 18
            for i in range(num):
                o2, i2, v2 = parse(packet[s:], indent+"    ")
                s += i2
                v += v2
                pvs.append(o2)
        t_op = [
            sum,
            lambda p: reduce(lambda x, y: x*y, p),
            min,
            max, max,
            lambda p: int(p[0] > p[1]),
            lambda p: int(p[0] < p[1]),
            lambda p: int(p[0] == p[1]),
        ]
        o = t_op[t](pvs)
        print(f"{indent}t={t} for {pvs} => {o}")
        return o, s, v


def aoc(line, e_v=-1, e_o=-1):
    print("")
    print("")

    print(f"parsing {line}")
    packet = "".join([format(int(i, 16), 'b').zfill(4) for i in line])
    o, i, v = parse(packet, "")
    print(f"part 1: version {v}")
    print(f"part 2: result {o}")
    print("done parsing one")

    if e_v != -1:
        if e_v == v:
            print("v value matches")
        else:
            print(f"v does not match expected {e_v}")
    if e_o != -1:
        if e_o == o:
            print("output matches")
        else:
            print(f"output does not match expected {e_o}")


aoc_day = __file__.split("/")[-2]
print(f"---------+ Day {aoc_day} example +-----------------------------------------------------------------------")
print("")
aoc("8A004A801A8002F478", 16, -1)
aoc("620080001611562C8802118E34", 12, -1)
aoc("C0015000016115A2E0802F182340", 23, -1)
aoc("A0016C880162017C3686B18A3D4780", 31, -1)
aoc("C200B40A82", -1, 3)
aoc("04005AC33890", -1, 54)
aoc("880086C3E88112", -1, 7)
aoc("CE00C43D881120", -1, 9)
aoc("D8005AC2A8F0", -1, 1)
aoc("F600BC2D8F", -1, 0)
aoc("9C005AC2F8F0", -1, 0)
aoc("9C0141080250320F1802104A08", -1, 1)
print("")
print(f"---------+ Day {aoc_day} solution +----------------------------------------------------------------------")
print("")
aoc("220D69802BE00A0803711E1441B1006E39C318A12730C200DCE66D2CCE360FA0055652CD32966E3004677EDF600B0803B1361741510076254138D8A00E4FFF3E3393ABE4FC7AC10410010799D2A4430003764DBE281802F3102CA00D4840198430EE0E00021D04E3F41F84AE0154DFDE65A17CCBFAFA14ADA56854FE5E3FD5BCC53B0D2598027A00848C63F2B918C7E513DEC3290051B3867E009CCC5FE46BD520007FE5E8AD344B37583D0803E40085475887144C01A8C10FE2B9803B0720D45A3004652FD8FA05F80122CAF91E5F50E66BEF8AB000BB0F4802039C20917B920B9221200ABF0017B9C92CCDC76BD3A8C4012CCB13CB22CDB243E9C3D2002067440400D9BE62DAC4D2DC0249BF76B6F72BE459B279F759AE7BE42E0058801CC059B08018A0070012CEC045BA01006C03A8000D46C02FA000A8EA007200800E00618018E00410034220061801D36BF178C01796FC52B4017100763547E86000084C7E8910AC0027E9B029FE2F4952F96D81B34C8400C24AA8CDAF4F1E98027C00FACDE3BA86982570D13AA640195CD67B046F004662711E989C468C01F1007A10C4C8320008742287117C401A8C715A3FC2C8EB3777540048272DFE7DE1C0149AC8BC9E79D63200B674013978E8BE5E3A2E9AA3CCDD538C01193CFAB0A146006AA00087C3E88B130401D8E304A239802F39FAC922C0169EA3248DF2D600247C89BCDFE9CA7FFD8BB49686236C9FF9795D80C0139BEC4D6C017978CF78C5EB981FCE7D4D801FA9FB63B14789534584010B5802F3467346D2C1D1E080355B00424FC99290C7E5D729586504803A2D005E677F868C271AA479CEEB131592EE5450043A932697E6A92C6E164991EFC4268F25A294600B5002A3393B31CC834B972804D2F3A4FD72B928E59219C9C771EC3DC89D1802135C9806802729694A6E723FD6134C0129A019E600")
print("")
print("--------------------------------------------------------------------------------------------------")
