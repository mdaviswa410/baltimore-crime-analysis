import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv("Data/Part1_Crime_Beta_3880953751259285714.csv")

print(df.head())
print(df.info())
print(df.columns)


#Deleting duplicates
df.drop_duplicates(inplace=True)

df['CrimeDateTime'] = pd.to_datetime(
    df['CrimeDateTime']
)

#Making columns
df['Year'] = df['CrimeDateTime'].dt.year
df['Month'] = df['CrimeDateTime'].dt.month
df['MonthName'] = df['CrimeDateTime'].dt.month_name()
df['DayofWeek'] = df['CrimeDateTime'].dt.day_name()
df['Hour'] = df['CrimeDateTime'].dt.hour

print(df[['CrimeDateTime','Year','MonthName','DayofWeek','Hour']].head())

missing_values = df.isnull().sum()

print(missing_values.sort_values(ascending=False))

#cleaning
df = df[df['Year'] >= 2011]
print(df['Year'].min())
print(df['Year'].max())

#Dashboard Section 1: Crime Overview
#Top 10 crimes
top_crime = df['Description'].value_counts()
print(top_crime.head(10))

plt.figure(figsize=(10,6))
top_crime.head(10).plot(kind='bar')

plt.title('Top 10 Crimes in Baltimore')
plt.xlabel('Crime Type')
plt.ylabel('Number of Incidents')
plt.tight_layout()
plt.savefig('top_10_crimes.png')
plt.show()


#Section 2: Trends over time
#is crime increasing or decreasing in Baltimore
yearly_trends = df.groupby('Year').size()
print(yearly_trends)

plt.figure(figsize=(10,6))
yearly_trends.plot()

plt.title('Baltimore Crime Incidents by Year')
plt.xlabel('Year')
plt.ylabel('Number of Incidents')
plt.tight_layout()
plt.savefig('crime_incident_year.png')
plt.show()



#section 3: Neighborhood analysis
neigborhood = df['Neighborhood'].value_counts().head(10)
print(neigborhood.head(20))

plt.figure(figsize=(10,6))
neigborhood.sort_values().plot(kind='barh')

plt.title('Top 10 Neighborhoods by Crime Incidents')
plt.xlabel('Number of incidents')
plt.ylabel('Neighborhood')
plt.tight_layout()
plt.savefig('top_10_neighbor.png')
plt.show()


#Section 4: Time of day analysis
hourly_trend = df.groupby('Hour').size()
print(hourly_trend)

plt.figure(figsize=(10,6))
hourly_trend.plot(kind='line', marker='o')
plt.title('Crime Incidents by Hour of Day')
plt.xlabel('Hour (Military Time)')
plt.ylabel('Number of Incidents')
plt.xticks(range(24))
plt.tight_layout()
plt.savefig('crime_by_hour.png')
plt.show()



print(df['Description'].value_counts().head(10))

print(df.groupby('Year').size())

print(df['Neighborhood'].value_counts().head(10))

print(df.groupby('Hour').size().sort_values(ascending=False).head(10))

df.to_csv(
    "data/baltimore_crime_cleaned.csv",
    index=False
)