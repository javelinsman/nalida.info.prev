function setText(text){
    document.getElementById("d-text").innerHTML = text;
}

function addButton(text, dst){
    dom = '<div class="button" onclick="setPage('+dst+')">'+text+'</div>';
    document.getElementById("buttons").innerHTML += dom;
}

function clearContents(){
    setText("");
    document.getElementById("buttons").innerHTML = "";
}

function setPage(i){
    clearContents();
    setText(datas[i].text);
    for(btn of datas[i].buttons){
        addButton(btn.text, btn.dst);
    }
}

setPage(0);
