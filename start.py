import data_requests.CryptoRequests as data_request
from data_requests.TradingViewPredictions import TradingViewPredictions
from database.Database import Database


database = Database()
database.add_to_data_base('ADA', 'EUR')
database.save_database()
#database.update_candles_on_currency('ADA')
#print(database.main_container['ADA']['1']['EUR'][-1].time)


#trading_view = TradingViewPredictions()
#trading_view.login()
