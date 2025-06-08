# Co2-Decoupling
This project aims to investigate the critical point at which economic growth no longer leads to a corresponding rise in carbon dioxide emissions.

There are two jupyter notebooks, the one titles 'GDP vs GDP per capita' aims to find which of the two metrics is better for identifying co2 decoupling. The second is called 'Co2 decoupling' which identifies the median value at which co2 decoupling occurs.

Becuase training takes a long time, I used a package called joblib to save the models so the code will run faster. If you want to run the training yourself, simply uncomment the relevent code and comment out the jb.load function that load in the models.

Population Data:

Institute for Health Metrics and Evaluation (IHME). Global Fertility, Mortality, Migration, and Population Forecasts 2017-2100. Seattle, United States of America: Institute for Health Metrics and Evaluation (IHME), 2020.
https://ghdx.healthdata.org/record/ihme-data/global-population-forecasts-2017-2100

Co2 Data:

Hannah Ritchie, Pablo Rosado, and Max Roser (2023) - “CO₂ and Greenhouse Gas Emissions” Published online at OurWorldinData.org.

Retrieved from: 'https://ourworldindata.org/co2-and-greenhouse-gas-emissions'
