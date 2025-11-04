def analys(df, x):
    medel = df[x].mean()
    median = df[x].median()
    min = df[x].min()
    max = df[x].max()
    return medel, median, min, max 
