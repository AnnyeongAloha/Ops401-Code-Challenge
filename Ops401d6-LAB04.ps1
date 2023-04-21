# SetPasswordComplexity.ps1 (Benchmark: 1.1.5)

# Define the security template file path
$securityTemplatePath = "ComplexPassword.inf"

# Create the security template file with the required settings
@"
[Version]
Signature="$CHICAGO$"

[Unicode]
Unicode=yes

[Password Policy]
ComplexityRequirements=1
"@ | Set-Content -Path $securityTemplatePath -Encoding Unicode

# Apply the security template
secedit /configure /db secedit.sdb /cfg $securityTemplatePath /areas SECURITYPOLICY /quiet

# Remove the temporary security template file
Remove-Item $securityTemplatePath

# Output success message
Write-Host "Password must meet complexity requirements has been set to enabled."


# Benchmark 18.4.3
# DisableSMBv1ClientDriver.ps1

# Define the registry key path
$regPath = "HKLM:\SYSTEM\CurrentControlSet\Services\mrxsmb10"

# Define the registry value name
$valueName = "Start"

# Define the value for disabling the SMB v1 client driver
$disableValue = 4

# Check if the registry key exists
if (Test-Path $regPath) {
    # Set the registry value to disable the SMB v1 client driver
    Set-ItemProperty -Path $regPath -Name $valueName -Value $disableValue

    # Output success message
    Write-Host "SMB v1 client driver has been set to Enabled: Disable driver."
} else {
    # Output error message
    Write-Host "The registry key for SMB v1 client driver could not be found. Ensure the system supports SMB v1."
}


# source:
# ChatGPT
