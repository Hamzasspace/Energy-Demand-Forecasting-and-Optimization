# importing the libraries
import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# reading the csv file:
df = pd.read_csv('dataset.csv')

# Splitting Dataset into Sub-DataFrames:

df_general = df[['country', 'year', 'iso_code', 'population', 'gdp']]
df_biofuel = df[['biofuel_cons_change_pct', 'biofuel_cons_change_twh', 'biofuel_cons_per_capita', 'biofuel_consumption', 'biofuel_elec_per_capita', 'biofuel_electricity', 'biofuel_share_elec', 'biofuel_share_energy']]
df_coal = df[['coal_cons_change_pct', 'coal_cons_change_twh', 'coal_cons_per_capita', 'coal_consumption', 'coal_elec_per_capita', 'coal_electricity',
              'coal_prod_change_pct', 'coal_prod_change_twh', 'coal_prod_per_capita', 'coal_production', 'coal_share_elec', 'coal_share_energy']]
df_gas = df[['gas_cons_change_pct', 'gas_cons_change_twh', 'gas_consumption', 'gas_elec_per_capita', 'gas_electricity', 'gas_energy_per_capita',
             'gas_prod_change_pct', 'gas_prod_change_twh', 'gas_prod_per_capita', 'gas_production', 'gas_share_elec', 'gas_share_energy']]
df_ghg_emissions = df[['greenhouse_gas_emissions']]
df_hydropower = df[['hydro_cons_change_pct', 'hydro_cons_change_twh', 'hydro_consumption', 'hydro_elec_per_capita', 'hydro_electricity', 
                    'hydro_energy_per_capita', 'hydro_share_elec', 'hydro_share_energy']]
df_nuclear = df[['nuclear_cons_change_pct', 'nuclear_cons_change_twh', 'nuclear_consumption', 'nuclear_elec_per_capita', 'nuclear_electricity',
                 'nuclear_energy_per_capita', 'nuclear_share_elec', 'nuclear_share_energy']]
df_oil = df[['oil_cons_change_pct', 'oil_cons_change_twh', 'oil_consumption', 'oil_elec_per_capita', 'oil_electricity', 'oil_energy_per_capita',
             'oil_prod_change_pct', 'oil_prod_change_twh', 'oil_prod_per_capita', 'oil_production', 'oil_share_elec', 'oil_share_energy']]
df_other_renewable = df[['other_renewable_consumption', 'other_renewable_electricity', 'other_renewable_exc_biofuel_electricity', 
                         'other_renewables_cons_change_pct', 'other_renewables_cons_change_twh', 'other_renewables_elec_per_capita', 
                         'other_renewables_elec_per_capita_exc_biofuel', 'other_renewables_energy_per_capita', 'other_renewables_share_elec', 
                         'other_renewables_share_elec_exc_biofuel', 'other_renewables_share_energy']]
df_renewable = df[['renewables_cons_change_pct', 'renewables_cons_change_twh', 'renewables_consumption', 'renewables_elec_per_capita', 
                   'renewables_electricity', 'renewables_energy_per_capita', 'renewables_share_elec', 'renewables_share_energy']]
df_solar = df[['solar_cons_change_pct', 'solar_cons_change_twh', 'solar_consumption', 'solar_elec_per_capita', 'solar_electricity', 
               'solar_energy_per_capita', 'solar_share_elec', 'solar_share_energy']]

df_wind = df[['wind_cons_change_pct', 'wind_cons_change_twh', 'wind_consumption', 'wind_elec_per_capita', 'wind_electricity', 
              'wind_energy_per_capita', 'wind_share_elec', 'wind_share_energy']]

# Saving the Sub-DaraFrames as a csv files on current directory

df_general.to_csv('df_general.csv', index=False)
df_biofuel.to_csv('df_biofuel.csv', index=False)
df_gas.to_csv('df_gas.csv', index=False)
df_ghg_emissions.to_csv('df_ghg_emissions.csv', index=False)
df_hydropower.to_csv('df_hydropower.csv', index=False)
df_nuclear.to_csv('df_nuclear.csv', index=False)
df_oil.to_csv('df_oil.csv', index=False)
df_other_renewable.to_csv('df_other_renewable.csv', index=False)
df_renewable.to_csv('df_renewable.csv', index=False)
df_solar.to_csv('df_solar.csv', index=False)
df_wind.to_csv('df_wind.csv', index=False)

# Display all rows (if needed) and columns:
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Data Cleaning:

# Drop rows where 'country'  or 'year' is missing
df_cleaned = df.dropna(subset=['country', 'year'])

# Check for missing values:
missing_values = df.isnull().sum()

# Analyze the Relationship Between CO₂ Emissions and Energy Mix:

# Selecting relevant columns for correlation analysis
columns_for_correlation = ['greenhouse_gas_emissions', 'fossil_share_energy', 
                           'renewables_share_energy', 'nuclear_share_energy', 
                           'hydro_share_energy', 'biofuel_share_energy', 
                           'solar_share_energy', 'wind_share_energy']
# Calculate correlation matrix
correlation_matrix = df[columns_for_correlation].corr()
# Scatter plots to visualize relationships with CO₂ emissions

plt.figure(figsize=(8, 6))
for i, energy_source in enumerate(columns_for_correlation[1:]):
    plt.subplot(2, 4, i+1)
    sns.scatterplot(data=df, x=energy_source, y='greenhouse_gas_emissions')
    plt.title(f"CO₂ Emissions vs {energy_source.capitalize().replace('_', ' ')}")
    plt.xlabel(energy_source.replace('_share_energy', ' Share'))
    plt.ylabel("CO₂ Emissions")

plt.tight_layout()

plt.figure(figsize=(4, 2))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", center=0)
plt.title("Correlation Matrix: CO₂ Emissions and Energy Mix Shares")
