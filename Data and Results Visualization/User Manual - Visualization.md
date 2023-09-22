User Manual - Visualization

The visualization part is the fifth major functionality of this program and serves as the final step in the primary workflow designed for this program. 

<img src="/Users/apple/Desktop/Screenshot 2023-09-22 at 1.17.48 pm.png" alt="Screenshot 2023-09-22 at 1.17.48 pm" style="zoom:33%;" />

1. Tabs "Visualization" -> "Resistivity" and "Visualization" -> "Water content":

   This step primarily involves comparing resistivity images and water content images for different dates and creating a time-serial animated presentation. 

2. Tab "Select Dates":

   Users can search for a subset of images of interest within the generated water image set and resistivity image set. And then clients could manually select them by corresponding dates. The program will convert this set of images, normalized based on legend value ranges, into an animated sequence displayed in chronological order. 

3. Tab "Play Time-Serial Animation":

   Users can simply watch this animation. 

4. Tab "Save Time-Serial Animation": 

   there is also an option tab for saving the animation for potential needs such as quick access and playback during academic presentations or teaching.

---

During the week 8 meeting with client, Prof. Sally Thompson presented additional requirements:

1. The program currently generates rainbow-colored images based on a full-color spectrum. The client expressed concern that such images might overwhelm the audience with unnecessary information during academic presentations. The client wishes to add a feature at this visualization stage of the program that allows users to choose different "color schemes" (as shown in the graph below) and supports saving and animating images with different color schemes.

   <img src="/Users/apple/Library/Application Support/typora-user-images/Screenshot 2023-09-22 at 1.13.14 pm.png" alt="Screenshot 2023-09-22 at 1.13.14 pm" style="zoom:20%;" />

   ​						Graph1. Sample of Color Schemes

2. To create animations for time-series images, we standardized the legend value ranges based on Jianguo Liu's suggestion (the PhD student of clients), ensuring that each frame of the animation uses the same legend range for either water content or resistivity changes. However, Prof. Sally Thompson makes a new requirement:

   1.  Sometimes, the client only needs to quickly compare multiple images of interest, focusing on key data points in each image. Specifically, the client is interested in the top 3 or top 5 modes among the thousands of data points. The client wants the legend value range segments corresponding to these modes to be enlarged, while other value range segments are scaled down as necessary. 
   2. In other words, the client requires both standardized legend value range animations and non-standardized animations with legend value ranges automatically customized.


These new client requirements will be implemented in the third phase.