try:
    import pandas as pd
    pd.set_option("display.max_columns", None)
except:
    print("No pandas installation found to set options.")
