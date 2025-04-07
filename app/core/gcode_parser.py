def parse_gcode_line(line: str):
    line = line.strip()
    if not line or line.startswith(";"):
        return None
    # Разбиваем команду (например, "G1X100Y200" -> ("G1", {"X": 100, "Y": 200}))

    cmd = None
    g_com = line.find("G")
    x_com = line.find("X")
    y_com = line.find("Y")
    z_com = line.find("Z")

    if g_com != -1 and x_com != -1:
        cmd = line[g_com:x_com]
    elif g_com != -1 and y_com != -1:
        cmd = line[g_com:y_com]
    elif g_com != -1 and z_com != -1:
        cmd = line[g_com:z_com]
    elif g_com != -1:
        cmd = line[g_com:]

    args = {}
    if x_com != -1 and y_com != -1:
        args["X"] = float(line[x_com + 1:y_com])
    elif x_com != -1 and z_com != -1:
        args["X"] = float(line[x_com + 1:z_com])
    elif x_com != -1:
        args["X"] = float(line[x_com + 1:])

    if y_com != -1 and z_com != -1:
        args["Y"] = float(line[y_com + 1:z_com])
    elif y_com != -1:
        args["Y"] = float(line[y_com + 1:])

    if z_com != -1:
        args["Z"] = float(line[z_com + 1:])

    return cmd, args