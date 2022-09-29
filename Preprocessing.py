import pandas as pd
import numpy as np
import simfin as sf
from datetime import datetime, date, timedelta

# Import names used for easy access to SimFin's data-columns.
from simfin.names import *


StocksSymbol = ["LOW","BJ","FND","ORLY","CVNA","ALL" ,"PGR","TRV","DHI","LEN"]
ColsToInsert = ["hurricane","category","date","stock","7change", "14change","28change","56change"]

class PreProcess():
    def __init__(self, path):
        self.file = pd.ExcelFile(path).parse('Sheet1')

        sf.set_data_dir('~/simfin_data/')
        # # Replace YOUR_API_KEY with your actual API-key.
        sf.set_api_key(api_key='NmFN8XBW6Se0bGezCbgvREZzWfKbVUWl')
        # self.df_income = sf.load_income(variant='annual', market='us')

        # We are interested in the US stock-market.
        market = 'us'

        # Add this date-offset to the fundamental data such as
        # Income Statements etc., because the REPORT_DATE is not
        # when it was actually made available to the public,
        # which can be 1, 2 or even 3 months after the Report Date.
        offset = pd.DateOffset(days=60)

        # Refresh the fundamental datasets (Income Statements etc.)
        # every 30 days.
        refresh_days = 30

        # Refresh the dataset with shareprices every 10 days.
        refresh_days_shareprices = 10

        self.stockfin = sf.load_shareprices(variant='daily', market=market, index=['Ticker'])
        self.stockfin = self.stockfin.loc[StocksSymbol]
        self.stockfin['Date'] = self.stockfin['Date'].apply(lambda x: x.strftime("%d/%m/%Y"))

        for i, name in enumerate(self.file["name"]):
            if name == "Unnamed":
                self.file["name"][i] = "Unnamed" + str(i)
        pd.to_datetime(self.file["date"])
        f = lambda x, y: x.replace(year=y)
        self.file["date"] = self.file.apply(lambda x: f(x["date"], x["year"]), axis=1)
        # for date, h_year, index in zip(self.file["date"], self.file["year"], range(0, len(self.file["date"].unique()))):
        #     self.file["date"][index] = date.replace(year=h_year)
        numOfStocks = len(ColsToInsert); numOfHurr = len(self.file["date"].unique())
        finalPD = pd.DataFrame(columns=ColsToInsert)

        self.stockfin['Date'] = pd.to_datetime(self.stockfin['Date'])
        self.stockfin['Date'] = self.stockfin['Date'].apply(lambda x: x.strftime("%m/%d/%Y"))
        for i, row in self.file.iterrows():
            for symbol in StocksSymbol:
                if self.dateExists(row["date"], symbol):
                    new_row = {"hurricane": row["name"], "category": row["category"], "date": row["date"], "stock": symbol,
                               "7change": self.calcChange(row["date"], 7, symbol), "14change": self.calcChange(row["date"], 14, symbol),
                               "28change": self.calcChange(row["date"], 28, symbol), "56change": self.calcChange(row["date"], 56, symbol)}
                    finalPD = finalPD.append(new_row, ignore_index=True)

        print("hasbulla the hero")

    def calcChange(self, date, days, stock):
        dateVal = self.stockfin[(self.stockfin.index == stock) & (self.stockfin["Date"] == date.strftime("%m/%d/%Y"))]["Open"]
        laterVal = self.stockfin[(self.stockfin.index == stock) & (self.stockfin["Date"] == (date + timedelta(days=3)).strftime("%m/%d/%Y"))]["Open"]
        return (((laterVal-dateVal)/dateVal)*100)[0]

    def dateExists(self, date, stock):
        var1 = stock
        var2 = date.strftime("%m/%d/%Y")
        if ((self.stockfin.index == var1) & (self.stockfin['Date'] == var2)).any():
            return True
        return False





    def get_file(self):
        return self.file

    def save_excel(self, savepath):
        self.file.to_excel(savepath, index=False)