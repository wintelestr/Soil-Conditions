# Performance Testing for Soil Conditions GUI

## Objective

The objective of this performance test is to assess the memory usage and performance of the Soil Conditions GUI.

**Tools Required:** Python & memory_profiler library

**Steps:**

**1. Installation of memory_profiler:**
Begin by installing the memory_profiler library using the following pip command:
						`pip install memory_profiler`

**2. Run Memory Profiling:** 
Execute the following command to start memory profiling of the GUI application:
`python -m memory_profiler final_demo.py`

**3. Data Collection:**
While the GUI application is running, memory_profiler will collect data on memory usage over time.

**4. Generate Memory Profile Data:**
After running the GUI, stop it, and execute the following command to generate memory profile data:
`mprof run final_demo.py`

**5. Generate Memory Usage Graph:**
To visualize memory usage data, use the following command:
						`mprof plot`
![image](https://github.com/wintelestr/Soil-Conditions/assets/133135894/36180949-d225-40f7-9bce-dbec5f5d32f8)


**7. Analysis:**
The generated graph will provide insights into memory usage patterns during the execution of the Soil Conditions GUI. The analysis of this data will help identify memory leaks or areas where memory optimization may be required to enhance the application's performance.

In the above results figure, it is evident that the software exhibits varying memory usage patterns during different stages of operation. 

- Upon launching the GUI, the software consumes just over 100MB of memory.
- When importing a day's worth of data, memory usage increases to 140MB.
- During the data cleaning process, memory usage rises to 160MB.
- Subsequent operations, such as domain determination and grid partitioning, result in memory consumption reaching 180MB.
- The most memory-intensive phase is the inversion model calculation, where memory usage peaks at 460MB.
- Once the inversion model calculation is complete, memory usage decreases to 320MB.
- Further operations, including water content conversion calculations and final result visualization, gradually increase memory usage from 320MB to 410MB.

It is noteworthy that the GUI's highest memory consumption occurs during the inversion calculation, but it remains within the range of 500MB. Overall, the software's memory footprint appears to be reasonable. However, for future work, optimizing the inversion model phase could be explored to reduce memory usage, enhancing the software's overall efficiency.

**8. Conclusion:**
By following these steps, you can assess the memory performance of the Soil Conditions GUI, ensuring it runs efficiently and without memory-related issues. This data is valuable for optimizing and fine-tuning the application for a smoother user experience.
