import numpy as np 
from math import sqrt
from scipy import stats
import pandas as pd

class HelthAnalyser: 
    """
    En klass för att köra olika analyser av en dataframe 
    """
    def __init__ (self, df: pd.DataFrame):
        if not isinstance(df, pd.DataFrame):
            raise TypeError("df måste vara en pandas Dataframe")
        self.df = df

    def add_columns(self, df):
        """
        Adderar kolumnerna height_m (längd i meter) och 
        räknar ut och lägger till kolumnen BMI. 
        """
        required_cols = ["height", "weight"]
        missing_cols = [c for c in required_cols if c not in df.columns]
        if missing_cols: 
            raise KeyError (f" Följande kolumner saknas {missing_cols}")

        new_df = df.copy()
        new_df["height_m"] = new_df["height"]/100
        new_df["BMI"] = new_df["weight"]/(new_df["height_m"]**2)
        return new_df
    
    def analys(self, df):
        """
        Gör en första beskrivande analys av de numeriska kolumnerna i tabellen och
        återger dem i medelvärde, median, minsta värde och största värde. 
        """
        required_cols = ["age", "weight", "height", "systolic_bp", "cholesterol", "BMI"]
        missing_cols = [c for c in required_cols if c not in df.columns]
        if missing_cols: 
            raise KeyError (f" Följande kolumner saknas {missing_cols}")
        
        return (df[cols].agg(["mean", "median", "min", "max"]).round(2))
    
    def smoker(self, df):
        """
        Grupperar datan i rökare och icke rökare och 
        räknar ut medelvärdet på gruppernas systoliska blodtryck.
        """
        required_cols = ["smoker", "systolic_bp"]
        missing_cols = [c for c in required_cols if c not in df.columns]
        if missing_cols: 
            raise KeyError (f" Följande kolumner saknas {missing_cols}")

        return df.groupby("smoker", observed=True)["systolic_bp"].agg(
            observations = ("count"),
            proportions = ("mean")
        ).reset_index()
    
    def  numeric_variables(self, df):
        """
        Gör om samtliga kolumner till numeriska värden. 
        """
        required_cols = ["smoker", "sex"]
        missing_cols = [c for c in required_cols if c not in df.columns]
        if missing_cols: 
            raise KeyError (f" Följande kolumner saknas {missing_cols}")
        
        df_num = df.copy() 
        df_num["sex"] = df_num["sex"].map({"M": 1, "F": 0})
        df_num = df_num.rename(columns={"sex": "male"})
        df_num["smoker"] = df_num["smoker"].map({"Yes": 1, "No": 0})
        return df_num 
    
def ci_mean_normal(numpy_array):
    """
    95%-CI för medel med normal-approximation:
    medel ± 1.96 * (s / sqrt(n))
    """
    numpy_array = np.asarray(numpy_array, dtype=float)
    n = len(numpy_array)
    if n == 0: 
        raise ValueError("Arrayen är tom")

    mean_value = float(np.mean(numpy_array))
    s = float(np.std(numpy_array, ddof=1))
    
    se = s/sqrt(n)

    z_critical = 1.96
    half_width = z_critical + se
    lo, hi = mean_value - half_width, mean_value + half_width
    return lo, hi, mean_value, s, n, se

def ci_mean_bootstrap(numpy_array, B= 5000, confidence = 0.95):
    """
    Räknar ut ett 95%- CI med bootstrapmetod
    """
    numpy_array = np.array(numpy_array, dtype = float)
    n = len(numpy_array)
    if n == 0: 
        raise ValueError("Arrayen är tom")
    
    mean_boot = np.empty(B)
    for b in range(B):
        boot_sample =  np.random.choice(numpy_array, size= n, replace=True)
        mean_boot[b] = np.mean(boot_sample)

    alpha = (1 - confidence) / 2
    lo, hi = np.percentile(mean_boot, [100*alpha, 100*(1 - alpha)])
    return float(lo), float(hi), float(np.mean(numpy_array))

def covers_true_mean(df, mean_bp, method = "normal", n=40, trials=200):
    """
    Testar metoderna för 95%- CI för att se hur många gånger 
    testets medelvärde hamnar inom den 95%iga intervallen för meldelvärdet. 
    """    
    hits = 0
    for _ in range(trials):
        sample = np.random.choice(df, size=n, replace=True)
        if method == "normal":
            lo, hi, *_ = ci_mean_normal(sample)
        else:
            lo, hi, *_ = ci_mean_bootstrap(sample, B=1500)
        hits += (lo <= mean_bp <= hi)
    return hits / trials


