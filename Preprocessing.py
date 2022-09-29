import pandas as pd
import numpy as np


StocksSymbol = ["LOW","BJ","FND","ORLY","CVNA","ALL" ,"PGR","TRV","DHI","LEN"]
ColsToInsert = ["Hurricane","Category","Date","Stock","7 change", "20 change","30 change","50 change"]

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
        numOfStocks = len(ColsToInsert) ; numOfHurr = len(self.file["date"].unique())
        finalPD = pd.DataFrame(np.zeros((numOfStocks *numOfHurr, numOfStocks)),columns=ColsToInsert)

        index = 0
        # for date in self.file["date"]:
        #     for symbol in StocksSymbol:








    def get_file(self):
        return self.file

    def save_excel(self, savepath):
        self.file.to_excel(savepath, index=False)