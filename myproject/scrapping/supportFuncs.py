import requests
import json
import pandas as pd

def get_financial_data_from_seeking_alpha(ticker):
    # data scrapping from seeking alpha
    url_financials = "https://seeking-alpha.p.rapidapi.com/symbols/get-financials"

    querystring = {"symbol": ticker, "target_currency": "USD", "period_type": "annual",
                   "statement_type": "income-statement"}
    headers = {
        "x-rapidapi-key": "fabd976876mshba6394391554afap11c851jsne567d36ceeb6",
        "x-rapidapi-host": "seeking-alpha.p.rapidapi.com"
    }

    response_financials = requests.get(url_financials, headers=headers, params=querystring).json()
    # Convert the data into a Pandas DataFrame
    df_financials = create_dataframe(response_financials)
    #save to file
    output_excel_file_financials = f"output_table_{ticker}_Financials.xlsx"
    df_financials.to_excel(output_excel_file_financials, index=False, sheet_name="Data")


def create_dataframe(response):
    table_data = []
    # Iterate through sections in the JSON
    for section in response:
        title = section.get("title", "Unknown Section")
        for row in section.get("rows", []):
            row_name = row.get("value", "Unknown Row")
            cells = row.get("cells", [])
            row_data = {cell["name"]: cell.get("value", None) for cell in cells}
            row_data["Row Name"] = row_name
            row_data["Section"] = title
            table_data.append(row_data)

    # Convert the data into a Pandas DataFrame
    df = pd.DataFrame(table_data)
    return df


def get_incomestatement_balancesheet_cashflow_data_from_seeking_alpha(ticker):
    url_b_sheet = "https://financial-statements.p.rapidapi.com/api/v1/resources/balance-sheet"
    url_cashflow = "https://financial-statements.p.rapidapi.com/api/v1/resources/cash-flow"
    url_incomest = "https://financial-statements.p.rapidapi.com/api/v1/resources/income-statement"

    querystring = {"ticker": ticker}

    headers = {
        "x-rapidapi-key": "fabd976876mshba6394391554afap11c851jsne567d36ceeb6",
        "x-rapidapi-host": "financial-statements.p.rapidapi.com"
    }

    response_b_sheet = requests.get(url_b_sheet, headers=headers, params=querystring)
    response_cashflow = requests.get(url_cashflow, headers=headers, params=querystring)
    response_incomest = requests.get(url_incomest, headers=headers, params=querystring)

    if isinstance(response_b_sheet.text, str):
        # Parse the JSON string into a Python object
        print("isinstance of string")
        data = json.loads(response_b_sheet.text)
    else:
        # Use the .json() method directly
        print("not instance of string")
        data = response_b_sheet.json()

    with open("data.json", "w") as file:
        file.write(response_b_sheet.text)

    # Reload and parse
    with open("data.json", "r") as file:
        data = json.load(file)

    print(data)


def process_json_file():
    with open("data_2.json", "r") as file:
        data = json.load(file)
    return data

# def scraping_sec_files():
#     # create request header
#     headers = {'User-Agent': "email@address.com"}
#
#     # get all companies data
#     companyTickers = requests.get(
#         "https://www.sec.gov/files/company_tickers.json",
#         headers=headers
#     )
#
#     # review response / keys
#     print(companyTickers.json().keys())
#
#     # format response to dictionary and get first key/value
#     firstEntry = companyTickers.json()['0']
#
#     # parse CIK // without leading zeros
#     directCik = companyTickers.json()['0']['cik_str']
#
#     # dictionary to dataframe
#     companyData = pd.DataFrame.from_dict(companyTickers.json(),
#                                          orient='index')
#
#     # add leading zeros to CIK
#     companyData['cik_str'] = companyData['cik_str'].astype(
#         str).str.zfill(10)
#
#     # review data
#     print(companyData[:1])
#
#     cik = companyData[0:1].cik_str[0]
#
#     # get company specific filing metadata
#     filingMetadata = requests.get(
#         f'https://data.sec.gov/submissions/CIK{cik}.json',
#         headers=headers
#     )

# review json
# print(filingMetadata.json().keys())
# filingMetadata.json()['filings']
# filingMetadata.json()['filings'].keys()
# filingMetadata.json()['filings']['recent']
# filingMetadata.json()['filings']['recent'].keys()
#
# # dictionary to dataframe
# allForms = pd.DataFrame.from_dict(
#     filingMetadata.json()['filings']['recent']
# )
#
# # review columns
# allForms.columns
# allForms[['accessionNumber', 'reportDate', 'form']].head(50)
#
# # 10-Q metadata
# allForms.iloc[11]
#
# # get company facts data
# companyFacts = requests.get(
#     f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json',
#     headers=headers
# )
#
# # review data
# companyFacts.json().keys()
# companyFacts.json()['facts']
# companyFacts.json()['facts'].keys()
#
# # filing metadata
# companyFacts.json()['facts']['dei'][
#     'EntityCommonStockSharesOutstanding']
# companyFacts.json()['facts']['dei'][
#     'EntityCommonStockSharesOutstanding'].keys()
# companyFacts.json()['facts']['dei'][
#     'EntityCommonStockSharesOutstanding']['units']
# companyFacts.json()['facts']['dei'][
#     'EntityCommonStockSharesOutstanding']['units']['shares']
# companyFacts.json()['facts']['dei'][
#     'EntityCommonStockSharesOutstanding']['units']['shares'][0]
#
# # concept data // financial statement line items
# companyFacts.json()['facts']['us-gaap']
# companyFacts.json()['facts']['us-gaap'].keys()
#
# # different amounts of data available per concept
# companyFacts.json()['facts']['us-gaap']['AccountsPayable']
# companyFacts.json()['facts']['us-gaap']['Revenues']
# companyFacts.json()['facts']['us-gaap']['Assets']
#
# # get company concept data
# companyConcept = requests.get(
#     (
#         f'https://data.sec.gov/api/xbrl/companyconcept/CIK{cik}'
#         f'/us-gaap/Assets.json'
#     ),
#     headers=headers
# )
#
# # review data
# companyConcept.json().keys()
# companyConcept.json()['units']
# companyConcept.json()['units'].keys()
# companyConcept.json()['units']['USD']
# companyConcept.json()['units']['USD'][0]
#
# # parse assets from single filing
# companyConcept.json()['units']['USD'][0]['val']
#
# # get all filings data
# assetsData = pd.DataFrame.from_dict((
#     companyConcept.json()['units']['USD']))
#
# # review data
# assetsData.columns
# assetsData.form
#
# # get assets from 10Q forms and reset index
# assets10Q = assetsData[assetsData.form == '10-Q']
# assets10Q = assets10Q.reset_index(drop=True)
#
# # plot
# assets10Q.plot(x='end', y='val')
