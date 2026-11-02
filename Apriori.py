import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

data = pd.DataFrame([
    [1, 1, 0],
    [1, 1, 1],
    [1, 0, 1],
    [0, 1, 1]
], columns=["Food", "Transport", "Shopping"])

frequent = apriori(
    data,
    min_support=0.25,
    use_colnames=True
)

rules = association_rules(
    frequent,
    metric="confidence",
    min_threshold=0.5
)

print(rules)