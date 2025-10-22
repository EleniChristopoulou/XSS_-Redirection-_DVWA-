# XSS_-Redirection-_DVWA

## Step 1
  In case you are planning to follow along, I would recommend to follow my intial steup guide. <br>
 [Click](https://github.com/EleniChristopoulou/DVWA_Initial_Setup-/tree/main) here to check it out.

 ## Step 2
  Now it is the time where we interact with site in order to discover actual functionality.<br>
  It is important to pay attention on the input and the output.<br>
  
  Head to `XSS (Stored)` tab. <br>
  So let's try out the value `someone` for name and `someone mess` as a message. We notice that we can enter any type of string as input.<br>  
  
<p align="center"> <img width="490" height="289" alt="image" src="https://github.com/user-attachments/assets/080a7fb8-bfb6-4f07-8064-be34143943c6" /></p>

## Step 3
  Now we are ready to initiate some logs. Back to our DVWA site on the `XSS (Stored)` tab we submit any type of value, our goal is just to see the log.

We interested in two logs, the type `POST` which is our request to display our input & `GET` which is the display of our data from server
  <p align="center"> <img width="963" height="267" alt="image" src="https://github.com/user-attachments/assets/f88c6ccd-c8fa-47a8-94e9-cb403832c055" />/


## Step 4
  On the `Repeater` tab, we spot 2 tabs. I first looked for the one that contains the `someone` value. I go ahead and rename my tab to `Input` and the second one that was left I rename it as `Output`. <br>
  
  <p align="center"><img width="934" height="529" alt="image" src="https://github.com/user-attachments/assets/7db18d0f-da46-49ea-a49b-a959f2fed17e" />
</p>

## Step 5
  Now I right click on my now `Output` tab, `Add to group`>`New tab group`.<br>
  
  <p align="center"><img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/2b03af5f-b148-440f-81d8-cc71d8fa8fbe" /></p>
  
## Step 6
  Heading back to our `Input` tab, we select the `somone \r \n` value inside the request and replace it with the following:<br>

  ```
  <script> window.location.href = "https://www.google.com"; </script>
  ```


<p align="center"><img width="921" height="560" alt="image" src="https://github.com/user-attachments/assets/270fdc95-1846-4d02-9b37-9437f10405ca" />
</p>

  Then we click right next to the `Send` button > `Send group in sequnce (seperate connections)`>`New tab group`.<br>
  
## Step 7
  Lastly we press the button to send the selected request. Just as it is depicted in the bellow screenshot.<br>
  
  <p align="center"><img width="942" height="457" alt="image" src="https://github.com/user-attachments/assets/d0991f25-49e1-44bf-a0cd-841f8f2be995" /></p>


  ## Step 8
  Now we have sent to the server our cross site scripting, what's left is to view our results.<br>
  Heading to the `Output` tab, we right click onto the tab and select Show response in browser.<br>

  We then copy the link that is given to us, and head to the browser open a new tab and paste our link to view our results.<br>
  
  <img width="948" height="474" alt="image" src="https://github.com/user-attachments/assets/700f50ec-a885-4b6f-adc3-394e6fe6755f" />

  Our result is well... google!<br>

  <img width="480" height="350" alt="image" src="https://github.com/user-attachments/assets/f4d8c421-7cdd-465e-83e3-8469e2258a4d" />

  Even if we head back to our intial site:<br>
  ```
  http://localhost/
  ```
  and then head to `XSS (Stored)` tab, we get redirected to google.



  

  
  


