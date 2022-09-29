import pandas as pd


class PreProcess():
    def __init__(self, path):
        self.file = pd.ExcelFile(path).parse('Sheet1')
        for i, name in enumerate(self.file["name"]):
            if name == "Unnamed":
                self.file["name"][i] = "Unnamed" + str(i)
        pd.to_datetime(self.file["date"])
        f = lambda x, y: x.replace(year=y)
        self.file["date"] = self.file.apply(lambda x: f(x["date"], x["year"]), axis=1)
        # for date, h_year, index in zip(self.file["date"], self.file["year"], range(0, len(self.file["date"].unique()))):
        #     self.file["date"][index] = date.replace(year=h_year)





    def get_file(self):
        return self.file

    def save_excel(self, savepath):
        self.file.to_excel(savepath, index=False)