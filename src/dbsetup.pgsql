CREATE TABLE holdings(
    _id SERIAL PRIMARY KEY,
    ticker varchar(20) NOT NULL,
    qty INTEGER,
    total_val NUMERIC
);

CREATE TABLE stock_transac(
    _id SERIAL PRIMARY KEY,
    trans_type varchar(5) NOT NULL,
    on_ticker varchar(20) NOT NULL,
    unit_price NUMERIC,
    qty INTEGER,
    profit NUMERIC 
);

CREATE TABLE accounts(
    _id SERIAL PRIMARY KEY,
    total_income NUMERIC DEFAULT 0,
    balance NUMERIC DEFAULT 0,
    Total_stck_val NUMERIC DEFAULT 0   
);

CREATE TABLE acc_transac(
    _id SERIAL PRIMARY KEY,
    amount NUMERIC,
    on_date DATE DEFAULT CURRENT_DATE,
    at_time TIME DEFAULT CURRENT_TIME
);

CREATE TABLE acc_holding_transac(
    _id SERIAL PRIMARY KEY,
    acc_id INT NOT NULL
    REFERENCES accounts(_id)
    ON DELETE CASCADE,
    holding_id INT
    REFERENCES holdings(_id)
    ON DELETE CASCADE,
    stck_transac_id INT
    REFERENCES stock_transac(_id)
    ON DELETE CASCADE,
    acc_transac_id INT NOT NULL REFERENCES acc_transac(_id)
    ON DELETE CASCADE    
);

CREATE TABLE users(
    _id SERIAL PRIMARY KEY,
    acc_id INT NOT NULL
    REFERENCES accounts(_id)
    ON DELETE CASCADE  
)

