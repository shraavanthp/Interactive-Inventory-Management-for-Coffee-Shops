function validate() {
    if(document.new_form.item_name.value == ""){
        alert("Please enter the name of the item!");
        document.new_form.item_name.focus();
        return false;
    }

    var radio = document.getElementsByName('type');
    for (var i=0; i<radio.length; i++) {
        if (radio[i].type == 'radio' && radio[i].checked) {
            return true;
        }
    }
    alert("Select Snack or Drink");
    return false;
}

$("#plus_btn").click(function(event) {
	$( "#ingredient-div" ).append('<input type="text" name="ingredients[]">');
});

$("#minus_btn").click(function(event) {
    if($("input[name='ingredients[]']").length > 1 ) {
        $("input[name='ingredients[]']:eq("+(length-1)+")").remove();
    }
});

$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();
});