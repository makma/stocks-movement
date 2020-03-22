import datetime
import yfinance as yf
import numpy as np
from ratelimit import limits
import os
import math
from template import *

startDate = "2019-12-01"
endDate = datetime.date.today()

# src https://drive.google.com/file/d/1skgUviLX-Zby_qyCSBLaEeMGxFBXvM8f/view
stockSymbols = "FOXA MMM ABT ABBV ANF ATVI ADBE AAP AMD AFL A AIG APD AKAM ALXN BABA ALGN ALL GOOGL GOOG AABA ATUS MO AMZN ABEV AMC AAL AEP AXP AMT AME AMGN APH ADI PLAN ANGI ANTM APA AAPL AMAT ATR ARCC ANET ASML T ADSK ADP AZO AVB AVP BIDU BHGE BLL BAC BAX BBT BDX BRK.B BYND BHP BIIB BMRN BIO BB BLK BX BK BA BKNG BAH BSX AVGO BEP BMY BF.B BG CDNS CZR CAJ COF CG CAT CBRE CELG CTL CERN SCHW CHTR CHKP CVX CHWY ZNH CMG CI XEC CTAS CSCO C CTXS CWEN CLDR CME KO CGNX CTSH CL CLNY CMCSA COP ED STZ GLW CTVA COST COTY BAP CRWD CCI CSX CVS CY DHR DAL DVN DLR APPS DFS DISCA DISH DOCU DG DLTR D DPZ DBX DUK DNKN DD DXC EBAY ECL EIX EW ELAN EA LLY ERJ EMR ECA EOG EFX EQIX EQR EL ETFC EB EVR EXC EXPE XOM FFIV FB FDS FDX RACE FCAU FEYE FSLR FIS FISV FIT FVRR FLT FL F FTNT FTV BEN FCX GPS IT GD GE GIS GM GILD GDDY GS GT GPRO GRPN GRUB GES HAL HBI HAS HCA HEI HSIC HLF HTZ HPE HLT HIMX HD HMC HON HPQ HUBS HUM HCM H IBM IDXX ITW ILMN IMGN INCY INFY INTC ICE INTU ISRG IVZ IQ IRBT JNJ JKHY JBHT JD JEF JBLU DE JPM JMIA JNPR K KEYS KMB KMI KKR KHC LB LRCX LVS LDOS LEVI LPL FWONK LYV LMT LOW LK LULU LYFT M MPC MAR MMC MA MTCH MXIM MCD MDT MELI MRK MET MGM MCHP MU MSFT MFG MDLZ MNST MCO MS MORN MSI MUFG MYL NDAQ NOV NTAP NTES NFLX NBIX NYT NEM NEE NKE NIO NMR NTRS NOC NVCR NTNX NVDA OAS OXY ODP OKTA OMC ON OKE OPK ORCL ORLY OSTK PG PCAR PANW PH PAYX PYPL PEP PFE PCG PM PSX PINS PXD PNC PPG PFPT PRU PEG PSA PSTG QCOM QLYS PWR QRTEA RL REAL RHT REGN REGI RMD QSR RNG ROK ROKU ROST RY SPGI CRM SLB STX SRE SHW SHOP SPG SIRI SKX SWKS WORK SNAP SNE BID SO SCCO LUV ONCE SPLK SPOT S SQ SSNC SWK SBUX STT STNE SYK SMFG SPWR RUN STI SSSS SYMC SNPS SYY TROW TTWO TSM TGT TTM AMTD TFX TME TSLA TXN TMO TJX TMUS TD TM TW TRV TCOM TRIP TWLO TWTR UBER ULTA UCTT UAA UA UNP UAL UNH UMC UTX UPS USB VALE VLO VEEV VTR VRSN VRSK VZ VRTX VFC VIA V VST VMW VG WBA WMT DIS WM W WB WFC WELL WDC WU WRK WEX WMB WDAY WYNN XEL XRX XLNX YUM YUMC ZEN ZBH ZTS ZM ZS ZNGA QAN"


class stockResult():
    def __init__(self, stockSymbol, pastValue, nowValue):
        self.stockSymbol = stockSymbol
        self.pastValue = np.round(pastValue, 2)
        self.nowValue = np.round(nowValue, 2)
        self.percentageMovement = nowValue/pastValue*100-100


@limits(calls=1, period=1) # slow down for rate limiting
def get_all_stocks_data():
    data = yf.download(stockSymbols, start=startDate, end=endDate)
    return data


resultsFileName = "docs/index.html"
if os.path.exists(resultsFileName):
    os.remove(resultsFileName)    

allStocksData = get_all_stocks_data()
beforeAndNow = allStocksData.Close.iloc[[0, -1]]
stockResults = []

for stockSymbol in stockSymbols.split():
    pastValue = beforeAndNow[stockSymbol][0]
    nowValue = beforeAndNow[stockSymbol][1]
    result = stockResult(stockSymbol, pastValue, nowValue)
    if not math.isnan(result.percentageMovement):
        stockResults.append(result)

stockResults.sort(key=lambda x: x.percentageMovement)

heading = ''
tableBody = ''

with open(resultsFileName, "a") as resultsFile:
    heading += ('<h1>Diff between {} and {} generated at {} UTC</h1> \n'.format(startDate, endDate, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

for result in stockResults:
    roundedPercentageMovement = np.round(result.percentageMovement, 2)
    print('{} {}%'.format(result.stockSymbol, roundedPercentageMovement))
    percentageMovementClass = 'positive-movement' if (roundedPercentageMovement > 0) else 'negative-movement'
    tableBody += "<tr> \n"
    tableBody += '<td><button onclick="renderChart(`{}`)">{}</button></td> \n'.format(result.stockSymbol, result.stockSymbol)
    tableBody += "<td>{}$</td> \n".format(result.pastValue)
    tableBody += "<td>{}$</td> \n".format(result.nowValue) 
    tableBody += "<td class='{}'>{}%</td> \n".format(percentageMovementClass, roundedPercentageMovement)  
    tableBody += "</tr> \n"

with open(resultsFileName, "a") as resultsFile:
    resultsFile.write(template.format(heading, tableBody))
