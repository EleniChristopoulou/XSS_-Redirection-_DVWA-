# XSS_-Redirection-_DVWA

## Step 1
  In case you are planning to follow along, I would recommend to follow my intial steup guide. <br>
 [Click](https://github.com/EleniChristopoulou/DVWA_Initial_Setup-/tree/main) here to check it out.

 ## Step 2
  Now it is the time where we interact with site in order to discover actual functionality.<br>
  It is important to pay attention on the input and the output.<br>
  
  Head to `XSS (Reflected)` tab. <br>
  So let's try out the value `someone`. We notice that we can enter any type of string as input.<br>  
  
<p align="center"> <img width="200" height="100" alt="image" src="https://github.com/user-attachments/assets/b76b563a-5b3d-4539-b25c-dab70092e5d9" />
</p>

## Step 3
  Now we are ready to initiate some logs. Back to our DVWA site on the `XSS (Reflected)` tab we submit any type of value, our goal is just to see the log.

Since I submited the value `someone`, I receive the respected query, within the id hold the value 1. By following the steps depicted within the picture, we have sent our log to the repeater tab in Burp. There will be able to forward and modify the request.
  <p align="center"><img width="500" height="190" alt="image" src="https://github.com/user-attachments/assets/8a560a27-b7df-4590-8746-8e5ff575c447" /></p>

## Step 4
  On the `Repeater` tab, we spot 2 tabs. I first looked for the one that contains the `someone` value. I go ahead and rename my tab to `Input` and the second one that was left I rename it as `Output`. <br>
  
  <p align="center"><img width="500" height="250" alt="image" src="https://github.com/user-attachments/assets/96b3c8f5-7122-46cb-a006-e1acb12b0e1e" /></p>

## Step 5
  Now I right click on my now `Output` tab, `Add to group`>`New tab group`.<br>
  
  <p align="center"><img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/2b03af5f-b148-440f-81d8-cc71d8fa8fbe" /></p>
  
## Step 6
  Heading back to our `Input` tab, we select the `somone` value inside the request and replace it with the following:<br>

  ```
  <script> window.location.href = "https://www.google.com"; </script>
  ```


<p align="center"><img width="947" height="474" alt="image" src="https://github.com/user-attachments/assets/afd467ee-0624-4a4d-aae2-04acdfb567d7" /></p>

  Then we click right next to the `Send` button > `Send group in sequnce (seperate connections)`>`New tab group`.<br>
  
## Step 7
  Lastly we press the button to sned the selected request. Just as it is depicted in the bellow screenshot.<br>
  
  <img width="948" height="474" alt="image" src="https://github.com/user-attachments/assets/700f50ec-a885-4b6f-adc3-394e6fe6755f" />


  

  
  


