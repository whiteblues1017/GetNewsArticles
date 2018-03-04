import pandas
import os
homepath=os.path.expanduser('~')

def load_tag_name():
    df=pandas.read_csv(homepath+'/_university/nikkei/data/mainichi/mainichi.csv',
                       header=None,names=['1st','2nd'])
    return df


def load_articles(first,second):
    df=pandas.read_csv(homepath+'/_university/nikkei/data/mainichi/'+first+'/'+second+'.csv')
    df=df.dropna(subset=['article'])
    return df

def format_date(df):
    list=df["date"].tolist()
    for i in range(len(list)):
        df["date"][i]=list[i].replace(' ','')
    return df

if __name__ == '__main__':
    #with open(homepath+'/_university/nikkei/data/asahi.csv','w') as fw:
    df=load_tag_name()
    first_tag=df['1st'].tolist()
    second_tags=df['2nd'].tolist()

    df_new=pandas.DataFrame(columns=["title","date","tags","article"]).dropna()
    for i in range(len(first_tag)):
        second_tag=second_tags[i].split(',')
        for j in range(len(second_tag)):
            df=load_articles(first_tag[i],second_tag[j])
            df=format_date(df)
            df_new=pandas.concat([df_new,df])

    df_new.to_csv(homepath+'/_university/nikkei/data/mainichi.csv',index=None)
