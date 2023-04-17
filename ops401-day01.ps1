# Set the timeout value in seconds (e.g., 900 seconds = 15 minutes)
$timeout = 300

# Enable the screensaver
Set-ItemProperty -Path "HKCU:\Control Panel\Desktop" -Name ScreenSaveActive -Value 1

# Set the screensaver timeout value
Set-ItemProperty -Path "HKCU:\Control Panel\Desktop" -Name ScreenSaveTimeOut -Value $timeout

# Enable password protection for the screensaver
Set-ItemProperty -Path "HKCU:\Control Panel\Desktop" -Name ScreenSaverIsSecure -Value 1

# Apply the changes
RUNDLL32.EXE user32.dll, UpdatePerUserSystemParameters
