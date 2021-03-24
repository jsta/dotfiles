try:
    import pandas as pd
    pd.set_option("display.max_columns", None)
    pd.set_option('display.max_rows', None)
except:
    print("No pandas installation found to set options.")
