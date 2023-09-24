## By Smukx
## https://github.com/Whitecat18


import os
import hashlib
import time
import argparse
import logging
from datetime import datetime

class ScheduledScan:
    def __init__(self, scan_interval_minutes, directories_to_scan):
        self.scan_interval = scan_interval_minutes * 60
        self.directories_to_scan = directories_to_scan

    def calculate_hash(self, file_path):
        try:
            with open(file_path, "rb") as file:
                data = file.read()
                md5_hash = hashlib.md5(data).hexdigest()
                sha256_hash = hashlib.sha256(data).hexdigest()
                return md5_hash, sha256_hash
        except Exception as e:
            return None, None

    def scan_directory_recursive(self, directory_path, signature_hashes_md5, signature_hashes_sha256, virus_extensions):
        detected_malicious_files = []

        for root, _, files in os.walk(directory_path):
            for filename in files:
                file_path = os.path.join(root, filename)
                _, file_extension = os.path.splitext(filename)
                checksum_md5, checksum_sha256 = self.calculate_hash(file_path)
                if checksum_md5 in signature_hashes_md5 or checksum_sha256 in signature_hashes_sha256 or file_extension[1:] in virus_extensions:
                    detected_malicious_files.append((file_path, checksum_md5, checksum_sha256, file_extension))

        return detected_malicious_files

    def run_partition_full_scan(self, log_file_path):
        logging.basicConfig(filename=log_file_path, level=logging.INFO, format="%(asctime)s - %(levelname)s: %(message)s")

        logging.info("Scheduled scan started.")
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logging.info(f"Scanned Date: {current_time}")

        no_malicious_files = True

        for directory_path in self.directories_to_scan:
            logging.info(f"Running Full Scan on: {directory_path}")
            logging.info("Scanning for malicious files...")

            # EXT_NEW
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            logging.info(f"Current Scanning Time: {current_time}")

            signature_hashes_md5 = set()
            signature_hashes_sha256 = set()
            with open("hashes/md5_hashes.txt", "r") as hash_file_md5, open("hashes/sha256_hashes.txt", "r") as hash_file_sha256:
                for line_md5, line_sha256 in zip(hash_file_md5, hash_file_sha256):
                    signature_hashes_md5.add(line_md5.strip())
                    signature_hashes_sha256.add(line_sha256.strip())

            virus_extensions = set()
            with open("hashes/virus-extensions.txt", "r") as ext_file:
                for line in ext_file:
                    virus_extensions.add(line.strip())

            detected_malicious_files = self.scan_directory_recursive(directory_path, signature_hashes_md5, signature_hashes_sha256, virus_extensions)

            if detected_malicious_files:
                no_malicious_files = False
                logging.info("Detected malicious files:")
                for file_info in detected_malicious_files:
                    file_path, checksum_md5, checksum_sha256, extension = file_info
                    logging.info(f"File: {file_path}, Extension: {extension}")
                    if self.confirm_and_remove_file(file_path, os.path.basename(file_path)):
                        logging.info(f"Malicious file {file_path} removed.")

        if no_malicious_files:
            logging.info("No malicious files found.")

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logging.info(f"Scan Completed at {current_time}")

    def confirm_and_remove_file(self, file_path, filename):
        # Check if the file is malicious
        is_malicious = True 

        if is_malicious:
            try:
                os.remove(file_path) 
                return True
            except Exception as e:
                logging.error(f"Failed to remove malicious file: {file_path} - {str(e)}")
                return False
        return False

    def start_scheduled_scan(self):
        try:
            while True:
                self.run_partition_full_scan("logfiles/schedule-log.txt")
                time.sleep(self.scan_interval)
        except KeyboardInterrupt:
            logging.info("Scheduled scan stopped by the user.")

def main():
    
    scan_interval_minutes = 60
    parser = argparse.ArgumentParser(description="Schedule Scan Program")
    parser.add_argument("scan_interval", type=int, help="Scan interval in minutes")
    args = parser.parse_args()

    directories_to_scan = [
        os.path.join(os.environ['USERPROFILE'], 'AppData', 'Local', 'Temp'),
    #    os.path.join(os.environ['USERPROFILE'], 'Desktop'),
        os.path.join(os.environ['USERPROFILE'], 'Pictures'),
        os.path.join(os.environ['USERPROFILE'], 'Music'),
    #    os.path.join(os.environ['USERPROFILE'], 'Downloads'),
    ]

    scheduled_scan = ScheduledScan(scan_interval_minutes, directories_to_scan)
    scheduled_scan.start_scheduled_scan()


if __name__ == '__main__':
    main()
