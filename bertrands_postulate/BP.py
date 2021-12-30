import pandas as pd
import numpy as np


class Bertrand:
        
    def bertrand_single(self, n, show_range=False):
        results = []
        end = 2*n - 2
        for i in range(n+1, end):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                results.append(i)
        if show_range:
            print(n, end)
            return results
        else:
            return results

    # save results to dataframe
    def bertrand_range(self, length):
        df = pd.DataFrame({'num': np.array([j for j in range(4,length)]), 'length': np.array([len(self.bertrand_single(i)) for i in range(4, length)])})
        return df

