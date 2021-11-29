import numpy as np
import pandas as pd

# data1
def generate(df):
    for i in range(0, 5000):
        if  (
                # gender 
                df.iloc[i][0] == 1
                # can_fly
                and df.iloc[i][7] == 0
                # profession_group
                and df.iloc[i][9] == 2
                # weapoon
                and df.iloc[i][14] == 4
                # DEX
                and df.iloc[i][18] >= 6000
            ):

            # isWind_Archer
            df.iloc[i][20] = 1

    return df
    
# data2
def generate1(df):
    for i in range(0, 5000):
        if  (
                # gender 
                df.iloc[i][0] == 1
                # weapoon
                and df.iloc[i][14] == 4
            ):

            # isWind_Archer
            df.iloc[i][20] = 1

    return df

if __name__ == '__main__':

    # who is wind_Archer
    data = {
        # normal_info
        'gender': np.random.randint(0, 2, size = 5000),
        'height': np.random.randint(140, 210, size = 5000),
        'weight': np.random.randint(40, 130, size = 5000),
        'age': np.random.randint(10, 60, size = 5000),
        'family':np.random.randint(0, 2, size = 5000),
        'rich':np.random.randint(0, 2, size = 5000),
        'curse':np.random.randint(0, 2, size = 5000),
        'can_fly':np.random.randint(0, 2, size = 5000),
        'popular':np.random.randint(0, 2, size = 5000),
        'profession_group':np.random.randint(1, 6, size = 5000),

        #style
        'hair_color': np.random.randint(1, 8, size = 5000),
        'clothing_color':np.random.randint(1, 8, size = 5000),
        'eyes_color':np.random.randint(1, 8, size = 5000),
        'skill_color':np.random.randint(1, 8, size = 5000),
        'weapon':np.random.randint(1, 7, size = 5000),
        'equipment':np.random.randint(1, 6, size = 5000),
        
        #ability
        'str':np.random.randint(10, 10000, size = 5000),
        'int':np.random.randint(10, 10000, size = 5000),
        'dex':np.random.randint(10, 10000, size = 5000),
        'lux':np.random.randint(10, 10000, size = 5000),
        'isWind_Archer': 0
    }

    df = pd.DataFrame(data)

    df_new = generate(df)
    df_new.to_csv('data.csv', index = False)

    df_new1 = generate1(df)
    df_new1.to_csv('data1.csv', index = False)