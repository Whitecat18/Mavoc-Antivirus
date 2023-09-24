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


## Types of Scans

**There are 6 Types of Scans** 

- Quick Scan 
- Schedule Scan 
- Full Scan
- Network Blocker
- Cloud Firm Scan
- Clean System


<details>
  <summary><h3>Quick Scan</h3></summary>
  <p>There are 2 types of Scans, Quick Recursive and Non-Recursive Scan.</p>
  <p>Quick Non-Recursive scan will simply look for common places where malware, payloads, etc., may be stored.</p>
  <p>Quick Recursive Scan will scan all files recursively in the common path, even inside temporary files and folders within the common directory path.</p>
</details>

<details>
  <summary><h3>Schedule Scan</h3></summary>
  <p>To initiate a Schedule Scan with Mavoc Antivirus, you need to start the Mavoc Antivirus application.</p>
  <p>Schedule Scan will scan the common path every 1 minute by default, but you can adjust the timing in the mavoc.ps1 script.</p>
</details>

<details>
  <summary><h3>Full Scan</h3></summary>
  <p>There are Two Types of Scans: Full Scan and Partition Scan.</p>
  <p>Full Scan will comprehensively scan your entire system, which may take hours, so please be patient when using this option.</p>
  <p>Partition Scan allows you to select a particular partition or folder to scan files recursively, making it the fastest scanning method.</p>
</details>

<details>
  <summary><h3>Network Blocker</h3></summary>
  <p>Network Blocker contains a list of more than 42,000 malicious sites. When enabled, it blocks access to these sites. You can reset it to the default settings by choosing to disable network blocker.</p>
</details>

<details>
  <summary><h3>Cloud Firm Scan</h3></summary>
  <p>This scan utilizes the VIRUS TOTAL API to scan a specific file.</p>
  <p>Important Note: If you are using the free VIRUS TOTAL API, limit your scans to a minimum of 3 files per minute.</p>
</details>

<details>
  <summary><h3>Clean System</h3></summary>
  <p>Clean System is used to remove unwanted files from common directory paths, such as temporary and registry paths. It automatically deletes these files to optimize system performance and enhance security.</p>
</details>



## Methods

