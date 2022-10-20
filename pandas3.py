########################################
from traceback import FrameSummary

################################
PANDAS DATA FrameS
################################

import pandas as pd

# Calling DataFrame constructor
df = pd.DataFrame()
print(df)

# list of strings
lst = ['Geeks', 'For', 'Geeks', 'is',
			'portal', 'for', 'Geeks']

lst2 = ['Geeks', 'For', 'Geeks', 'is',
			'portal', 'for', 'Geeks']

# Calling DataFrame constructor on list
df = pd.DataFrame(lst,lst2)
print(df)
