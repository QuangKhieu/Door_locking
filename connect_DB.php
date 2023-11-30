// thông tin kết nối
const _HOST = 'localhost';
const _DB = 'fingerprint';
const _USER = 'root';
const _PASS = '';

try{
  if(class_exists('PDO')){

    $dsn = 'mysql:dbname='._DB.';host='._HOST;

    $options = [
      PDO::MYSQL_ATTR_INIT_COMMAND => 'SET NAMES utf8', // Set utf8 (tieng viet)
      PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION // Tao thong bao ra ngoai le khi gap loi
    ];

    $con = new PDO($dsn,_USER,_PASS,$options);
    var_dump($con);
  }
}catch(Exception $exception){
  echo '<div style="color:red; padding: 5px 15px; border: 1px solid red;">';
  echo $exception -> getMessage().'<br>';
  echo '</div>';
  die();
}