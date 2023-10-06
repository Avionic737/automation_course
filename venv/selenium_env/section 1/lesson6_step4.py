from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

'''
<html><head>
    <meta charset="utf-8">
    <title>Simple registration form</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js" integrity="sha384-smHYKdLADwkXOn1EmN1qk/HfnUcbVRZyYmZ4qpPea6sjB/pTJ0euyQp0Mk8ck+5T" crossorigin="anonymous"></script>
    <script src="jquery_min.js"></script>

</head>

<body class="bg-light">

  <h3 class="timer">
      <span class="nowrap" id="timeLeft">Oops, </span>
      <span class="nowrap" id="countdown"> time is up :(</span>

  </h3>

  <div class="container" style="padding-top: 90px;">

    <h1>Hello!</h1>
    <p>Please, fill out the form with the find methods and required locators.</p>
    <p>Finally, your script should click Submit button and you'll see the verification code for Stepik quiz. </p>

    <form action="#" method="get" onsubmit="showResult(3)">
      <div class="form-group">
        <label>First name:*</label>
        <input type="text" name="first_name" class="form-control" required="" maxlength="32">
      </div>
      <div class="form-group">
        <label>Last name:*</label>
        <input type="text" name="last_name" class="form-control" required="" maxlength="32">
      </div>
      <div class="form-group">
        <label>City:*</label>
        <input type="text" name="firstname" class="form-control city" required="" maxlength="32">
      </div>
      <div class="form-group">
        <label>Country:*</label>
        <input type="text" name="firstname" class="form-control" id="country" required="" maxlength="32">
      </div>
      <button id="submit_button" type="submit" class="btn btn-default" disabled="disabled">Submit</button>
    </form>
  <script type="text/javascript">
    var isFinished = false;
    countDown(4);
  </script>



</div></body></html>
'''