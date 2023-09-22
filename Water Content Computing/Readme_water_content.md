# Water Content Calculation!

The Water Content window in this PyQt5-based application allows users to perform water content calculations on inverted model data using the PyGIMLi library. Water content calculation is a crucial and final step in modeling, where you can determine the distribution of soil water content based on the resistivity obtained from the inversion model and the relationship between resistivity and water content at different temperatures. This readme provides an overview of the Water Content window and its functionalities.

![mainwindow_watercontent](https://github.com/wintelestr/Soil-Conditions/assets/133135894/a4a86b9a-4df6-4498-9cb0-c85facdf8fc2)

## Temperature Parameter (T)

Users have the option to either set a constant temperature or import a temperature field to consider the effect of temperature on water content.

**Spinbox Name:** Temperature
**Temperature Field Import Button:** Import Soil Temperature Field

**Description:** In the Water Content window, users can specify the constant temperature (default is 25 degrees) using the spinbox or import a two-dimensional distribution file of soil temperature to configure the water content calculation process.

**Range:**
If you do not consider the distribution of soil temperature in your analysis, you can specify a constant temperature (default is 25 degrees), assuming uniform soil temperature.If you want to consider the distribution of soil temperature, you should import a temperature field file to perform the conversion from resistivity to water content.

**Usage:** By taking into account the influence of different temperatures, you can achieve a more accurate conversion from resistivity to water content. The actual calculation process involves computing the water content at each grid point based on empirical formulas at different temperatures, considering that temperature is a two-dimensional field. This results in a two-dimensional distribution of water content throughout the soil.


## Applying Water Content Calculation

To perform water content calculation with the specified temperature, follow these steps:

Click the "Import" button in the "Data" tab to input your geophysical data and select the data file.

Create a mesh in the "Domain and Mesh" window.

Adjust the parameters in the "Inversion" tab to complete the inversion calculation.

In the "Water Content" tab, adjust the temperature value or import a temperature field file for water content calculation.

Click the "Calculate" button to start the calculation process. The program will generate a two-dimensional distribution of water content based on the temperature's influence.

Water Content Results: The water content of the selected grid will be displayed in the center of the window.

Please remember that whether you choose a constant temperature or import a real temperature field should be guided by your observed data and the precision requirements for the final water content results.

![watercontent_result_display](https://github.com/wintelestr/Soil-Conditions/assets/133135894/5b2ec9a9-dff1-442e-9e83-b99ba6cee72d)


## Saving Water Content Results

The water content calculation results will be automatically saved in JPG format in the directory, following a naming convention.


## Additional Notes

Ensure that you have completed the inversion model calculation process before performing water content calculation.

The water content calculation process may take some time, depending on whether a temperature field is imported. Please be patient and monitor the progress.

For more detailed guidance on selecting an appropriate temperature field, please refer to the application's user manual or consult with experts in geophysics.


