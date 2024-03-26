# Cs795
CS795
## Personalized Screen Reader Speed Adjustments & Insights

## Team Members:
1) Bhuvanesh Marineni
2) Siva Naga Durga Janakala
3) Lokesh Reddy Sonti
4) Deeven Kumar Menda
   
## Project Statement:
The project seeks to revolutionize the use of screen readers for individuals with visual impairments by employing advanced machine learning techniques to understand and adapt to user preferences in real-time. At its core, the initiative focuses on capturing detailed user interaction data with screen readers, including speed adjustments, navigation patterns, and content engagement times. This data will be meticulously logged, including specific metrics like timestamps and speed changes, to build a comprehensive dataset.
Using this dataset, the project aims to train machine learning models to identify patterns in how users interact with screen readers, particularly focusing on their preferences for reading speeds in different contexts. The ultimate goal is to automate the adjustment of the screen reader’s speed settings based on these identified patterns, making the technology more responsive and personalized to the user’s needs. This would mark a significant step forward in making screen readers more intuitive and effective, removing barriers to digital content access for people with visual impairments.

## Literature Survey:

We have gone through different screen readers that are useful for the blind people. Out of them the three major screen readers we found were the NVDA screen reader which is only compatible with windows, Voice Over which is compatible with MacOS and Windows narrator which is only compatible with windows os.
For that purpose we have surveyed all these screen readers and the way of their operation.
Below are some of the research papers we have cited.

## 1.Design of An Electronic Narrator on Assistant Robot for Blind People 
https://www.matec-conferences.org/articles/matecconf/pdf/2016/05/matecconf_iccma2016_03013.pdf

The paper presents the development of an electronic narrator for assisting visually impaired individuals by converting printed text into speech using a Raspberry Pi, a webcam for image capture, and integrated OCR and TTS libraries. Testing showed improved text recognition with better lighting and preprocessing adjustments. While effective in controlled conditions, the system requires further development for automatic adaptability and broader practical use. The study highlights the potential of such technology to make printed materials more accessible to the visually impaired.

## 2.Understanding the Usages, Lifecycle, and Opportunities of Screen Readers’ Plugins
https://dl.acm.org/doi/full/10.1145/3582697

The article explores the usage, development, and challenges associated with screen reader plugins, which are small code pieces enhancing screen reader capabilities for blind users. Through interviews with 14 blind users and analysis of 2,000 online posts, the study uncovers various reasons why users rely on plugins, such as improving usability and accessing partially accessible applications. It highlights the ease of installation, but challenges in finding and uninstalling plugins, often leading to security risks. The technical complexity of plugin development limits their availability, and most plugins become obsolete due to lack of updates and financial incentives. The study emphasizes the importance of community collaboration among blind users, online forums, and developers in plugin creation, suggesting the need for a centralized repository and raising awareness about plugin benefits and risks. The findings propose embracing a community-driven approach to combat accessibility issues and foster collaboration between blind users and developers in the field of Human-Computer Interaction (HCI).

## 3.Screen Reader Voices: Effects of Pauses and Voice Changes on Comprehension
https://journals.sagepub.com/doi/epdf/10.1177/1071181322661291

The paper "Screen Reader Voices: Effects of Pauses and Voice Changes on Comprehension" by Cecelia A. Henderson and Yingchen He explores how modifications in text-to-speech (TTS) delivery, specifically pauses and voice pitch changes, impact the comprehension and retention of information among both sighted and visually impaired listeners. Through experiments with audio recordings of passages, the study examines whether such alterations can improve the recognition of structure and key details in spoken text. Preliminary results suggest potential benefits of adding pauses, but conclusive evidence requires more data. This research contributes to the ongoing discussion on optimizing TTS technology for educational and assistive purposes, highlighting the need for further investigation into auditory information processing and learning strategies.

## 4.Python Programming Education with Semantics-oriented Screen Reading for K-12 Students with Vision Impairments
https://dl.acm.org/doi/pdf/10.1145/3626253.3635494

The paper introduces JupyterVox, a semantics-oriented screen reader designed to improve Python programming education for K-12 students with vision impairments. It addresses the limitations of conventional screen readers in interpreting programming code, which often misrepresent or complicate the understanding of code syntax and semantics. By leveraging compiler techniques for lexical and syntax analyses, JupyterVox interprets and vocalizes Python code based on its meaning, facilitating better comprehension and navigation through code. Initial evaluations suggest JupyterVox significantly enhances the accuracy of understanding programming statements, indicating its potential to boost independent coding skills among visually impaired students.

