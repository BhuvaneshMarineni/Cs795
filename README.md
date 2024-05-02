# Cs795
CS795
## Personalized Screen Reader Speed Adjustments & Insights

## Team Members:
1) Bhuvanesh Marineni
2) Siva Naga Durga Janakala
3) Harshit Koncherla
4) Deeven Kumar Menda
   
## Project Statement:
The primary objective of this project is to develop a personalized screen reader speed adjustment system that can adapt to individual user preferences and provide insights into their reading behavior and log this data for continuous improvement. The primary objective of this project is to develop a personalized screen reader speed adjustment system tailored to individual user preferences. This system aims to enhance the reading experience for users with visual impairments by dynamically adapting the reading speed based on user interactions and collecting data on reading behavior.
## Architecture:
![image](https://github.com/BhuvaneshMarineni/Cs795/assets/122952070/54773dab-bb75-4fa1-a4b1-44bd642227fe)
## Implementation:
# Logger.py
The Logger.py file is responsible for logging the screen reader data and print that in the console.

Steps for using Logger.py:

Step 1: Download Logger.py from GitHub, Go to Hidden icons in the taskbar and right click on the NVDA symbol. Select preferences → settings.

![image](https://github.com/BhuvaneshMarineni/Cs795/assets/122952070/b9af12d0-eb7b-407e-b517-e24d980d906e)


Step 2:  Now select Advanced, Click on checkbox “I understand that changing these settings may cause NVDA to function incorrectly” and click on checkbox “Enable loading custom code from Developer Scratchpad” and select open developer scratchpad directory.

![image](https://github.com/BhuvaneshMarineni/Cs795/assets/122952070/22242fd7-466a-49de-a315-30df50b49875)


Step 3: Upload the logger file in global plugins.

![image](https://github.com/BhuvaneshMarineni/Cs795/assets/122952070/0677e3ef-0a52-4ab5-83b2-cee7a92d5a32)


Step 4 : After uploading select tools → Reload plugins.

![image](https://github.com/BhuvaneshMarineni/Cs795/assets/122952070/2be23fab-ff83-450b-b218-297ff6b86984)


Step 5 : To view the logs, select tools → view log

## Automatic Speed Adjustment
# Adjustment.py

Step 1: Download Adjustment.py from GitHub, Go to Hidden icons in the taskbar and right click on the NVDA symbol. Select preferences → settings.

Step 2:  Now select Advanced, Click on checkbox “I understand that changing these settings may cause NVDA to function incorrectly” and click on checkbox “Enable loading custom code from Developer Scratchpad” and select open developer scratchpad directory.

Step 3: Upload the lAdjustment.py file in global plugins.

Step 4 : After uploading select tools → Reload plugins.

The NVDA will proceed with the speed adjustments.
