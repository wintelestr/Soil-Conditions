# Create mesh and domain 
 
The Domain and Mesh window in this PyQt5-based application allows users to create a domain and mesh based on their data. Users can customize grid boundaries and finite element density as needed. 

The below screenshot is not up to date
![mainwindow_domain&mesh](https://github.com/wintelestr/Soil-Conditions/blob/2-2-creation-of-domain-and-mesh/Domain%20Selection%20and%20meshing/MainWindow_domain%26mesh.png)

## Parameters 

### Domain Parameters
**1. Start Point**
Spinbox Name: spinBox_startX & spinBox_startY

Description: The values of "spinBox_startX" and "spinBox_startY" represent the x-axis and y-axis positions of the starting point, respectively.

**2. End Point**
Spinbox Name: spinBox_endX & spinBox_endY

Description: The values of "spinBox_endX" and "spinBox_endY" represent the x-axis and y-axis positions of the ending point, respectively.

### Mesh Parameters
**1. Quality**
Spinbox Name: doubleSpinBox_quality

Description: The "quality" parameter is a parameter that controls the quality of generated grid elements, typically triangles or quadrilaterals. Generally, higher values of quality result in a more uniform and closer-to-regular shape grid. However, higher quality values may require more computational time. In this project, we typically set the quality around 33.5.

Maximum value:34

**2. Area**
Spinbox Name: doubleSpinBox_area

Description: The "area" parameter represents the size of grid elements, controlling the size of the generated grid units. Smaller "area" values result in smaller grid units, while larger values produce larger grid units. In this project, we typically set this value around 0.5.

## Generate Domain and Mesh

To create a domain and mesh, follow these steps:

Click the "Choose your file" button to select the data file and click the "Import" button in the "Data" tab to input your geophysical data.

Enter the value of "spinBox_startX", "spinBox_startY", "spinBox_endX", and "spinBox_endY" to generate a domain.

The below screenshot is not up to date
![domain_creation](https://github.com/wintelestr/Soil-Conditions/blob/2-2-creation-of-domain-and-mesh/Domain%20Selection%20and%20meshing/domain.png)


Enter the value of "doubleSpinBox_quality" and "doubleSpinBox_area" to generate a mesh.
The below screenshot is not up to date
![mesh_creation](https://github.com/wintelestr/Soil-Conditions/blob/2-2-creation-of-domain-and-mesh/Domain%20Selection%20and%20meshing/mesh1.png)

## Saving generated figures

If users want to save any domain or mesh they created, simply click the "save" button to save the figures to the local directory.


## Additional Notes

Ensure that you input an appropriate value for "area". 

The choice of the "area" parameter affects the precision of geographical data representation. If the "area" value is too large, it may result in overly coarse grid elements, which might fail to capture underground details. Conversely, if the "area" value is too small, it may lead to the generation of an excessive number of small grid elements, resulting in poor visualization quality.

Please refer to the user manual if you need any help relevant to the application.


