<?
error_reporting(0);
#file_put_contents("data.txt", print_r($_POST, true));
$name = isset($_POST['name']) ? substr($_POST['name'], 0, 30) : '';
$email = isset($_POST['email']) ? substr($_POST['email'], 0, 30) : '';
$subj = isset($_POST['subject']) ? substr($_POST['subject'], 0, 100) : '';
$department = isset($_POST['department']) ? strip_tags(trim($_POST['department'])) : '';
$text = isset($_POST['text']) ? strip_tags(substr($_POST['text'], 0, 1024)) : '';
$phone = isset($_POST['phone']) ? strip_tags(substr($_POST['phone'], 0, 100)) : '';

// начало записи в файл ящика отправителя
$file = 'email.csv';
$fp = fopen($file, "a+");
fwrite($fp, $email.';'."\n");
fclose($fp);
// конец записи в файл ящика отправителя

$mailto = 'a.nechausov@khai.edu, martin.bagniuk@gmail.com, andreevsm@gmail.com, nataliya.vz407@gmail.com, s.horelik@khai.edu, khaigismedia@gmail.com '; // ящик получателя
$mailfrom = 'khaigismedia@gmail.com'; // ящик "отправителя"

$success = false; // правильные ли данные

$subject = '';
$message = '';

if($name && $email && $text) {
	$subject = "Письмо с сайта KHAI-GIS: ".$subj; // тема письма
	$message =
	"Имя - $name\r\n".
	"Ящик - $email\r\n".
	"Категория - $department\r\n".
	"Сообщение - $text\r\n";
	$success = true;
}
if($phone) {
	$subject .= "Письмо с сайта KHAI-GIS: кто-то оставил номер телефона"; // тема письма
	$message .= "Позвоните по номеру $phone\r\n";
	$success = true;
}

if($success) {
	$eol = "\r\n";
	$boundary = md5(uniqid(time()));
	$header  = 'From: '.$mailfrom.$eol;
	$header .= 'Reply-To: '.$mailfrom.$eol;
	$header .= 'MIME-Version: 1.0'.$eol;
	$header .= 'Content-Type: multipart/mixed; boundary="'.$boundary.'"'.$eol;
	$header .= 'X-Mailer: PHP v'.phpversion().$eol;
	$body  = 'This is a multi-part message in MIME format.'.$eol.$eol;
	$body .= '--'.$boundary.$eol;
	$body .= 'Content-Type: text/plain; charset=UTF-8'.$eol;
	$body .= 'Content-Transfer-Encoding: 8bit'.$eol;
	$body .= $eol.stripslashes($message).$eol;
	mail($mailto, $subject, $body, $header);
	#file_put_contents("mail.txt", $subject."\r\n".$message);

	echo '{"success": true}';
} else
	echo '{"success": false}';
?>