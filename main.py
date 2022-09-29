import Preprocessing as pp


if __name__ == '__main__':
    path = "florida_hurricanes"
    pp.PreProcess(path + ".xlsx").save_excel(path + "_new.xlsx")
    print("lol")
