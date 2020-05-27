import datetime
import yfinance as yf
import numpy as np
from ratelimit import limits
import os
import math
from template import *
import requests 
from lxml import html

firstDate = "2019-04-01"
secondDate = "2019-12-02"
endDate = datetime.date.today()

# src https://drive.google.com/file/d/1skgUviLX-Zby_qyCSBLaEeMGxFBXvM8f/view
stockSymbols = "FOXA TWOU MMM WUBA ABT ABBV ANF ATVI ADBE AAP AMD AES AFL A AGNC ACHN AIG AL APD AKS AKAM AA ALRS ALXN BABA ALGN ALLT MDRX ALL ALLY GOOGL GOOGL ATUS MO AMZN ABEV AMC AAL AXL AEO AEP AXP AMH AMT COLD AME AMGN FOLD AMRX APH ADI PLAN ANGI AU NLY ANSS AM AR ANTM AOS APA ARI AAPL AMAT APRE ATR ARMK ARNC ARCC ADM ANET ARR ARQL ASNA ASML HOME ADSK ATHM ADP AZO AVLR AVB AVP EQH AXTA BTG BIDU BKR BLL BBAR BBD BMA BSBR BSMX BAC BK GOLD BHC BAX BDX BDC BBY BYND BHP BILI BIO BIIB BMRN BITA BJ BB BLK BX BA BKNG BAH BWA BSX BOX BRFS BMY BRX AVGO BAM BIP BEP BG COG CDNS CZR CRC CPE CAJ COF CAH CCL CRZO CARS CAT CBL CBOE CBRE CELG CX CVE CNC CDEV CNP CTL CERN CF CIEN CI XEC CTAS CSCO C CFG CTXS CCO CWEN CLF CLDR NET CLVS CME CNX KO CDE CGNX CTSH CL CLNY CMCSA CMA COMM CYH SBS CIG SID BVN CAG CNDT CXO COP ED STZ CLR GLW CTVA COST COTY BAP CROX CRWD CCI CSX CVS CY DHI DAN DDOG DVA DE DELL DAL DNR DVN DO DLR APPS DFS DISCA DHR DISCK DISH DOCU DG DLTR D DPZ DOW DBX DUK DRE DNKN DD DXC ETFC EBAY ECL EIX EW ELAN EGO EA ESI LLY ERJ EMR ECA ENIA ET ENLC EPD NVST EOG EQT EFX EQIX EQNR ETRN EQR EL ETSY EB EVR XGN EXEL EXC EXPE STAY XOM FFIV FB FDS FAST FDX RACE FCAU FIS FITB FEYE FHN AG FSLR FE FISV FIT FVRR FLT FLEX FLR FL F FTNT FTV BEN FCX FREQ FTR FSK GME GCI GPS IT GDS GD GE GIS GM GNTX GNW GGB GILD GNL GLUU GDDY GOL GFI GS GT GPRO GPK GO GRPN GRUB SUPV TV GES GPOR HRB HAL HBI HOG HMY HIG HAS HCA HDB HDB HL HEI HSIC HLF HTZ HES HPE HEXO HGV HLT HIMX HFC HOLX HMC HON HRL HST HPQ HTHT HUBS HUM HBAN HUN HCM HUYA H SCHW CHTR CHKP CC LNG CHK CVX CHWY CHS CIM CHL ZNH CMG IAG IBM IBN IDXX IGMS ITW ILMN IMGN INCY INFN INFY INTC IBKR ICE IGT IP IPG INTU ISRG IVZ IVR ISBC NVTA INVH IQ IRBT IRM ITUB JBHT JCP JKHY JD JEF JBLU JKS JNJ JPM JMIA JNPR KAR K KDP KEY KEYS KMB KIM KMI KGC KKR KNX KSS KOS KHC KTOS KR KT LB LRCX LPI LVS LTM LSCC LDOS LEN LEVI LXRX LX LPL FWONK LYV LTHM LKQ LMT LOMA LOW LTC LK LULU LYFT M MRO MPC MAR MMC MRVL MAS MA MTDR MTCH MAT MXIM MDR MCD MUX MPW MDT MLCO MELI MRK MET MFA MTG MGM MCHP MU MSFT MIK MUFG MFG MBT MOMO MDLZ MGI MNST MCO MS MORN MOS MSI MPLX MUR MYL NBR NDAQ NOV NAVI NKTR NPTN NTAP NTES NFLX NBIX NBEV EDU NRZ NYCB NYT NWL NEM NWSA SSSS NEE NKE NIO NOAH NBL NMR JWN NSC NTRS NOC NLOK NCLH NVCR NRG NUE NTNX NUVA NVDA NYMT ORLY OAS OXY ODP OKTA OLN OMC ON OKE OPK ORCL ONVO OSTK PCAR PD PANW PAM PAAS PH PE PTEN PAYX PYPL PBF PTON PBCT PEP PBR PFE PCG PM PSX PDD PING PINS PXD PBI PVTL PAA PLUG PS PNC PPG PPL PBH PRI PG PGR PLD PFPT PRU PEG PSA PHM PSTG QTWO QEP QCOM QLYS PWR QD QRTEA RL RRC RTN RLGY REAL O REGN RF REGI RMD QSR RNG RAD ROK ROKU ROST RY RCL RES SPGI CRM SBH SGMO STX SRE SNH SENS SHAK SHW SHOP SLB SBGL SPG SIRI SKX SWKS WORK SLM SM SMAR SNAP SQM SOGO SNE SO SCCO LUV SWN ONCE SPLK SPOT S SFM SQ SSNC SWK SBUX TSG STT STLD SFIX STNE SYK SMFG SU SPWR RUN STI SYF SNPS SYY TMUS TROW TLRD TSM TTWO TAK TAL SKT TPR TEDU TRGP TGT TTM AMTD TECK FTI TFX VIV TELL TPX TME TER TSLA TEVA TXN CG GEO WU TXMD TMO TIF TSU TJX TD TM TW TRXC TRV TCOM TRIP TGI TFC TRQ TWLO TWTR TWO TSN USB SLCA UBER ULTA UCTT UGP UAA UA UNP UAL UMC UPS X UTX UNH UNIT UNM TIGR URBN UXIN VALE VLO VGR VEEV VTR VER VRSN VRSK VZ VRTX VFC VIACA VICI VIE VIPS SPCE V VST VMW VG WBA WMT DIS WPG WM W WB WFC WELL WEN WDC WAB WRK WEX WY WLL WMB WING WIT WDAY WWE WPX WYNN XEL XRX XLNX AUY YPF YUMC YUM YY ZAYO ZBRA ZEN Z ZBH ZION ZTS ZM ZS ZTO ZNGA"
# stockSymbols = "MSFT AAPL"
class stockResult():
    def __init__(self, stockSymbol, firstPrice, secondPrice, currentPrice, bankruptcyProbability):
        self.stockSymbol = stockSymbol
        self.firstPrice = np.round(firstPrice, 2)
        self.secondPrice = np.round(secondPrice, 2)
        self.currentPrice = np.round(currentPrice, 2)
        self.firstPercentageMovement = np.round(currentPrice/firstPrice*100-100, 2)
        self.secondPercentageMovement = np.round(currentPrice/secondPrice*100-100, 2)
        self.bankruptcyProbability = bankruptcyProbability

