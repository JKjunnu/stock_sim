from dotenv import load_dotenv
import src.backend.server_endpoints.transactions as tr
import src.backend.server_endpoints.stock_info as si

load_dotenv()

try:
    # print(si.search_stocks('APPLE'))
    tr.buy_stock('MSFT' , 2)
except Exception as e:
    print(e)




