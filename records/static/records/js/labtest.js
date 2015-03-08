
// selection on click method
// numeric form creation is to be done using this
function selectionNumeric(id, maleRange, femaleRange, childRange)
{
    //get our  node with id that is to be hidden after selection
    var x = document.getElementById(id);
    x.style.visibility = "hidden";

    var form_id = "form_"+id;

    //create a new div
    var newdiv = document.createElement("div");
    newdiv.setAttribute('id', form_id );

    //create label
    var label = document.createElement("LABEL");
    label.innerHTML = id;

    var input = document.createElement("input");
    input.setAttribute('type','number');
    input.setAttribute('name', id );
    input.setAttribute('step', '0.01');
    input.setAttribute('min', '0');

    var male = null;
    var female = null;
    var child = null;

    if(maleRange == femaleRange && femaleRange==childRange)
    {
        male = document.createElement("LABEL");
        male.innerHTML = maleRange;
    }

    else if(maleRange != femaleRange && femaleRange == childRange)
    {
        male = document.createElement("LABEL");
        male.innerHTML = maleRange;
        female = document.createElement("LABEL");
        female.innerHTML = femaleRange;
    }

    else
    {
        male = document.createElement("LABEL");
        male.innerHTML = maleRange;
        female = document.createElement("LABEL");
        female.innerHTML = femaleRange;
        child = document.createElement("LABEL");
        child.innerHTML = childRange;
    }

    //create button
    var button = document.createElement("input");
    button.type = "button";
    button.value = "cancel";
    button.addEventListener("click", function () { cancelClick(form_id); } );

    //append
    newdiv.appendChild(label);
    newdiv.appendChild(input);
    if(male)
    {
        newdiv.appendChild(male);
    }
    if(female)
    {
        newdiv.appendChild(female);
    }
    if(child)
    {
        newdiv.appendChild(child);
    }
    newdiv.appendChild(button);

    /*
    var temp = document.getElementsByTagName("form")[0];
    temp.appendChild(newdiv);
    */

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
    var v = document.getElementById(duplicate);
    v.style.visibility = "visible";

    var x = document.getElementById(id);
    x.remove();
}
