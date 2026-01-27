import pandas as pd
# import sys

# print(f"Python version: {sys.version}")
# print(f"Pandas version: {pd.__version__}")
# print(f"Pandas file location: {pd.__file__}")
# df=pd.read_csv('datatest.csv')
df=pd.read_csv('C:\\Users\Dinamicka Laptop\Downloads\Datatest.csv')
#type(df)
#print(df)

### create and write info to csv file
# df2=pd.DataFrame.from_dict({'a':[1,2],'b':[3,4]})
# print(df2)

# df.to_csv('./tmp.csv')

### informtion about dataset
#df.info() 

###size, names coluumns, head, tail
# print(df.shape)
# print(df.columns)
# print(df.head())
# print(df.tail())
# print(df.dtypes)

# print(df['price'])
# print(df[['name','price']].head(3))
# print(df.loc[[5,10,15],['name','price']])
# print(df.iloc[[5,10,15],[0,1]])
# print(df[df['price']>100])
# print(df['price']>100)
print(df[df['price'].isin([100,200])])