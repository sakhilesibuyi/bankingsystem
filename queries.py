

sql_queries = [
    {
       "query":"""INSERT INTO api_branch (branch_name, branch_code) VALUES (?, ?);""",
       "data":[('MIDRAND - BOULDERS', '12345643'),('MIDRAND - CARLSWALD', '787533213'),('MIDRAND - BLUE HILLS', '78753'),('MIDRAND - SAGEWOOD', '7875213')]
    },
    {
        "query":"INSERT INTO api_bank(bank_name,branch_id) values(?,?)",
        "data":[('FIRST NATIONAL BANK LTD','1'),('FIRST NATIONAL BANK LTD','2'),('FIRST NATIONAL BANK LTD','3'),('FIRST NATIONAL BANK LTD','4')]
    },
    {
        "query":"""INSERT INTO api_client(name,address,contact_no) values(?,?,?)""",
        "data":[('Sakhile Sibuyi','URBAN RIDGE SOUTH MIDRAND 1686','0862534564'),('Jason Statum','23 Rabbie Ridge Midrand 1685','0867893726')]
    },
    {
        "query":"""INSERT INTO api_accountType(type) values(?)""",
        "data":[('Savings',),('Credit',)]
    },
    {
        "query": """INSERT INTO api_account(owner_id,account_type_id,bank_id,balance) values(?,?,?,?)""","data":[(1,1,2,40),(2,1,2,50)]},
    {
        "query":"""INSERT INTO api_deposit(amount,account_id) values(?,?)""","data":[(3000,1),(100,2)]},
    {
        "query":"""INSERT INTO api_withdrawal(amount,account_id) values(?,?)""","data":[(100,1)]}
    ]

    #{
    #    "query":"""INSERT INTO api_transfer(account,branch) values(?,?)""","data":[]
    #}
