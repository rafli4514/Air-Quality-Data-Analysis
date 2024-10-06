import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul Dashboard
st.title("Dashboard Polusi Udara")

# Path file dataset
file_path = os.path.join(os.getcwd(), 'dataset.csv')

# Load Data
def load_data():
    df = pd.read_csv(file_path)
    return df

df = load_data()

# Data Cleaning
def clean_data(df):
    df['PM2.5'].fillna(df['PM2.5'].median(), inplace=True)
    df['PM10'].fillna(df['PM10'].median(), inplace=True)
    df['SO2'].fillna(df['SO2'].median(), inplace=True)
    df['NO2'].fillna(df['NO2'].median(), inplace=True)
    df['CO'].fillna(df['CO'].median(), inplace=True)
    df['O3'].fillna(df['O3'].median(), inplace=True)
    df['TEMP'].fillna(df['TEMP'].median(), inplace=True)
    df['PRES'].fillna(df['PRES'].median(), inplace=True)
    df['DEWP'].fillna(df['DEWP'].median(), inplace=True)
    df['RAIN'].fillna(df['RAIN'].median(), inplace=True)
    df['WSPM'].fillna(df['WSPM'].median(), inplace=True)

    # mengisi data yang hilang dengan modus
    df['wd'].fillna(df['wd'].mode()[0], inplace=True)
    
    return df

df = clean_data(df)

# Tren Polusi dari Tahun ke Tahun
st.header("Tren Polusi dari Tahun ke Tahun")
data_tahunan = df.select_dtypes(include=['float64', 'int64']).groupby(df['year']).mean()

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(data_tahunan.index, data_tahunan['PM2.5'], label='PM2.5', marker='o')
ax.plot(data_tahunan.index, data_tahunan['PM10'], label='PM10', marker='o')
ax.plot(data_tahunan.index, data_tahunan['SO2'], label='SO2', marker='o')
ax.plot(data_tahunan.index, data_tahunan['NO2'], label='NO2', marker='o')
ax.plot(data_tahunan.index, data_tahunan['O3'], label='O3', marker='o')
ax.set_title('Tren Polusi Udara dari Tahun ke Tahun')
ax.set_xlabel('Tahun')
ax.set_ylabel('Rata-rata Konsentrasi Polusi')
ax.legend()
ax.grid(True)
st.pyplot(fig)

# Grafik CO terpisah
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(data_tahunan.index, data_tahunan['CO'], label='CO', marker='o', color='blue')
ax.set_title('Tren Konsentrasi Karbon Monoksida')
ax.set_xlabel('Tahun')
ax.set_ylabel('Rata-rata Konsentrasi CO')
ax.legend()
ax.grid(True)
st.pyplot(fig)

# konsentrasi bulanan
st.header("Konsentrasi Bulanan Rata-Rata PM2.5")
monthly_avg_pm25_by_year = df.groupby(['year', 'month'])['PM2.5'].mean().reset_index()
monthly_avg_pm25_pivot = monthly_avg_pm25_by_year.pivot(index='year', columns='month', values='PM2.5')

fig, ax = plt.subplots(figsize=(14, 8))
sns.heatmap(monthly_avg_pm25_pivot, annot=True, fmt=".1f", cmap='YlGnBu', linewidths=1, ax=ax)
ax.set_title('Konsentrasi Bulanan Rata-Rata dari tahun 2013 hingga 2017')
ax.set_xlabel('Bulan')
ax.set_ylabel('Tahun')
st.pyplot(fig)

