

import pandas as pd
import numpy as np
from scipy import stats

# Load dataset
taxi_data = pd.read_csv("2017_Yellow_Taxi_Trip_Data.csv", index_col = 0)

taxi_data.describe(include='all')

# Looking up the average fare amount for each payment type

taxi_data.groupby('payment_type')['fare_amount'].mean()


# The results show that those who pay with credit card on average spend more than those who pay with cash
# but this difference can be due to random sampling so we will conduct a hypothesis test to see if there is
# a statistically significant difference between the two payment types
    

# Conducting the hypothesis test with a significant level of 5%

significance_level = 0.05

cash = taxi_data[taxi_data['payment_type'] == 2]['fare_amount']
credit_card = taxi_data[taxi_data['payment_type'] == 1]['fare_amount']
stats.ttest_ind(a = credit_card, b = cash, equal_var = False)

# Since the P value is smaller than the significance level we reject the null hypothesis, meaning there IS a significant difference in the total fare between credit cards and cash

# *** Some import things to note: Firstly, the key business insight gained from this A/B testing is that
# encouraging customers to pay with credit cards will increase revenue. Secondly, this project was done to
# showcase the ability to conduct hypothesis testing on python, in actuality there may be many other
# factors that play into why credit card payments are on average larger (for example: long trip distances
# might cause the fare to be more than the average amount of cash a customer carries, therefore leading to
# credit card payment). Here the assumption is that payment type influences fare amount but fare amount can
# very likely be the influencing factor. ***
