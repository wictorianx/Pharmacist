
var nameinputx = document.getElementById("name_input")
var passinputx = document.getElementById("pass_input")
nameinputx.addEventListener("keypress", function (e){
    if (e.key === "Enter"){
        submit()
        passinputx.focus()
    }
})
passinputx.addEventListener("keypress", function (e){
    if (e.key === "Enter"){
        submit()
    }
})
//nameinputx.value="TC"
//passinputx.value="Şifre"
var outputx = document.getElementById("output")
function submit() {
    //outputx.textContent = inputx.value
    for (var i = 0; i < accounts.length; i++) {
        let TC = accounts[i].TCX
        if (parseInt(nameinputx.value) == parseInt(TC)) {   
            if (passinputx.value == accounts[i].password) {
                localStorage.setItem("account", JSON.stringify(accounts[i]))
                window.location.href = "prescriptions"
                console.log(1)
            }
    
    
    }
}
}
function fieldclicked(x) {
    if (x.value == "TC" && x.value == "Şifre"){  x.value = "" }
    console.log(x.value)
    // x.style.color = "black"
    }





