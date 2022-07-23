import src.backend.database.main as db

class ValidationError(Exception):
    pass

def ticker_exists(ticker):
    try:
        data = db.queryGet("SELECT * FROM symbol_name WHERE symbol = '%s'" % (ticker))
        if(len(data) == 0):
            raise ValidationError("Ticker does not exist")
        return 
    except ValidationError as v_err:
        raise v_err
    except Exception as e:
        raise Exception("Internal error")
