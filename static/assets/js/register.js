//function showAlert(){
//
//var username=document.getElementById('username').value;
//var email=document.getElementById('email').value;
//var password=document.getElementById('password').value;
//var password1=document.getElementById('password1').value;
//
//
//if(!username ||!email || !password || !password1)
//{
//alert("Please fill the required filled")
//}
//else
//{
//alert("Registration successfully")
//}
//
//}
 function validateForm() {
            var username = document.getElementById("username").value;
            var email = document.getElementById("email").value;
            var password = document.getElementById("password").value;
            var cpassword= document.getElementById("password1").value;

            if (username == "" || email == "" ||password=="" ||cpassword=="") {
                alert("Please fill the details");
                return false;
            }

            var emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
            if (!emailPattern.test(email)) {
                alert("Please enter correct email");
                return false;
            }

            alert("Registration successfully");
            return true;
        }