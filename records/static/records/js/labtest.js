

function selectionNumeric(id)
{
    id = id.replace(/\s+/g,' ');
    var selected = document.getElementById("selected");
    
    var text = id.split(" ");
    text = text.slice(1, text.length);
    var sel_text = text.join("_");
    //alert(sel_text);

    var newdiv = document.createElement("div");
    newdiv.setAttribute('id', sel_text);

    var label = document.createElement("LABEL");
    var t = document.createTextNode(sel_text);
    label.appendChild(t);

    var button = document.createElement("input");
    button.type = "button";
    button.value = "cancel";
    button.addEventListener("click", function () { cancelClick(sel_text); } );

    newdiv.appendChild(label);
    newdiv.appendChild(button);

    var divappend = document.getElementById("selected");
    divappend.appendChild(newdiv);

}

function selectionBoolean(id)
{
    alert(id);

    var selected = document.getElementById("selected");
}

function cancelClick(id)
{
    var x = document.getElementById(id);
    x.remove();
}