## Proposed Approach:
NVDA Installation and Functionality Exploration: This is the initial stage where the NVDA screen reader is installed and its features are explored to understand how it operates and how users interact with it.
## Data Collection: 
In this step, there are two main activities:
Gather User History Data: Collecting historical data on how users have previously interacted with the screen reader, including their speed preferences.
Collect Data from Webpage Sections: Gathering data from different sections of web pages that the users visit to understand if there's a pattern in speed preference depending on the type of content.
## Machine/Deep Learning Model:
Analyze Trends in User History Data: Utilizing machine learning or deep learning algorithms to identify patterns and trends in the collected user history data.
## Model Training:
Use Data to Train the Machine Learning Model: The identified patterns and trends are used to train the machine learning model, aiming to predict the optimal speed settings for different contexts.Automatic Speed Adjustment:
## Implement Functionality to Adjust Speed: 
Based on the predictions of the trained model, the functionality to automatically adjust the reading speed of the screen reader is implemented.
## Process User Interface Integration (UI):
The automatic speed adjustment feature is integrated into the screen reader's user interface, making the functionality accessible and seamless for the end-user.
For the Data Collection We are building a chrome extension that  can monitor and log user actions such as scroll events, clicks, and time spent on different parts of a webpage. If you're starting from scratch, you would indeed need to build or modify an existing Chrome extension to collect the specific data you're interested in.

## Proposed Architecture

## Overall Project Status
We installed NVDA (NonVisual Desktop Access), a screen reader designed for individuals with visual impairments and navigated to the NVDA website, downloaded the latest version, and successfully installed the software, ensuring its proper functionality. Through exploration, we've familiarized with NVDA's fundamental features, including navigating the Windows interface, reading text in various applications, and customizing preferences. Particularly, we’ve focused on understanding the speed adjustment commands, discovering that the default keys for altering speech rate are Ctrl + Alt + NVDA + Minus (to decrease speed) and Ctrl + Alt + NVDA + Plus (to increase speed). This allowed me to fine-tune the screen reader's speed globally or within specific applications. Additionally, we verified the real-time impact of these adjustments, gaining insights into the user-friendly interface and effective auditory feedback provided by NVDA. This initial exploration sets the foundation for our goal of implementing personalized automatic narrating speed adjustments based on user history data and machine learning models. By going through the plugins paper we have mentioned above we were able to get a clear understanding of how installing additional plugins for the NVDA screen reader facilitates the process of automating the speed adjustments.
But we had encountered some issues running the NVDA programmatically on the local system. We had set up the visual studio environment for running the NVDA but we are still encountering some issues and we had some difficulties in understanding the huge codebase. 

One other approach we tried is to capture the data of NVDA from a chrome extension we have built. The issue we faced is that the extension we built is solely based on the mouse pointer movement thereby capturing the data pointed and speed of the mouse pointer. But the NVDA has far more complex operations as it can be run by the keyboard commands and is independent of the mouse pointer. For capturing that data we had to intercept the backend of the NVDA and log the data. For that purpose we have gone through a lot of plugins which can be used with NVDA to log the data.The issue lies with running the NVDA programmatically. For the purpose of the time being we have gone through other softwares as well.
We have successfully tested the Voice Over which is an inbuilt screen reader for MacOS but we are unable to proceed with that as it is a commercial software and not available as an open source.
Then we started to run the Windows Narrator which is being run successfully on the windows system and narrating the sequences. We are able to log the data from the windows narrator. But this does n’t seem to be that effective when compared to the NVDA. Still we ran the windows narrator and were able to log some data.  



## Logger:
We have created a Chrome extension named "Screen Reader Logger," designed to monitor and record the activity of screen readers across various websites. Screen readers are crucial tools that assist visually impaired individuals by audibly reading aloud the content displayed on web pages. Understanding how screen readers interact with different websites can provide valuable insights into website accessibility and user behavior.

To accomplish this goal, the extension employs several key components. Firstly, the content.js script is responsible for detecting specific user actions, particularly when a space key is pressed, indicating the completion of a word being read by the screen reader. Upon detecting this event, the script retrieves the preceding word from the webpage and communicates this information to the background script, background.js.

Within the background script, incoming messages from the content script are processed. When the message indicates that a word has been read by the screen reader, the background script logs the word along with the current timestamp. This logged data is stored locally using Chrome's storage API, enabling the extension to accumulate a record of screen reader activity over time.

Meanwhile, the popup.js script manages the presentation of logged data to the user. Upon loading the extension's popup HTML (popup.html), the script retrieves the stored screen reader activity from local storage and dynamically generates a list of logged entries. Each entry typically consists of the word that was read, the timestamp indicating when it was read, and the URL of the webpage where the reading occurred.

In addition to it , a Python script named middlemen.py acts as an intermediary between the Chrome extension and the Narrator API. This script facilitates the integration of the extension with the Narrator API, allowing the extension to interact with the screen reader software and gather relevant data about the text being read.

During the development process of the "Screen Reader Logger" Chrome extension, we encountered challenges that prevented it from functioning as intended. Despite our efforts, we faced issues that may have been caused by compatibility problems with screen reader software or errors in our code. To address these challenges, we are committed to investigating the issues further, testing the extension in different environments.

The code is pushed to git and the repo is mentioned below.
https://github.com/BhuvaneshMarineni/Cs795  
