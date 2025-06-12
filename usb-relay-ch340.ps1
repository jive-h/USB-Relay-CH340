# [System.IO.Ports.SerialPort]::getportnames()

$bytesOn = [byte[]](0xA0, 0x01, 0x01, 0xA2)
$bytesOff = [byte[]](0xA0, 0x01, 0x00, 0xA1)

$port= new-Object System.IO.Ports.SerialPort COM3,9600,None,8,one
$port.open()
$port.write($bytesOn, 0, $bytesOn.Length)
Start-Sleep -Milliseconds 100
$port.write($bytesOff, 0, $bytesOff.Length)
$port.close()
