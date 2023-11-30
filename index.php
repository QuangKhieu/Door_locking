<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css" integrity="sha512-z3gLpd7yknf1YoNbCzqRKc4qyor8gaKU1qmn+CShxbuBusANI9QpRohGBreCFkKxLhei6S9CQXFEbbKuqLg0DA==" crossorigin="anonymous" referrerpolicy="no-referrer" />

  <link rel="stylesheet" href="assets/bootstrap/bootstrap.min.css">

  <link rel="stylesheet" href="assets/css/base.css">
  <link rel="stylesheet" href="assets/css/style.css">

  <title>FingerPrint Server | Khoá cửa vân tay</title>
</head>

<body>
  <header class="header">

    <div class="row">
      <div class="col-xl-12">
        <div class="inner-title">Don't See What You're Looking For? Join Our Talent Community! 🎉🎉🎉</div>
      </div>
    </div>

    <div class="container">
      <div class=" inner-wrap row">
        <div class="inner-logo col-xl-4">
          <span class="inner-icon"><i class="fa-solid fa-fingerprint"></i></span>
          <span class="inner-name">Fingerprint</span>
        </div>

        <div class="inner-team col-xl-4">
          <img src="assets/images/logouet.png" alt="">
          <a href="#" class="inner-name">Group 14</a>
        </div>

        <div class="inner-box-login col-xl-2">
          <a href="#" type="button" class="inner-login button" data-toggle="modal" data-target="#exampleModal">Login</a>
          <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered">

              <div class="modal-content">
                <div class="modal-header">
                  <div class="modal-title" id="exampleModalLabel">
                    <div class="inner-temp">
                      <div class="inner-logo">
                        <span class="inner-icon"><i class="fa-solid fa-fingerprint"></i></span>
                        <span class="inner-name">Fingerprint</span>
                      </div>
                      <div class="inner-team">
                        <img src="assets/images/logouet.png" alt="">
                        <a href="#" class="inner-name">Group 14</a>
                      </div>
                    </div>

                  </div>
                  <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                  </button>
                </div>
                <div class="modal-body">

                  <?php
                  $errors = [];
                  $formSubmitted = false;

                  if ($_SERVER["REQUEST_METHOD"] == "POST") {
                    $formSubmitted = true;

                    $username = isset($_POST['username']) ? $_POST['username'] : '';
                    $password = isset($_POST['password']) ? $_POST['password'] : '';

                    if (empty($username)) {
                      $errors['username']['required'] = 'This attribute is required';
                    } else {
                      if (strlen($username) < 5) {
                        $errors['username']['min_length'] = 'Not enough';
                      }
                    }

                    if (empty($password)) {
                      $errors['password']['required'] = 'This attribute is required';
                    }

                    if (empty($username) || empty($password)) {
                      $errors['login']['required'] = 'Username and password are required';
                    } else {
                      if ($username === 'admin' && $password === 'group14') {
                        // Nếu username và password đúng, chuyển hướng người dùng đến trang khác
                        header("Location: admin_page.php");
                        exit;
                      } else {
                        $errors['login']['invalid'] = 'Invalid username or password';
                      }
                    }
                    unset($username);
                    unset($password);
                    unset($errors);
                  }
                  ?>

                  <form class="inner-form" method="post" action="">
                    <div class="form-group">
                      <label for="exampleInputEmail1">Username</label>
                      <input type="text" name="username" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Tên đăng nhập *">
                      <div class="text-danger" id="username-error">
                        <?php
                        if ($formSubmitted) {
                          echo !empty($errors['username']['required']) ? $errors['username']['required'] : '';
                          echo !empty($errors['username']['min_length']) ? $errors['username']['min_length'] : '';
                        }
                        ?>
                      </div>
                    </div>
                    <div class="form-group">
                      <label for="exampleInputPassword1">Password</label>
                      <input type="password" name="password" class="form-control" id="exampleInputPassword1" placeholder="Mật khẩu *">
                      <div class="text-danger" id="password-error">
                        <?php
                        if ($formSubmitted) {
                          echo !empty($errors['password']['required']) ? $errors['password']['required'] : '';
                          echo !empty($errors['login']['invalid']) ? $errors['login']['invalid'] : '';
                        }
                        ?>
                      </div>
                    </div>
                    <div class="forget-pass"><a href="#">Bạn quên mật khẩu? Kệ bạn</a></div>
                    <button type="button" class="btn btn-primary button-second" onclick="validateForm()">Đăng nhập</button>
                  </form>

                  <script>
                    function validateForm() {
                      const username = document.getElementsByName("username")[0].value;
                      const password = document.getElementsByName("password")[0].value;
                      const usernameError = document.getElementById("username-error");
                      const passwordError = document.getElementById("password-error");

                      usernameError.innerHTML = ''; // Xóa thông báo lỗi cũ
                      passwordError.innerHTML = ''; // Xóa thông báo lỗi cũ

                      if (username.trim() === "") {
                        usernameError.innerHTML = "This attribute is required";
                        return;
                      } else if (username.length < 5) {
                        usernameError.innerHTML = "Not enough";
                        return;
                      }

                      if (password.trim() === "") {
                        passwordError.innerHTML = "This attribute is required";
                        return;
                      }

                      // Kiểm tra thông tin đăng nhập
                      if (username === 'admin' && password === 'group14') {
                        // Nếu thông tin đúng, chuyển hướng người dùng đến trang khác
                        window.location.href = "admin_page.php";
                      } else {
                        passwordError.innerHTML = "Invalid username or password";
                      }
                    }
                  </script>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-xl-2">
          <a href="https://www.instagram.com/trithanh_on_g/" class="inner-about button-second" target="_blank">About us</a>
        </div>
      </div>
    </div>
    </div>
  </header>

  <div class="section-one">
    <div class="container">
      <div class="row">
        <div class="inner-main col-xl-6">
          <div class="inner-info">
            <h1 class="inner-title">Identify visitors you can trust. And those you can't.</h1>
            <div class="inner-desc">Over 6,000 companies trust Fingerprint's highly accurate, real-time device
              intelligence to determine the true intentions of every user — even if they're anonymous.</div>
            <div class="inner-social">
              <a href="#" class="button-second">
                <i class="fa-brands fa-facebook-f"></i>
              </a>
              <a href="#" class="button-second">
                <i class="fa-brands fa-twitter"></i>
              </a>
              <a href="#" class="button-second">
                <i class="fa-brands fa-instagram"></i>
              </a>
            </div>
          </div>
        </div>
        <div class="col-xl-6 text-center">
          <img src="assets/images/fingerprint.svg" class="filter-green" alt="">
        </div>
      </div>
    </div>
  </div>




  <script src="assets/bootstrap/jquery.slim.min.js"></script>
  <script src="assets/bootstrap/bootstrap.bundle.min.js"></script>

</body>

</html>