def get_probability_of_bankruptcy_url(symbol):
    return "https://www.macroaxis.com/invest/ratio/{}--Probability-Of-Bankruptcy".format(symbol)

def get_baknruptcy_probability(symbol):
    try:
        page = requests.get(get_probability_of_bankruptcy_url(stockSymbol))
        tree = html.fromstring(page.content)
        bankruptcyProbability = tree.xpath("//div[contains(@class, \'importantValue\')]/text()")[0]
        print bankruptcyProbability
    except:
        bankruptcyProbability = "unknown"
    
    return bankruptcyProbability

bankruptcyProbabilityUrlTemplate =  "https://www.macroaxis.com/invest/ratio/{}--Probability-Of-Bankruptcy"

@limits(calls=1, period=1) # slow down for rate limiting
def get_all_stocks_data():
    data = yf.download(stockSymbols, start=firstDate, end=endDate)
    return data


resultsFileName = "docs/index.html"
if os.path.exists(resultsFileName):
    os.remove(resultsFileName)    

allStocksData = get_all_stocks_data()
stockResults = []

for stockSymbol in stockSymbols.split():
    firstPrice = allStocksData.Close[stockSymbol][firstDate]
    secondPrice = allStocksData.Close[stockSymbol][secondDate]
    currentPrice = allStocksData.Close[stockSymbol][-1]
    bankruptcyProbability = get_baknruptcy_probability(stockSymbol)
    result = stockResult(stockSymbol, firstPrice, secondPrice, currentPrice, bankruptcyProbability)
    if not math.isnan(result.secondPercentageMovement):
        stockResults.append(result)

stockResults.sort(key=lambda x: x.secondPercentageMovement)

heading = ''
tableBody = ''

with open(resultsFileName, "a") as resultsFile:
    heading += ('<h1>Diff generated at {} UTC</h1> \n'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

for result in stockResults:
    firstPercentageMovementClass = 'positive-movement' if (result.firstPercentageMovement > 0) else 'negative-movement'
    secondPercentageMovementClass = 'positive-movement' if (result.secondPercentageMovement > 0) else 'negative-movement'

    tableBody += "<tr> \n"
    tableBody += '<td><button onclick="renderChart(`{}`)">{}</button></td> \n'.format(result.stockSymbol, result.stockSymbol)
    tableBody += "<td>{}$</td> \n".format(result.firstPrice)
    tableBody += "<td>{}$</td> \n".format(result.secondPrice)
    tableBody += "<td>{}$</td> \n".format(result.currentPrice) 
    tableBody += "<td class='{}'>{}%</td> \n".format(firstPercentageMovementClass, result.firstPercentageMovement)
    tableBody += "<td class='{}'>{}%</td> \n".format(secondPercentageMovementClass, result.secondPercentageMovement)
    tableBody += "<td>{}</td> \n".format(result.bankruptcyProbability)     
    tableBody += "</tr> \n"

with open(resultsFileName, "a") as resultsFile:
    resultsFile.write(template.format(heading, tableBody))