# Lonjakan Polusi Sepanjang Hari
st.header("Lonjakan Polusi Sepanjang Hari")
hourly_data = df.select_dtypes(include=['float64', 'int64']).groupby(df['hour']).mean()

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(hourly_data.index, hourly_data['PM2.5'], label='PM2.5', marker='o')
ax.plot(hourly_data.index, hourly_data['PM10'], label='PM10', marker='o')
ax.plot(hourly_data.index, hourly_data['SO2'], label='SO2', marker='o')
ax.plot(hourly_data.index, hourly_data['NO2'], label='NO2', marker='o')
ax.plot(hourly_data.index, hourly_data['O3'], label='O3', marker='o')
ax.set_title('Lonjakan Polusi Terjadi di Sepanjang Hari')
ax.set_xlabel('Jam')
ax.set_ylabel('Rata-rata Konsentrasi Polusi')
ax.legend()
ax.grid(True)
st.pyplot(fig)

# Grafik CO terpisah
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(hourly_data.index, hourly_data['CO'], label='CO', marker='o', color='blue')
ax.set_title('Lonjakan Konsentrasi Karbon Monoksida')
ax.set_xlabel('Jam')
ax.set_ylabel('Rata-rata Konsentrasi CO')
ax.legend()
ax.grid(True)
st.pyplot(fig)

# Pengaruh Kecepatan dan Arah Angin terhadap Polusi
st.header("Pengaruh Kecepatan dan Arah Angin terhadap Polusi")

# Scatter plot kecepatan angin vs PM2.5
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(df['WSPM'], df['PM2.5'], alpha=0.5, color='skyblue')
ax.set_title('Hubungan Kecepatan Angin dan Konsentrasi PM2.5')
ax.set_xlabel('Kecepatan Angin (m/s)')
ax.set_ylabel('Konsentrasi PM2.5')
ax.grid(True)
st.pyplot(fig)

# Polusi berdasarkan arah angin
wind_direction_counts = df.groupby('wd')[['PM2.5', 'PM10', 'SO2', 'NO2', 'O3']].mean(numeric_only=True)
fig, ax = plt.subplots(figsize=(10, 6))
wind_direction_counts.plot(kind='bar', stacked=True, colormap='viridis', ax=ax)
ax.set_title('Rata-rata Konsentrasi Polusi Udara Berdasarkan Arah Angin')
ax.set_xlabel('Arah Angin')
ax.set_ylabel('Rata-rata Konsentrasi Polusi')
plt.xticks(rotation=45)
st.pyplot(fig)

# Hubungan Suhu dan Polusi Udara
st.header("Hubungan Suhu dan Polusi Udara")
df['TEMP_bins'] = pd.cut(df['TEMP'], bins=10)

correlation_temp = df.groupby('TEMP_bins')[['PM2.5', 'PM10', 'SO2', 'NO2', 'O3']].mean(numeric_only=True)

fig, ax = plt.subplots(figsize=(10, 6))
correlation_temp.plot(kind='bar', stacked=True, colormap='viridis', ax=ax)
ax.set_title('Rata-rata Konsentrasi Polusi Udara Berdasarkan Suhu')
ax.set_xlabel('Suhu')
ax.set_ylabel('Rata-rata Konsentrasi Polusi')
plt.xticks(rotation=45)
st.pyplot(fig)

# Pengaruh Curah Hujan terhadap Polusi
st.header("Pengaruh Curah Hujan terhadap Polusi")
df['RAIN_bins'] = pd.cut(df['RAIN'], bins=[0, 10, 20, 50, 100, 150], labels=['0-10', '10-20', '20-50', '50-100', '100-150'])

correlation_rain = df.groupby('RAIN_bins')[['PM2.5', 'PM10', 'SO2', 'NO2', 'O3']].mean(numeric_only=True)

fig, ax = plt.subplots(figsize=(10, 6))
correlation_rain.plot(kind='bar', stacked=True, colormap='viridis', ax=ax)
ax.set_title('Rata-rata Konsentrasi Polusi Udara Berdasarkan Curah Hujan')
ax.set_xlabel('Curah Hujan (mm)')
ax.set_ylabel('Rata-rata Konsentrasi Polusi')
plt.xticks(rotation=45)
st.pyplot(fig)