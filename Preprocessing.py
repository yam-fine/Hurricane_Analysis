import pandas as pd
import numpy as np


StocksSymbol = ["LOW","BJ","FND","ORLY","CVNA","ALL" ,"PGR","TRV","DHI","LEN"]
ColsToInsert = ["hurricane","category","date","stock","7change", "20change","30change","50change"]

class PreProcess():
    def __init__(self, path):
        self.file = pd.ExcelFile(path).parse('Sheet1')
        self.stockfin =.....
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
        for i, row in self.file.iterrows():
            for symbol in StocksSymbol:

                new_row = {"Hurricane": row["name"],"Category": row["category"],"Date":row["date"],"Stock":symbol,"7change":calcChange(row["date"],7,row["name"]), "20change" : calcChange(row["date"],20,row["name"]) ,"30change" : calcChange(row["date"],30,row["name"]),"50change": calcChange(row["date"],30,row["name"])}
                finalPD = finalPD.append(new_row, ignore_index=True)

    def calcChange(self, date, days, stock):
        dateVal = self.stockfin[(self.stockfin["stock"] == stock) & (self.stockfin["Date"] == date)]["open"]
        laterVal = self.stockfin[(self.stockfin["stock"] == stock) & (self.stockfin["Date"] == date + days)]["open"]
        return ((laterVal-dateVal)/dateVal)*100







    def get_file(self):
        return self.file

    def save_excel(self, savepath):
        self.file.to_excel(savepath, index=False)