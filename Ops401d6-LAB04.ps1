# SetPasswordComplexity.ps1

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
