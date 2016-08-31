# http://info.kingcounty.gov/health/ehs/foodsafety/inspections/Results.aspx?Output=W&Business_Name=name_of_b&Business_Address=address_here&Longitude=&Latitude=&City=city_here&Zip_Code=98105
#&Inspection_Type=All&Inspection_Start=&Inspection_End=&Inspection_Closed_Business=A&Violation_Points=&
#Violation_Red_Points=&Violation_Descr=&Fuzzy_Search=N&Sort=B

import requests
import io

DOMAIN = 'http://info.kingcounty.gov'
PATH = '/health/ehs/foodsafety/inspections/Results.aspx'

search_terms = {
    'Output': 'W',
    'Business_Name': '',
    'Business_Address': '',
    'Longitude': '',
    'Latitude': '',
    'City': '',
    'Zip_Code': '',
    'Inspection_Type': 'All',
    'Inspection_Start': '',
    'Inspection_End': '',
    'Inspection_Closed_Business': 'A',
    'Violation_Points': '',
    'Violation_Red_Points': '',
    'Violation_Descr': '',
    'Fuzzy_Search': 'N',
    'Sort': 'H',
}


def get_inspection_page(**kwargs):
    url = DOMAIN + PATH
    params = search_terms.copy()
    for key, val in kwargs.items():
        if key in search_terms:
            params[key] = val
    resp = requests.get(url, params=params)
    #resp.raise_for_status()     # <- This is a no-op if there is no HTTP error
    # remember, in requests `content` is bytes and `text` is unicode
    return resp.content, resp.encoding


def write_results_to_file(results):
    f = io.open('inspection_page.html', mode='w', buffering=-1, encoding=None, errors=None, newline=None, closefd=True)
    f.write(results)
    f.close()

print('retrieving data...')
r = get_inspection_page(Business_Name='Pizza')
print(r)
print('writing results to file...')
write_results_to_file(r)
print('file written.')
