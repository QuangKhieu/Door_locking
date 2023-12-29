<!DOCTYPE html>
<html lang="en">
<?php

?>

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css" integrity="sha512-z3gLpd7yknf1YoNbCzqRKc4qyor8gaKU1qmn+CShxbuBusANI9QpRohGBreCFkKxLhei6S9CQXFEbbKuqLg0DA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
  <link rel="stylesheet" href="assets/css/owl.carousel.min.css">

  <link rel="stylesheet" href="assets/bootstrap/bootstrap.min.css">

  <link rel="stylesheet" href="assets/css/base.css">
  <link rel="stylesheet" href="assets/css/style-admin.css">

  <title>Admin Page</title>
</head>

<body>
  <div class="header row">
    <div class="inner-box col-2">
      <div class="inner-logo">
        <img src="assets/images/logouet.png" alt="">
        <a href="#" class="inner-name">Group 14</a>
      </div>
      <div class="inner-menu">
        <div class="inner-dashboard">
          <span class="inner-icon"><i class="fa-solid fa-table-columns"></i></span>
          <a href="#" class="dashboard">Dashboard</a>
        </div>
      </div>
    </div>
    <div class="inner-body col-10">
      <div class="inner-section-one row">
        <div class="inner-name col-xl-10 col-8">Admin Page</div>
        <div class="inner-user col-2">
          <img src="assets/images/fourteen.png" alt="" style="background-color: #EFD161;">
          <span class="admin">Admin</span>
        </div>
      </div>
      <div class="inner-section-two row align-items-center">
        <p class="admin-page col-10">Admin Page</p>
        <div class="col-2">
          
        </div>
      </div>

      <style>
        table {
          border-collapse: collapse;
          width: 100%;
          margin-bottom: 25px;
        }

        th,
        td {
          border: 1px solid #dddddd;
          text-align: left;
          padding: 8px;
        }
      </style>
      <?php


      $servername = "localhost";
      $username = "root";
      $password = "";
      $dbname = "fingerprint";

      $conn = new mysqli($servername, $username, $password, $dbname);

      if ($conn->connect_error) { // nếu kết nối thất bại
        die("Kết nối đến MySQL thất bại: " . $conn->connect_error);
      }



      // Thực hiện thêm dữ liệu nếu có dữ liệu được gửi từ biểu mẫu
      if ($_SERVER["REQUEST_METHOD"] == "POST") {
        if (isset($_POST["add"])) {
          $hoTen = $_POST["hoTen"];
          $queQuan = $_POST["queQuan"];
          $question1 = $_POST["question1"];
          $answer1 = $_POST["answer1"];
          $question2 = $_POST["question2"];
          $answer2 = $_POST["answer2"];
          $question3 = $_POST["question3"];
          $answer3 = $_POST["answer3"];

          $sql = "INSERT INTO listfinger (HoTen, QueQuan, Question1, Answer1, Question2, Answer2, Question3, Answer3) VALUES ('$hoTen', '$queQuan', '$question1', '$answer1', '$question2', '$answer2', '$question3', '$answer3')";

          if ($conn->query($sql) === TRUE) {
            echo "Dữ liệu đã được thêm thành công!\n";
          } else {
            echo "Lỗi: " . $conn->error;
          }
        } elseif (isset($_POST["delete"])) {
          $idToDelete = $_POST["idToDelete"];

          $sql = "DELETE FROM listfinger WHERE ID = $idToDelete";

          if ($conn->query($sql) === TRUE) {
            echo "Dữ liệu đã được xoá thành công!\n";
          } else {
            echo "Lỗi: " . $conn->error;
          }
        }
      }

      // Hiển thị database lên 
      $sql = "SELECT * FROM listfinger";
      $result = $conn->query($sql);

      if ($result->num_rows > 0) {
        echo "<table>";
        echo "<tr><th>ID</th><th>Họ Tên</th><th>Quê Quán</th><th>Question 1</th><th>Answer 1</th><th>Question 2</th><th>Answer 2</th><th>Question 3</th><th>Answer 3</th><th>Action</th></tr>";

        while ($row = $result->fetch_assoc()) {
          echo "<tr><td>" . $row["ID"] .
            "</td><td>" . $row["HoTen"] .
            "</td><td>" . $row["QueQuan"] .
            "</td><td>" . $row["Question1"] .
            "</td><td>" . $row["Answer1"] .
            "</td><td>" . $row["Question2"] .
            "</td><td>" . $row["Answer2"] .
            "</td><td>" . $row["Question3"] .
            "</td><td>" . $row["Answer3"] .
            "</td><td>
          <form method='post'><input type='hidden' name='idToDelete' value='" . $row["ID"] . "'>
          <input type='submit' name='delete' value='Xoá'>
          </form>
          </td></tr>";
        }

        echo "</table>";
      } else {
        echo "Không có dữ liệu";
      }

      if (isset($_POST['delete'])) {
        $idToDelete = $_POST['idToDelete'];
    
        // Xoá hàng từ cơ sở dữ liệu
        $sqlDelete = "DELETE FROM listfinger WHERE ID = $idToDelete";
        $conn->query($sqlDelete);
    
        // Cập nhật ID cho các hàng còn lại
        $sqlUpdateID = "SET @num := 0;
                        UPDATE listfinger SET ID = @num := (@num + 1);
                        ALTER TABLE listfinger AUTO_INCREMENT = 1;";
        $conn->multi_query($sqlUpdateID);
    }

      $conn->close();

      
      ?>


      <!-- Button trigger modal -->
      <button type="button" class="btn btn-primary button" data-toggle="modal" data-target="#exampleModal">
        Add user
      </button>

      <!-- Modal -->
      <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalLabel">Hãy điền đầy đủ thông tin theo mẫu dưới đây</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
              <form method="post">
              <div class="form-group">
                <label for="hoTen">Họ Tên:</label>
                <input type="text" class="form-control" name="hoTen" required>
                <br>
              <!-- </div> -->

              <!-- <div class="form-group"> -->
                <label for="queQuan">Quê Quán:</label>
                <input type="text" class="form-control" name="queQuan" required>
                <br>
              <!-- </div> -->

              <!-- <div class="form-group"> -->
                <label for="question1">Question 1:</label>
                <input type="text" class="form-control" name="question1" required>
                <br>
              <!-- </div> -->

              <!-- <div class="form-group"> -->
                <label for="answer1">Answer 1:</label>
                <input type="text" class="form-control" name="answer1" required>
                <br>
              <!-- </div> -->

              <!-- <div class="form-group"> -->
                <label for="question2">Question 2:</label>
                <input type="text" class="form-control" name="question2" required>
                <br>
              <!-- </div>   -->

              <!-- <div class="form-group"> -->
                <label for="answer2">Answer 2:</label>
                <input type="text" class="form-control" name="answer2" required>
                <br>
              <!-- </div> -->

              <!-- <div class="form-group"> -->
                <label for="question3">Question 3:</label>
                <input type="text" class="form-control" name="question3" required>
                <br>
              <!-- </div> -->

              <!-- <div class="form-group"> -->
                <label for="answer3">Answer 3:</label>
                <input type="text" class="form-control" name="answer3" required>
                <br>
              </div>
              
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
              <button type="submit" name="add" class="btn btn-primary">Save changes</button>
              </form>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>


  <script src="assets/js/jquery-3.3.1.min.js"></script>
  <script src="assets/js/popper.min.js"></script>
  <script src="assets/js/bootstrap.min.js"></script>
  <script src="assets/js/main.js"></script>

</body>

</html>