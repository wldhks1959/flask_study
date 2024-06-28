import pandas as pd

def save(location, clean, built):
    idx = len(pd.read_csv("database.csv"))
    new_df = pd.DataFrame({"location":location,
                           "clean":clean,
                           "built":built}, 
                         index = [idx])
    new_df.to_csv("database.csv",mode = "a", header = False)
    return None

def load_list():
    house_list = []
    df = pd.read_csv("database.csv")
    for i in range(len(df)):
        house_list.append(df.iloc[i].tolist())
    print(house_list)
    # return house_list

def now_index():
    df = pd.read_csv("database.csv")
    return len(df)-1


def load_house(idx):
    df = pd.read_csv("database.csv")
    house_inf = df.iloc[idx]
    return house_info


if __name__ =="__main__":
    load_list()