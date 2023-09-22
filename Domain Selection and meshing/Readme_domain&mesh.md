# Create mesh and domain & Select different resistivity measurement methods 

The Domain and Mesh window in this PyQt5-based application allows users to create a domain and mesh based on their data.Users can customise grid boundaries and finite element density as needed, generate figures that better suit their needs by selecting two different geoelectric exploration methods. This readme provides an overview of the Domain and Mesh window and its functionalities.

![mainwindow_domain&mesh](https://github.com/wintelestr/Soil-Conditions/blob/2-2-creation-of-domain-and-mesh/Domain%20Selection%20and%20meshing/MainWindow_domain%26mesh.png)

## Parameters 

### Domain Parameters
**1. Start Point**
Spinbox Name: startX & startY

Description: The value of "startX" and "startY" represent the x-axis and y-axis positions of the starting point, respectively.

Range: Minimum value:0, Maximum value:10

**2. End Point**
Spinbox Name: endX & endY

Description: The value of "endX" and "endY" represent the x-axis and y-axis positions of the ending point, respectively.

Range: Minimum value:-8, Maximum value:47

### Mesh Parameters
**1. Quality**
Spinbox Name: quality

Description: The "quality" parameter is a parameter that controls the quality of generated grid elements, typically triangles or quadrilaterals. Generally, higher values of quality result in a more uniform and closer-to-regular shape grid. However, higher quality values may require more computational time. In this project, we typically set the quality around 33.5.

Range: Minimum value:0, Maximum value:50

**2. Area**
Spinbox Name: area

Description: The "area" parameter represents the size of grid elements, controlling the size of the generated grid units. Smaller "area" values result in smaller grid units, while larger values produce larger grid units. In this project, we typically set this value around 0.5.

Range: Minimum value:0, Maximum value:1


## Generate Domain and Mesh

To create a domain and mesh, follow these steps:

Click the "Choose your file" button to select the data file and click "Import" button in the "Data" tab to input your geophysical data.

Enter the value of "startX", "startY", "endX", "endY" to generate a domain.

![domain_creation](https://github.com/wintelestr/Soil-Conditions/blob/2-2-creation-of-domain-and-mesh/Domain%20Selection%20and%20meshing/domain.png)


Enter the value of "quality" and "area" to generate a mesh.
![mesh_creation](https://github.com/wintelestr/Soil-Conditions/blob/2-2-creation-of-domain-and-mesh/Domain%20Selection%20and%20meshing/mesh1.png)

To measure the resistivity in different method, follow these steps:

Click the "Wenner Array(WA)" or "Dipole-Dipole(DD)" button to show resistivity using different electrode arrangement schemes.
![Wenner_Array_Method](https://github.com/wintelestr/Soil-Conditions/blob/2-2-creation-of-domain-and-mesh/Domain%20Selection%20and%20meshing/wa_method.png)

![DipoleDipole_Method](https://github.com/wintelestr/Soil-Conditions/blob/2-2-creation-of-domain-and-mesh/Domain%20Selection%20and%20meshing/dd_method.png)


## Saving generated figures

If users want to save any domain or mesh they created, simply click save button to save the figures to the local directory.


## Additional Notes

Ensure that you input an appropriate value for "area". 

The choice of "area" parameter affects the precision of geographical data representation. If the "area" value is too large, it may result in overly coarse grid elements, which might fail to capture underground details. Conversely, if the "area" value is too small, it may lead to the generation of an excessive number of small grid elements, resulting in poor visualization quality.

Please refer to the user manual if you need any help relevant to the application.


