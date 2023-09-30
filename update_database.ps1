# Powershell script to download the lastes hashes from malware bazzar. 
# Mavoc-Antivirus : https://github.com/Whitecat18/Mavoc-Antivirus
$md5Url = "https://bazaar.abuse.ch/export/txt/md5/recent/"
$sha256Url = "https://bazaar.abuse.ch/export/txt/sha256/recent/"
$md5FileName = "hashes/md5_hashes.txt"
$sha256FileName = "hashes/sha256_hashes.txt"
Invoke-WebRequest -Uri $md5Url -OutFile $md5FileName
Invoke-WebRequest -Uri $sha256Url -OutFile $sha256FileName

if (Test-Path $md5FileName -and Test-Path $sha256FileName) {
    Write-Host "Files downloaded successfully."
} else {
    Write-Host "Failed to download files."
}
