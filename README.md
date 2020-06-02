# Attendance-Marker-App
An application that automatically marks attendance on Excel spreadsheets by parsing Chat text files generated during online lectures on conferencing platforms like Zoom, Cisco Webex Meet, etc.

(This version is developed considering how lectures operate in MIT WPU.)

Download and run source code if you've python already.
Else,
## To run the application on any system, Download the Released executable and install the setup.
Install on desired path, do not change the folder structure.
Run interface.exe

### Input:
Chat file (text), Classlist spread sheet (excel)

The excel file must use the following table structure:
(Note: Column sequence is vital, names can differ)

|Sr.No.|Roll No.|PRN/ Unique Id|Candidate Name|
|------|--------|--------------|--------------|
|      |        |              |              |
|      |        |              |              |
|      |        |              |              |

### Output:
A new column will be appended on to existing table on every run. It corresponds to new lecture of the same class.
The total number of candidates present in a lecture is appended in the last row.

### GUI:
![home](https://github.com/Priya-SB/Attendance-Marker-App/blob/master/GUI/Screenshot%20(207).png)
------
##### Info Messages

![chatdone](https://github.com/Priya-SB/Attendance-Marker-App/blob/master/GUI/Screenshot%20(211).png)
![classdone](https://github.com/Priya-SB/Attendance-Marker-App/blob/master/GUI/Screenshot%20(210).png)
![done](https://github.com/Priya-SB/Attendance-Marker-App/blob/master/GUI/Screenshot%20(213).png)
------
##### Error Messages

![err1](https://github.com/Priya-SB/Attendance-Marker-App/blob/master/GUI/Screenshot%20(208).png)
![err2](https://github.com/Priya-SB/Attendance-Marker-App/blob/master/GUI/Screenshot%20(209).png)
![err3](https://github.com/Priya-SB/Attendance-Marker-App/blob/master/GUI/Screenshot%20(212).png)
------
