//{}
//console.log(window.account)
//console.log(window.account[0])
let price = 0
let account = (JSON.parse(localStorage.getItem("account")))
// let prescription_ids = []
// for (var i = 0; i < prescriptions.length; i++) {
//     if (prescriptions[i].owners_tc == account.TCX){
//         //console.log(prescriptions[i].owners_tc,account.TCX)
//         if (prescription_ids.includes( prescriptions[i].prescription_id) === false)
//         {prescription_ids.push( prescriptions[i].prescription_id)}
//     }    
//     else {
//         let tc = prescriptions[i].owners_tc
// }
// }
function br(target){
    target.appendChild(document.createElement('br'));
}
function buy(){

    //localStorage.setItem('price',price)
    price = localStorage.getItem('price')
    localStorage.setItem('cart',cart)
    if (price>0){
        console.log(price)
        console.log(cart)
    window.open("buy","mozillaTab");}
    else{
        alert("İlaç Seçmediniz")
    }

}
function calculate(){
    let label = document.querySelector('#paylabel');
    console.log(label);
    let p = 0
    checkboxList.forEach(function(item){
        if (item.checked){

            cart.push(item.name)
            p+=parseInt(item.dataset.price)

        }
    })
    localStorage.setItem("price",p)
    label.innerHTML = "Ödenecek Tutar : "+p+"₺"
}

function selectAll(element){
    checkboxList.forEach(function(item){

        if (element.checked){
        item.checked = true}
        else{
            item.checked = false
        }
    })
}

let checkboxList = []
let cart = []
let drugs = Object.keys(drugs_prices)
function prescribe(drugs) {
    let counter = -1
drugs.forEach(element => {
    if (nopresdrugs.includes(element)){
     
    // if (prescription_ids.includes(element.prescription_id)){
        counter++
    let tbl = document.querySelector("#ptable")
    let selectAllButton = document.querySelector("#select-all")
    selectAllButton.style.accentColor="#7fc097";
    selectAllButton.addEventListener("click", () =>selectAll(selectAllButton))
    selectAllButton.addEventListener("click",calculate)
    let drug = element
    let inp = document.createElement("input");
    inp.type="checkbox";
    inp.addEventListener("click",calculate)
    inp.addEventListener("click",function(){selectAllButton.checked=false})
    checkboxList.push(inp);
    inp.style.accentColor="#7fc097";
    inp.id = counter 
    inp.name = drug
    price = parseInt(drugs_prices[drug])
    // price *= (100-parseInt(account.sgk))/100
    
    inp.dataset.price = price
    
    
    selectAllButton.style.fontWeight="bold";
    selectAllButton.style.fontStyle="Alegreya";
    selectAllButton.style.fontSize="larger";
    let row = document.createElement("tr")
    let labelcolumn = document.createElement("td")
    labelcolumn.style.fontWeight="bold";
    labelcolumn.style.fontStyle="Alegreya";
    labelcolumn.style.fontSize="larger";
    
    let inpcolumn = document.createElement("td") 
    let pricecolumn = document.createElement("td")
    pricecolumn.style.fontWeight="bold";
    pricecolumn.style.fontStyle="Alegreya";
    pricecolumn.style.fontSize="larger";
    labelcolumn.innerHTML = drug
    inpcolumn.appendChild(inp) 
    pricecolumn.innerHTML = String(price)+"₺"
    row.appendChild(labelcolumn)
    row.appendChild(pricecolumn)
    row.appendChild(inpcolumn)
    tbl.appendChild(row)
    //div.appendChild(lbl)
    //div.appendChild(inp)
    br(prescription)
}
    

});
}
function buyWithout(){
    window.open("noprescription","mozillaTab");
}
//     let finalrow = document.createElement("tr")
//    let table = document.querySelector("#ptable")
    let div = document.querySelector("#container")

    let paybtn = document.createElement("button")
    let paylabel = document.createElement("p")
    div.appendChild(paybtn)
    div.appendChild(paylabel)

    paylabel.id = "paylabel"
    paylabel.textContent = "Ödenecek Tutar : 0₺"
    paybtn.id = "paybtn"
    
    paybtn.onclick = buy
    paybtn.innerHTML = "Öde"
    paybtn.id="paybtn"



    // let nopresbtn = document.createElement("button")
    // div.appendChild(nopresbtn)

    // nopresbtn.id = "nopresbtn"
    
    // nopresbtn.onclick = buyWithout
    // nopresbtn.innerHTML = "Reçetesiz Al"
    // nopresbtn.id="nopresbtn"
//     let col1 = document.createElement("td")
//     col1.appendChild(paybtn)
//     let col2 = document.createElement("td")
//     col2.innerHTML = "Ödenecek Tutar : "
//     let col3 = document.createElement("td")
//     col3.appendChild(paylabel)
//     finalrow.appendChild(col1)
//     finalrow.appendChild(col2)
//     finalrow.appendChild(col3)
//     table.appendChild(finalrow)
// }
prescribe(drugs)
calculate()
