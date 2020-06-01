# Attendance-Marker-App
An application that automatically marks attendance on Excel spreadsheets by parsing Chat text files generated during online lectures on conferencing platforms like Zoom, Cisco Webex Meet, etc.

(This version is developed considering how lectures operate in MIT WPU.)

### To run the application on your system, Download the Released executable and install the setup.
Install on desired path, do not change the folder structure.
Run interface.exe

#### Input:
Chat file (text), Classlist spread sheet (excel)

The excel file must use the following table structure:
(Note: Column sequence is vital, names can differ)

|Sr.No.|Roll No.|PRN/ Unique Id|Candidate Name|
|------|--------|--------------|--------------|
|      |        |              |              |
|      |        |              |              |
|      |        |              |              |

#### Output:
A new column will be appended on to existing table on every run. It corresponds to new lecture of the same class.

#### GUI:
