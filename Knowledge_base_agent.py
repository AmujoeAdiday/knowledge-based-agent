
import sys

def or_operation(str_each):

    y = str_each.replace("(","")
    z = y.replace(")","")
    a = z.replace(" ","")
    list_z = a.split("V")
    #print(list_z)
    for j in range(len(list_z)):
        if "~False" in list_z[j]:
            list_z[j] = "True"
        if "~True" in list_z[j]:
            list_z[j] = "False"
    if "True" in list_z:
        return "True"
    else:
        return "False"


def and_operation(str_each):
    y = str_each.replace("(", "")
    z = y.replace(")", "")
    a = z.replace(" ", "")
    list_z = a.split("^")
    #print(list_z)
    for j in range(len(list_z)):
        if "~False" in list_z[j]:
            list_z[j] = "True"
        if "~True" in list_z[j]:
            list_z[j] = "False"

    if "False" in list_z:
        return False
    else:
        return True

def verify_values_var(st):
    first_comma_position = st.find(",")
    logic_part = st[:first_comma_position]
    var_values = st[first_comma_position:]

    s = var_values.replace(" ","")
    comma_list = []
    equal_list = []
    for i in range(len(s)):
        if s[i] == ",":
            comma_list.append(i)
        if s[i] == "=":
            equal_list.append(i)
    #print("comma list ", comma_list)
    #print("equal list", equal_list)

    num = len(comma_list)
    dict_keys = []
    for i in range(num):
        dict_keys.append(s[comma_list[i] + 1: equal_list[i]])
    #print(dict_keys)

    dict_values = []
    for j in range(num):
        dict_values.append(s[equal_list[j] + 1:equal_list[j] + 2])
    #print(dict_values)

    for i in range(len(dict_values)):
        if dict_values[i] == "T":
            dict_values[i] = "True"
        elif dict_values[i] == "F":
            dict_values[i] = "False"
    #print(value_list)

    dict_of_var_value = dict(zip(dict_keys, dict_values))

    return dict_of_var_value,logic_part

def read_file(file_name):
    with open(file_name) as f:
        lines = [line.rstrip() for line in f]
    return lines
#print(read_file("prep.kb"))


# x = [st_full,st_full2,st_full3]
# for i in range(len(x)):
def run_program(st):
    # lis = [st_full,st_full2,st_full3]



    dict_of_values,logic = verify_values_var(st)

    #print(dict_of_values)

    for key, value in dict_of_values.items():

        logic = logic.replace(key, value)

    #print("1 st Logic non x",logic)
    out = logic.split("^")
    #print("OUT PUT or or",out)

    for i in range(len(out)):
        #print(or_operation(out[i]))
        out[i] = or_operation(out[i])
    #print("Out put ",out)


    # for i in range(len(out)):
    #     #print(out[i])

    open_list = []
    close_list = []
    for i in range(len(logic)):
        if logic[i] == "(":
            open_list.append(i+1)
        elif logic[i] == ")":
            close_list.append(i)
    #print("Open list ",open_list)
    #print("Close list", close_list)

    keys = []

    for m in range(len(out)):
        keys.append(logic[open_list[m]:close_list[m]])


    dict_o= dict(zip(keys, out))


    for key, value in dict_o.items():

        logic = logic.replace(key, value)


    return and_operation(logic)
    #print("Output >>", truth_values)

#lis = [st_full,st_full2,st_full3]


def output_program(list_x):

    len_list = len(list_x)
    truth_values_list = ""
    for i in range(len_list):
        truth_values_list += str(run_program(list_x[i]))+" "

    print(truth_values_list)

file_name = "prep.kb"
output_program(read_file(file_name))



























