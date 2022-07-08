param ( [string]$SourceExe, [string]$DestinationPath )

$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut($SourceExe)
$Shortcut.TargetPath = $DestinationPath
$Shortcut.Save()