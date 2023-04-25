import pandas


class Definition:

    def __init__(self, term):
        self.term = term

    def get(self):
        df = pandas.read_csv('OPTED-Dictionary.csv')
        return tuple(df.loc[df['Word'] == self.term]['Definition'])


# d = Definition(term='Sun')
# print(d.get())
