import numpy as np 
from math import sqrt
from scipy import stats

class HelthAnalyser: 
    def __init__ (self, df):
        self.df = df

    def add_columns(self, new_df):
        new_df = new_df.copy()
        new_df["height_m"] = new_df["height"]/100
        new_df["BMI"] = new_df["weight"]/(new_df["height_m"]**2)
        return new_df
    
    def analys(self, df):
        return (df[["age", "weight", "height", "systolic_bp", "cholesterol", "BMI"]]
            .agg(["mean", "median", "min", "max"]
                ).round(2))
    
    def smoker(self, df):
        return df.groupby("smoker", observed=True)["systolic_bp"].agg(
            observations = ("count"),
            proportions = ("mean")
        ).reset_index()
    
    def  numeric_variables(self, df):
        df_num = df.copy() 
        df_num["sex"] = df_num["sex"].map({"M": 1, "F": 0})
        df_num = df_num.rename(columns={"sex": "male"})
        df_num["smoker"] = df_num["smoker"].map({"Yes": 1, "No": 0})
        return df_num 
    
    # def sick_df (self, df):
    #     df = df[df["disease"] == 1]
    #     return df
    
    # def sick_sex(self, df):
    #     return df.groupby("sex" , observed=True).agg(
    #         observations = ("disease", "count"),
    #         mean_bp= ("systolic_bp", "mean"), 
    #         mean_cholesterol = ("cholesterol", "mean"),
    #         mean_age = ("age", "mean"),
    #         weight_mean = ("weight", "mean"),
    #         smoker_count=("smoker", lambda x: (x == "Yes").sum())
    #     ).reset_index()
    



def ci_mean_normal(x):
    """
    95%-CI för medel med normal-approximation:
    medel ± 1.96 * (s / sqrt(n))
    """
    x = np.asarray(x, dtype=float)
    mean_x = float(np.mean(x))
    s = float(np.std(x, ddof=1))
    n = len(x)
    se = s/sqrt(n)

    z_critical = 1.96
    half_width = z_critical + se
    lo, hi = mean_x - half_width, mean_x + half_width
    return lo, hi, mean_x, s, n, se

def ci_mean_bootstrap(x, B= 5000, confidence = 0.95):
    x = np.array(x, dtype = float)
    n = len(x)
    boot_means = np.empty(B)
    for b in range(B):
        boot_sample =  np.random.choice(x, size= n, replace=True)
        boot_means[b] = np.mean(boot_sample)

    alpha = (1 - confidence) / 2
    lo, hi = np.percentile(boot_means, [100*alpha, 100*(1 - alpha)])
    return float(lo), float(hi), float(np.mean(x))

def covers_true_mean(df, mean_bp, method = "normal", n=40, trials=200):
    hits = 0
    for _ in range(trials):
        sample = np.random.choice(df, size=n, replace=True)
        if method == "normal":
            lo, hi, *_ = ci_mean_normal(sample)
        else:
            lo, hi, *_ = ci_mean_bootstrap(sample, B=1500)
        hits += (lo <= mean_bp <= hi)
    return hits / trials


