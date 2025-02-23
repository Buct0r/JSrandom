const Generate = document.getElementById("generate");
const text = document.getElementById("Password");
const copy = document.getElementById("copy");

let passwordLength
let includeLowercase 
let includeUppercase 
let includeNumbers 
let includeSymbols 


let allowedChars = ""
let generatedPassword = ""


const lowercaseChars = "abcdefghijklmnopqrstuvwxyz";
const uppercaseChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const numberChars = "0123456789";
const symbolChars = "!@#$%^&*()_+-=";



Generate.onclick = function(){

    passwordLength = document.getElementById("Length").value;
    includeLowercase = document.getElementById("lower");
    includeUppercase = document.getElementById("upper");
    includeNumbers = document.getElementById("numb");
    includeSymbols = document.getElementById("symb");


    function password(passwordLength, includeLowercase, includeUppercase, includeNumbers, includeSymbols){


        allowedChars += includeLowercase.checked ? lowercaseChars : "";
        allowedChars += includeUppercase.checked ? uppercaseChars : "";
        allowedChars += includeNumbers.checked ? numberChars : "";
        allowedChars += includeSymbols.checked ? symbolChars : "";
    

    
        if(passwordLength <= 0 || passwordLength==null){
            return `(Password length must be at least 1)`;
        }
        if(allowedChars.length === 0){
            return `(At least 1 set of character needs to be selected)`;
        }
    
        for(let i = 0; i < passwordLength; i++){
            const randomIndex = Math.floor(Math.random() * allowedChars.length);
            generatedPassword += allowedChars[randomIndex];
        }
    
        return generatedPassword;
    }

    const Password = password(passwordLength, includeLowercase, includeUppercase, includeNumbers, includeSymbols);



    text.textContent = Password;
    console.log(Password);
    generatedPassword = "";
    allowedChars = "";
}

copy.onclick = function(){
    navigator.clipboard.writeText(text.textContent);
}

