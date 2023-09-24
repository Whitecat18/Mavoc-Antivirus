<div align="center">
  <h1>Mavoc Antivirus</h1>
  <img width="160px" src="images/mavoc_antivirus_logo.png" />
  <br>

  <p><i> An opensource antivirus tool that scans system files and removes malware , Torjans , payloads, botnets, Ransomeweres(If not Active) ..etc 
  <br>created by<a href="https://twitter.com/Smukx07"> @Smukx</a> .</i></p>
  <br />
</div>


> ":warning: The tool is in its early developmental stage. The Heuristic method is still under development. It will come with a new feature in the next update.


## Working Methodology

<div align="center">
  
  <img src="images/Core.png" width=70% /><br/>
  <p>Flowchart for working methodology </p>
  <br>
  </div>
 
**Scans files using Hashing algorithm such as sha256 and md5 hashes .**

**Uses Heuristic Method to Scan 1st Set of Lines .**
  
**Scans files using malicious extensions over 900+ popular malicious extensions .**

**Network Protection Restricts Malicious websites over 42 Thousand websites .**


### Types of Scans

**There are 6 Types of Scans** 

- Quick Scan 
- Schedule Scan 
- Full Scan
- Network Blocker
- Cloud Firm Scan
- Clean System


###  Quick Scan 

There are 2 types of Scans , Quick Recursive and Non Recursive Scan.

Quick non Recursive scan will just look for the particular common places where they will be an chance of storing malware , payloads etc ... 

Quick Recursive Scan will scan all files recursively on the common path , even scans inside all the temp files, on every Folder in the common Directory Path .

### Schedule Scan

To start the Schedule Scan with mavoc antivirus  , you need to start the mavoc antivirus 
Schedule Scan will Scan all the common path for every 1 min . For Default i have given every 10 Mins to maintain Stability , you can even change the timing on the mavoc.ps1 .

### Full Scan 

**There are Two Types of Scans Full Scan and Partition Scan .**

Full Scan will completely Scans your whole Systems. It May Take Hours so be patient using the option

**Partition Scan**

In this scan , you can select an particular partition or an folder to scan the files recursively. 
The Fastest Method.

### Network Blocker

Network Blocker has more than 42K malicious sites , when you enable network blocker , it blocks all the malicious sites , you can reset it to default by choosing disable network blocker .

### Cloud Firm Scan

This scan uses VIRUS TOTAL API to Scan an particular file . 

**Remember :** ***IF YOU ARE USING FREE VIRUS TOTAL API , SCAN MINIMUM 3 FILES FOR AN MINUTE .*** **There are Two Types of Scans Full Scan and Partition Scan .**


### Clean System

Clean System is used to clean all unwanted files on the common directories paths such as temp path registry path etc .. and deletes the files automatically to make your system fast and to keep it secure .

### Working Methodology

