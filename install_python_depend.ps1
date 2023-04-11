# Install Python
$url = "https://www.python.org/ftp/python/3.11.3/python-3.11.3-amd64.exe"
$output = "python-installer.exe"
Invoke-WebRequest -Uri $url -OutFile $output
Start-Process $output -ArgumentList '/quiet InstallAllUsers=1 PrependPath=1' -Wait
Remove-Item $output

# Update pip
python -m pip install --upgrade pip

# Install required Python libraries
python -m pip install pyautogui requests schedule psutil

# Print success message
Write-Host "Python and required libraries have been installed successfully."