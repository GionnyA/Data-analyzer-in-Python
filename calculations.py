class Calculations:
    def __init__(self, df_clean):
        self.df = df_clean

    def mean(self, selected_col):
        return self.df[selected_col].mean()

    def median(self, selected_col):
        return self.df[selected_col].median()

    def std_dev(self, selected_col):
        return self.df[selected_col].std()