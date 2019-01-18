# Device Fingerprinting for Access Control over a Campus and Isolated Network
Device Fingerprinting (DFP) is a technique to identify devices using Inter-Arrival Time (IAT) of packets and without using any other unique identifier. Our experiments include generating graphs of IATs of 100 packets and using Convolutional Neural Network on the generated graphs to identify a device. We did two experiments where the first experiment was on Raspberri Pi and other experiment was on crawdad dataset.

## First Experiment: Raspberry Pi
We developed a packet sniffer application to capture IAT of packets. Packet sniffer application was installed on Raspberry pi that was configured to work as router. We connceted two devices iPad4 and iPhone 7 Plus to the router and created IAT graphs for these two devices. Our scheme based on Convolution Neural Network (CNN) was able to identify the devices with accuracy of 86.7\%.

## Second Experiment: Crawdad Dataset
In the second experiment, we tested the scheme with [Crawdad dataset](https://crawdad.org/gatech/fingerprinting/20140609). The proposed scheme achieved accuracy of 95.5\% for [GTID](https://crawdad.org/gatech/fingerprinting/20140609) that is 3\% higher than previous scheme \cite{gatech-fingerprinting-20140609} for 14 devices and 5 device types on isolated network while 40\% efficient in time to test a device fingerprint.

In the second experiment, we divided the dataset into three separate datasets

### D1-IsolatedNetworkPassiveDFP


### D21-CampusNetworkActiveDFP


### D22-CampusNetworkPassiveDFP



## Feedback
Please submit your feedback to [Dr. Nagender Aneja](http://expert.ubd.edu.bn/nagender.aneja). Please write an email (nagender.aneja@ubd.edu.bn) if you are interested to impement the model in a mobile app or web app. We welcome people and organization who can provide more data on plants from different countries to join this project. 

## Project Members
*  [Dr. Sandhya Aneja](http://expert.ubd.edu.bn/sandhya.aneja), sandhya.aneja@ubd.edu.bn
*  [Dr. Nagender Aneja](http://expert.ubd.edu.bn/nagender.aneja), nagender.aneja@ubd.edu.bn
*  Md Shohidul Islam, 14b6057@ubd.edu.bn
*  [Prof. Bharat Bhargava](https://www.cs.purdue.edu/homes/bb/), bb@cs.purdue.edu
