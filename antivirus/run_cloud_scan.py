from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui  
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

import os
import requests

def run_cloud_scan(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File for Cloud Scan", "", "All Files (*)", options=options)

        if file_path:
            self.log(f"Running Cloud Scan on: {file_path}\n")
            self.status("Uploading file to Cloud Scanner...\n")

            api_key = "6aabdf6fb02bc2dccdab39f086f2ccd2319080ed65807aafb2915d8022c69f08"
            scan_id = self.upload_to_virustotal(file_path, api_key)

            if scan_id:
                self.status("File uploaded. Checking scan status...\n")
                scan_results = self.check_scan_status(scan_id, api_key)

                if scan_results:
                    self.log("Cloud scan results:\n")
                    self.status_text_edit.insertPlainText("Cloud Scan Results:\n")
                    for engine, result in scan_results.items():
                        result_text = f"Engine: {engine}, Result: {result['detected']}, Version: {result['version']}, Update: {result['update']}\n"
                        self.log(result_text)
                        self.status_text_edit.insertPlainText(result_text)
                else:
                    self.log("Cloud scan failed or results not available.\n")
                    self.status("Cloud scan failed or results not available.")
            else:
                self.log("Cloud scan upload failed.\n")
                self.status("Cloud scan upload failed.")
        else:
            self.log("Cloud Scan canceled by user.\n")


def upload_to_virustotal(self, file_path, api_key):
        url = "https://www.virustotal.com/vtapi/v2/file/scan"
        params = {"apikey": api_key}
        
        with open(file_path, "rb") as file:
            files = {"file": (os.path.basename(file_path), file)}
            response = requests.post(url, files=files, params=params)
            if response.status_code == 200:
                return response.json()["scan_id"]
            return None

def check_scan_status(self, scan_id, api_key):
        url = f"https://www.virustotal.com/vtapi/v2/file/report"
        params = {"apikey": api_key, "resource": scan_id}
        
        response = requests.get(url, params=params)
        if response.status_code == 200:
            scan_results = response.json()
            if scan_results["response_code"] == 1:
                return scan_results["scans"]
        return None
