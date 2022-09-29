import pandas as pd


class PreProcess():
    def __init__(self, path):
        self.file = pd.ExcelFile(path).parse('Sheet1')
        for i, name in enumerate(self.file["name"]):
            if name == "Unnamed":
                self.file["name"][i] = "Unnamed" + str(i)

    def get_file(self):
        return self.file

    def save_excel(self, savepath):
        self.file.to_excel(savepath, index=False)