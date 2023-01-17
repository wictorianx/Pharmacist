let sales
let past =[]
let date = new Date()
let year = date.getFullYear()
let month = date.getMonth()
let day = date.getDate()
let fdate = [day,month,year]
let table = document.querySelector("table")
function raporla(sale){
    console.log(sale)
    let tr = document.createElement("tr")
    let time = document.createElement("td")
    let tc = document.createElement("td")
    let drug = document.createElement("td")
    time.innerHTML = sale["time"]
    tc.innerHTML = sale["tc"]
    drug.innerHTML = sale["drug"]

    tr.appendChild(drug)
    tr.appendChild(tc)
    tr.appendChild(time)
    table.appendChild(tr)
}

function showAll(){
    
    past.forEach(raporla)
}

$.getJSON("static/sales.json", function(json) {
    sales= json["sales"];
    
    sales.forEach(function(sale){
        let time = new Date(sale["time"])
        let saleday = time.getDate()
        let salemonth = time.getMonth()
        let saleyear = time.getFullYear()
        let saledate = [saleday,salemonth,saleyear]
        console.log(sale)
        if (JSON.stringify(saledate) === JSON.stringify(fdate)) {
            raporla(sale)
        }
        else{
            console.log("dsfdfsd")
            past.push(sale)
        }
    }
    )
    })












