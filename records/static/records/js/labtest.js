

function selectionNumeric(id)
{
    var numeric = document.getElementById('numeric');
    var x = document.getElementById(id);
    numeric.removeChild(x);

    var sel_text = "form_"+id;

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
    var numeric = document.getElementById('boolean');
    var x = document.getElementById(id);
    numeric.removeChild(x);

    var sel_text = "form_"+id;

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


function cancelClick(id)
{
    alert(id);
    var x = document.getElementById(id);
    x.remove();
}
