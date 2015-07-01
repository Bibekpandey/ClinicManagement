var $error_template = $(".error-template");

// for id of new error panel
var hash = 2;

// CreateErrorPanel
var CreateErrorPanel = function(content)
{
    var $new_panel = $error_template.clone();
    $new_panel.find(".error-content").html(content);
    var id = "error-" + hash;
    ++hash;
    $new_panel.find(".panel-body").attr("id", id);
    $new_panel.css("display", "block");

    // assign close hander
    $new_panel.find(".error-close").click(function() 
    { 
        $("#" + id).css("display", "none");
    });

    $("#error-panel").append($new_panel);
}
