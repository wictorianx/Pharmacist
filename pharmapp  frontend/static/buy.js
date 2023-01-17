let cards
let menu
let tbox
let cartx
let cardid
let ownertc = "11"
let iter = 0
let price = localStorage.getItem("price")
let validthru
let username
let surname
let validbox = document.querySelector("#validbox")
let namebox = document.querySelector("#namebox")
let surnamebox = document.querySelector("#surnamebox")
menu = document.getElementById("cardmenu")
menu.addEventListener("change",cardChosen)
function cardChosen() {
    validthru = cards[menu.value].valid_thru
    fullname = (cards[menu.value].owner_name).split(" ")
    username = fullname[0]
    surname =  fullname[1]

    namebox.innerHTML = username
    surnamebox.innerHTML = surname
    validbox.innerHTML = validthru
}
tbox = document.getElementById("talkbox")
submitbutton = document.getElementById("submit")
function choose(){
    let balance = parseInt(cards[menu.value].content)
    ownertc = cards[menu.value].owner_tc
    cardid = parseInt(cards[menu.value].card_id)
    console.log(ownertc)
    // console.log(cards[menu.value].content)
    // console.log(menu.value)
    // console.log(localStorage.getItem("price"))
    
    if (balance>=price){
        balance-=price
        talkbox.textContent = "Kalan Bakiye : "+balance+"₺"
        
        main(menu.value)
        submitbutton.onclick = function(){alert("Aynı İşlemi İkinciye Yapamazsınız")}
        localStorage.clear();
        console.log(1);
        let homeTimer = setInterval(returnHome,500)
        

    }
    else{
        talkbox.textContent = "Bakiyeniz Yetersiz olduğu için işleminiz gerçekleşemedi" 
    }

}
function returnHome(){
    console.log(2)
    switch(iter%3) {
        case 2:
          talkbox.textContent = "Ana Ekrana Dönülüyor ..."
          iter++;
          break;
        case 1:
          talkbox.textContent = "Ana Ekrana Dönülüyor .."
          iter++;
          break;
        case 0:
          talkbox.textContent = "Ana Ekrana Dönülüyor ."
          iter++;
          break;
        default:
            talkbox.textContent = "Ana Ekrana Dönülüyor"
            iter++;
            break;
      }
      console.log(iter)
    if (iter === 6){
        console.log(1423412342)
        window.location.href="login"
    }
    
}
function home(){window.location.href = "login"}
function parseCards(tc){
    let val = []
    console.log("CARDS",cards)
    for(let i=0; i<cards.length; i++) {
        if (String(cards[i].owners_tc) === String(tc)){
            val.push(cards[i])
        }
    }
    return val
}
function main(){
    {
        let cartx = localStorage.getItem('cart').split(",");
        var postData = {}
        // alert(typeof cartx)
        postData.cart=[]
        postData.price=price
        postData.userid = ownertc
        postData.cardid = cardid 
        cartx.forEach(function (x){
            postData.cart.push(x)
        })
    
            $.ajax({
                type: "POST",
                url: "http://127.0.0.1:5000/json",
                data: JSON.stringify(postData),
                contentType: "application/json",
                dataType: "json",
                done: function() {
                    // Clear out the posted message...
                    let x = 0
                    // alert(postData)
                },
                fail: function(e) {
                    confirm("Error", e.message);
                }
            });
            // prevent default posting of form (since we're making an Ajax call)...
            
        }
}




$.getJSON("static/cards.json", function(json) {
    cards = json["cards"];
    // alert(cards)
    console.log(cards)

    main()
   



for (let i = 0; i<cards.length;i++){
    let option = document.createElement("option")
    option.value = cards[i].card_id
    option.dataset.x = "s"
    //option.classList.add("opt")
    let num = String(cards[i].num)
    let txt = "**** **** **** " + num.substring(cards[i].length, 4)
    console.log(txt)
    option.textContent = txt
    console.log(menu)
    menu.appendChild(option)
}

console.log(cards)
document.cookie="key=value"
console.log(document.cookie)


console.log("12312312312dsfsdf3") 
console.log(cards)

cards = parseCards(localStorage.getItem("account").TCX) })


// let cartx = localStorage.getItem('cart').split(",");
// console.log(cards)
// document.cookie="key=value"
// console.log(document.cookie)
// let menu = document.getElementById("cardmenu")
// let tbox = document.getElementById("talkbox")




