import pandas as pd

data={
    "Name":[
        "Harsh Gupta","Steven Smith","Mitchell Johnson",
        "Kevin Piterson","Duggy Bolinger"
    ],
    "Phone":[
        "9599284282","8979514282","1234567890","0987654321",
        "6543210987"
    ],
    "Email":[
        "hgagra12@gmail.com","steven@yahoo.co.in","mitch@gmail.com",
        "kevin@gmail.com","duggy@outlook.com"
    ],

    "Address":[
        "India","Australia","Germany","Italy","France"
    ]
}
df=pd.DataFrame(data)
df.to_csv("contact.csv",index=False)