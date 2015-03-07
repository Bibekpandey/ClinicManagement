
// selection on click method
// numeric form creation is to be done using this
function selectionNumeric(id)
{
    //get our  node with id that is to be hidden after selection
    var x = document.getElementById(id);
    //numeric.removeChild(x);
    x.style.visibility = "hidden";

    var form_id = "form_"+id;

    //create a new div
    var newdiv = document.createElement("div");
    newdiv.setAttribute('id', form_id );

    //create label
    var label = document.createElement("LABEL");

    //extract the name part
    var t = document.createTextNode(id);
    label.appendChild(t);

    //create button
    var button = document.createElement("input");
    button.type = "button";
    button.value = "cancel";
    button.addEventListener("click", function () { cancelClick(form_id); } );

    //append
    newdiv.appendChild(label);
    newdiv.appendChild(button);


    //append to our div
    var divappend = document.getElementById("selected");
    divappend.appendChild(newdiv);

}

// radio button type of form to be created here
function selectionBoolean(id)
{
    //get our  node with id that is to be hidden after selection
    var x = document.getElementById(id);
    x.style.visibility = "hidden";

    var form_id = "form_"+id;

    var newdiv = document.createElement("div");
    newdiv.setAttribute('id', form_id);

    var label = document.createElement("LABEL");
    var t = document.createTextNode(id);
    label.appendChild(t);

    var button = document.createElement("input");
    button.type = "button";
    button.value = "cancel";
    button.addEventListener("click", function () { cancelClick(form_id); } );

    newdiv.appendChild(label);
    newdiv.appendChild(button);

    var divappend = document.getElementById("selected");
    divappend.appendChild(newdiv);

}


function cancelClick(id)
{
    //remove 'form_' part from form id
    var duplicate = id.slice(5,id.length);
    var splitted = duplicate.split(" ");
    var type = splitted[0];

    var x = document.getElementById(duplicate);
    x.style.visibility = "visible";

    var x = document.getElementById(id);
    x.remove();
}
